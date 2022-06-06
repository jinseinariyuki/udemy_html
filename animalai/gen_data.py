from operator import index
from PIL import Image
import os,glob
import numpy as np
from sklearn import cross_validation

classes = ["monkey","boar","crow"]
num_classes = len(classes)
image_size = 50

#画像の読み込み

X = []
Y = []
for index, class in enumerate(classes):
    photos_dir = "./" + class
    files = glob.glob(phjotos_dir + "/*.jpg")
    for i, file in enumerate(files):
    if i > 200: break
    image = Image.open(file)
    image = Image.convert("RGB")
    image = Image.resize((image_size,image_size))
    data = np.asarray(image)
    X.append(data)
    Y.append(index)

X = np.array(X)
Y = np.array(Y)