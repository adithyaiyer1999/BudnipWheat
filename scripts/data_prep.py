import rasterio
from rasterio.mask import mask
import geopandas as gpd
import pandas as pd
import pandas as pd
from matplotlib import pyplot as plt
import fiona
import rasterio
import rasterio.plot
import matplotlib as mpl
from descartes import PolygonPatch
import numpy as np
import os
from rasterio import plot
from rasterio.plot import show

def raster_to_df(raster):
    df = pd.DataFrame()
    i = 0
    for i in range(1,13):
        img = raster.read(i)
        df['B'+str(i)] = img.flatten()
    return df

def vector_to_df(raster):
    df = pd.DataFrame()
    i = 0
    
    for band in raster:
        i +=1
        df['B'+str(i)] = band.flatten()
    
    return df 

def vectorFilePreprocessing(vector,raster):
    crs_of_raster = (raster.crs.data['init']).upper()
    vector_projected = vector.to_crs("EPSG:32632")
    
    vector_projected = vector_projected[vector_projected['geometry'].area>150]
    vector_projected['geometry']= vector_projected['geometry'].buffer(-3)
    
    return vector_projected

def make_dataframe_with_bands(vector_path,raster_path):
    raster = rasterio.open(raster_path)
    vector = gpd.read_file(vector_path)
    vector = vectorFilePreprocessing(vector,raster)
    
    out_img, out_transform = mask(raster, vector['geometry'], crop=True,filled = False)
    df_final = vector_to_df(out_img.data)
    
    values =(((out_img.mask[0]==False)*1).flatten())
    
    df_final['isWheat'] = values
    return df_final
    
    
    
    
    
    
    
    
    
    
    
    