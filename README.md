# graph-bench

Benchmarks suite for performance study of various graph analysis frameworks for CPU/GPU computations.

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


## How to build tools

### Spla

```shell
python3 scripts/build_spla.py
```

### Gunrock

```shell
python3 scripts/build_gunrock.py
```

### GraphBLAST

```shell
python3 scripts/build_graphblast.py
```

### LaGraph

```shell
python3 scripts/build_lagraph.py
```

## How to run benchmarks

