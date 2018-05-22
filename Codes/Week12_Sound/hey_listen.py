import psychopy.sound
import psychopy.core


hey = psychopy.sound.Sound('hey.wav', stereo = True)
listen = psychopy.sound.Sound('listen.wav', stereo = True)
hey.play()
psychopy.core.wait(hey.getDuration())
listen.play()

psychopy.core.wait(2)