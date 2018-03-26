# coding= latin-1

import datetime
import random
import numpy

import Trials
import PsychoPyInterface
import ExpSetting
 
class Experiment(object):
    '''
    THE EXPERIMENT.
    '''
    def __init__(self):
        '''
        '''
        self.data_file = open('representationinterference.dat', 'a')
        self.data_log = open('log.dat', 'a')

        self.exp_setting = ExpSetting.ExpSetting()
        self.psypy = PsychoPyInterface.CoreInterface(self.exp_setting)
        self.recorder = PsychoPyInterface.Recorder(self.psypy.window)

        self.pID = 999
        self.session = 1

        self.recorder.hideCursor()

        self._setupPracticeTrials()
        self._setupExpTrials()

        self.log('experiment created.')

        self.pID, self.session = self._getPIDNSession()

    def log(self, msg):
        current_time = datetime.datetime.now()
        time_str = current_time.strftime('%d-%b-%Y %I-%M-%S')
        
        self.data_log.write('{}\t{}\t{}\t{}\n'.format(time_str, self.pID, self.session, msg))

    def _getPIDNSession(self):
        pID = self.psypy.getString(self.recorder, 'Participant ID: ', x = -0.5, y = 0.45)
        session = self.psypy.getString(self.recorder, 'Session: ',  x = -0.5, y = 0.45)
        
        return pID, session

    def _setupPracticeTrials(self):
        self.psypy.clear()
        self.psypy.drawText('Please stand by, the first hamster is running as fast as it can.')
        self.psypy.refresh()

        self.p_trials = []
        for trial_index in range(self.exp_setting.n_practice):
            self.p_trials.append(self._getTrial(trial_index))

        numpy.random.shuffle(self.p_trials)

    def _setupExpTrials(self):
        self.psypy.clear()
        self.psypy.drawText('Please stand by, the second hamster is running as fast as it can.')
        self.psypy.refresh()

        self.trials = []
        for trial_index in range(self.exp_setting.n_trials):
            self.trials.append(self._getTrial(trial_index))

        numpy.random.shuffle(self.trials)

    def _getTrial(self, trial_index):
        vals = numpy.random.choice(range(360), 6, replace = False)

        color_batch1 = [
            Trials.ColorStimulus(
                vals[0],
                self.exp_setting, 
                s_type = 'color',
                serial_position = 1,
                spatial_position = 1,
                pos = (self.exp_setting.item_x[0], self.exp_setting.item_y_first_batch)
            ),
            Trials.ColorStimulus(
                vals[1],
                self.exp_setting, 
                s_type = 'color',
                serial_position = 1,
                spatial_position = 2,
                pos = (self.exp_setting.item_x[1], self.exp_setting.item_y_first_batch)
            ),
            Trials.ColorStimulus(
                vals[2],
                self.exp_setting, 
                s_type = 'color',
                serial_position = 1,
                spatial_position = 3,
                pos = (self.exp_setting.item_x[2], self.exp_setting.item_y_first_batch)
            )
        ]

        color_batch2 = [
            Trials.ColorStimulus(
                vals[3],
                self.exp_setting, 
                s_type = 'color',
                serial_position = 2,
                spatial_position = 4,
                pos = (self.exp_setting.item_x[0], self.exp_setting.item_y_second_batch)
            ),
            Trials.ColorStimulus(
                vals[4],
                self.exp_setting, 
                s_type = 'color',
                serial_position = 2,
                spatial_position = 5,
                pos = (self.exp_setting.item_x[1], self.exp_setting.item_y_second_batch)
            ),
            Trials.ColorStimulus(
                vals[5],
                self.exp_setting, 
                s_type = 'color',
                serial_position = 2,
                spatial_position = 6,
                pos = (self.exp_setting.item_x[2], self.exp_setting.item_y_second_batch)
            )
        ]

        orientation_batch1 = [
            Trials.OrientationStimulus(
                vals[0],
                self.exp_setting, 
                s_type = 'color',
                serial_position = 1,
                spatial_position = 1,
                pos = (self.exp_setting.item_x[0], self.exp_setting.item_y_first_batch)
            ),
            Trials.OrientationStimulus(
                vals[1],
                self.exp_setting, 
                s_type = 'color',
                serial_position = 1,
                spatial_position = 2,
                pos = (self.exp_setting.item_x[1], self.exp_setting.item_y_first_batch)
            ),
            Trials.OrientationStimulus(
                vals[2],
                self.exp_setting, 
                s_type = 'color',
                serial_position = 1,
                spatial_position = 3,
                pos = (self.exp_setting.item_x[2], self.exp_setting.item_y_first_batch)
            )
        ]

        orientation_batch2 = [
            Trials.OrientationStimulus(
                vals[3],
                self.exp_setting, 
                s_type = 'color',
                serial_position = 2,
                spatial_position = 4,
                pos = (self.exp_setting.item_x[0], self.exp_setting.item_y_second_batch)
            ),
            Trials.OrientationStimulus(
                vals[4],
                self.exp_setting, 
                s_type = 'color',
                serial_position = 2,
                spatial_position = 5,
                pos = (self.exp_setting.item_x[1], self.exp_setting.item_y_second_batch)
            ),
            Trials.OrientationStimulus(
                vals[5],
                self.exp_setting, 
                s_type = 'color',
                serial_position = 2,
                spatial_position = 6,
                pos = (self.exp_setting.item_x[2], self.exp_setting.item_y_second_batch)
            )
        ]

        probed_location = numpy.random.choice([0, 1, 2], 1)[0]

        if trial_index % 12 == 0:
            # orientation-color, orientation only, 1st item-batch
            first_stimuli_batch = orientation_batch1
            second_stimuli_batch = color_batch2

            probe = Trials.OrientationStimulus(
                numpy.random.randint(0, 359), 
                self.exp_setting,
                serial_position = 1,
                spatial_position = probed_location + 1,
                pos = (self.exp_setting.item_x[probed_location], self.exp_setting.item_y_first_batch)
            )
            beginning_msg = self.exp_setting.beginning_msg_single.format(
                'erstes Item',
                'oben',
                'Orientierung'
            )
            set_size = 3
        elif trial_index % 12 == 1:
            # color-orientation, orientation only, 2st item-batch
            first_stimuli_batch = color_batch1
            second_stimuli_batch = orientation_batch2

            probe = Trials.OrientationStimulus(
                numpy.random.randint(0, 359), 
                self.exp_setting,
                serial_position = 2,
                spatial_position = probed_location + 4,
                pos = (self.exp_setting.item_x[probed_location], self.exp_setting.item_y_second_batch)
            )
            beginning_msg = self.exp_setting.beginning_msg_single.format(
                'zweites Item',
                'unten',
                'Orientierung'
            )
            set_size = 3
        elif trial_index % 12 == 2:
            # color-orientation, color only, 1st item-batch
            first_stimuli_batch = color_batch1
            second_stimuli_batch = orientation_batch2

            probe = Trials.ColorStimulus(
                numpy.random.randint(0, 359), 
                self.exp_setting,
                serial_position = 1,
                spatial_position = probed_location + 1,
                pos = (self.exp_setting.item_x[probed_location], self.exp_setting.item_y_first_batch)
            )
            beginning_msg = self.exp_setting.beginning_msg_single.format(
                'erstes Item',
                'oben',
                'Farbe'
            )
            set_size = 3
        elif trial_index % 12 == 3:
            # orientation-color, color only, 2st item-batch
            first_stimuli_batch = orientation_batch1
            second_stimuli_batch = color_batch2

            probe = Trials.ColorStimulus(
                numpy.random.randint(0, 359), 
                self.exp_setting,
                serial_position = 2,
                spatial_position = probed_location + 4,
                pos = (self.exp_setting.item_x[probed_location], self.exp_setting.item_y_second_batch)
            )
            beginning_msg = self.exp_setting.beginning_msg_single.format(
                'zweites Item',
                'unten',
                'Farbe'
            )
            set_size = 3
        elif trial_index % 12 == 4:
            # orientation-orientation, orientation only, 1st item-batch
            first_stimuli_batch = orientation_batch1
            second_stimuli_batch = orientation_batch2

            probe = Trials.OrientationStimulus(
                numpy.random.randint(0, 359), 
                self.exp_setting,
                serial_position = 1,
                spatial_position = probed_location + 1,
                pos = (self.exp_setting.item_x[probed_location], self.exp_setting.item_y_first_batch)
            )
            beginning_msg = self.exp_setting.beginning_msg_double
            set_size = 6
        elif trial_index % 12 == 5:
            # orientation-orientation, orientation only, 2st item-batch
            first_stimuli_batch = orientation_batch1
            second_stimuli_batch = orientation_batch2

            probe = Trials.OrientationStimulus(
                numpy.random.randint(0, 359), 
                self.exp_setting,
                serial_position = 2,
                spatial_position = probed_location + 4,
                pos = (self.exp_setting.item_x[probed_location], self.exp_setting.item_y_second_batch)
            )
            beginning_msg = self.exp_setting.beginning_msg_double
            set_size = 6
        elif trial_index % 12 == 6:
            # color-color, color only, 1st item-batch
            first_stimuli_batch = color_batch1
            second_stimuli_batch = color_batch2

            probe = Trials.ColorStimulus(
                numpy.random.randint(0, 359), 
                self.exp_setting,
                serial_position = 1,
                spatial_position = probed_location + 1,
                pos = (self.exp_setting.item_x[probed_location], self.exp_setting.item_y_first_batch)
            )
            beginning_msg = self.exp_setting.beginning_msg_double
            set_size = 6

        elif trial_index % 12 == 7:
            # color-color, color only, 2st item-batch
            first_stimuli_batch = color_batch1
            second_stimuli_batch = color_batch2

            probe = Trials.ColorStimulus(
                numpy.random.randint(0, 359), 
                self.exp_setting,
                serial_position = 2,
                spatial_position = probed_location + 4,
                pos = (self.exp_setting.item_x[probed_location], self.exp_setting.item_y_second_batch)
            )
            beginning_msg = self.exp_setting.beginning_msg_double
            set_size = 6

        elif trial_index % 12 == 8:
            # orientation-color, mixed, 1st item-batch
            first_stimuli_batch = orientation_batch1
            second_stimuli_batch = color_batch2

            probe = Trials.OrientationStimulus(
                numpy.random.randint(0, 359), 
                self.exp_setting,
                serial_position = 1,
                spatial_position = probed_location + 1,
                pos = (self.exp_setting.item_x[probed_location], self.exp_setting.item_y_first_batch)
            )
            beginning_msg = self.exp_setting.beginning_msg_double
            set_size = 6

        elif trial_index % 12 == 9:
            # color-orientation, mixed, 2st item-batch
            first_stimuli_batch = color_batch1
            second_stimuli_batch = orientation_batch2

            probe = Trials.OrientationStimulus(
                numpy.random.randint(0, 359), 
                self.exp_setting,
                serial_position = 2,
                spatial_position = probed_location + 4,
                pos = (self.exp_setting.item_x[probed_location], self.exp_setting.item_y_second_batch)
            )
            beginning_msg = self.exp_setting.beginning_msg_double
            set_size = 6

        elif trial_index % 12 == 10:
            # color-orientation, mixed, 1st item-batch
            first_stimuli_batch = color_batch1
            second_stimuli_batch = orientation_batch2

            probe = Trials.ColorStimulus(
                numpy.random.randint(0, 359), 
                self.exp_setting,
                serial_position = 1,
                spatial_position = probed_location + 1,
                pos = (self.exp_setting.item_x[probed_location], self.exp_setting.item_y_first_batch)
            )
            beginning_msg = self.exp_setting.beginning_msg_double
            set_size = 6

        elif trial_index % 12 == 11:
            # orientation-color, mixed, 2st item-batch
            first_stimuli_batch = orientation_batch1
            second_stimuli_batch = color_batch2

            probe = Trials.ColorStimulus(
                numpy.random.randint(0, 359), 
                self.exp_setting,
                serial_position = 2,
                spatial_position = probed_location + 4,
                pos = (self.exp_setting.item_x[probed_location], self.exp_setting.item_y_second_batch)
            )
            beginning_msg = self.exp_setting.beginning_msg_double
            set_size = 6

        return Trials.Trial(
            beginning_msg,
            [first_stimuli_batch, second_stimuli_batch],
            probe,
            set_size,
            self.exp_setting,
            self.log
        )

    def run(self):
        self.showPracticeMessage()
        self.log('beginning practice:')
        for trial in self.p_trials:
            trial.run(self.psypy, self.recorder)
            self.log(trial)


        self.showExperimentMessage()
        self.log('beginning trials:')
        for t_ind, trial in enumerate(self.trials):
            trial.run(self.psypy, self.recorder)
            self.log(trial)
            self.save2file(trial)

            if t_ind % int(self.exp_setting.n_trials / 10) == 0 and t_ind != 0:
                self.doBreak(t_ind / int(self.exp_setting.n_trials / 10))

        self._endofExperiment()

    def showPracticeMessage(self):
        self.psypy.showMessage(
            'Mit Leertaste weiter zu den Ubungsaufgaben',
            ['space'],
            self.recorder)

        self.psypy.clear(refresh = True)
        self.psypy.wait(500)

    def showExperimentMessage(self):
        self.psypy.showMessage(
            'Mit Leertaste weiter zu den Testaufgaben',
            ['space'],
            self.recorder)

        self.psypy.clear(refresh = True)
        self.psypy.wait(500)
        
    def doBreak(self, n_block):
        self.log('taking a break')

        self.psypy.drawText('Block: {}/10 passed.'.format(n_block))
        self.psypy.refresh()
        self.psypy.wait(1000)

        self.psypy.showMessage(
            'Gelegenheit fur kurze Pause. Weiter mit Leertaste.',
            ['space'], 
            self.recorder)

        self.psypy.clear(refresh = True)
        self.psypy.wait(500)

    def _endofExperiment(self):
        self.log('experiment finished, closing files.')
        self.data_file.close()
        
        self.psypy.showMessage(
            u'Ende des Experiments: Bitte Versuchsleiter rufen',
            ['space'],
            self.recorder)
        
        self.log('exiting program.')
        self.data_log.close()

    def save2file(self, trial):
        self.data_file.write(
            '{}\t{}\t{}\n'.format(
                self.pID,
                self.session,
                trial
            )
        )

if __name__ == '__main__':
    exp = Experiment()
    exp.run()