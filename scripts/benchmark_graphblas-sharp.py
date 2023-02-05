import subprocess
import config
import csv
import os
import json

#Copy local configs and datasets to source
config_directory = config.ROOT / "scripts" / "configs"
dest_directory = config.DEPS / "graphblas-sharp" / "benchmarks" / "GraphBLAS-sharp.Benchmarks"
subprocess.call(f'cp {config_directory / "config_graphblas-sharp.txt"} {dest_directory / "Configs" / "Context.txt"}', shell=True)
subprocess.call(f'rsync -a {config_directory / "targets"}/ {dest_directory / "Configs"}', shell=True)
subprocess.call(f'rsync -a {config.DATASET}/ {dest_directory / "Datasets"}', shell=True)

targets = [line.strip() for line in open(config_directory / "targets_graphblas-sharp.txt", 'r').readlines()]

#Clearing previous results
dotnet_artifacts = config.ROOT / "BenchmarkDotNet.Artifacts" / "results"
artifacts = config.ROOT / "artifacts"
subprocess.call(f'rm { dotnet_artifacts / "*"}', shell=True)
subprocess.call(f'rm { artifacts / "*"}', shell=True)

#Executing benchmarks
for target in targets:
	project_directory = config.DEPS / "graphblas-sharp" / "benchmarks" / "GraphBLAS-sharp.Benchmarks"
	binaries = project_directory / "bin" / "Release" / "net7.0"
	subprocess.call(f'dotnet {binaries / "GraphBLAS-sharp.Benchmarks.dll"} --exporters csv briefjson --filter *{target}*', shell=True)

#Copying results for uploading
subprocess.call(f'rsync -a {dotnet_artifacts}/ {artifacts}', shell=True)

#Parsing matrix names in jsons to draw charts(FullName = matrix.mtx)
json_files = [file for file in os.listdir(artifacts) if file.endswith(".json")]

for file in json_files:
	with open(artifacts / file, "r+") as file:
		data = json.load(file)
		for benchmark in data["Benchmarks"]:	
			name_field = benchmark["FullName"] 
			matrix_name = name_field.split(":")[-1][:-1].strip()
			print(matrix_name)
			benchmark["FullName"] = matrix_name

		file.seek(0)
		json.dump(data, file)
		file.truncate()