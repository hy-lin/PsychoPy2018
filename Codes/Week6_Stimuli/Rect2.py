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

rect = psychopy.visual.Rect(
    window,
    width = 0.2,
    height = 0.2,
    lineWidth = 5,
    lineColor = (0, 0, 0),
    lineColorSpace = 'rgb255',
    fillColor = None,
)
rect.draw()

window.flip()

response = psychopy.event.waitKeys(keyList = ['space'])