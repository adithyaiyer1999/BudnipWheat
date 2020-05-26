import numpy as np

def NDVI(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = ((img[7]-img[3])/(img[7]+img[3]))
    arr = np.nan_to_num(arr)
    return arr

def AFRI1(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = ((img[8]-0.66*img[11])/(img[8]+0.66*img[3]))
    arr = np.nan_to_num(arr)

    return arr

def BNDVI(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = ((img[7]-img[1])/(img[7]+img[1]))
    return arr


def BRI(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = (1/img[2]-1/img[4])/img[5]
    arr = np.nan_to_num(arr)
    return arr

def BWDWVI(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = (0.1*img[6]-img[1])/(0.1*img[6]-img[1])
    arr = np.nan_to_num(arr)
    return arr

def CCCI(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = ((img[7]-img[4])/(img[7]+img[4])) / ((img[7]-img[3])/(img[7]+img[3]))  
    arr = np.nan_to_num(arr)
    return arr


def CVI(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = ((img[7]*img[3])/(img[2]*img[2]))
    arr = np.nan_to_num(arr)
    return arr

def DATT1(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = ((img[7]-img[4])/(img[7]+img[3]))
    return arr

def DVI(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = 2.4*img[7]-img[3]
    arr = np.nan_to_num(arr)
    return arr

def EVI(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = 2.5*((img[7]-img[3])/(img[7]+6*img[3]-7.5*img[1]+1))
    arr = np.nan_to_num(arr)
    return arr

def GARI(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = ((img[7]-img[2]+img[1]-img[3])/(img[7]-img[2]-img[1]+img[3]))
    arr = np.nan_to_num(arr)
    return arr

def GNDVI(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = ((img[7]-img[2])/(img[7]+img[2]))
    arr = np.nan_to_num(arr)
    return arr

def GLI(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = (2*img[2]-img[4]-img[1])/(2*img[2]+img[4]+img[1])
    arr = np.nan_to_num(arr)
    return arr

def GNDVI2(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = ((img[6]-img[2])/(img[6]+img[2]))
    arr = np.nan_to_num(arr)
    return arr

def GRNDVI(img):
    arr = np.zeros((img.shape[0]+1,img.shape[1],img.shape[2]))
    arr[0:img.shape[0]] = img
    arr[img.shape[0]] = ((img[7]-img[2]+img[4])/(img[7]+img[2]-img[4]))
    arr = np.nan_to_num(arr)
    return arr


def allIndices(img):
    # 12
    arr = NDVI(img)
    ###
    arr = AFRI1(arr)
    arr = BNDVI(arr)
    #arr = BRI(arr)#15
    #arr = BWDWVI(arr)#16
    ##arr = CCCI(arr)#17
    #arr = CVI(arr)#18
    arr = DATT1(arr)
    arr = DVI(arr)
    #arr = EVI(arr)#21
    #arr = GARI(arr)
    arr = GNDVI(arr)
    arr = GLI(arr)
    arr = GNDVI2(arr)
    
    return arr

def normalize(x):
    z = (x - x.mean(axis=(1,2), keepdims=True)) / x.std(axis=(1,2), keepdims=True)
    z = np.nan_to_num(z)
    return z








