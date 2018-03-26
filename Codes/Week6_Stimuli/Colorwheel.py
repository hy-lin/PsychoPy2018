import psychopy.visual
import psychopy.event
import numpy

def _getWheelCoord():
    colorwheel_radius1 = 0.35
    colorwheel_radius2 = 0.4

    x1 = numpy.zeros(361)
    x2 = numpy.zeros(361)
    y1 = numpy.zeros(361)
    y2 = numpy.zeros(361)

    for ang in range(361):
        radian = 2 * numpy.pi * (ang+1) / 360
        if (ang+1) > 360:
            radian = 2 * numpy.pi / 360

        x1[ang] = colorwheel_radius1 * numpy.cos(radian)
        y1[ang] = colorwheel_radius1 * numpy.sin(radian)
        x2[ang] = colorwheel_radius2 * numpy.cos(radian)
        y2[ang] = colorwheel_radius2 * numpy.sin(radian)

    coords = []
    for ang in range(360):
        coords.append([(x1[ang], y1[ang]),
                        (x2[ang], y2[ang]),
                        (x2[ang+1], y2[ang+1]),
                        (x1[ang+1], y1[ang+1])])
    
    return coords

def _cacheColorwheel(window):
    # this function cache the colorwheel, so a lot of the computation can
    # be out sourced at the beginning of the trail.
    polys = []
    coords = _getWheelCoord()

    for ang in range(360):
        polys.append(psychopy.visual.ShapeStim(window,
                                      fillColorSpace = 'hsv',
                                      fillColor = (ang, 0.5, 1.0),
                                      lineWidth = 0, 
                                      vertices = coords[ang],
                                      ))

    return polys

window = psychopy.visual.Window(
    units = 'height',
    fullscr=True,
    color = (200, 200, 200),
    colorSpace = 'rgb255', 
    winType = 'pyglet',
    screen = 0
)

polys = _cacheColorwheel(window)
for poly in polys:
    poly.draw()

window.flip()

response = psychopy.event.waitKeys(keyList = ['space'])