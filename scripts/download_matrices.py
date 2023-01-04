import config
import os
import ssgetpy

present_matrices = os.listdir(config.DATASET)

for matrix in config.GRAPHS_NAMES:
	file_name = matrix + ".mtx"
	if file_name not in present_matrices:
		ssgetpy.search(name=matrix)[0].download(format='MM', destpath=config.DATASET, extract=True)
		os.rename(config.DATASET/matrix/file_name, config.DATASET/file_name)
		os.rmdir(config.DATASET/matrix)