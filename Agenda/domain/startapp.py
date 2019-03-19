from uiclass import ui
from Repofileact import Repofileact
from Repofilepers import Repofilep
from Repactivitate import repoactivitate
from Reppersoana import repopersoana
from controller import cpersoana
r1=Repofilep("persoana.txt")
r2=Repofileact("activitate.txt",r1)
c=cpersoana(r1,r2)
ui(c).run()


