#
#To do:
#ad exception if going back and changing the world
#
#
#

class Dane:
    #tab = [0] * 107
    #def __init__(self, tab):
    #    self.tab = [0] * 107
    def __init__(self, actual_x, actual_y):
        #self.move = move
        self.tab = []
        self.actual_x = actual_x
        self.actual_y = actual_y


    def add_data_by_one_data_just_demo(self, text):
        file = open('data_before.txt', 'w')
        for i in range(1):
            self.tab.append([int(j) for j in text.split()])

    def add_data(self):
        file = open('data_before.txt', 'w')
        print("Ile chcesz slow podac")
        #tab = []
        n = int(input())
        for i in range(n):
            self.tab.append([int(j) for j in input().split()])

        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                file.write(str(self.tab[i][j]))
                file.write(' ')
            file.write('\n')

        file.close()
        return self.tab

    def read_data(self):
        file = open('data_before.txt', 'r')
        #tab = []
        #lines = file.split('\n')
        tab_temp = []
        for line in file:
            tab_temp.append(line)
        n=len(tab_temp)
        for i in range(n):
            self.tab.append([int(j) for j in tab_temp[i].split()])

        return self.tab

    def go_to(self, move):# actual_x, actual_y):
        if move == 'next':
            if self.actual_x > len(self.tab)-1:
                return 404
            elif self.actual_y == len(self.tab[self.actual_x])-1:
                self.actual_x += 1
                if self.actual_x > len(self.tab)-1:
                    return 404
                self.actual_y = -1
                #self.actual_y = 0
                return 777
            else:
                self.actual_y += 1
                return self.tab[self.actual_x][self.actual_y]
        if move == 'left':
            if self.actual_y <= 0:
                self.actual_x -= 1
                return 777
            else:
                self.actual_y -= 1
                return self.tab[self.actual_x][self.actual_y]
        #elif move == 'stop':
        #        return self.tab[self.actual_x][self.actual_y]
        elif move == 'stop':
            if self.actual_x > len(self.tab)-1:
                return 404
            elif self.actual_y > len(self.tab[self.actual_x]):
                return 777
            else:
                return self.tab[self.actual_x][self.actual_y]

    def give_actual(self):
        return self.actual_x, self.actual_y

    def getDataSize(self):
        n = 0
        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                n+=1

        return n



class Wyniki:
    def __init__(self, tab):
        self.tab = tab
        self.temp_tab = tab

    def copy(self):
        file = open('data_after.txt', 'w')
        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                file.write(str(self.tab[i][j]))
            file.write('\n')
        file.close()

    def change(self, actual_x, actual_y, time):
        if tab_temp[actual_x][actual_y] == 1:
            tab_temp[actual_x][actual_y] = 0
        else:
            tab_temp[actual_x][actual_y] = 1

        if time == 1:
            file = open('data_after.txt', 'w')
            for i in range(len(self.temp_tab)):
                for j in range(len(self.temp_tab[i])):
                    file.write(str(self.temp_tab[i][j]))
                file.write('\n')
            file.close()
