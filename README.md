
Overview
The Graph Optimization Project provides implementations of various graph algorithms, including Minimum Spanning Tree (MST) and Traveling Salesman Problem (TSP). This project showcases the use of both C++ and Python to solve these problems, leveraging different algorithmic approaches and libraries.

##
Features
- **Minimum Spanning Tree (MST) Algorithms**:
  - Boruvka's Algorithm
  - Prim's Algorithm
- **Traveling Salesman Problem (TSP) Solution**:
  - Double TSP approximation technique
  - Minimum-Cost Perfect Matching using Integer Programming
- **Graph Representations and Utilities**:
  - Union-Find data structure for cycle detection and union operations

##
Installation Instructions

### Prerequisites
- **C++ Compiler** (e.g., `g++`)
- **Python 3.x**
- **Gurobi Optimizer** (Python library)
- **Git** to clone the repository

### Steps
1. **Clone the Repository**
    ```bash
    git clone https://github.com/leotac/graph.git
    cd graph
    ```

2. **C++ Compilation**
    - Ensure you have a C++ compiler installed.
    - Compile the C++ files:
    ```bash
    g++ -o graph main.cpp
    ```

3. **Python Setup**
    - Ensure you have Python 3 installed.
    - Install the Gurobi library (Make sure you have a valid Gurobi license):
    ```bash
    pip install gurobipy
    ```

##
Usage Examples

### Running the C++ Implementation
```bash
./graph
```

### Using the Python Implementation
```python
import mst
import tsp

nodes = [0, 1, 2, 3, 4, 5]
cost = [
    [0, 0, 3.2, 2.2, 0, 0],
    [0, 0, 2, 4, 0, 0],
    [3.2, 2, 0, 3.1, 0, 0],
    [2.2, 4, 3.1, 0, 3, 0],
    [0, 0, 0, 3, 0, 1],
    [0, 0, 0, 0, 1, 0]
]

# Solve MST using Python
mst_tree = mst.kruskal(nodes, cost)
print("MST:", mst_tree)

# Solve TSP using Python
tsp_tour = tsp.double_tsp(nodes, cost)
print("TSP Tour:", tsp_tour)
```

##
Code Summary

- **main.cpp**: Entry point for the C++ implementation. Defines the cost matrix and initializes the algorithms.
- **mst.cpp**: Contains the C++ implementation for MST algorithms using Boruvka's and Prim's methods.
- **mst.py**: Contains the Python implementation for MST using Kruskal's algorithm.
- **tsp.cpp**: Implements a double TSP approximation technique in C++.
- **tsp.py**: Implements TSP approximation and minimum-cost perfect matching using Integer Programming via Gurobi.

##
Contributing Guidelines
We welcome contributions to improve and expand the project. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch to your fork.
4. Create a pull request with a description of your changes.

Please ensure that your code adheres to the existing code style and includes tests where appropriate.

##
License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

### Important Note
Replace the placeholder `LICENSE` with the actual path to your license file in the repository. If there is no license file, add one using the text of the MIT License or whichever you prefer.