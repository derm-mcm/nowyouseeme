from psychopy import visual, core

win = visual.Window([400,400])
message = visual.TextStim(win, text='hello')
message.setAutoDraw(True)  # automatically draw every frame
win.flip()
core.wait(2.0)
message.setText('world')  # change properties of existing stim
win.flip()
core.wait(2.0)
