from dem2basin import dem2basin

shape_input = "/work/08449/kag/stampede2/DEM2basin/references/south_east_texas_smallest_area.geojson"
coverage_input ="/work/08449/kag/stampede2/DEM2basin/references/TNRIS_LIDAR_AVAILABILITY_dirname_exists.geojson"
dem_tile_projects_parent_directory ="/scratch/projects/tnris/tnris-lidardata"
new_coverage_file_parameter = "/work/08449/kag/stampede2/DEM2basin/references/new_coverage_smallest_area_SEtexas_normal.shp"
new_coverage_file_out = "/work/08449/kag/stampede2/DEM2basin/references/new_coverage_smallest_area_SEtexas_out_normal.shp"
bounding_box_se_texas = dem2basin.get_bounding_boxes_from_coverage_by_shape(shape_input,coverage_input,dem_tile_projects_parent_directory,new_coverage_file = new_coverage_file_parameter)
bounding_box_se_texas.to_file(new_coverage_file_out)
