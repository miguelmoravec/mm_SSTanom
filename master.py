#!/usr/bin/env python

import subprocess
try:
    import pyferret
except ImportError:
    print "You must module load pyferret"
    exit(1)   

def mymain():

    basedir = '/archive/x1y/FMS/c3/CM2.1_ECDA/CM2.1R_ECDA_v3.1_1960_pfl_auto/gfdl.ncrc3-intel-prod-openmp/history/tmp/2016'
    filedir = "01.ocean_month.ensm.nc"

    print 'Please answer the following questions to plot SST anomalies over the Pacific for the last 4 months...'
    month = raw_input("Enter today's month (i.e. 09,10,11, etc): ")
    num = int(month)
    if num < 1 or num > 12:
	print 'invalid month input, please try again'
	exit(1)
    pre1 = '0' + str(num - 1)
    pre2 = '0' + str(num - 2)
    pre3 = '0' + str(num - 3)
    pre4 = '0' + str(num - 4)
    year = raw_input("Enter today's year (i.e. 15,16,17, etc): ")
    yr_num = int(year)
    if yr_num < 1 or num > 99:
	print 'invalid year input, please try again'
	exit(1)
    print 'Generating plots for months preceeding', month,'/', year, '...'

    dirWhereIwantThisToHappen="/home/mmm/SSTanom"
    child = subprocess.Popen(["dmget", basedir + pre1 + filedir, basedir + pre2 + filedir, basedir + pre3 + filedir, basedir + pre4 + filedir],cwd=dirWhereIwantThisToHappen)
    child.communicate() #this will close the subprocess

    pyferret.start(quiet=True)
    
    action="Go"
    fname="1head.jnl"
    cmd = ' '.join([action,fname])
    (errval, errmsg) = pyferret.run(cmd)

    action="Use"
    fname= basedir + pre1 + filedir
    cmd2 = ' '.join([action,fname])
    (errval, errmsg) = pyferret.run(cmd2)

    action="Go"
    fname="2body.jnl"
    cmd3 = ' '.join([action,fname])
    (errval, errmsg) = pyferret.run(cmd3)

    action="Use"
    fname=basedir + pre2 + filedir
    cmd4 = ' '.join([action,fname])
    (errval, errmsg) = pyferret.run(cmd4)

    action="Go"
    fname="3body.jnl"
    cmd5 = ' '.join([action,fname])
    (errval, errmsg) = pyferret.run(cmd5)
    
    action="Use"
    fname=basedir + pre3 + filedir
    cmd6 = ' '.join([action,fname])
    (errval, errmsg) = pyferret.run(cmd6)

    action="Go"
    fname="4body.jnl"
    cmd7 = ' '.join([action,fname])
    (errval, errmsg) = pyferret.run(cmd7)

    action="Use"
    fname=basedir + pre4 + filedir
    cmd8 = ' '.join([action,fname])
    (errval, errmsg) = pyferret.run(cmd8)

    action="Go"
    fname="5body.jnl"
    cmd9 = ' '.join([action,fname])
    (errval, errmsg) = pyferret.run(cmd9)

    cmd10 = 'FRAME/FILE=tempa_latest4mon_' + month + '_' + year + '.png'
    (errval, errmsg) = pyferret.run(cmd10)

    print 'Plots generated for months preceeding', month,'/', year, ', and are located at ', cmd10

if __name__=="__main__":
    mymain()



