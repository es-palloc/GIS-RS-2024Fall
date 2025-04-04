# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# single statistics.py
# Created on: 2024-10-28 15:04:31.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
arcpy.CheckOutExtension('Spatial')
import os
import re

arcpy.env.overwriteOutput = True


# Local variables:
Province = "C:\\Users\\Zengx\\Desktop\\ArcGIS\\Lab\\Lab6\\Data 6.1 Precipitation\\Province.shp"
tifdir = "C:\\Users\\Zengx\\Desktop\\ArcGIS\\Lab\\Lab6\\Data 6.1 Precipitation\\month"


for tif in os.listdir(tifdir):
    print(tif)
    if re.findall(r'\d*_\d*.tif', tif):
        input_file = tifdir + os.sep + tif
        print(input_file)
        output_file = tifdir + os.sep + tif[:-4] + " statistics.dbf"
        print(output_file)
        arcpy.gp.ZonalStatisticsAsTable_sa(Province, "NAME", input_file, output_file, "DATA", "ALL")
        print(output_file + "is finished!")

