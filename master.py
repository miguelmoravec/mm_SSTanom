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

    math1 = date + datetime.timedelta(days=-30)
    pre1 =  math1.strftime('%Y%m') #generates date in format of nc files

    math2 = date + datetime.timedelta(days=-60)
    pre2 =  math2.strftime('%Y%m')

    math3 = date + datetime.timedelta(days=-90)
    pre3 =  math3.strftime('%Y%m')

    math4 = date + datetime.timedelta(days=-120)
    pre4 =  math4.strftime('%Y%m')

    print 'Generating plots for months preceeding', month,'/', year, '...'

    dirWhereIwantThisToHappen="."
    child = subprocess.Popen(["dmget", basedir + pre1 + filedir, basedir + pre2 + filedir, basedir + pre3 + filedir, basedir + pre4 + filedir, "/archive/x1y/yxue/realtime/temp.clim.1981_2010.nc"],cwd=dirWhereIwantThisToHappen)
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

    print 'Plots (if generated) for months preceeding', month,'/', year, ' are located in the local directory and are named ', cmd10

if __name__=="__main__":
    mymain()



