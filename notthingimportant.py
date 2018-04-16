class Node(object):
    def __init__(self, parent = None, children = []]):
        self.parent = parent
        self.children = children

        self.pos
        self.text


    def addChild(self, new_child):
        self.children.append(new_child)

    def draw(self)
        drawSelf()
        drawLinestoChildren()

    def drawLinestoChildren(self):
        for child in self.children:
            drawline(child.pos, self.pos)
