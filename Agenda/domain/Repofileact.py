from Repactivitate import repoactivitate
from activitate import Activitate
from Reppersoana import repopersoana
from Repofilepers import Repofilep
class Repofileact(repoactivitate):
    #constructor
    def __init__(self, fisier,repopersoana):
        repoactivitate.__init__(self,repopersoana)
        self.__fisier= fisier
        self.loadFromF() 
    #Descriere: Citeste din fisier si adauga in lista de persoane
    #Date in:self
    #Date out: lista de persoane modificata
    def loadFromF(self):
        f=open(self.__fisier,"r")
        line=f.readline().strip()
        while (line!=''):
            line=line.strip()
            elem=line.split("-")
            idact=int(elem[0])
            idp=int(elem[1])
            zi=int(elem[2])
            luna=int(elem[3])
            an=int(elem[4])
            ora=elem[5]
            desc=elem[6]
            act=Activitate(idact,idp,zi,luna,an,ora,desc)
            self.adaugaactivitate(act,repopersoana)
            line=f.readline().strip()
        f.close()
    #Descriere:Salveaza toate modificariile in fisier
    #Date in:self
    #Date out:-  
    def saveAll(self):
        f=open(self.__fisier,"w") 
        for act in self.getactivitati():
            f.write(str(act)+'\n')
        f.close()
