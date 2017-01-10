class HandHeldClicker:
    def __init__(self):
        self._counter = 0

    def push(self):
        self._counter += 1
        print( "Counter: %d" % self._counter )

    def reset(self):
        self._counter = 0

if __name__ == '__main__':
    h = HandHeldClicker()
    for i in xrange(10):
        h.push()
    h.reset()

    for i in xrange(10):
        h.push()
