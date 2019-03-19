class ui:
    #Descriere:constructor
    #Date in:un controller c
    #Date out:o instanta de tip ui
    def __init__(self,c):
        self.__ctrl=c
    #Descriere:adauga o persoana
    #Date in:obiect curent
    #Date out:obiectul curent modificat
    def adaugarepersoane(self):
        id=int(input("Dati id-ul persoanei:"))
        nume=input("Dati numele persoanei:")
        nr=int(input("Dati numarul de telefon:"))
        adresa=input("Dati adresa:")
        self.__ctrl.adaugarepersoane(id,nume,nr,adresa)
    #Descriere:adauga o activitate
    #Date in:obiect curent
    #Date out:obiectul curent modificat
    def adaugareactivitati(self):
        ida=int(input("Dati id-ul activitatii:"))
        idp=int(input("Dati id-ul persoanei:"))
        ziua=int(input("Dati ziua:"))
        luna=int(input("Dati luna:"))
        anul=int(input("Dati anul:"))
        ora=input("Dati ora:")
        descriere=input("Dati descrierea:")
        self.__ctrl.adaugareactivitati(ida,idp,ziua,luna,anul,ora,descriere)
    #Descriere:elimina o persoana
    #Date in:obiect curent
    #Date out:obiectul curent modificat
    def eliminarepersoane(self):
        idp=int(input("Dati id-ul persoanei pe care doriti sa o eliminati:"))
        self.__ctrl.eliminarepersoana(idp)
    #Descriere:elimina o activitate
    #Date in:obiect curent
    #Date out:obiectul curent modificat
    def eliminareactivitati(self):
        ida=int(input("Dati id-ul activitatii pe care doriti sa o eliminati:"))
        self.__ctrl.eliminareactivitate(ida)
    #Descriere:actualizeaza o persoana
    #Date in:obiect curent
    #Date out:obiectul curent modificat
    def updatepersoane(self):
        id1=int(input("Dati id-ul:"))
        n2=input("Dati noul nume:")
        nr2=int(input("Dati noul nr. de tel:"))
        adr2=input("Dati noua adresa:")
        self.__ctrl.actualizarepersoane(id1,n2,nr2,adr2)
    #Descriere:actualizeaza o activitate
    #Date in:obiect curent
    #Date out:obiectul curent modificat
    def updateactivitati(self):
        id1=int(input("Dati id-ul:"))
        idp2=int(input("Dati noul id al persoanei:"))
        z2=int(input("Dati ziua:"))
        l2=int(input("Dati luna:"))
        a2=int(input("Dati anul:"))
        h2=input("Dati ora:")
        d2=input("Dati noua descriere:")
        self.__ctrl.actualizareactivitati(id1,idp2,z2,l2,a2,h2,d2)
    #Descriere:cauta o persoana
    #Date in:obiect curent
    #Date out:-
    def cautapersoane(self):
        idp=int(input("Dati id-ul persoanei pe care doriti sa o cautati:"))
        print(self.__ctrl.cautarepersoane(idp))
    #Descriere:cauta o activitate
    #Date in:obiect curent
    #Date out:-
    def cautaactivitati(self):
        ida=int(input("Dati id-ul activitatii pe care doriti sa o cautati:"))
        print(self.__ctrl.cautareactivitati(ida))
    #Descriere:sorteaza activitatile unei persoane dupa data si le afiseaza intr-o lista
    #Date in:obiect curent
    #Date out:-
    def sortareactivitatipersdata(self):
        idp=int(input("Dati id-ul persoanei:"))
        lista=self.__ctrl.sortare1(idp)
        print(str(lista))
    #Descriere:afiseaza o lista cu persoanele care au activitati intre doua date si le afiseaza intr-o lista
    #Date in:obiect curent
    #Date out:-
    def listapersoane(self):
        z1=int(input("Dati ziua initiala:"))
        l1=int(input("Dati luna initiala:"))
        a1=int(input("Dati anul initial:"))
        z2=int(input("Dati ziua finala:"))
        l2=int(input("Dati luna finala:"))
        a2=int(input("Dati anul final:"))
        list=self.__ctrl.listapersoanedata(z1,l1,a1,z2,l2,a2)
        print(str(list))
    #Descriere:sorteaza persoanele cu activitati intre doua date dupa data si le afiseaza intr-o lista
    #Date in:obiect curent
    #Date out:-
    def sortaredata(self):
        z1=int(input("Dati ziua initiala:"))
        l1=int(input("Dati luna initiala:"))
        a1=int(input("Dati anul initial:"))
        z2=int(input("Dati ziua finala:"))
        l2=int(input("Dati luna finala:"))
        a2=int(input("Dati anul final:"))
        lista=self.__ctrl.sortare2(z1,l1,a1,z2,l2,a2)
        print(str(lista))
    #Descriere:sorteaza persoanele cu activitati intre doua date dupa descriere si le afiseaza intr-o lista
    #Date in:obiect curent
    #Date out:-
    def sortaredescriere(self):
        z1=int(input("Dati ziua initiala:"))
        l1=int(input("Dati luna initiala:"))
        a1=int(input("Dati anul initial:"))
        z2=int(input("Dati ziua finala:"))
        l2=int(input("Dati luna finala:"))
        a2=int(input("Dati anul final:"))
        s=self.__ctrl.sortare3(z1,l1,a1,z2,l2,a2)
        print(str(s)) 
    #Descriere:afiseaza lista de persoane
    #Date in:obiect curent
    #Date out:-
    def afiseazapersoane(self):
        self.__ctrl.afisare1()
    #Descriere:afiseaza lista de activitati
    #Date in:obiect curent
    #Date out:-
    def afiseazaactivitati(self):
        self.__ctrl.afisare2()   
    #Descriere:afiseaza lista de optiuni
    #Date in:obiect curent
    #Date out:-
    def meniu(self):
        print("1.Adauga persoana")
        print("2.Adauga activitate")
        print("3.Elimina persoana")
        print("4.Elimina activitate")
        print("5.Actualizeaza persoana")
        print("6.Actualizeaza activitate")
        print("7.Cauta persoana")
        print("8.Cauta activitate")
        print("9.Afisare persoane")
        print("10.Afisare activitati")
        print("11.Sorteaza activitatile unei persoane dupa data")
        print("12.Afiseaza lista de persoane cu activitati programate intre doua date calendaristice")
        print("13.Sorteaza persoanele dupa data activitatii")
        print("14.Sorteaza persoanele dupa descrierea activitatii")
        print("0.Iesire")
    #Descriere:main program
    #Date in:obiect curent
    #Date out:-
    def run(self):
        stopcond=False
        while(not stopcond):
            self.meniu()
            opt=int(input("Dati optiunea:"))
            if(opt==0):
                self.__ctrl.savetofile()
                self.__ctrl.savetofile2()
                stopcond=True
            elif(opt==1):
                self.adaugarepersoane()
            elif(opt==2):
                self.adaugareactivitati()
            elif(opt==3):
                self.eliminarepersoane()
            elif(opt==4):
                self.eliminareactivitati()
            elif(opt==5):
                self.updatepersoane()
            elif(opt==6):
                self.updateactivitati()
            elif(opt==7):
                self.cautapersoane()
            elif(opt==8):
                self.cautaactivitati()
            elif(opt==9):
                self.afiseazapersoane()
            elif(opt==10):
                self.afiseazaactivitati()
            elif(opt==11):
                self.sortareactivitatipersdata()
            elif(opt==12):
                self.listapersoane()
            elif(opt==13):
                self.sortaredata()
            elif(opt==14):
                self.sortaredescriere()
            else:
                print("Optiunea nu e valida!!!")