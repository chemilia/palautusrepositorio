# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
<<<<<<< HEAD
print(f"{x} + {y} = {summa(x, y)}")
print(f"{x} - {y} = {erotus(x, y)}"

logger("lopetetaan ohjelma")
print("goodbye!")

# tehdään muutos kopiossa mainissa
=======
print(f"Lukujen {x} ja {y} summa on {summa(x, y)}")  # muutos bugikorjaus-branchissa
print(f"Lukujen {x} ja {y} erotus on {erotus(x, y)}")  # muutos bugikorjaus-branchissa

logger("lopetetaan ohjelma")
print("goodbye!")
>>>>>>> cd194fc (tehtiin muutos index.py bugikorjaus brachissä)
