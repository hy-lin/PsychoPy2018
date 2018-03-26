from psychopy import visual
from psychopy import core
from psychopy import event
import numpy

import Trials


def pos2ang(mouse_pos):
    x, y = mouse_pos
    dist = numpy.sqrt(x**2 + y**2)
    ang = numpy.arccos(abs(x/dist)) * 180 / numpy.pi

    if x < 0 and y > 0:
        ang = ang
    elif x < 0 and y <= 0:
        ang = 360 - ang
    elif x >=0 and y <= 0:
        ang = ang + 180
    elif x >=0 and y > 0:
        ang = 180 - ang
    
    if ang >= 360:
        ang = ang - 360
    
    return int(ang)


def pressedAKEY():
    print('You pressed a key!')

win = visual.Window([1280, 720],
                    fullscr=True,
                    units = 'height', 
                    colorSpace = 'rgb255', 
                    color = (0, 0, 0), 
                    screen = 1)

# event.globalKeys.clear()
# event.globalKeys.add(key='Ctrl', func = pressedAKEY)

exp_setting = Trials.ExpSetting()

sti_ori = Trials.OrientationStimulus(30, exp_setting, win = win, pos = (0, 0.1))

sti_col = Trials.ColorStimulus(30, exp_setting, win = win, pos = (0, -0.1))

trial = Trials.Trial('Hello World', [sti_ori, sti_col], sti_col, exp_setting)

sti_poly = visual.ShapeStim(win, vertices = ((-0.5, -0.5), (-0.5, -0.2), (-0.2, -0.2), (-0.2, -0.4)))

mouse = event.Mouse(win = win)

# sti_line = visual.Line(win, start = (-0.5, 0), end=(0, 0))
# sti_circle = visual.Circle(win, 0.25)

# # sti = visual.BufferImageStim(win, stim = [sti_line, sti_circle])

# # sti.setAutoDraw(True)
# ori = 10




# pressed = []

# while 'space' not in pressed:
#     sti_poly.draw()
#     # mouse_pos = mouse.getPos()
#     # ang = pos2ang(mouse_pos)

#     # sti_ori.update(ang)
#     pressed = event.getKeys(['space'])

#     win.flip()


# print(win.fps(), win.getMsPerFrame(msg='Please stand by'))
trial.run(win)
print(trial)

# # while True:
#     core.wait(0.1)
#     sti.ori += 10
#     sti.draw()

#     print(sti.ori)

#     win.flip(True)