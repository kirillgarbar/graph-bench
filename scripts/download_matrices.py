import config
import os
import ssgetpy

present_matrices = os.listdir(DATASET)

for matrix in GRAPHS_NAMES:
	file_name = matrix + ".mtx"
	if file_name not in present_matrices:
		ssgetpy.search(name=matrix)[0].download(format='MM', destpath=DATASET, extract=True)
	os.rename(DATASET/matrix/file_name, DATASET/file_name)