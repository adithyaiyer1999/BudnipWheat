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

def vector_to_df(raster):
    '''
    Input : Raster file after rasterio.open
    
    Output : pandas dataframe
    
    '''
    
    df = pd.DataFrame()
    i = 0
    
    for band in raster:
        i +=1
        df['B'+str(i)] = band.flatten()
    
    return df 

def vectorFilePreprocessing(vector,raster):
    '''
    Input : Vector file after gpd.read_file
            Raster after rasterio.open
    
    '''
    
    crs_of_raster = (raster.crs.data['init']).upper()
    vector_projected = vector.to_crs(crs_of_raster)
    
    print (vector_projected.crs)
    # Area selection > 150 m square and removing boundaries
    vector_projected = vector_projected[vector_projected['geometry'].area>150]
    vector_projected['geometry']= vector_projected['geometry'].buffer(-3)
    
    return vector_projected

def make_dataframe_with_bands(vector_path,raster_path):
    '''
    Input : path to vector shapefile (String)
            path to raster image (String)
            
    Output : Pandas Dataframe object
    
    '''
    
    raster = rasterio.open(raster_path)
    vector = gpd.read_file(vector_path)
    vector = vectorFilePreprocessing(vector,raster)
    
    out_img, out_transform = mask(raster, vector['geometry'], crop=True,filled = False)
    df_final = vector_to_df(out_img.data)
    
    values =(((out_img.mask[0]==False)*1).flatten())
    
    df_final['isWheat'] = values
    return df_final

def split_image_into_516x516(vector_path,raster_path):
    
    '''
    Input : path to vector shapefile (String)
            path to raster image (String)
            
    Output : Pandas Dataframe object with n images split as represented by different columns
    
    '''
    
    raster = rasterio.open(raster_path)
    vector = gpd.read_file(vector_path)
    vector = vectorFilePreprocessing(vector,raster)
    
    out_img, out_transform = mask(raster, vector['geometry'], crop=True,filled = False)
    
    row_multiple = int((out_img.data.shape)[1]/516)
    column_multiple = int((out_img.data.shape)[2]/516)
    df = pd.DataFrame()
    t = 0
    for i in range(1,row_multiple+1):
        for j in range(1,column_multiple+1):
            l = 0
            t = t+1
            for band in out_img.data:
                l = l+1
                df['img_'+str(t)+'B'+str(l)] = band[512*(i-1):512*i,512*(j-1):512*j].flatten()
            values =(((out_img.mask[0][512*(i-1):512*i,512*(j-1):512*j]==False)*1).flatten())
            df['img_'+str(t)+'isWheat'] = values
    
    
    return df
                
    
    
    
    
    
    
    
    
    
    
    
    
