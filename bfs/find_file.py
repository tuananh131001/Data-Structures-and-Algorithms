from os import listdir
from os.path import isfile, join
from collections import deque

# Loop through all the folder and files in the currnet folder, if node is a file, print out it names, if node is folder, add it to queue to continue search
def printnames(start_dir):
    queue = deque()
    queue.append(start_dir)
    while queue:
        path = queue.popleft()
        print(path)
        for file in sorted(listdir(path)):
            fullpath = join(path, file)
            if isfile(fullpath):
                print(fullpath)
            else:
                queue.append(fullpath)
printnames("new")
