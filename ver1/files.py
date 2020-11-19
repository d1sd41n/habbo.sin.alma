import glob, os


def getImageNames():
    images = {}
    path = "assets/cafeteria"
    for image in os.listdir(path):
        pathfile = path + image
        images[image.split('.')[0]] = pathfile
    return images