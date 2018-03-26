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

mouse = psychopy.event.Mouse(win = window)

frame_pos = [
    (-0.2, 0.3),
    (-0.4, 0.0),
    (-0.2, -0.3),
    (0.2, -0.3),
    (0.4, 0.0),
    (0.2, 0.3)
]

rects = []
for i in range(6):
    rects.append(
        psychopy.visual.Rect(
            window,
            width = 0.2,
            height = 0.2,
            lineWidth = 5,
            lineColor = (0, 0, 0),
            lineColorSpace = 'rgb255',
            fillColor = None,
            fillColorSpace = 'rgb255',
            pos = frame_pos[i], 
        )
    )


orientation = 0
response = []

while 'space' not in response:
    orientation += 1
    if orientation >= 360:
        orientation = 0

    for rect in rects:
        rect.ori = orientation

        if mouse.isPressedIn(rect, buttons = [0]):
            rect.fillColor = (255, 0, 0)
            
        rect.draw()

    window.flip()
    response = psychopy.event.getKeys(keyList = ['space'])
    psychopy.core.wait(0.01667)