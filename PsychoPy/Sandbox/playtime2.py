# -*- coding: utf-8 -*-

"""
First Attempt at creating two stimuli side-by-side
* Two stimuli together X
* Then have them turning on and off
* One will flash
* Increase flash to flicker
* Choose which is flickering
* Stairwise increase in flicker speed
* Randomize which side flickers
** Record Results!
Dermott McMorrough, 2016.
"""


# -----------------------------
# STIMULUS TYPES AND PROPERTIES
# -----------------------------

# Modules
from psychopy import core, visual, gui, data, event, monitors
from psychopy.tools.filetools import fromFile, toFile



try:#try to get a previous parameters file
    expInfo = fromFile('lastParams.pickle')
except:#if not there then use a default set
    expInfo = {'observer':'jwp', 'refOrientation':0}

# Here, we load up a dialogue box to set up parameters for the experiment.
#present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='simple Exp', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo)#save params to file for next time
else:

    #make a text file to save data
fileName = expInfo['observer'] + expInfo['dateStr']
dataFile = open(fileName+'.csv', 'w')#a simple text file with 'comma-separated-values'

#create the staircase handler
staircase = data.StairHandler(startVal = 20.0,
                          stepType = 'db', stepSizes=[8,4,4,2,2,1,1],
                          nUp=1, nDown=3,  #will home in on the 80% threshold



win = visual.Window()
win.color = 'black'
#stim_text = visual.TextStim(win, text='Welcome', color='black')
#stim_text.draw()
#win.flip()
#event.waitKeys()
my_monitor = monitors.Monitor('testMonitor', width=34.3, distance=65)
my_monitor.setSizePix([1024, 768])

win.close()
win = visual.Window(monitor=my_monitor, color='black')

stim_shape1 = visual.ShapeStim(win, units='cm', size=5,
    fillColorSpace='dkl', fillColor=[0, 45, 1], pos=[3, 0])  # strong, medium luminance
stim_shape2 = visual.ShapeStim(win, units='cm', size=5,
    fillColorSpace='dkl', fillColor=[0, 215, 0.3], pos=[-3, 0],  # should be a pale isoluminant contrast color
    vertices=[[0,0], [1,0], [1,1], [0,1]])
stim_shape2.vertices -= [0.5, 0.5]

stim_shape1.draw()
stim_shape2.draw()
win.flip()
event.waitKeys()

# Try to combine these two sections. 
#-------------------------------------------------------------------------------


                          #create window and stimuli
win = visual.Window([800,600],allowGUI=True, monitor='testMonitor', units='deg')
foil = visual.GratingStim(win, sf=1, size=4, mask='gauss', ori=expInfo['refOrientation'])
target = visual.GratingStim(win, sf=1, size=4, mask='gauss', ori=expInfo['refOrientation'])
fixation = visual.GratingStim(win, color=-1, colorSpace='rgb', tex=None, mask='circle',size=0.2)

#and some handy clocks to keep track of time
globalClock = core.Clock()

#display instructions and wait
message1 = visual.TextStim(win, pos=[0,+3],text='Hit a key when ready.')
message2 = visual.TextStim(win, pos=[0,-3],
    text="Then press left or right to identify the %.1f deg probe." %expInfo['refOrientation'])
message1.draw()
message2.draw()
fixation.draw()
win.flip()#to show our newly drawn 'stimuli'
#pause until there's a keypress
