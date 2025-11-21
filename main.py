class wallet:
    def __init__(self, couleur, taille):
        self.couleur = couleur
        self.taille = taille
        self.vola = 0
        self.isOpen = True
        self.isLost = False

    def addvola(self, amount):
        self.vola += amount

    def getVola(self, amount):
        self.vola -= amount

    def checkVola(self, amount):
        return self.vola
    
    def isLost(self):
        return self.isLost
