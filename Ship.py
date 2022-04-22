class Ship:
    def __init__(self,x = 0,y = 0,len = 0,arrow = True,live = False):
        self.x = x
        self.y = y
        self.len = len
        self.arrow = arrow
        self.live = live

    @property
    def x_y(self):
        return self.x, self.y
    @x_y.setter
    def x_y(self,value):
        self.x , self.y = map(int,value.split())

    @property
    def n_len(self):
        return self.len

    @property
    def n_arrow(self):
        return self.arrow

    @property
    def _live(self):
        return self.live

    @_live.setter
    def _live(self, value):
        self.live = False
