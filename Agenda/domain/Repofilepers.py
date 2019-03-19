from Reppersoana import repopersoana
from persoana import Persoana
class Repofilep(repopersoana):
    #constructor
    def __init__(self,fn):
        repopersoana.__init__(self)
        self.__numeFisier=fn
        self.loadFromFile()
    #Descriere: Citeste din fisier si adauga in lista de persoane
    #Date in:self
    #Date out: lista de activitati modificata
    def loadFromFile(self):
        try:
            fin=open(self.__numeFisier,"r")
        except:
            print("Fisierul nu a putut fi deschis")  
     
        line=fin.readline().strip()
        while (line!=""):
            line=line.strip()
            elem=line.split("-")
            id=int(elem[0])
            nume=elem[1]
            tel=(elem[2])
            ad=elem[3]
            p=Persoana(id,nume,tel,ad)
            self.adaugapersoana(p)
            line=fin.readline().strip()
        fin.close()
    #Descriere:Salveaza toate modificariile in fisier
    #Date in:self
    #Date out:-  
    def saveAll(self):
        fout=open(self.__numeFisier,"w")
        for p in self.getpersoane():
            fout.write(str(p)+'\n')
        fout.close()           

    

    
    
