# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# python script.py
# Created on: 2024-10-21 14:59:37.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
arcpy.CheckOutExtension('Spatial')
import os

arcpy.env.overwriteOutput = True

tifdir = r"C:\Users\Zengx\Desktop\ArcGIS\Lab\Lab6\Data 6.1 Precipitation\month"
mask = r"C:\Users\Zengx\Desktop\ArcGIS\Lab\Lab6\Data 6.1 Precipitation"

for tif in os.listdir(tifdir):
	if tif.endswith


# Local variables:
v2010_05_tif = "2010-05.tif"
china_dem_60s_tif = "china_dem_60s.tif"
ext_201005 = "C:\\Users\\Zengx\\Desktop\\ArcGIS\\Lab\\Lab6\\Data 6.1 Precipitation\\ext_201005"

# Process: Extract by Mask
arcpy.gp.ExtractByMask_sa(v2010_05_tif, china_dem_60s_tif, ext_201005)

