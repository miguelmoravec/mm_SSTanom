#!/usr/bin/env python

import subprocess
import datetime

try:
    import pyferret
except ImportError:
    print "You must module load pyferret"
    exit(1)   

def mymain():    

    basedir = '/archive/x1y/FMS/c3/CM2.1_ECDA/CM2.1R_ECDA_v3.1_1960_pfl_auto/gfdl.ncrc3-intel-prod-openmp/history/tmp/'
    filedir = "01.ocean_month.ensm.nc"

    print 'Please answer the following questions to plot SST anomalies over the Pacific for the last 4 months...'
    today = raw_input("Enter today's date (mmyyyy): ")
    
    date = datetime.datetime.strptime('25' + today, '%d%m%Y')
    
    month = date.strftime('%m')
    year = date.strftime('%Y')

    print 'Generating plots for months preceeding', month,'/', year, '...'

    pyferret.start(quiet=True)
    
    cmd = "Go 1head.jnl"
    (errval, errmsg) = pyferret.run(cmd)

    count = 0

    while (count < 4):
	
	count = count + 1

    	math = date + datetime.timedelta(days=(-30*count))
    	prev_date =  str(math.strftime('%Y%m'))
        prev_month =  str(math.strftime('%m'))

	dirWhereIwantThisToHappen="."
        child = subprocess.Popen(["dmget", basedir + prev_date + filedir, "/archive/x1y/yxue/realtime/temp.clim.1981_2010.nc"],cwd=dirWhereIwantThisToHappen)
        child.communicate() #this will close the subprocess

        cmd1 ="Use " + basedir + prev_date + filedir
        (errval, errmsg) = pyferret.run(cmd1)

        cmd2 = 'Let diff1 = temp[d=' + str(count+1) + ',l=1] - temp[d=1,l=' + prev_month + ']'
        (errval, errmsg) = pyferret.run(cmd2)

        cmd3 = 'set viewport V' + str(count)
        (errval, errmsg) = pyferret.run(cmd3)

        cmd4 = "Go 2body_alt.jnl"
        (errval, errmsg) = pyferret.run(cmd4)


    cmd9 = 'set mode/last verify'
    (errval, errmsg) = pyferret.run(cmd9)

    cmd10 = 'FRAME/FILE=tempa_latest4mon_' + month + '_' + year + '.png'
    (errval, errmsg) = pyferret.run(cmd10)

    print 'Plots (if data was available in archive) for 4 months preceeding', month,'/', year, ' are located in the local directory and are named ', cmd10

if __name__=="__main__":
    mymain()



