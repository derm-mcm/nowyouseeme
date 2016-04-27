from psychopy import visual, core

#setup stimulus
win=visual.Window([400,400])
gabor = visual.GratingStim(win, tex='sin', mask='gauss', sf=5,
    name='gabor', autoLog=False)
fixation = visual.GratingStim(win, tex=None, mask='gauss', sf=0, size=0.02,
    name='fixation', autoLog=False)

clock = core.Clock()
#let's draw a stimulus for 2s, drifting for middle 0.5s
for frameN in range(200):#for exactly 200 frames
    if 10 <= frameN < 150:  # present fixation for a subset of frames
        fixation.draw()
    if 50 <= frameN < 100:  # present stim for a different subset
        gabor.setPhase(0.1, '+')  # increment by 10th of cycle
        gabor.draw()
    win.flip()
