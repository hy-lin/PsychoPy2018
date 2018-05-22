import psychopy.microphone
import psychopy.core

psychopy.microphone.switchOn()
# psychopy.core.wait(5)

mic = psychopy.microphone.AudioCapture()
mic.record(5, 'you_listen.wav')