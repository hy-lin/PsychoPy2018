# -*- coding: utf-8 -*-

import psychopy.visual
import psychopy.core
import psychopy.event
import numpy.random
import codecs

def getTrialInfo(condition_index, word_list):
    setsizes = [1, 2, 3, 4, 5, 6]
    probe_types = ['old', 'new']
    trial_info = {
        'setsize': setsizes[condition_index // 2],
        'probe_type': probe_types[condition_index % 2]
    }

    trial_info['serial_position'] = numpy.random.randint(trial_info['setsize']) + 1
    trial_info['stimuli'] = numpy.random.choice(
        word_list,
        trial_info['setsize'],
        replace = False
    )
    if trial_info['probe_type'] == 'old':
        trial_info['probe'] = trial_info['stimuli'][trial_info['serial_position']-1]
    else:
        trial_info['probe'] = numpy.random.choice(word_list, 1)

    trial_info['display_duration'] = 500/1000.0

    return trial_info

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

############ MAIN CODE ############
window = psychopy.visual.Window()

word_list = []
word_file = codecs.open('WordList.txt', 'r', encoding='utf-8')
for line in word_file:
    word_list.append(line.rstrip()) # removing '\n' in the end of the line
    
word_file.close()

# greeting message
hi = psychopy.visual.TextStim(window, text = 'Welcome to the classic memory experiment.')
hi.draw()
window.flip()

psychopy.core.wait(1.0)

# setting up trial
# trial_info = {
#     'setsize': 6,
#     'display_duration': 500/1000.0,
#     'stimuli': [
#         'bent',
#         'cart',
#         'line',
#         'birth',
#         'mogen',
#         'excuse'
#     ],
#     'probe_type': 'old',
#     'serial_position': 3,
#     'probe': 'line'
# }

trial_info = getTrialInfo(11, word_list)

runTrial(1, trial_info, window)