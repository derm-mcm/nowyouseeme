from psychopy import core, visual, gui, data, event

primeStim.draw()
win.flip()
my_clock.reset()

for frameN in range(3):
    primeStim.draw()
    win.flip()
timing = my_clock.getTime()
timing = timing*1000
print(timing)
