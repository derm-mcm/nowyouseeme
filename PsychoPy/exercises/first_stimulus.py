from psychopy import visual, core  # import some libraries from PsychoPy

#create a window
mywin = visual.Window([800,600], monitor="testMonitor", units="deg")

#create some stimuli
grating = visual.GratingStim(win=mywin, mask="circle", size=3, pos=[-4,0], sf=3)
fixation = visual.GratingStim(win=mywin, size=0.5, pos=[0,0], sf=0, rgb=-1)

#draw the stimuli and update the window
# grating.draw()
# fixation.draw()
# mywin.update()


# for frameN in range(200):
while True: #this creates a never-ending loop
    grating.setPhase(0.05, '+')  # advance phase by 0.05 of a cycle
    grating.draw()
    fixation.draw()
    mywin.update()

    if len(event.getKeys())>0: break
    event.clearEvents()
#pause, so you get a chance to see it!
#core.wait(5.0)
