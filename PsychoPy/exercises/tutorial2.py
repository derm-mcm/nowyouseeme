from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile


try:#try to get a previous parameters file
    expInfo = fromFile('lastParams.pickle')
except:#if not there then use a default set
    expInfo = {'observer':'jwp', 'refOrientation':0}

#present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='simple JND Exp', fixed=['dateStr'])
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
