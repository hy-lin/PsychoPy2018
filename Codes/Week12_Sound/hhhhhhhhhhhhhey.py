import psychopy.visual
import psychopy.event

import psychopy.sound
import psychopy.core

def heyListen(window):
    showMessage('HEY LISTEN', window)

    hey = psychopy.sound.Sound('hey2.wav', stereo = True)
    listen = psychopy.sound.Sound('listen2.wav', stereo = True)
    hey.play()
    psychopy.core.wait(hey.getDuration())
    listen.play()

def showMessage(msg, window, autopilot = False):
    msg_stim = psychopy.visual.TextStim(
        window,
        text = msg
    )
    msg_stim.draw()
    window.flip()

window = psychopy.visual.Window(
    units = 'height',
    fullscr=False,
    color = (200, 200, 200),
    colorSpace = 'rgb255', 
    winType = 'pyglet',
    screen = 0
)

zelda = psychopy.sound.Sound(
    'zelda_theme.wav',
    volume = 0.5,
    startTime = 27.5
)
zelda.play()

while True:
    response = psychopy.event.getKeys()
    if 'space' in response:
        break
    if response != []:
        heyListen(window)
    else:
        psychopy.core.wait(0.01)
        window.flip()