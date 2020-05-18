import numpy as np

def giveImages(numpy_image):
    img = np.zeros((8,numpy_image.shape[0],numpy_image.shape[1],numpy_image.shape[2]))
    img[0] = numpy_image
    img[1] = np.rot90(numpy_image, k=1, axes=(1,2))
    img[2] = np.rot90(numpy_image, k=2, axes=(1,2))
    img[3] = np.rot90(numpy_image, k=3, axes=(1,2))
    img[4]= np.flip(img[0],1)
    img[5] = np.flip(img[1],1)
    img[6]= np.flip(img[2],1)
    img[7] = np.flip(img[3],1)
    
    return img
    
def giveImagesForMask(numpy_image):
    img = np.zeros((8,numpy_image.shape[0],numpy_image.shape[1]))
    img[0] = numpy_image
    img[1] = np.rot90(numpy_image, k=1)
    img[2] = np.rot90(numpy_image, k=2)
    img[3] = np.rot90(numpy_image, k=3)
    img[4]= np.flip(img[0],0)
    img[5] = np.flip(img[1],0)
    img[6]= np.flip(img[2],0)
    img[7] = np.flip(img[3],0)
    
    return img    
    