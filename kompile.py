"""
State have to have every option like if 0/1/_ next to each other
otherwise it will work bad
"""
import matrix


def parser(file_path):
    file = open(file_path, 'r')
    nr_stanu = 0
    goToStan = [0,0,0]
    marker = [0,0,0]
    skok = [0,0,0]
    var = 0
    #oper var for option
    oper = False
    iter = 0
    #done it variable which shows you that the state is end
    done = 1
    for line in file:
        #first state has to be 0
        if done == 3:
            done = 1
            stan = matrix.State(nr_stanu, skok[1], marker[1], goToStan[1], skok[0], marker[0], goToStan[0], skok[2], marker[2], goToStan[2])
            stan.uploadToTxt()
        iter+=1
        if line != '\n':
            if oper == False:
                try:
                    nr_stanu = int(line[1])
                    try:
                        var = int(line[len(line)-2:len(line)-1])
                    except:
                        var = 2
                    done += 1
                except:
                    print(line)
                    print(var,' ',nr_stanu)
                    print("Fail in line ",iter)
                    exit(0)
                oper = True
            elif oper:
                try:
                    goToStan[var] = int(line[1])
                    marker[var] = int(line[4])
                    if line[6] == '>':
                        skok[var] = 2
                    elif line[6] == '<':
                        skok[var] = 1
                    elif line[6] == '_':
                        skok[var] = 0
                except:
                    print(line)
                    print(var, ' ',nr_stanu)
                    print(marker[var],' ', goToStan[var],' ',skok[var])
                    print("Fail in line",iter)
                    exit(0)
                oper = False
    file.close()

def main():
    parser('hello_world.txt')

if __name__ == '__main__':
    main()
