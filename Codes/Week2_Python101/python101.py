# first and foremost
'Hello World'
print('Welcome to the classic memory experiment.')

# let python remembering the outcome
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
print('Beginning trial {}, good luck.'.format(trial_index))
# print('Beginning trial ' + str(trial_index) + ', good luck.')

# print(stimuli[0])
# print(stimuli[1])
# print(stimuli[2])
# print(stimuli[3])
# print(stimuli[4])
# print(stimuli[5])


for i in range(setsize):
    print(stimuli[i])

print('*')

print(probe)
response = raw_input('o/n?')


# def setupProbe(stimuli, probe_type, serial_position):
#     # this function determines the content of the probe

#     if probe_type == 'new':
#         probe = 'dogs'
#     else:
#         probe = stimuli[serial_position - 1]

#     return probe
