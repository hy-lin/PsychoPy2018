import psychopy.visual
import psychopy.core

window = psychopy.visual.Window()

# greeting message
hi = psychopy.visual.TextStim(window, text = 'Welcome to the classic memory experiment.')
hi.draw()
window.flip()

# setting up trial
setsize = 6 
display_duration = 200  # in ms.
ISI = 2000 # in ms.
display_duration = display_duration / 1000.0  # in s.
ISI = ISI / 1000.0

stimuli = ['bent',
           'cart',
           'line',
           'birth',
           'ultra',
           'excuse']

probe_type = 'old'
serial_position = 3
probe = stimuli[serial_position-1]

# let's run it!
trial_index = 1
trial_beginning_msg = psychopy.visual.TextStim(
    window,
    text = 'Beginning trial {}, good luck.'.format(trial_index)
)
trial_beginning_msg.draw()
window.flip()

for i in range(setsize):
    stim = psychopy.visual.TextStim(window, text = stimuli[i])
    stim.draw()
    window.flip()
    #psychopy.core.wait(display_duration)

    t0 = psychopy.core.getTime()
    response = psychopy.event.waitKeys(maxWait = display_duration, keyList = ['c', 'a'])
    reaction_time = psychopy.core.getTime() - t0
    psychopy.core.wait(display_duration - reaction_time)

    window.flip() # present blank screen regardless
    
    if reaction_time >= display_duration:
        # participant failed to give the response during the stimulus onset
        # keep recording the response
        t1 = psychopy.core.getTime()
        response = psychopy.event.waitKeys(maxWait = ISI, keyList = ['a', 'c'])
        
        reaction_time2 = psychopy.core.getTime() - t1
        psychopy.core.wait(ISI - reaction_time2)
        reaction_time = reaction_time + reaction_time2
    else:
        # participant gave response during stimulus onset
        # wait patiently
        psychopy.core.wait(ISI)

    print(response, reaction_time)

eol_msg = psychopy.visual.TextStim(window, text = '*')
eol_msg.draw()
window.flip()

psychopy.core.wait(1.0)

probe_text = psychopy.visual.TextStim(window, text = probe)
probe_text.draw()
window.flip()

#to wait for key input from participant:
response = psychopy.event.waitKeys(keyList = ['o', 'n'])
print(response) 

stimuli_list_2 = stimuli_list_1
