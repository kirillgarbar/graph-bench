# graph-bench

Benchmarks suite for performance study of various graph analysis frameworks for CPU/GPU computations.

## Dataset

| Name              | Vertices | Edges | Max Degree |                                                                                          Download |
|:------------------|---------:|------:|-----------:|--------------------------------------------------------------------------------------------------:| 
| soc-LiveJournal   |        0 |     0 |          0 |      [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/soc-LiveJournal1.tar.gz) |
| hollywood-2009    |        0 |     0 |          0 |         [link](https://suitesparse-collection-website.herokuapp.com/MM/LAW/hollywood-2009.tar.gz) |
| com-Orcut         |        0 |     0 |          0 |             [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/com-Orkut.tar.gz) |
| roadNet-CA        |        0 |     0 |          0 |            [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/roadNet-CA.tar.gz) |
| indochina-2004    |        0 |     0 |          0 |         [link](https://suitesparse-collection-website.herokuapp.com/MM/LAW/indochina-2004.tar.gz) |
| cit-Patents       |        0 |     0 |          0 |           [link](https://suitesparse-collection-website.herokuapp.com/MM/SNAP/cit-Patents.tar.gz) |
| coAuthorsCiteseer |        0 |     0 |          0 | [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/coAuthorsCiteseer.tar.gz) |
| coPapersDBLP      |        0 |     0 |          0 |      [link](https://suitesparse-collection-website.herokuapp.com/MM/DIMACS10/coPapersDBLP.tar.gz) |

## Tools

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