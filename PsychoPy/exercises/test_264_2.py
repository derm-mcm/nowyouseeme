#!/usr/bin/env python2

#This is an extended version of the base timeByFrames demo, adding
#the ability to set the psychopy experiment runtime process priority
#and disable python garbage collection to see if either influences
#the precision of your frame flips.

import gc, numpy
from psychopy import visual, logging, core, event
from matplotlib import *


nIntervals = 500
visual.useFBO=True #if available (try without for comparison)
disable_gc = False
process_priority = 'normal' # 'high' or 'realtime'

if process_priority == 'normal':
    pass
elif process_priority == 'high':
    core.rush(True)
elif process_priority == 'realtime':
    # Only makes a diff compared to 'high' on Windows.
    core.rush(True, realtime = True)
else:
    print 'Invalid process priority:',process_priority,"Process running at normal."
    process_priority = 'normal'

if disable_gc:
    gc.disable()

import matplotlib
matplotlib.use('Qt4Agg')#change this to control the plotting 'back end'
import numpy as np
import matplotlib.pyplot as plt


win = visual.Window([1280,800], fullscr=True, allowGUI=False, waitBlanking=True)
progBar = visual.PatchStim(win, tex=None, mask=None,
    size=[0,0.05],color='red',pos=[0,-0.9],
    autoLog=False)
myStim = visual.PatchStim(win, tex='sin', mask='gauss',
    size=300,sf=0.05, units='pix',
    autoLog=False)
#logging.console.setLevel(logging.INFO)#uncomment if you want to print every frame time

fliptimes = numpy.zeros(nIntervals+1)

win.recordFrameIntervals = True
for frameN in range(nIntervals+1):
    progBar.setSize([2.0*frameN/nIntervals, 0.05])
    progBar.draw()
    myStim.setPhase(0.1,'+')
    myStim.setOri(1,'+')
    myStim.draw()
    if event.getKeys():
        print 'stopped early'
        break
    win.logOnFlip(msg='frame=%i' %frameN, level=logging.EXP)
    fliptimes[frameN] = win.flip()

if disable_gc:
    gc.enable()
core.rush(False)

win.close()

#calculate some values
intervalsMS = np.array(win.frameIntervals)*1000
m=np.mean(intervalsMS)
sd=np.std(intervalsMS)
# se=sd/pylab.sqrt(len(intervalsMS)) # for CI of the mean
nTotal=len(intervalsMS)
nDropped=sum(intervalsMS>(1.5*m))
ifis= (fliptimes[1:]-fliptimes[:-1])*1000

#plot the frameintervals
plt.figure(figsize=[12,8],)

plt.subplot2grid((2, 2),(0, 0),colspan=2)
plt.plot(intervalsMS, '-')
plt.ylabel('t (ms)')
plt.xlabel('frame N')
plt.title("Dropped/Frames = %i/%i = %.3f%%. Process Priority: %s, GC Disabled: %s" %(nDropped,nTotal, 100*nDropped/float(nTotal),process_priority,str(disable_gc)), fontsize=12)
#
plt.subplot2grid((2, 2),(1, 0))
plt.hist(intervalsMS, 50, normed=0, histtype='stepfilled')
plt.xlabel('t (ms)')
plt.ylabel('n frames')
plt.title("win.frameIntervals\nMean=%.2fms, s.d.=%.2f, 99%%CI(frame)=%.2f-%.2f" %(m,sd,m-2.58*sd,m+2.58*sd), fontsize=12)

#
plt.subplot2grid((2, 2),(1, 1))
plt.hist(ifis, 50, normed=0, histtype='stepfilled')
plt.xlabel('t (ms)')
plt.ylabel('n frames')
plt.title("Inter Flip Intervals\nMean=%.2fms, s.d.=%.2f, range=%.2f-%.2f ms"%(ifis.mean(), ifis.std(),ifis.min(), ifis.max()), fontsize=12)

plt.tight_layout()
plt.show()
