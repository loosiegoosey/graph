from gurobipy import *
import random
import math

# Model data


def tsp(nodes, arcs, cost):

     n=len(nodes)
     arcs = tuplelist(arcs)

     # Create all possible subsets (minus empty and full set)
     subsets = [[nodes[i]  for i in xrange(0,n) if k/2**i%2 == 1] for k in xrange(1,2**n-1)]

     # Create optimization model
     m = Model('tsp')

     # Create variables
     x = {}
     for i,j in arcs:
          x[i,j] = m.addVar(vtype=GRB.BINARY, obj=cost[i,j], name='x_%s_%s' % (i, j))
          #x[i,j] = m.addVar(lb=0, ub=1, obj=cost[i,j], name='x_%s_%s' % (i, j))
     m.update()

     # Arc capacity constraints
     for i in nodes:
         m.addConstr(quicksum(x[i,j] for (i,j) in arcs.select(i,'*')) == 1, 'degree_out_%s' % (i))
         m.addConstr(quicksum(x[j,i] for (j,i) in arcs.select('*',i)) == 1, 'degree_in_%s' % (i))

     for k in range(len(subsets)):
         m.addConstr(quicksum(x[i,j] for i in subsets[k] for j in set(nodes).difference(set(subsets[k])) if (i,j) in arcs)>=1, 'cut_out_%s' % (k))	
         m.addConstr(quicksum(x[j,i] for i in subsets[k] for j in set(nodes).difference(set(subsets[k])) if (j,i) in arcs)>=1, 'cut_out_%s' % (k))	                            
     
     #m.update()
     #m.write('tsp.lp')

     
     # Compute optimal solution
     m.optimize()

     # Print solution
     if m.status == GRB.status.OPTIMAL:
             print '\nOptimal tour:'
             for i,j in arcs:
                 if x[i,j].x > 0.1:
                     print i, '->', j, ':', x[i,j].x
             tour = [nodes[0]]
             for i in xrange(n-1):
                             for (a,b) in arcs.select(tour[i],'*'):
                                     if x[a,b].x == 1:
                                             tour.append(b)
                                             break
             print tour     
                     
                




def main(n):
     nodes = ['Detroit', 'Denver', 'Boston', 'New York', 'Seattle']
     x={}
     y={}

     import os
     import string

     random.seed(8)
     
     #n=15
     nodes=[]
     for i in range(n):
             #nodes.append(''.join(random.choice(string.letters+string.digits+"_") for i in xrange(5)))
             nodes.append(string.letters[i%len(string.letters)]*(1+i/len(string.letters)))
             x[nodes[i]]=random.random()*10.0
             y[nodes[i]]=random.random()*10.0
     arcs = []
     cost={}
     for i in range(n):
             for j in range(i+1,n):
                  arcs.append((nodes[i],nodes[j]))
                  arcs.append((nodes[j],nodes[i]))
                  cost[nodes[i],nodes[j]]=cost[nodes[j],nodes[i]]=math.sqrt((x[nodes[i]]-x[nodes[j]])**2 + (y[nodes[i]]-y[nodes[j]])**2)
##     print x
##     print y
##     print arcs
##     print cost
     
##     arcs, cost = multidict({
##       ('Detroit', 'Boston'):   300,
##       ('Detroit', 'New York'):  80,
##       ('Detroit', 'Seattle'):  120,
##       ('Denver',  'Boston'):   120,
##       ('Denver',  'New York'): 100,
##       ('Denver',  'Seattle'):  90,
##       ('New York', 'Boston'):   40,
##       ('New York', 'Detroit'):   40,
##       ('Boston',  'Seattle'):   60,
##       ('Boston',  'Detroit'):   100,
##       ('Boston',  'Denver'):   80,
##       ('Seattle',  'Denver'):   60,
##       ('Detroit', 'Denver'):   70,
##       })

     tsp(nodes,arcs, cost)
         
     return 0

if __name__ == '__main__':
	main()
