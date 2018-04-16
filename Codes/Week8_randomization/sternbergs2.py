# -*- coding: utf-8 -*-

import psychopy.visual
import psychopy.core
import psychopy.event

def runTrial(trial_index, trial_info, window):
    trial_index = 1
    trial_beginning_msg = psychopy.visual.TextStim(
        window,
        text = 'Beginning trial {}, good luck.'.format(trial_index)
    )
    trial_beginning_msg.draw()
    window.flip()
    psychopy.core.wait(1.0)

    for i in range(trial_info['setsize']):
        stim = psychopy.visual.TextStim(window, text = trial_info['stimuli'][i])
        stim.draw()
        window.flip()
        psychopy.core.wait(trial_info['display_duration'])

    eol_msg = psychopy.visual.TextStim(window, text = '*')
    eol_msg.draw()
    window.flip()
    psychopy.core.wait(1.0)

    probe_text = psychopy.visual.TextStim(window, text = trial_info['probe'])
    probe_text.draw()
    window.flip()

    response = psychopy.event.waitKeys(
        keyList = ['o', 'n']
    )

    return response

window = psychopy.visual.Window()

# greeting message
hi = psychopy.visual.TextStim(window, text = 'Welcome to the classic memory experiment.')
hi.draw()
window.flip()

psychopy.core.wait(1.0)

# setting up trial
trial_info = {
    'setsize': 6,
    'display_duration': 500/1000.0,
    'stimuli': [
        'bent',
        'cart',
        'line',
        'birth',
        'mogen',
        'excuse'
    ],
    'probe_type': 'old',
    'serial_position': 3,
    'probe': 'line'
}

runTrial(1, trial_info, window)