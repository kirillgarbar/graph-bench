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
| rgg_n_2_22_s0     |     4.1M |  60.7M |         36 |     [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/rgg_n_2_22_s0.tar.gz) |
| soc-LiveJournal   |     4.8M |  68.9M |      20333 |      [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/soc-LiveJournal1.tar.gz) |
| indochina-2004    |     7.5M | 194.1M |     256425 |         [link](https://suitesparse-collection-website.herokuapp.com/MM/LAW/indochina-2004.tar.gz) |
| rgg_n_2_23_s0     |     8.3M |   127M |         40 |     [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/rgg_n_2_23_s0.tar.gz) |

## Instructions

### 1. How to get source code

Download benchmark repository source code.

```shell
git clone https://github.com/EgorOrachyov/graph-bench.git
```

Within repo folder init git submodule to get all source code of tools.

```shell
git submodule update --init --recursive
```

### 2. How to build tools

#### 2.1 Spla

Build bundled Spla library.

```shell
python3 scripts/build_spla.py
```

#### 2.2 Gunrock

Build bundled Gunrock library.

```shell
python3 scripts/build_gunrock.py
```

#### 2.3 GraphBLAST

Build bundled GraphBLAST library.

```shell
python3 scripts/build_graphblast.py
```

#### 2.4 LaGraph

Build bundled SuiteSparse and LaGraph libraries.

```shell
python3 scripts/build_lagraph.py
```

### 3. How to download data

Download all graphs one by one archives and extract into [dataset](./dataset) folder.
Alternatively, download all graphs within single archive from [google drive](https://drive.google.com/file/d/1bgovKsmjexYyXfEZLxNi-0uoxmDalIGn/view?usp=sharing).

### 4. How to prepare data

Convert graphs into undirected graphs

```shell
python3 scripts/config.py
```

### 5. How to run benchmarks

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

See help for more options.

```shell
python3 scripts/benchmark.py -h
```