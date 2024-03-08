import os
import shutil
import numpy as np

folder_path = "/home/flash/Downloads/lg_PfamTestingAlignments"
files = os.listdir(folder_path)

weights = []
for i, file_name in enumerate(files):
    file = os.path.join(folder_path, file_name)
    with open(file, "r") as f:
        n, m = f.readline().split()
        weights.append([int(n) * int(m), int(n), int(m), int(i)])

weights.sort()

"""
Choose 20 files here
"""
chosen_file = []
for i in range(0, len(weights), 20):
    chosen_file.append(weights[i][3])

print(chosen_file)
for i, file_name in enumerate(files):
    if i in chosen_file:
        # print("here")
        src_file = os.path.join(folder_path, file_name)
        des_file = os.path.join("/home/flash/pQMaker/example/custom-pfam", file_name)
        shutil.copy(src_file, des_file)