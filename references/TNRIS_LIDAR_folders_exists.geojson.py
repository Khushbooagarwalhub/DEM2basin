from dem2basin import dem2basin
from osgeo import gdal
(exit)
exit()
exit
\q
conda env list
cdw
exit
exit()
\q
exit()
import fiona
import rasterio
 rasterio.open /scratch/projects/tnris/tnris-lidardata
rasterio.open /scratch/projects/tnris/tnris-lidardata
pwd
ls
rasterio.open /scratch/projects/tnris/tnris-lidardata/watershed-boundary-dataset/wbd_hydrologic_unit_06.shp
exit()
from dem2basin import dem2basin
ls
dem2basin
dir(dem2basin)
dir
exit()
from dem2basin import dem2basin
dir(dem2basin)
ls
print(dem2basin.methods)
from inspect import getmembers, isfunction
print(getmembers(dem2basin, isfunction))
print(dir(dem2basin))
print(dir(get_catchments_by_huc))
import dem2basin
from dem2basin import *
exit()
from dem2basin import dem2basin
dem2basin
dem2basin.
exit()
import dem2basin
dem2basin.
exit()
from dem2basin import dem2basin
import dem2basin
dem2basin.
ls
exit()
import geopandas as gpd
exit()
rasterio.open("/scratch/projects/tnris/tnris-lidardata/stratmap-2018-50cm-upper-coast/dem")
import rasterio
cd("/scratch/projects/tnris/tnris-lidardata/stratmap-2018-50cm-upper-coast/dem")
rasterio.open("/scratch/projects/tnris/tnris-lidardata/stratmap-2018-50cm-upper-coast/dem")
rasterio.open("/scratch/projects/tnris/tnris-lidardata/stratmap-2018-50cm-upper-coast/dem/stratmap18-1m-2995554a3.img")
rasterio.open("/scratch/projects/tnris/tnris-lidardata/usgs-2018-70cm-texas-west-central/dem/usgs18-1m_14SLB210810.img")
rasterio.open("/scratch/projects/tnris/tnris-lidardata/stratmap-2018-50cm-upper-coast/dem/stratmap18-1m_2995554a3.img
rasterio.open("/scratch/projects/tnris/tnris-lidardata/stratmap-2018-50cm-upper-coast/dem/stratmap18-1m_2995554a3.img")
import dem2basin
;
import dem2basin
pwd
import dem2basin
exit()
conda activate
import dem2basin
import dem2basin_callgraph
dem2basin_callgraph.pycallgraph_bounding_boxes_smallest_tx_hu12()
exit()
import geopandas as gpd
fp = "/scratch/projects/tnris/dhl-flood-modelling/TNRIS-LIDAR-Availability-20210812.shp"
data = gpd.read_file(fp)
type(data)
data.head()
print(data[demname]
print(data["demname"])
len(data)
for i in range(0,len(data):
for i in range(0,len(data)):
 print(i)
for i in range(0,len(data)):
path_list = []
import geopandas as gpd
fp = "/scratch/projects/tnris/dhl-flood-modelling/TNRIS-LIDAR-Availability-20210812.shp"
path = "/scratch/projects/tnris/tnris-lidardata/"
subdir = "dem"
data = gpd.read_file(fp)
type(data)
data.head()
#print(data["demname"])
#len(data)
path_list = []
for i in range(0,len(data)):
   path_list.append(path + data["dirname"] + subdir + data["demname"] )
print path_list[0:10]
print len(path_list)
print (path_list[0:10])
print (len(path_list))
for i in range(0,len(data)):
   path_list.append(path + data["dirname"] + subdir + data["demname"] )
print (data["dirname"][0])
path_list = []
for i in range(0,len(data)):
   path_list.append(path + data["dirname"][i] + subdir + data["demname"][i] )
print (path_list[0:10])
print (len(path_list))
path_list = []
for i in range(0,len(data)):
   path_list.append(path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".img" )
print (path_list[0:10])
print (len(path_list))
path_list = []
for i in range(0,len(data)):
   path_list.append(path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".img" )
print (path_list[0:10])
print (len(path_list))
import geopandas as gpd
import os.path
fp = "/scratch/projects/tnris/dhl-flood-modelling/TNRIS-LIDAR-Availability-20210812.shp"
path = "/scratch/projects/tnris/tnris-lidardata/"
subdir = "dem"
data = gpd.read_file(fp)
type(data)
data.head()
#print(data["demname"])
#len(data)
path_exists_list = []
path_not_exists_list = []
for i in range(0,len(data)):
    file_path = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".img"
    if (os.path.exists(file_path)):
        path_exists_list.append(file_path)
    else:
        path_not_exists_list.append(file_path)
for i in range(0,10):
    file_path = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".img"
    if (os.path.exists(file_path)):
        path_exists_list.append(file_path)
    else:
        path_not_exists_list.append(file_path)
print (len(path_exists_list))
print (len(path_not_exists_list))
print (path_not_exists_list[0:10])
print (path_not_exists_list)
import geopandas as gpd
import os.path
fp = "/scratch/projects/tnris/dhl-flood-modelling/TNRIS-LIDAR-Availability-20210812.shp"
path = "/scratch/projects/tnris/tnris-lidardata/"
subdir = "dem"
data = gpd.read_file(fp)
type(data)
data.head()
#print(data["demname"])
#len(data)
path_exists_list = []
path_not_exists_list = []
for i in range(0,len(data)):
    file_path = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".img"
    if (os.path.exists(file_path)):
        path_exists_list.append(file_path)
    else:
        path_not_exists_list.append(file_path)
print (len(path_exists_list))
print (len(path_not_exists_list))
print (path_not_exists_list[0:10])
print (path_not_exists_list)
exit()
import geopandas as gpd
import os.path
fp = "/scratch/projects/tnris/dhl-flood-modelling/TNRIS-LIDAR-Availability-20210812.shp"
path = "/scratch/projects/tnris/tnris-lidardata/"
subdir = "dem"
data = gpd.read_file(fp)
type(data)
data.head()
path_exists_list = []
path_not_exists_list = []
for i in range(0,len(data)):
    file_path = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".img"
    if (os.path.exists(file_path)):
        path_exists_list.append(file_path)
    else:
        path_not_exists_list.append(file_path)
print (len(path_exists_list))
print (len(path_not_exists_list))
print (path_not_exists_list[0:10])
import geopandas as gpd
import os.path
fp = "/scratch/projects/tnris/dhl-flood-modelling/TNRIS-LIDAR-Availability-20210812.shp"
path = "/scratch/projects/tnris/tnris-lidardata/"
subdir = "dem"
data = gpd.read_file(fp)
type(data)
data.head()
#print(data["demname"])
#len(data)
path_exists_list = []
path_not_exists_list = []
for i in range(0,len(data)):
    file_path = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".img"
    file_path1 = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".dem"
    file_path2 = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".tiff"
    file_path3 = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".jpg"
    if (os.path.exists(file_path) | os.path.exists(file_path1) | os.path.exists(file_path2) | os.path.exists(file_path3)):
        path_exists_list.append(file_path)
    else:
        path_not_exists_list.append(file_path)
print (len(path_exists_list))
print (len(path_not_exists_list))
print (path_not_exists_list[0:10])
path_exists_list = []
path_not_exists_list = []
for i in range(0,len(data)):
    file_path = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".img"
    file_path1 = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".dem"
    file_path2 = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".tiff"
    file_path3 = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".jpg"
    if (os.path.exists(file_path)):
        path_exists_list.append(file_path)
    elif (os.path.exists(file_path1)):
        path_exists_list.append(file_path1)
    elif (os.path.exists(file_path2)):
        path_exists_list.append(file_path2)
    elif (os.path.exists(file_path3)):
        path_exists_list.append(file_path3)
    else:
        path_not_exists_list.append(file_path)
path_exists_list = []
path_not_exists_list = []
for i in range(0,len(data)):
    file_path = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".img"
    file_path1 = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".dem"
    file_path2 = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".tiff"
    file_path3 = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".jpg"
    if (os.path.exists(file_path)):
        path_exists_list.append(file_path)
    elif (os.path.exists(file_path1)):
        path_exists_list.append(file_path1)
    elif (os.path.exists(file_path2)):
        path_exists_list.append(file_path2)
    elif (os.path.exists(file_path3)):
        path_exists_list.append(file_path3)
    else:
        path_not_exists_list.append(file_path)
print (len(path_exists_list))
print (len(path_not_exists_list))
print (len(path_exists_list))
print (len(path_not_exists_list))
print (path_exists_list)
path_exists_list = []
path_not_exists_list = []
count_img = 0
count_dem = 0
count_tiff = 0
count_jpg = 0
for i in range(0,len(data)):
    file_path = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".img"
    file_path1 = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".dem"
    file_path2 = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".tiff"
    file_path3 = path + data["dirname"][i] + "/" + subdir + "/" + data["demname"][i] + ".jpg"
    if (os.path.exists(file_path)):
        path_exists_list.append(file_path)
        count_img+=1
    elif (os.path.exists(file_path1)):
        path_exists_list.append(file_path1)
        count_dem+=1
    elif (os.path.exists(file_path2)):
        path_exists_list.append(file_path2)
        count_tiff+=1
    elif (os.path.exists(file_path3)):
        path_exists_list.append(file_path3)
        count_jpg+=1
    else:
        path_not_exists_list.append(file_path)
print (len(path_exists_list))
print(count_img,count_dem,count_tiff,count_jpg)
print (len(path_not_exists_list))
print (path_not_exists_list[0:10])
exit()
import dem2basin
import sqlAlchemy
exit()
import dem2basin
import sqlAlchemy
conda install flask_sqlalchemy
exit()
import sqlAlchemy
exit()
from flask_sqlalchemy import SQLAlchemy
exit()
idev
shape_input = "/work/08449/kag/stampede2/WBD-TX-Smallest_HU12.geojson"
coverage_input ="/scratch/projects/tnris/dhl-flood-modelling/TNRIS-LIDAR-Availability-20210812.shp"
dem_tile_projects_parent_directory ="/scratch/projects/tnris/tnris-lidardata"
dem2basin.get_bounding_boxes_from_coverage_by_shape(shape_input,coverage_input,dem_tile_projects_parent_directory)
import dem2basin
import geopandas as gpd
dem2basin.get_bounding_boxes_from_coverage_by_shape(shape_input,coverage_input,dem_tile_projects_parent_directory)
 shape_input = "/work/08449/kag/stampede2/WBD-TX-Smallest_HU12.geojson"
shape_input = "/work/08449/kag/stampede2/WBD-TX-Smallest_HU12.geojson"
coverage_input ="/scratch/projects/tnris/dhl-flood-modelling/TNRIS-LIDAR-Availability-20210812.shp"
dem_tile_projects_parent_directory ="/scratch/projects/tnris/tnris-lidardata"
dem2basin.get_bounding_boxes_from_coverage_by_shape(shape_input,coverage_input,dem_tile_projects_parent_directory)
exit()
import dem2basin
import geopandas as gpd
shape_input = "/work/08449/kag/stampede2/WBD-TX-Smallest_HU12.geojson"
coverage_input ="/scratch/projects/tnris/dhl-flood-modelling/TNRIS-LIDAR-Availability-20210812.shp"
dem_tile_projects_parent_directory ="/scratch/projects/tnris/tnris-lidardata"
dem2basin.get_bounding_boxes_from_coverage_by_shape(shape_input,coverage_input,dem_tile_projects_parent_directory)
bounding_box =dem2basin.get_bounding_boxes_from_coverage_by_shape(shape_input,coverage_input,dem_tile_projects_parent_directory)
bounding_box
bounding_box.to_csv("bounding_box.csv",index=False)
scp kag@remotehost.edu:bounding_box.csv /local/dir
bounding_box.describe()
bounding_box.info()
bounding_box[lidar_file].type
bounding_box["lidar_file"].type
bounding_box["lidar_file"].dtype
bounding_box
bounding_box.columns
coverage_input ="/scratch/projects/tnris/dhl-flood-modelling/TNRIS-LIDAR-Availability-20210812.shp"
coverage =gpd.read_file("/scratch/projects/tnris/dhl-flood-modelling/TNRIS-LIDAR-Availability-20210812.shp")
coverage
project_coverage = coverage.dissolve(by=['dirname'])
project_coverage.to_file('/work/08449/kag/stampede2/TNRIS-LIDAR-BYPROJECT.geojson',driver ='GeoJSON')
projects = []
for project in project_coverage.index:
        projects = append_subdirectory(
            projects,
            dem_tile_projects_parent_directory,
            project,
            'dem'
        )
dem_tile_project_parent_directory = "/scratch/projects/tnris/tnris-lidardata"
project_coverage.reset_index()
project_coverage.reset_index(drop=False,inplace =True)
project_coverage
project_coverage['dirname_absolute']=project_coverage['dirname'].apply(lambda dirname: Path(dem_tile_projects_parent_directory).joinpath(dirname)
)
import Pathlib from Path
import Pathlib from path
from pathlib from Path
from pathlib import Path
project_coverage['dirname_absolute']=project_coverage['dirname'].apply(lambda dirname: Path(dem_tile_projects_parent_directory).joinpath(dirname))
project_coverage['dirname_absolute'].apply(lambda dirname : dirname.is_dir())
project_coverage['dirname_exists']=project_coverage['dirname_absolute'].apply(lambda dirname : dirname.is_dir())
project_coverage['dirname_dem']=project_coverage['dirname_absolute'].apply(lambda dirname : dirname.joinpath('dem'))
project_coverage['dirname_dem']=project_coverage['dirname_absolute'].apply(lambda dirname : dirname.joinpath('tiles'))
project_coverage['dirname_dem']=project_coverage['dirname_absolute'].apply(lambda dirname : dirname.joinpath('dem'))
project_coverage['dirname_tiles']=project_coverage['dirname_absolute'].apply(lambda dirname : dirname.joinpath('tiles'))
project_coverage['dirname_dem'].apply(lambda dirname : dirname.is_dir())
project_coverage["dirname_dem_exists"]=project_coverage['dirname_dem'].apply(lambda dirname : dirname.is_dir())
project_coverage["dirname_tiles_exists"]=project_coverage['dirname_tiles'].apply(lambda dirname : dirname.is_dir())
project_coverage["dirname_tiles_exists"]
project_coverage["dirname_dem_exists"]
project_coverage.to_file('/work/08449/kag/stampede2/DEM2basin/references/TNRIS_LIDAR_folders_exists.geojson',driver ='GeoJSON')
project_coverage_converted = project_coverage.copy()
project_coverage_converted.columns
project_coverage['dirname_absolute'].apply(lambda dirname :str(dirname))
project_coverage_converted['dirname_absolute']=project_coverage_converted['dirname_absolute'].apply(lambda dirname :str(dirname))
project_coverage_converted['dirname_dem_exists']=project_coverage_converted['dirname_dem_exists'].apply(lambda dirname :str(dirname))
project_coverage_converted['dirname_dem']=project_coverage_converted['dirname_dem'].apply(lambda dirname :str(dirname))
project_coverage_converted['dirname_tiles']=project_coverage_converted['dirname_tiles'].apply(lambda dirname :str(dirname))
project_coverage_converted['dirname_dem_exists']=project_coverage['dirname_dem_exists']
project_coverage_converted.to_file('/work/08449/kag/stampede2/DEM2basin/references/TNRIS_LIDAR_folders_exists.geojson',driver ='GeoJSON')
import readline
readline.write_history_file('/work/08449/kag/stampede2/DEM2basin/references/TNRIS_LIDAR_folders_exists.geojson.py')
