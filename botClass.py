import random



class bot:
    def export(self):
        file = open("data/"+self.type+".txt","w")
        for old,new,point in self.data:
            for d in old:
                file.write(str(d)+" ")
            for d in new:
                file.write(str(d)+" ")
            file.write(str(point))
            file.write("\n")
        file.close()

    def __init__(self, type):
        self.oldChoice = []
        self.type = type
        self.data = [(tuple(i.split()[:9]), tuple(i.split()[9:18]), i.split()[-1]) for i in open("data/"+type+".txt","r").readlines()]




    def makeChoice(self, btns):
        #print(self.data)
        pos = tuple([btn if btn!="" else "-" for btn in btns])
        choice = [i for i in self.data if i[0]==pos]
        if len(choice)>=1:
            choice = max(choice, key=lambda x:int(x[2]))
        else:
            c = 0
            while c < 100:
                index = random.randint(0, 8)
                while btns[index] != "":
                    index = random.randint(0, 8)

                newBtns = list(pos)
                newBtns[index] = self.type
                try:
                    if int(min([i for i in self.data if i[1] == newBtns], key=lambda x: x[2])[2]) >= 0:
                        c = 100
                    else:
                        c+=1
                except ValueError:
                    c+=1




            choice = [pos,newBtns,0]
        self.oldChoice.append(list(choice))
        return [c if c!="-" else "" for c in choice[1]]


    def win(self):
        self.oldChoice[-1][2] = int(self.oldChoice[-1][2]) + 5
        for c in self.oldChoice:
            c[2] = int(c[2])+5
            self.data.append(c)
        self.oldChoice.clear()
    def lose(self):
        self.oldChoice[-1][2] = int(self.oldChoice[-1][2]) - 2
        for c in self.oldChoice:
            c[2] = int(c[2])-1
            self.data.append(c)
        self.oldChoice.clear()





