import os

class Obj:
    filename = ""
    v = []

    def __init__(self, fn):
        self.filename = os.getcwd()+fn
        return
    
    def smaller(self):
        print("FILENAME IS" + self.filename)
        with open(self.filename) as fp:
            line = fp.readline()
            while line:
                #print(line)
                vs = line.split()
                if (len(vs) >=3) and (vs[0] == "v"):
                    self.v.append([float(vs[i])/100 for i in range(1,4)])
                    #print(vs)
                line = fp.readline()
        return self.v