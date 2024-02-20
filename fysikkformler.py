
g = 9.81 #m/s^2
#tyngdekrafts akselerasjonen på Jorda


class basisobject:
    """ skaper grunnnleggende egenskaper for object """
    def __init__(self, masse, friksjonstall):
        """ konstruktør """
        self.masse = masse
        self.friksjonstall = friksjonstall
    def friksjon(self):
        """ regner ut friksjon """
        friksjon = self.friksjonstall * (self.masse * g)
        self.friksjon = friksjon
        return friksjon
    





    