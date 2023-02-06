# graph-bench

[![JB Research](https://jb.gg/badges/research-flat-square.svg)](https://research.jetbrains.org/)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/JetBrains-Research/spla-bench/blob/master/LICENSE.md)

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

## Manually running benchmarks

### 1. How to get source code

Download benchmark repository source code.

```shell
git clone https://github.com/kirillgarbar/graph-bench.git
```

Within repo folder init git submodule to get all source code of tools.

```shell
git submodule update --init --recursive
```

You can also track your own GraphBLAS-sharp repo and branch.

```shell
git config -f .gitmodules submodule.deps/graphblas-sharp.url https://github.com/username/GraphBLAS-sharp.git
git config -f .gitmodules submodule.deps/graphblas-sharp.branch branch_name
git submodule sync
git submodule update --init --recursive --remote deps/graphblas-sharp/
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

#### 2.5 GraphBLAS-sharp

Build bundled GraphBLAS-sharp library.

```shell
cd deps/graphblas-sharp/
dotnet build -c Release
cd ../../
```

### 3. How to download data

#### 3.1 Manual copying

Download all graphs one by one archives and extract into [dataset](./dataset) folder.
Alternatively, download all graphs within single archive from [Google Drive](https://drive.google.com/file/d/1bgovKsmjexYyXfEZLxNi-0uoxmDalIGn/view?usp=sharing).

#### 3.2 Downloading with script

Graphs listed in `scripts/matrices.txt` file can be automatically downloaded using this script.

```shell
python3 scripts/download_matrices.py
```

### 4. How to run benchmarks

#### 4.1 GraphBLAS-sharp

Dataset folder with all nested directories will be copied to the corresponding GraphBLAS-sharp directory, so make sure all graphs are placed in correct folders.
All configs are present in `scripts/configs` folder. 

`config_graphblas-sharp.txt` chooses the device and work-group size.
`targets_graphblas-sharp.txt` contais all benchmarks that are going to be performed.
`targets` directory contains files with graph names corresponding to each benchmark.

Run all listed benchmarks.

```shell
python3 scripts/benchmark_graphblas-sharp.py
```

Result will be stored in `artifacts` directory.

#### 4.2 Other libraries

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

## Benchmark using workflows

This project supports automated benchmarks using github actions.

### 1. Getting source code

Since you'll need to commit config files and run benchmarks using your own action runner, fork of this repo is required.
Once you have your own repository, follow the [insctructions](#1-how-to-get-source-code) to set submodule for your own GraphBLAS-sharp repository.
You'll also need to [host your own actions runner](https://docs.github.com/en/actions/hosting-your-own-runners/adding-self-hosted-runners) on remote machine.

### 2. Uploading dataset

After your runner is hosted, dataset can be downloaded remotely using a script or copied to a folder manually. 

### 3. Benchmarking

Benchmarking workflow can be started by pushing a commit with conifgs.
Results are uploaded to github in action's summary as an artifact.

## License

This project licensed under MIT License. License text can be found in the
[license file](./LICENSE.md).

## Acknowledgments <img align="right" width="15%" src="https://github.com/EgorOrachyov/graph-bench/raw/main/docs/jetbrains-logo.png?raw=true&sanitize=true">

This is a research project of the Programming Languages and Tools Laboratory
at JetBrains-Research. Laboratory website [link](https://research.jetbrains.org/groups/plt_lab/).