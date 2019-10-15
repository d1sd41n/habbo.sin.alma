import glob, os
# os.chdir("/mydir")
# for file in glob.glob("assets/cafeteria/*.png"):
#     print(file)


    # import os
path = "assets/cafeteria"
for filename in os.listdir(path):
    pathfile = path + filename
    print (filename.split('.')[0])
    print(pathfile)