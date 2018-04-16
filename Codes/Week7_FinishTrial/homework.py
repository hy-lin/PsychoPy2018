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

target = 3
normal_rotation = 1

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
response = None
t0 = psychopy.core.getTime()

while response is None:
    orientation += 1
    if orientation >= 360:
        orientation = 0

    # for rect in rects:
    for i in range(6):
        if i == target-1:
            rects[i].ori = orientation * normal_rotation * -1
        else:
            rects[i].ori = orientation * normal_rotation

        if mouse.isPressedIn(rects[i], buttons = [0]):
            rects[i].fillColor = (255, 0, 0)
            response = i+1
           
        rects[i].draw()

    window.flip()
    psychopy.core.wait(0.01667)

correctness = response == target
RT = psychopy.core.getTime() - t0

print([response, correctness, RT])
