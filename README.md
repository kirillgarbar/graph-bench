# graph-bench

Benchmarks suite for performance study of various graph analysis frameworks for CPU/GPU computations.

## Tools description

| Name       | Brief                                                              | Platform | Technology |                                        Source Page |
|:-----------|:-------------------------------------------------------------------|---------:|-----------:|---------------------------------------------------:|
| Spla       | Generalized linear sparse linear algebra for multi-GPU computation |      GPU |     OpenCL | [link](https://github.com/JetBrains-Research/spla) |
| GraphBLAST | High-performance linear algebra-based graph primitives on GPUs     |      GPU |       CUDA |      [link](https://github.com/gunrock/graphblast) |
| Gunrock    | High-performance graph primitives on GPUs                          |      GPU |       CUDA |         [link](https://github.com/gunrock/gunrock) |
| LaGraph    | Collection of graph algorithms for SuiteSparse:GraphBLAS libray    |      CPU |     OpenMP |       [link](https://github.com/GraphBLAS/LAGraph) |

## Dataset description

| Name              | Vertices |  Edges | Max Degree |                                                                                          Download |
|:------------------|---------:|-------:|-----------:|--------------------------------------------------------------------------------------------------:|
| coAuthorsCiteseer |   227.3K |   1.6M |       1372 | [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/coAuthorsCiteseer.tar.gz) |
| coPapersDBLP      |   540.4K |  30.4M |       3299 |      [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/coPapersDBLP.tar.gz) |
| hollywood-2009    |     1.1M | 113.8M |      11467 |         [link](https://suitesparse-collection-website.herokuapp.com/MM/LAW/hollywood-2009.tar.gz) |
| roadNet-CA        |     1.9M |   5.5M |         12 |            [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/roadNet-CA.tar.gz) |
| com-Orcut         |       3M |   234M |      33313 |             [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/com-Orkut.tar.gz) |
| cit-Patents       |     3.7M |  16.5M |        793 |           [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/cit-Patents.tar.gz) |
| soc-LiveJournal   |     4.8M |  68.9M |      20333 |      [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/soc-LiveJournal1.tar.gz) |
| indochina-2004    |     7.5M | 194.1M |     256425 |         [link](https://suitesparse-collection-website.herokuapp.com/MM/LAW/indochina-2004.tar.gz) |

## Instructions

### 1. How to download data

Download archive with graphs data. Extract archive and place data into [dataset](./dataset) folder.

### 2. How to prepare data

Convert graphs into undirected graphs

```shell
python3 scripts/config.py
```

### 3. How to build tools

#### 3.1 Spla

Build bundled Spla library.

```shell
python3 scripts/build_spla.py
```

#### 3.2 Gunrock

Build bundled Gunrock library.

```shell
python3 scripts/build_gunrock.py
```

#### 3.3 GraphBLAST

Build bundled GraphBLAST library.

```shell
python3 scripts/build_graphblast.py
```

#### 3.4 LaGraph

Build bundled SuiteSparse and LaGraph libraries.

```shell
python3 scripts/build_lagraph.py
```

### 4. How to run benchmarks

Run all algorithms & graphs & tools performance measurements.

```shell
python3 scripts/benchmark.py
```

Run particular tool for performance measurements.

```shell
python3 scripts/benchmark.py --tool=[all, spla, lagraph, gunrock, graphblast]
```

Run particular algorithm for performance measurements.

```shell
python3 scripts/benchmark.py --algo=[all, bfs, sssp, tc]
```