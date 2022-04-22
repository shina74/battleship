class Field:
    def __init__(self, x=0, y=0, empty=True, miss=False, dead=False, view='\t-'):
        self.x = x
        self.y = y
        self.empty = empty
        self.miss = miss
        self.dead = dead
        self.view = view

    @property
    def get(self):
        return self.view

    @property
    def x_y(self):
        return self.x, self.y

    @property
    def check(self):
        return self.miss or self.dead

    @property
    def put(self):
        return self.empty

    @put.setter
    def put(self, value):
        if value:
            self.empty = False
        else:
            self.empty = False
            self.view = '\t' + chr(9744)

    @property
    def shoot(self):
        return self.empty

    @shoot.setter
    def shoot(self, value):
        if value:
            self.miss = True
            self.view = '\t' + chr(9747)
        else:
            self.dead = True
            self.view = '\t' + chr(9746)

    @property
    def win(self):
        return self.dead
