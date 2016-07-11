#!/usr/bin/env python

#This script automatically generates plots of SST anomlies over the Pacific for the preceding 4 months
#This script relies on a standard naming convention of SST NetCDF files in this directory: /archive/x1y/FMS/c3/CM2.1_ECDA/CM2.1R_ECDA_v3.1_1960_pfl_auto/gfdl.ncrc3-intel-prod-openmp/history/tmp/
#This script also relies on the historical data located in this archived file: /archive/x1y/yxue/realtime/temp.clim.1981_2010.nc

import subprocess
import datetime
import os

try:
	import pyferret
except ImportError:
	print "You must module load pyferret"
	exit(1)   

def mymain():    

	#the following sets file naming convention and time variables, used in generation of NetCDFs, plots, and file names

	basedir = '/archive/x1y/FMS/c3/CM2.1_ECDA/CM2.1R_ECDA_v3.1_1960_pfl_auto/gfdl.ncrc3-intel-prod-openmp/history/tmp/'
	filetail = "01.ocean_month.ensm.nc"

	print 'Please answer the following question to plot SST anomalies over the Pacific for the last 4 months...'
	today = raw_input("Enter desired end date (mmyyyy): ")
    
	date = datetime.datetime.strptime('25' + today, '%d%m%Y')
    
	month = date.strftime('%m')
	year = date.strftime('%Y')

	#the following automates the pyferret plot generation and saves a png image file in the local directory	

	print 'Generating plots for months preceeding', month,'/', year, '...'

	filename = 'tempa_latest4mon_' + month + '_' + year + '.png'

	pyferret.start(quiet=True)
	os.remove("ferret.jnl")
    
	header()

	count = 0

	while (count < 4):
	
		count = count + 1

    		math = date + datetime.timedelta(days=(-30*count))
    		prev_date =  str(math.strftime('%Y%m'))
        	prev_month =  str(math.strftime('%m'))

		dirWhereIwantThisToHappen="."
        	child = subprocess.Popen(["dmget", basedir + prev_date + filetail, "/archive/x1y/yxue/realtime/temp.clim.1981_2010.nc"],cwd=dirWhereIwantThisToHappen)
        	child.communicate()

        	cmd1 ="Use " + basedir + prev_date + filetail
        	cmd2 = 'Let diff1 = temp[d=' + str(count+1) + ',l=1] - temp[d=1,l=' + prev_month + ']'
       	 	cmd3 = 'set viewport V' + str(count)

        	(errval, errmsg) = pyferret.run(cmd1)
        	(errval, errmsg) = pyferret.run(cmd2)
        	(errval, errmsg) = pyferret.run(cmd3)

		body()

	cmd9 = 'set mode/last verify'
	cmd10 = 'FRAME/FILE=' + filename

	(errval, errmsg) = pyferret.run(cmd9)
	(errval, errmsg) = pyferret.run(cmd10)

	print 'The image file containing the SST anomoly plots for the 4 months preceeding ', month,'/', year, ' is located in the local directory (if data was available in archive) and is named: ', filename
	print 'If no plots generated, please see script comments to find necessary input files.'

def header():

	com2 = 'cancel data/all'
	com3 = 'def sym print_opt $1"0"'
	com4 = 'define VIEWPORT/xlim=0.,0.5/ylim=0.5,1.0 V1'
	com5 = 'define VIEWPORT/xlim=0.,0.5/ylim=0.,0.5 V2'
	com6 = 'define VIEWPORT/xlim=0.5,1.0/ylim=0.5,1.0 V3'
	com7 = 'define VIEWPORT/xlim=0.5,1.0/ylim=0.,0.5 V4'
	com8 = 'set mem/size=240'
	com9 = 'use "/archive/x1y/yxue/realtime/temp.clim.1981_2010.nc"'

	(errval, errmsg) = pyferret.run(com2)
	(errval, errmsg) = pyferret.run(com3)
	(errval, errmsg) = pyferret.run(com4)
	(errval, errmsg) = pyferret.run(com5)
	(errval, errmsg) = pyferret.run(com6)
	(errval, errmsg) = pyferret.run(com7)
	(errval, errmsg) = pyferret.run(com8)
	(errval, errmsg) = pyferret.run(com9)

def body():

	com10 = 'cancel mode nodata_lab'
	com11 = 'fill/lev=(-inf)(-7,-3,1)(-3,3,0.5)(3,7,1)(inf)/PALETTE=blue_darkred diff1[z=0:300,y=2s:2n@ave,x=120e:78w]'

	(errval, errmsg) = pyferret.run(com10)
	(errval, errmsg) = pyferret.run(com11)

if __name__=="__main__":
    mymain()
