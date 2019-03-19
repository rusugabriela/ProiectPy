class repoactivitate:
    #Descriere:constructor
    #Date in:repository
    #Date out:o instanta de tip repo
    def __init__(self,rep):
        self.__activitati=[]
        self.__repopers=rep
    #Descriere:adauga o activitate in lista
    #Date in:obiect curent,activitate a,repository
    #Date out:lista modificata sau mesaj in caz ca nu exista persoana
    def adaugaactivitate(self,a,repopers):
        idp=a.getidp()
        ok=0
        l=self.__repopers.getpersoane()
        for i in range (0,len(l)):
            if (l[i].getid()==idp):
                ok=1
                self.__activitati.append(a)
        if(ok==0):
            print("Aceasta persoana nu exista!")
    #Descriere:acceseaza toate activitatile
    #Date in:obiect curent
    #Date out:lista de activitati
    def getactivitati(self):
        return self.__activitati
    #Descriere:converteste la string
    #Date in:obiect curent
    #Date out:string
    def tostring(self):
        return str(self.__activitati)
    #Descriere:elimina o activitate
    #Date in:obiect curent,id activitate
    #Date out:lista modificata
    def eliminareactivitate(self,ida):
        i=0
        while(i<len(self.__activitati)):
            if(self.__activitati[i].getida()==ida):
                del(self.__activitati[i])
            else:
                i=i+1
    #Descriere:actualizeaza datele pt. o activitate
    #Date in:obiect curent,id activitate,noua activitate,repository
    #Date out:o instanta de tip repo
    def actualizareactivitate(self,ida,an,repopers):
        ok=0
        idp=an.getidp()
        l=self.__repopers.getpersoane()
        for i in range (0,len(l)):
            if (l[i].getid()==idp):
                ok=1
        for i in range(0,len(self.__activitati)):
            if(self.__activitati[i].getida()==ida and ok==1):
                self.__activitati[i]=an
    #Descriere:cauta o activitate in lista
    #Date in:obiect curent,activitate
    #Date out:activitatea sau none daca aceasta nu exista
    def cautareactivitate(self,a):
        i=0
        while(i<len(self.__activitati)):
            if(self.__activitati[i]==a):
                return self.__activitati[i]
            else:
                i=i+1
        return None
    #Descriere:returneaza lista de activitati pt. o persoana
    #Date in:obiect curent,id persoana
    #Date out:o lista
    def activitatipersoana(self,idp):
        l=[]
        i=0
        while(i<len(self.__activitati)):
            if(self.__activitati[i].getidp()==idp):
                l.append(self.__activitati[i])
            i=i+1
        return l
        
    
                                                    