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

    word_candidates = numpy.random.choice(
        word_list,
        trial_info['setsize']+1,
        replace = False
    )

    trial_info['serial_position'] = numpy.random.randint(trial_info['setsize']) + 1
    trial_info['stimuli'] = word_candidates[0:trial_info['setsize']]
    if trial_info['probe_type'] == 'old':
        trial_info['probe'] = trial_info['stimuli'][trial_info['serial_position']-1]
    else:
        trial_info['probe'] = word_candidates[trial_info['setsize']]
        trial_info['probe'] = numpy.random.choice(word_list, 1)[0]
        while trial_info['probe'] in trial_info['stimuli']:
            trial_info['probe'] = numpy.random.choice(word_list, 1)[0]
        # trial_info['probe'] = word_list[10]

    trial_info['display_duration'] = 500/1000.0

    return trial_info

def runTrial(trial_index, trial_info, window):
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

    t0 = psychopy.core.getTime()
    response = psychopy.event.waitKeys(
        keyList = ['o', 'n']
    )
    RT = psychopy.core.getTime() - t0

    return response[0] == 'o', RT

def saveTrial(trial_info, save_file, pID):
    max_setsize = 6

    output_string = '' # initiate 
    output_string += '{}\t'.format(pID)
    output_string += '{}\t'.format(trial_info['display_duration'])
    output_string += '{}\t'.format(trial_info['setsize'])
    output_string += '{}\t'.format(trial_info['probe_type'])
    output_string += '{}\t'.format(trial_info['serial_position'])
    
    for stimulus in trial_info['stimuli']:
        output_string += '{}\t'.format(stimulus)

    for i in range(max_setsize - trial_info['setsize']):
        output_string += 'xxx\t'
        
    output_string += '{}\t'.format(trial_info['probe'])
    output_string += '{}\t'.format(trial_info['response'])
    output_string += '{}\t'.format(trial_info['correctness'])
    output_string += '{}\n'.format(trial_info['RT'])
    
    save_file.write(output_string)

############ MAIN CODE ############
window = psychopy.visual.Window()

pID = 1

word_list = []
word_file = codecs.open('C:\\Users\\user\\Documents\\GitHub\\PsychoPy2018\\Codes\\Week8_randomization\\WordList.txt', 'r', encoding='utf-8')
for line in word_file:
    word_list.append(line.rstrip()) # removing '\n' in the end of the line
    
word_file.close()

# open save file
save_file = codecs.open('save_file.txt', 'a', encoding='utf-8')

# greeting message
hi = psychopy.visual.TextStim(window, text = 'Welcome to the classic memory experiment.')
hi.draw()
window.flip()

psychopy.core.wait(1.0)

# practice trials
n_practice_trials = 2
condition_indexes = numpy.random.choice(range(12), n_practice_trials, replace = False)
for i in range(n_practice_trials):
    condition_index = condition_indexes[i]
    trial_info = getTrialInfo(condition_index, word_list)
    runTrial(i+1, trial_info, window)

# actual experiment trials
condition_indexes = numpy.arange(2)
condition_indexes = condition_indexes % 12

numpy.random.shuffle(condition_indexes)

for i, condition in enumerate(condition_indexes):
    trial_info = getTrialInfo(condition, word_list)
    response, RT = runTrial(i+1, trial_info, window)
    trial_info['response'] = int(response) + 1
    trial_info['RT'] = RT

    if trial_info['response'] == 2:
        if trial_info['probe_type'] == 'old':
            trial_info['correctness'] = 1
        else:
            trial_info['correctness'] = 0
    else:
        if trial_info['probe_type'] == 'old':
            trial_info['correctness'] = 0
        else:
            trial_info['correctness'] = 1

    saveTrial(trial_info, save_file, pID)

save_file.close()