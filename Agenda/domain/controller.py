from persoana import Persoana
from activitate import Activitate
class cpersoana:
    #constructor
    #Date in:2 repository
    #Date out:o instanta de tip controller
    def __init__(self,repo1,repo2):
        self.__rep1=repo1
        self.__rep2=repo2
    #Descriere:adauga o persoana
    #Date in: id-ul, numele, telefonul si adresa unei persone 
    #Date out:obiectul curent modificat
    def adaugarepersoane(self,id,nume,nr,adresa):
        p=Persoana(id,nume,nr,adresa)
        self.__rep1.adaugapersoana(p)
    #Descriere:adauga o activitate
    #Date in: id-ul activitatii, id persoana,zi,luna,an,ora,descriere
    #Date out:obiectul curent modificat
    def adaugareactivitati(self,ida,idp,ziua,luna,anul,ora,descriere):
        a=Activitate(ida,idp,ziua,luna,anul,ora,descriere)
        self.__rep2.adaugaactivitate(a,self.__rep1)
    #Descriere:acceseaza toate persoanele
    #Date in: obiectul curent
    #Date out:lista de persoane
    def getrepo1(self):
        return self.__rep1
    #Descriere:acceseaza toate activitatile
    #Date in: obiectul curent
    #Date out:lista de activitati
    def getrepo2(self):
        return self.__rep2
    #Descriere:elimina o persoana
    #Date in: obiectul curent,id persoana
    #Date out:obiectul curent modificat
    def eliminarepersoana(self,idp):
        self.__rep1.eliminarepersoana(idp)
    #Descriere:elimina o activitate
    #Date in: obiectul curent,id activitate
    #Date out:obiectul curent modificat
    def eliminareactivitate(self,ida):
        self.__rep2.eliminareactivitate(ida) 
    #Descriere:actualizeaza o persoana
    #Date in: obiectul curent,id persoana,noul nume,noul nr. de tel,noua adresa
    #Date out:obiectul curent modificat
    def actualizarepersoane(self,id1,n2,nr2,adr2):   
        p=Persoana(id1,n2,nr2,adr2)
        self.__rep1.actualizarepersoana(id1,p) 
    #Descriere:actualizeaza o activitate
    #Date in: obiectul curent,id activitate, id pers.,zi,luna,an,ora,descriere(noua activitate)
    #Date out:obiectul curent modificat
    def actualizareactivitati(self,id1,idp2,z2,l2,a2,h2,d2):
        newa=Activitate(id1,idp2,z2,l2,a2,h2,d2)
        self.__rep2.actualizareactivitate(id1,newa,self.__rep1)
    #Descriere:cauta o persoana
    #Date in: obiectul curent,id persoana
    #Date out:persoana
    def cautarepersoane(self,idp):
        p=Persoana(idp,"",0,"")
        return self.__rep1.cautarepersoana(p)
    #Descriere:cauta o activitate
    #Date in: obiectul curent,id activitate
    #Date out:activitatea  
    def cautareactivitati(self,ida):
        a=Activitate(ida,0,0,0,0,"","")
        return self.__rep2.cautareactivitate(a)
    #Descriere:sorteaza activitatile unei persoane dupa data
    #Date in: obiectul curent,id persoana
    #Date out:lista de activitati sortata
    def sortare1(self,idp):
        l=self.__rep2.activitatipersoana(idp)
        for i in range(0,len(l)-1):
            for j in range(i+1,len(l)):
                z1=l[i].getziua()
                z2=l[j].getziua()
                l1=l[i].getluna()
                l2=l[j].getluna()
                a1=l[i].getanul()
                a2=l[j].getanul()
                if((z1>z2 and l1==l2 and a1==a2)or (l1>l2 and a1==a2)or(a1>a2)):
                    aux=l[i]
                    l[i]=l[j]
                    l[j]=aux
        return l
    #Descriere:returneaza o lista cu persoanele care au activitati intre doua date 
    #Date in: obiectul curent,cele doua date(zi,luna,an)
    #Date out:lista de persoane
    def listapersoanedata(self,z1,l1,a1,z2,l2,a2):
        la=self.__rep2.getactivitati()
        ld=[]
        for i in range(0,len(la)):
            if(la[i].getziua()>=z1 and la[i].getziua()<=z2 and la[i].getluna()>=l1 and la[i].getluna()<=l2 and la[i].getanul()>=a1 and la[i].getanul()<=a2):
                ld.append(la[i])
        lp=[]
        for i in range (0,len(ld)):
            idp=ld[i].getidp()
            ok=1
            for j in range (0,len(lp)):
                if(lp[j].getid()==idp):
                    ok=0
            if(ok==1):
                pers=Persoana(idp,"",0,"")
                p=self.__rep1.cautarepersoana(pers)
                lp.append(p)
        return lp
    #Descriere:sorteaza persoanele cu activitati intre doua date dupa data
    #Date in: obiectul curent,cele doua date
    #Date out:lista de persoane sortata care in deplineste proprietatea
    def sortare2(self,z1,l1,a1,z2,l2,a2):
        la=self.__rep2.getactivitati()
        ld=[]
        for i in range(0,len(la)):
            if(la[i].getziua()>=z1 and la[i].getziua()<=z2 and la[i].getluna()>=l1 and la[i].getluna()<=l2 and la[i].getanul()>=a1 and la[i].getanul()<=a2):
                ld.append(la[i])
        for i in range(0,len(ld)-1):
            for j in range(i+1,len(ld)):
                z1=ld[i].getziua()
                z2=ld[j].getziua()
                l1=ld[i].getluna()
                l2=ld[j].getluna()
                a1=ld[i].getanul()
                a2=ld[j].getanul()
                if((z1>z2 and l1==l2 and a1==a2)or (l1>l2 and a1==a2)or(a1>a2)):
                    aux=ld[i]
                    ld[i]=ld[j]
                    ld[j]=aux
        lp=[]
        for i in range (0,len(ld)):
            idp=ld[i].getidp()
            ok=1
            for j in range (0,len(lp)):
                if(lp[j].getid()==idp):
                    ok=0
            if(ok==1):
                pers=Persoana(idp,"",0,"")
                p=self.__rep1.cautarepersoana(pers)
                lp.append(p)
        return lp
    #Descriere:sorteaza persoanele cu activitati intre doua date dupa descriere
    #Date in: obiectul curent,cele doua date
    #Date out:lista de persoane sortata care in deplineste proprietatea
    def sortare3(self,z1,l1,a1,z2,l2,a2):
        la=self.__rep2.getactivitati()
        ld=[]
        for i in range(0,len(la)):
            if(la[i].getziua()>=z1 and la[i].getziua()<=z2 and la[i].getluna()>=l1 and la[i].getluna()<=l2 and la[i].getanul()>=a1 and la[i].getanul()<=a2):
                ld.append(la[i])
        sortedlist=sorted(ld,key=Activitate.getdescriere)
        lp=[]
        for i in range (0,len(sortedlist)):
            idp=sortedlist[i].getidp()
            ok=1
            for j in range (0,len(lp)):
                if(lp[j].getid()==idp):
                    ok=0
            if(ok==1):
                pers=Persoana(idp,"",0,"")
                p=self.__rep1.cautarepersoana(pers)
                lp.append(p)
        return lp
    #Descriere:afiseaza lista de persoane
    #Date in:obiect curent
    #Date out:-
    def afisare1(self):
        print(self.__rep1.tostring())
    #Descriere:afiseaza lista de activitati
    #Date in:obiect curent
    #Date out:-   
    def afisare2(self):
        print (self.__rep2.tostring())
    def savetofile(self):
        self.__rep1.saveAll()
    def savetofile2(self):
        self.__rep2.saveAll()
        