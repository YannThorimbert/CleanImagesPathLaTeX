""" This script gathers all the needed images in a LaTeX file in a same, common
folder. Then, it rewrites the path of the different images to point to the
new folder.

Usage : open the script, insert the parameters as indicated and then run the
script.

Author : Yann Thorimbert 2019
"""
import os, shutil


fn = "./LICENSE"
new_fn = "./new_main.tex"
tag = "includegraphics" #will select the images typically
root = "./" #root of the project
dst = "./gather_all_images" #path of the new folder where all the files go

with open(fn, "r") as f:
    lines = f.readlines()

#1. Select files
for line in lines:
    if tag in line:
        if "{" in line and "}" in line:
            filename = line.split("{")[1].split("}")[0]
            filename = os.path.join(root, filename)
            target = os.path.join(dst, os.path.basename(filename))
            print("Copying", filename, "to", target)
            try:
                shutil.copy(filename, target)
            except:
                print("Could not copy", filename, "to", target)
        else:
            print("Line with no { and } :", line)


#2. Rewrite paths
f = open(new_fn, "w")
for line in lines:
    if tag in line:
        if "{" in line and "}" in line:
            part1 = line.split("{")[0]
            part3 = line.split("}")[-1]
            filename = line.split("{")[1].split("}")[0]
            new_filename = os.path.basename(filename)
            line = part1+"{"+new_filename+"}"+part3
    f.write(line)
f.close()
