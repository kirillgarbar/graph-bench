import subprocess
import config
import csv

#Copy local configs to source
config_directory = config.ROOT / "scripts"
dest_directory = config.DEPS / "graphblas-sharp" / "benchmarks" / "GraphBLAS-sharp.Benchmarks" / "Configs"
subprocess.call(f'cp {config_directory / "config_graphblas-sharp.txt"} {dest_directory / "Context.txt"}', shell=True)

matrices = [matrix + ".mtx" for matrix in GRAPHS_NAMES]

with open(f'{dest_directory / "BFSBenchmarks.txt"}', 'w') as file:
	file.writelines(matrices)

#Executing benchmarks
project_directory = config.DEPS / "graphblas-sharp" / "benchmarks" / "GraphBLAS-sharp.Benchmarks"
binaries = project_directory / "bin" / "Release" / "net7.0"
subprocess.call(f'dotnet {binaries / "GraphBLAS-sharp.Benchmarks.dll"} --exporters json --filter *BFSBenchmarks*')