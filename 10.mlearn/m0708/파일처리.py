import os

path=os.listdir('/Users/uk/Desktop/[라벨]맨몸운동_Labeling/')
path=[s for s in path if "DS_Store" not in s]
print(path)
for i in path:
    files=os.listdir(f'/Users/uk/Desktop/[라벨]맨몸운동_Labeling/{i}')
    print(i)
    print(files)
    files_2d=[s for s in files if "3d" not in s] 
    print(files_2d)