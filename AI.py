from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import os
import numpy as np

def load_dataset():
    kotak=[]
    segitiga=[]
    lingkaran=[]
    centang=[]
    silang=[]
    love=[]

    for file in os.listdir("kotak"):
        img = Image.open("kotak/"+file)
        img = np.array(img)
        img = img.flatten()
        kotak.append(img)
    
    for file in os.listdir("lingkaran"):
        img = Image.open("lingkaran/"+file)
        img = np.array(img)
        img = img.flatten()
        lingkaran.append(img)

    for file in os.listdir("segitiga"):
        img = Image.open("segitiga/"+file)
        img = np.array(img)
        img = img.flatten()
        segitiga.append(img)

    for file in os.listdir("centang"):
        img = Image.open("centang/"+file)
        img = np.array(img)
        img = img.flatten()
        centang.append(img)

    for file in os.listdir("silang"):
        img = Image.open("silang/"+file)
        img = np.array(img)
        img = img.flatten()
        silang.append(img)

    for file in os.listdir("love"):
        img = Image.open("love/"+file)
        img = np.array(img)
        img = img.flatten()
        love.append(img)

    return kotak, lingkaran, segitiga, centang, silang, love

def load_ai():
    model = KNeighborsClassifier(n_neighbors=5)
    print("[INFO] Loading Dataset")
    kotak, lingkaran, segitiga, centang, silang, love= load_dataset()
    print("[INFO] Loading Model")
    y_kotak = np.zeros(len(kotak))
    y_lingkaran = np.ones(len(lingkaran))
    y_segitiga = np.ones(len(segitiga)) * 2
    y_centang = np.ones(len(centang)) * 3
    y_silang = np.ones(len(silang)) * 4
    y_love = np.ones(len(love)) * 5

    x = kotak + lingkaran + segitiga + centang + silang + love
    y = np.concatenate([y_kotak, y_lingkaran, y_segitiga, y_centang, y_silang, y_love])
    model.fit(x, y)
    return model