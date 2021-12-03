#!/bin/bash
##
##------------------------------------------------------------------------------
## Usage:
##  sbatch node_task_processor.sbatch.sh --job 1 --path_img ../geoflood_docker_tacc.sif --path_sh node_task_processor.sh --path_log geoflood_singularity.log --path_cmds workflow_commands-geoflood_singularity.sh --path_cmd_outputs workflow_outputs-geoflood_singularity.txt --path_rc workflow_configuration-geoflood_singularity.sh --queue development --start_time $(date -u +%s) HUC1 HUC2 HUC3
##
## Workflow that returns height-above-nearest-drainage (HAND) from source data  
## Author: Daniel Hardesty Lewis
## Copyright: Copyright 2020, Daniel Hardesty Lewis
## Credits: Daniel Hardesty Lewis
## License: GPLv3
## Version: 1.0.0
## Maintainer: Daniel Hardesty Lewis
## Email: dhl@tacc.utexas.edu
## Status: Production
##
## This Stampede-2 job script is designed to create a GeoFlood session on 
## KNL long nodes through the SLURM batch system. Once the job
## is scheduled, check the output of your job (which by default is
## stored in your home directory in a file named hand-taudem.out)
##
## Aspects of this scripts were incorporated from `job.vnc`
##  located at /share/doc/slurm/job.vnc on stampede2.tacc.utexas.edu
##
## Note: you can fine tune the SLURM submission variables below as
## needed.  Typical items to change are the runtime limit, location of
## the job output, and the allocation project to submit against (it is
## commented out for now, but is required if you have multiple
## allocations).  
##
## To submit the job, issue: "sbatch hand-taudem.sbatch.sh" 
##
## For more information, please consult the User Guide at: 
##
## https://portal.tacc.utexas.edu/user-guides/stampede2
##-----------------------------------------------------------------------------
##
#SBATCH -J dem2basin_bounds_SE_Texas_development.%j    # Job name
#SBATCH -o dem2basin_bounds_SE_Texas_development.o%j    # Name of stdout output file (%j expands to jobId)
#SBATCH -e dem2basin_bounds_SE_Texas_devepoment.e%j    # Name of stderr error file (%j expands to jobId)
#SBATCH -p development ## <- change this line to 'normal' and then resubmit it         # Queue name
#SBATCH -N 1                  # Total number of nodes requested (48 cores/node)
#SBATCH -n 67                 # Total number of mpi tasks requested
#SBATCH -t 02:00:00    ## <- if above line is 'normal', then this should be '48:00:00'      # Run time (hh:mm:ss) - 2 hours
#SBATCH -A PT2050-DataX

##------------------------------------------------------------------------------
##------- You normally should not need to edit anything below this point -------
##------------------------------------------------------------------------------

module unload python2
eval "$(conda shell.bash hook)"
conda activate dem2basin

DEM2BASIN_KAG=/work/08449/kag/stampede2/DEM2basin

cd $DEM2BASIN_KAG/src

python3 $DEM2BASIN_KAG/src/get_bounds_for_projects_se_development_Texas.py
