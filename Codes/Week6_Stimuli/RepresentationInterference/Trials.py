'''
Most of the code required for complete a trial.

exp_setting.line_width
exp_setting.line_length
exp_setting.circle_size
exp_setting.default_color
exp_setting.colorcenter
'''

import PsychoPyInterface
import CIELAB
import numpy


class Stimulus(object):
    '''
    '''
    def __init__(self, val, exp_setting, s_type = 'orientation', serial_position = 1, spatial_position = 1, pos = (0, 0)):
        '''
        constructor
        '''

        self.val = val
        self.exp_setting = exp_setting
        self.s_type = s_type
        self.serial_position = serial_position
        self.spatial_position = spatial_position # 1-6, 1-3 belong to top row, and 4-6 belongs to button row.
        self.pos = pos

    def __str__(self):
        '''
        overwrite the __str__ function
        '''
        return '{}\t{}\t{}\t{}'.format(self.val, self.s_type, self.serial_position, self.spatial_position)

class OrientationStimulus(Stimulus):
    '''
    '''
    def __init__(self, val, exp_setting, s_type = 'orientation', serial_position = 1, spatial_position = 1, pos = (0, 0)):
        '''
        constructor
        '''

        super(OrientationStimulus, self).__init__(val, exp_setting, s_type, serial_position, spatial_position, pos)

    def draw(self, display):
        display.drawFilledCircle(self.pos[0], self.pos[1], self.exp_setting.orientation_circle_size, self.exp_setting.default_color)

        coords = self._rotating_stimulus()
        display.drawPoly(coords, self.exp_setting.default_bg_color, antialias = True)

    def _rotating_stimulus(self):
        x_origin = [
            0,
            2*self.exp_setting.orientation_gap_width,
            2*self.exp_setting.orientation_gap_width,
            0
        ]

        y_origin = [
            -self.exp_setting.orientation_gap_width,
            -self.exp_setting.orientation_gap_width,
            self.exp_setting.orientation_gap_width,
            self.exp_setting.orientation_gap_width
        ]

        x = [0, 0, 0, 0]
        y = [0, 0, 0, 0]

        coords = []
        for i in range(4):
            x[i] = x_origin[i] * numpy.cos(self.val * numpy.pi / 180) + \
                   y_origin[i] * -numpy.sin(self.val * numpy.pi / 180) + \
                   self.pos[0]
            y[i] = x_origin[i] * numpy.sin(self.val * numpy.pi / 180) + \
                   y_origin[i] * numpy.cos(self.val * numpy.pi / 180) + \
                   self.pos[1]

            coords.append((x[i], y[i]))

        return coords

    def update(self, new_val = None):
        if new_val is not None:
            self.val = new_val

class ColorStimulus(Stimulus):
    '''
    '''
    def __init__(self, val, exp_setting, s_type = 'color', serial_position = 1, spatial_position = 1, pos = (0, 0)):
        '''
        constructor
        '''
        super(ColorStimulus, self).__init__(val, exp_setting, s_type, serial_position, spatial_position, pos)

    def update(self, new_val = None):
        if new_val is not None:
            self.val = new_val

    def draw(self, display):
        display.drawFilledCircle(self.pos[0], self.pos[1], self.exp_setting.orientation_circle_size, CIELAB.angle2RGB(self.val, self.exp_setting.color_center, self.exp_setting.color_radius))

def pos2ang(pos, ref_pos):
    x, y = pos
    ref_x, ref_y = ref_pos
    dx = x-ref_x
    dy = y-ref_y

    dist = numpy.sqrt(dx**2 + dy**2)
    ang = 180 * numpy.arccos(abs(dx/dist)) / numpy.pi
    
    if dx < 0 and dy > 0:
        ang = 180 - ang
    elif dx <= 0 and dy <= 0:
        ang = ang + 180
    elif dx > 0 and dy < 0:
        ang = 360 - ang
        
    ang = ang % 360
            
    try:
        return int(numpy.floor(ang))
    except:
        return 0

class Trial(object):
    '''
    The class for a single trial.
    '''
    def __init__(self, beginning_msg, stimuli_batches, probe, set_size, exp_setting, logger):
        '''
        '''

        self.beginning_msg = beginning_msg
        self.stimuli_batches = stimuli_batches
        self.probe = probe

        self.exp_setting = exp_setting

        self.logger = logger

        self.set_size = set_size
        self.probe_type = self.probe.s_type

        if self.probe_type == 'color':
            self.shift = numpy.random.randint(0, 359)
        else:
            self.shift = 0


    def run(self, psypy, recorder):
        self.showBeginningMsg(psypy)
        self.showStimuli(psypy)
        self.getResponse(psypy, recorder)

        psypy.clear(True)
        psypy.wait(500)

    def showBeginningMsg(self, psypy):
        '''
        This function shows the message at the beginning of the trial. 
        The message serves as a cue for guiding which item participant has to pay attention to.
        '''
        psypy.clear()
        psypy.drawText(self.beginning_msg)
        psypy.refresh()

        self.logger('Displaying beginning msg: {}'.format(self.beginning_msg))
        
        t0 = psypy.getTime()
        self.logger('Start caching colorwheel')
        psypy._cacheColorwheel(self.shift)
        t1 = psypy.getTime()
        self.logger('Finished caching colorwheel, time spent: {}'.format((t1-t0)*1000))

        psypy.wait(self.exp_setting.beginning_msg_duration - (t1-t0)*1000)

    def showStimuli(self, psypy):
        '''
        This function shows the stimuli batch of the trial one by one.
        '''
        psypy.clear()
        for stimuli_batch in self.stimuli_batches:
            for stimulus in stimuli_batch:
                stimulus.draw(psypy)
            
            self.logger('Showing stimuli batch')

            psypy.refresh()
            psypy.wait(self.exp_setting.stimulus_onset)

            psypy.clear(True)
            psypy.wait(self.exp_setting.stimulus_offset)

    def getResponse(self, psypy, recorder):
        '''
        '''
        recorder.showCursor()
        recorder.setMousePos()

        buttons = [0, 0, 0]

        while buttons[0] != 1:
            buttons = recorder.getMousePressed()
            x, y = recorder.getMousePos()
            
            if self.probe_type == 'orientation':
                ang = pos2ang((x, y), self.probe.pos)
            else:
                ang = pos2ang((x, y), (0, 0))

            ang = (ang + self.shift) % 360

            psypy.clear()

            if self.probe_type == 'color':
                psypy.drawColorwheel()

            self.probe.update(ang)
            self.probe.draw(psypy)

            keys = recorder.getKeyboard(['d'])
            if 'd' in keys:
                self.logger('Because Danielle demands it')
                raise KeyboardInterrupt('Because Danielle demands it')
            
            psypy.refresh()
            psypy.wait(15)

        recorder.hideCursor()

    def __str__(self):
        out_string = ''

        out_string += '{}\t'.format(self.set_size)
        out_string += '{}\t'.format(self.probe.serial_position)
        out_string += '{}\t'.format(self.probe.spatial_position)
        out_string += '{}\t'.format(self.probe_type)

        for stimuli_batch in self.stimuli_batches:
            for stimulus in stimuli_batch:
                out_string += '{}\t'.format(stimulus)

        out_string += '{}'.format(self.probe)

        return out_string