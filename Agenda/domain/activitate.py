class Activitate:
    #Descriere:constructor
    #Date in: id1,id2,z,l,a,h,d
    #Date out: O activitate
    def __init__(self,id1,id2,z,l,a,h,d):
        self.__ida=id1
        self.__idp=id2
        self.__ziua=z
        self.__luna=l
        self.__anul=a
        self.__ora=h
        self.__descriere=d
    #Descriere : getter
    #Date in: Activitatea curenta
    #Date out: Id-ul unei activitati
    def getida(self):
        return self.__ida
    #Descriere :getter
    #Date in: Activitatea curenta
    #Date out: Id-ul unei persoane
    def getidp(self):
        return self.__idp
    #Descriere : getter
    #Date in: Activitatea curenta
    #Date out: ziua unei activitati
    def getziua(self):
        return self.__ziua
    #Descriere : getter
    #Date in: Activitatea curenta
    #Date out: luna unei activitati
    def getluna(self):
        return self.__luna
    #Descriere : getter
    #Date in: Activitatea curenta
    #Date out: anul unei activitati
    def getanul(self):
        return self.__anul
    #Descriere : getter
    #Date in: Activitatea curenta
    #Date out: ora unei activitati
    def getora(self):
        return self.__ora
    #Descriere : getter
    #Date in: Activitatea curenta
    #Date out: descrierea unei activitati
    def getdescriere(self):
        return self.__descriere
    #Descriere :setter
    #Date in: Activitatea (self), noul id al activitatii
    #Date out : Activitatea curenta modificata
    def setida(self,id1):
        self.__ida=id1
    #Descriere :setter
    #Date in: Activitatea (self), noul id al persoanei
    #Date out : Activitatea curenta modificata
    def set_idp(self, id2):
        self.__idp = id2
    #Descriere :setter
    #Date in: Activitatea (self), noua zi a activitatii
    #Date out : Activitatea curenta modificata
    def set_ziua(self,z):
        self.__ziua =z
    #Descriere :setter
    #Date in: Activitatea (self), noua luna a activitatii
    #Date out : Activitatea curenta modificata
    def set_luna(self,l):
        self.__luna =l
    #Descriere :setter
    #Date in: Activitatea (self), noul an al activitatii
    #Date out : Activitatea curenta modificata
    def set_anul(self,a):
        self.__anul =a
    #Descriere :setter
    #Date in: Activitatea (self), noua ora a activitatii
    #Date out : Activitatea curenta modificata
    def set_ora(self,h):
        self.__ora =h
    #Descriere :setter
    #Date in: Activitatea (self), noua descriere a activitatii
    #Date out : Activitatea curenta modificata
    def set_descriere(self,d):
        self.__descriere =d
    #Descriere: Converteste la string o activitate
    #Date in: Activitatea curenta (self)
    #Date out: Un string cu informatie utila
    def tostring(self):
        return str(self.__ida)+'-'+str(self.__idp)+'-'+str(self.__ziua)+'-'+str(self.__luna)+'-'+str(self.__anul)+"-"+self.__ora+'-'+self.__descriere
    #Descriere: Converteste la string o activitate
    #Date in: Activitatea curenta (self)
    #Date out: Un string cu informatie utila   
    def __str__(self):
        return str(self.__ida)+'-'+str(self.__idp)+'-'+str(self.__ziua)+'-'+str(self.__luna)+'-'+str(self.__anul)+"-"+self.__ora+'-'+self.__descriere
    #Descriere: Converteste la string o activitate
    #Date in: Activitatea curenta (self)
    #Date out: Un string cu informatie utila
    def __repr__(self):
        return str(self.__ida)+'-'+str(self.__idp)+'-'+str(self.__ziua)+'-'+str(self.__luna)+'-'+str(self.__anul)+"-"+self.__ora+'-'+self.__descriere
    #Descriere:comparator
    #Date in:activitate curenta,o alta activitate
    #Date out:true,daca activitatile au acelasi id,false altfel
    def eq(self,f):
        return(self.__ida==f.__ida)
    #Descriere:comparator
    #Date in:activitate curenta,o alta activitate
    #Date out:true,daca activitatile au acelasi id,false altfel    
    def __eq__(self,f):
        return (self.__ida==f.__ida)