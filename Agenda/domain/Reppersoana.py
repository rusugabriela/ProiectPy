class repopersoana:
    #constructor
    #Date in:-
    #Date out:o instanta a lui repo
    def __init__(self):
        self.__persoane=[]
    #Descriere:acceseaza toate persoanele
    #Date in:obiectul curent 
    #Date out:lista de persoane
    def getpersoane(self):
        return self.__persoane
    #Descriere:adauga o persoana in lista
    #Date in:obiectul curent,o persoana p
    #Date out:lista modificata
    def adaugapersoana(self,p):
        self.__persoane.append(p)
    #Descriere:elimina o persoana din lista
    #Date in:obiectul curent,id-ul persoanei ce trebuie eliminata
    #Date out:lista modificata
    def eliminarepersoana(self,idp):
        i=0
        while(i<len(self.__persoane)):
            if(self.__persoane[i].getid()==idp):
                del self.__persoane[i]
            else:
                i=i+1
    #Descriere:converteste la string
    #Date in:obiectul curent
    #Date out:string
    def tostring(self):
        return str(self.__persoane)
    #Descriere:actualizeaza datele unei persoane
    #Date in:obiectul curent,id-ul persoanei,noua persoana pn
    #Date out:lista modificata
    def actualizarepersoana(self,idp,pn):
        for i in range(0,len(self.__persoane)):
            if(self.__persoane[i].getid()==idp):
                self.__persoane[i]=pn
    #Descriere:cauta o persoana in lista
    #Date in:obiectul curent,persoana cautata
    #Date out:persoana sau none daca nu exista aceasta persoana
    def cautarepersoana(self,p):
        i=0
        while(i<len(self.__persoane)):
            if(self.__persoane[i]==p):
                return self.__persoane[i]
            else:
                i=i+1
        return None