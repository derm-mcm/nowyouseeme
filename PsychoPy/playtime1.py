# -*- coding: utf-8 -*-

"""
First Attempt at creating two stimuli side-by-side
* Two stimuli together
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

# Generic layout
from psychopy import visual, event, monitors
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
