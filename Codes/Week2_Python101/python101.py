# first and foremost
'Hello World'
print('Welcome to the classic memory experiment.')

# let python remembering the outcome
setsize = 6
display_duration = 500  # in ms.
display_duration = display_duration / 1000  # in s.

stimuli = ['bent',
           'cart',
           'line',
           'birth',
           'ultra',
           'excuse']

probe_type = 'old'
serial_position = 3  # tbd after the probe type is set
probe = ''  # tbd after the probe type is set

probe, serial_position = setupProbe(stimuli, probe_type, serial_position)

# let's run it!

trial_index = 1
print('Beginning trial {}'.format(trial_index))
# print('Beginning trial', trial_index)

for i in range(setsize):
    print(stimuli[i])

print('*')

print(probe)
response = raw_input('o/n?')


def setupProbe(stimuli, probe_type=None, serial_position=None):
    # this function determines the content of the probe

    if probe_type is None:
        probe_type = 'old'

    # fill in serial_position here

    if probe_type == 'new':
        probe = 'dogs'
    else:
        probe = stimuli[serial_position - 1]

    return probe, serial_position
