import CIELAB

class ExpSetting(object):
    def __init__(self):
        #orientation stimulus
        self.orientation_gap_width = 0.025 # in relation to windows height
        self.orientation_circle_size = 0.05

        #color stimulus
        self.color_circle_size = 0.05
        self.color_center = CIELAB.Color_Lab(70, 20, 38)
        self.color_radius = 70

        self.colorwheel_radius1 = 0.35
        self.colorwheel_radius2 = 0.4

        self.default_color = (0, 0, 0)
        self.default_bg_color = (200, 200, 200)

        # time related
        self.beginning_msg_duration = 3000
        self.stimulus_onset = 1000
        self.stimulus_offset = 500

        # item positions
        self.item_y_first_batch = 0.12
        self.item_y_second_batch = -0.12

        self.item_x = [-0.18, 0.0, 0.18]

        self.font_size = 24
        # beginning message
        self.beginning_msg_single = '{}/{}: {}'
        self.beginning_msg_double = 'Beide'

        # trial setting
        self.n_trials = 300
        self.n_practice = 10
