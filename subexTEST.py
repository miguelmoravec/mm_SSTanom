#!/usr/bin/env python

import subprocess
try:
    import pyferret
except ImportError:
    print "You must module load pyferret"
    exit(1)
    ## or could
    #raise
    ##which will print the "traceback", but that could be long and people might not see your "hint"
    
#import argparse ##is the package you'd (probably) want to use for command line argument stuff

def doesStuff():
    print "what you'd want to run when executing form the cmd line"    
    
def mymain():

    print 'Please answer the following questions to plot SST anomalies over the Pacific for the last 4 months...'
    month = raw_input('What month is it today: ')
    year = raw_input('What year is it today: ')
    print 'Generating plots for ', month, year, ' and preceeding three months...'

    # #doesStuff()
    
    # dirWhereIwantThisToHappen="."
    # #runs abitrary shell command
    # child = subprocess.Popen(["ls","-ltr"],cwd=dirWhereIwantThisToHappen)
    # child.communicate() #this will close the subprocess

    # ### This example captures stdout, and stderr
    # ##child = subprocess.Popen(["ls","-ltr"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd=dirWhereIwantThisToHappen)
    # ##out,err = child.communicate() #this returns the stdout and stderr from your child process
    # ##print out

    # ###can also use "stdin" to pipe data into a child if you need.
    
    # returnCode = child.returncode #this is the *nix return code, 0 is usually success

    # ###simple
    # #    child = subprocess.Popen(["myprogramcall","myfilename"])    

    # #ends subprocess example

    ################## PYFERRET example
    ##startup
    pyferret.start(quiet=True)

    ###most basic, type cmd fully
    ##cmd = 'use coads_climatology'

    #here you use simple string concat
    #set our intended fileset
    ##myfname = "coads_climatology"
    ##construct the pyferret command
    ##cmd = "use " + myfname

    action="Go"
    fname="may16.jnl"
    #cmd = "%s %s" %(action,fname)
    cmd = ' '.join([action,fname]) #lets say your "action" operates with many files #' '.join([action,f1,f2,f3,])
    
    #execute the cmd
    (errval, errmsg) = pyferret.run(cmd)

    #another cmd
    #cmd2 = 'show data'
    #(errval, errmsg) = pyferret.run(cmd2)
    
        
    

if __name__=="__main__":
    mymain()



