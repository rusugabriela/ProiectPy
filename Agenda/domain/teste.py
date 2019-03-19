from persoana import Persoana
from activitate import Activitate
from Reppersoana import repopersoana
from Repactivitate import repoactivitate
from controller import cpersoana
def testpersoana():
    p1=Persoana(231,"Rusu Maria",123,"Tazlau.Mocanitei.10")
    assert p1.getid()==231
    assert p1.getnume()=="Rusu Maria"
    assert p1.getnumar()==123
    assert p1.getadresa()=="Tazlau.Mocanitei.10"
    p1.setid(34)
    assert p1.getid()==34
    assert p1.tostring()=="34-Rusu Maria-123-Tazlau.Mocanitei.10"
    p1=Persoana(231,"Rusu Maria",123,"Tazlau.Mocanitei.10")
    p2=Persoana(231,"Rusu Maria",123,"Tazlau.Mocanitei.10")
    p3=Persoana(12,"Bara Lorena",456,"Tazlau.Mocanitei.10")
    assert p1.eq(p2)==True
    assert p1.eq(p3)==False
testpersoana()
def testactivitate():
    a=Activitate(12,2,14,7,2016,"12:34","Blabla")
    assert a.getida()==12
    assert a.getidp()==2
    assert a.getziua()==14
    assert a.getluna()==7
    assert a.getanul()==2016
    assert a.getora()=="12:34"
    assert a.getdescriere()=="Blabla"
    a.set_idp(2)
    assert a.getidp()==2
    assert a.tostring()=="12-2-14/7/2016-12:34-Blabla"
    a1=Activitate(12,2,14,7,2016,"12:34","Blabla")
    assert a.eq(a1)==True
testactivitate()
def testrepopers():
    repo=repopersoana()
    p=Persoana(231,"Rusu Maria",123,"Tazlau.Mocanitei.10")
    repo.adaugapersoana(p)
    assert repo.getpersoane()[0].getid()==231
    p2=Persoana(12,"Bara Lorena",456,"Stefan cel Mare.14")
    repo.adaugapersoana(p2)
    assert repo.getpersoane()[1]==p2
    p3=Persoana(10,"Zgriban Lucretia",789,"Roznov.Teilor.34")
    repo.actualizarepersoana(12,p3)
    assert repo.getpersoane()[1]==p3
    repo.eliminarepersoana(10)
    assert repo.getpersoane()==[p]
    assert repo.cautarepersoana(p)==p
    assert repo.cautarepersoana(p3)==None
testrepopers()
def testrepoact():
    repop=repopersoana()
    repo=repoactivitate(repop)
    p=Persoana(2,"Popescu Irina",32,"Strada Bistritei")
    repop.adaugapersoana(p)
    a=Activitate(12,2,14,7,2016,"12:34","Blabla")
    repo.adaugaactivitate(a,repop)
    assert repo.getactivitati()[0].getida()==12
    p2=Persoana(4,"Ionescu",89,"Zorilor")
    repop.adaugapersoana(p2)
    a2=Activitate(10,4,3,11,2015,"14:00","Dansat")
    repo.adaugaactivitate(a2,repop)
    assert repo.getactivitati()[1]==a2
    p3=Persoana(5,"Rusu",45,"Mocanitei")
    repop.adaugapersoana(p3)
    a3=Activitate(3,5,12,5,2014,"13:50","Cantat")
    repo.actualizareactivitate(12,a3,repop)
    assert repo.getactivitati()[0]==a3
    repo.eliminareactivitate(3)
    assert repo.getactivitati()==[a2]
    # assert repo.cautareactivitate(10)==a2
    #assert repo.cautareactivitate(3)==None
testrepoact()
def testcontroller():
    r1=repopersoana()
    r2=repoactivitate(r1)
    c=cpersoana(r1,r2)
    c.adaugarepersoane(231,"Rusu Maria",123,"Tazlau.Mocanitei.10")
    assert c.getrepo1().getpersoane()[0].getid()==231
    c.adaugarepersoane(10,"Zgriban Lucretia",789,"Roznov.Teilor.34")
    c.actualizarepersoane(10,"Bara Lorena",456,"Stefan cel Mare.14")
    assert c.getrepo1().getpersoane()[1].getnume()=="Bara Lorena"
    p=Persoana(10,"Bara Lorena",456,"Stefan cel Mare.14")
    assert c.cautarepersoane(10)==p
    assert c.cautarepersoane(17)==None
    c.eliminarepersoana(12)
    assert c.getrepo1().getpersoane()[0].getid()==231
    c.adaugareactivitati(11,10,9,11,2016,"12:45","Intalnire oficiala")
    assert c.getrepo2().getactivitati()[0].getida()==11
    c.adaugareactivitati(3,10,12,5,2014,"13:50","Cantat")
    c.actualizareactivitati(3,231,3,11,2015,"14:00","Dansat")
    assert c.getrepo2().getactivitati()[1].getidp()==231
    #assert c.cautareactivitati(10)==a
    c.eliminareactivitate(10)
    assert c.getrepo2().getactivitati()[0].getida()==11  
testcontroller()
def teststatistici():
    r1=repopersoana()
    r2=repoactivitate(r1)
    c=cpersoana(r1,r2)
    p1=Persoana(231,"Rusu Maria",123,"Tazlau.Mocanitei.10")
    p2=Persoana(10,"Zgriban Lucretia",789,"Roznov.Teilor.34")
    c.adaugarepersoane(231,"Rusu Maria",123,"Tazlau.Mocanitei.10")
    c.adaugarepersoane(10,"Zgriban Lucretia",789,"Roznov.Teilor.34")
    c.adaugareactivitati(11,10,9,11,2016,"12:45","Intalnire oficiala")
    c.adaugareactivitati(3,231,12,5,2016,"13:50","Cantat")
    assert c.sortare3(1,1,2016,12,12,2016)==[p1,p2]
    assert c.sortare2(1,1,2016,12,12,2016)==[p1,p2]
    assert c.listapersoanedata(4,11,2016,20,12,2016)==[p2]
    c.adaugareactivitati(9,10,1,9,2016,"13:00","Drumetie")
    a1=Activitate(11,10,9,11,2016,"12:45","Intalnire oficiala")
    a2=Activitate(3,231,12,5,2016,"13:50","Cantat")
    a3=Activitate(9,10,1,9,2016,"13:00","Drumetie")
    assert c.sortare1(10)==[a3,a1]
teststatistici()

    