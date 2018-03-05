import psychopy.visual

window = psychopy.visual.Window()

hi = psychopy.visual.TextStim(window, text = 'Hello World!')
hi.draw()

window.flip()

response = raw_input('Press enter to exit')
