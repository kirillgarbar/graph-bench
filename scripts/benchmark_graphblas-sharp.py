import subprocess
import config
import csv

#Copy local configs and datasets to source
config_directory = config.ROOT / "scripts" / "configs"
dest_directory = config.DEPS / "graphblas-sharp" / "benchmarks" / "GraphBLAS-sharp.Benchmarks"
subprocess.call(f'cp {config_directory / "config_graphblas-sharp.txt"} {dest_directory / "Configs" / "Context.txt"}', shell=True)
subprocess.call(f'cp -a {config.DATASET / "."} {dest_directory / "Datasets"}')

matrices = [matrix + ".mtx" for matrix in config.GRAPHS_NAMES]
targets = [line.strip() for line in open(config_directory / "graphblas-sharp_targets.txt", 'r').readlines()]

for target in targets:
	#Writing config for each target
	with open(f'{dest_directory / "Configs" / "{target}.txt"}', 'w') as file:
		file.writelines(m + "\n" for m in matrices)

	#Executing benchmarks
	project_directory = config.DEPS / "graphblas-sharp" / "benchmarks" / "GraphBLAS-sharp.Benchmarks"
	binaries = project_directory / "bin" / "Release" / "net7.0"
	subprocess.call(f'dotnet {binaries / "GraphBLAS-sharp.Benchmarks.dll"} --exporters json --filter *{target}*', shell=True)

	#TODO: Copying csv for uploading