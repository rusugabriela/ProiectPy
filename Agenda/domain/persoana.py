class Persoana():

    #Descriere:constructor
    #Date in:idp,n,nrtel,adr
    #Date out: o persoana (self)
    def __init__(self,idp,n,nrtel,adr):
        self.__id=idp
        self.__nume=n
        self.__nr=nrtel
        self.__adresa=adr
    #Descriere : getter
    #Date in: Persoana curenta
    #Date out: Id unei persoane
    def getid(self):
        return self.__id
    #Descriere : getter
    #Date in: Persoana curenta
    #Date out: numele unei persoane
    def getnume(self):
        return self.__nume
    #Descriere : getter
    #Date in: Persoana curenta
    #Date out: numarul de telefon al unei persoane
    def getnumar(self):
        return self.__nr
    #Descriere : getter
    #Date in: Persoana curenta
    #Date out: adresa unei persoane
    def getadresa(self):
        return self.__adresa
    #Descriere:setter
    #Date in: persoana (self), noul id (idp)
    #Date out : Persoana curenta modificata (self)
    def setid(self,idp):
        self.__id=idp
    #Descriere:setter
    #Date in: persoana (self), noul nume(n)
    #Date out : Persoana curenta modificata (self)
    def setnume(self,n):
        self.__nume=n
    #Descriere:setter
    #Date in: persoana (self), noul  nr.de telefon(nrtel)
    #Date out : Persoana curenta modificata (self)
    def setnr(self,nrtel):
        self.__nr=nrtel
    #Descriere:setter
    #Date in: persoana (self), noua adresa (adr)
    #Date out : Persoana curenta modificata (self)
    def setadresa(self,adr):
        self.__adresa=adr
    #Descriere: Converteste la string o persoana
    #Date in: Persoana curenta (self)
    #Date out: Un string cu informatie utila
    def tostring(self):
        return str(self.__id)+'-'+self.__nume+'-'+str(self.__nr)+'-'+self.__adresa
    #Descriere: Converteste la string o persoana
    #Date in: Persoana curenta (self)
    #Date out: Un string cu informatie utila
    def __str__(self):
        return str(self.__id)+'-'+self.__nume+'-'+str(self.__nr)+'-'+self.__adresa
    #Descriere: Converteste la string o persoana
    #Date in: Persoana curenta (self)
    #Date out: Un string cu informatie utila
    def __repr__(self):
        return str(self.__id)+'-'+self.__nume+'-'+str(self.__nr)+'-'+self.__adresa
    #Descriere:comparator
    #Date in:obiect curent,alta persoana
    #Date out:true daca persoanele sunt identice,false altfel
    def eq(self,f):
        return (self.__id==f.__id)  
    #Descriere:comparator
    #Date in:obiect curent,alta persoana
    #Date out:true daca persoanele sunt identice,false altfel
    def __eq__(self,f):
        return (self.__id==f.__id)