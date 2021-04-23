#
#To do:
#I have to give it more exceptions if there would be more worlds
#but it also not realy important because version 0.1 will only work
#with one word ;)
#

class State:
    def __init__(self, nr, move, marker, goToStan, omove, omarker, ogoToStan, endmove, endmarker, endgoToStan):
        self.nr = nr #numer stanu
        #to jesli 1
        self.move = move #gdzie przejesc 0-zostac 1-lewo 2-prawo
        self.marker = marker #co napisac
        self.goToStan = goToStan #nr stanu do ktorego przeniesc
        #to dla 0
        self.omove = omove
        self.omarker = omarker
        self.ogoToStan = ogoToStan
        #dla ostatniego znaku ciagu 404
        self.endmove = endmove
        self.endmarker = endmarker
        self.endgoToStan = endgoToStan


    def getData(self):
        return self.nr, self.move, self.marker, self.goToStan, self.omove, self.omarker, self.ogoToStan

    def getNr(self):
        return self.nr

    def getoNr(self):
        return self.onr

    def getendNr(self):
        return self.endnr

    def getMove(self):
        return self.move

    def getoMove(self):
            return self.omove

    def getendMove(self):
            return self.endmove

    def getMarker(self):
        return self.marker

    def getoMarker(self):
        return self.omarker

    def getendMarker(self):
        return self.endmarker

    def getGoToStan(self):
        return self.goToStan

    def getoGoToStan(self):
        return self.ogoToStan

    def getendGoToStan(self):
        return self.endgoToStan

    def uploadToTxt(self):
        file = open('states.txt', 'a')
        file.write(str(self.nr))
        file.write('\n')
        file.write(str(self.move))
        file.write('\n')
        file.write(str(self.marker))
        file.write('\n')
        file.write(str(self.goToStan))
        file.write('\n')
        file.write(str(self.omove))
        file.write('\n')
        file.write(str(self.omarker))
        file.write('\n')
        file.write(str(self.ogoToStan))
        file.write('\n')
        file.write(str(self.endmove))
        file.write('\n')
        file.write(str(self.endmarker))
        file.write('\n')
        file.write(str(self.endgoToStan))
        file.write('\n')
        file.close()

    def getDataFromFile(self, nr):
        file = open('states.txt', 'r')
        #lines = file.split('\n')
        temp_tab = []
        for line in file:
            temp_tab.append(line)
        n=len(temp_tab)
        for i in range(int(n/7)):
            iter = i*7
            if nr == int(temp_tab[iter]):
                self.nr = int(temp_tab[iter])
                self.move = int(temp_tab[iter+1])
                self.marker = int(temp_tab[iter+2])
                self.goToStan = int(temp_tab[iter+3])
                self.omove = int(temp_tab[iter+4])
                self.omarker = int(temp_tab[iter+5])
                self.ogoToStan = int(temp_tab[iter+6])
                self.endmove = int(temp_tab[iter+7])
                self.endmarker = int(temp_tab[iter+8])
                self.endgoToStan = int(temp_tab[iter+9])
                break

        file.close()
