import psychopy.visual
import psychopy.event

window = psychopy.visual.Window(
    units = 'height',
    fullscr=True,
    color = (200, 200, 200),
    colorSpace = 'rgb255', 
    winType = 'pyglet',
    screen = 0
)

hi = psychopy.visual.TextStim(window, text = 'Hello World!')
hi.draw()
window.flip()

response = psychopy.event.waitKeys(keyList = ['space'])
