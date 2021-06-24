import os
from pathlib import Path
from FCG import *
from christofides import *
from time import perf_counter
import matplotlib.pyplot as plt



# a loop for some instances in random folder using FCG algorithm 

def plt_FCG():
    runtime=[]
    dat=[]

    pathlist = Path(os.getcwd()+"\\random").glob('**/*.dat')
    for path in pathlist:
    # because path is object not string
        file= str(path)
        dat.append(file[file.index('t'):-4])   # get the files noun from random folder
        start = perf_counter()
        solve_FCG(file)
        runtime.append(perf_counter()-start)
    plt.figure(figsize=(7,7))    
    plt.bar(dat, runtime)
    plt.xlabel('Instance')
    plt.xticks(rotation=90)
    plt.ylabel('run-time in seconds')
    plt.show
    plt.savefig('fig1')
    return 






# plot for instances from random folder using chritofides algorithm

def plt_chrisf():
    runtime=[]
    dat=[]

    pathlist = Path(os.getcwd()+"\\random").glob('**/*.dat')
    for path in pathlist:
    # because path is object not string
        file= str(path)
        dat.append(file[file.index('t'):-4])   # get the files label from random folder
        start = perf_counter()
        christof(file)
        runtime.append(perf_counter()-start)
    plt.figure(figsize=(14,11))    
    plt.plot(dat, runtime)
    plt.xlabel('Instance')
    plt.xticks(rotation=90)
    plt.ylabel('run-time in seconds')
    plt.show
    plt.savefig('fig2')
    return 




# plots for some instances from tsp library

def plt_tsplib():
    runtime=[]
    dat=['berlin52','rd100','pr136','tsp225','pcb442', 'p654']
    pathlist=[]
    for e in dat:
        path=os.getcwd()+"\\tsplib\\"+e+".dat"
        pathlist.append(path)
    
    for path in pathlist:
        start = perf_counter()
        christof(path)                           # change name for solve_FCG
        runtime.append(perf_counter()-start)
    plt.figure(figsize=(14,11))    
    plt.plot(dat, runtime)
    plt.xlabel('Instance')
    plt.xticks(rotation=90)
    plt.ylabel('run-time in seconds')
    plt.show
    plt.savefig('fig3')
    return 

        
    