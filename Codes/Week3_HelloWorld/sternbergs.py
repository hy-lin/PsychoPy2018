import psychopy.visual

window = psychopy.visual.Window()

# greeting message
hi = psychopy.visual.TextStim(window, text = 'Welcome to the classic memory experiment.')
hi.draw()
window.flip()

# setting up trial
setsize = 6 
display_duration = 500  # in ms.
display_duration = display_duration / 1000.0  # in s.

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
trial_beginning_msg = psychopy.visual.TextStim(window, text = 'Beginning trial {}, good luck.'.format(trial_index))
trial_beginning_msg.draw()
window.flip()

for i in range(setsize):
    stim = psychopy.visual.TextStim(window, text = stimuli[i])
    stim.draw()
    window.flip()

eol_msg = psychopy.visual.TextStim(window, text = '*')
eol_msg.draw()
window.flip()

print(probe)

response = raw_input('o/n?')