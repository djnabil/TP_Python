
#Exo 1


#  https://github.com/djnabil/TP_Python


import random
import sys
from threading import Thread, RLock
import time


verrou = RLock()

class ThreadCS(Thread):
    """Thread chargé simplement d'afficher une letre dans la console."""
    def __init__(self, nombres):
        Thread.__init__(self)
        self.nombres = nombres

    def run(self):
        """Code à exécuter pendant l'exécution du thread"""
        self.calcul_square()
    def calcul_square(self):
        for i in range(0, len(self.nombres)):
            carre = self.nombres[i] * self.nombres[i]
            text=(str(self.nombres[i])+"² = ",str(carre))
            with verrou:
                for lettre in text:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
                sys.stdout.write("\n")


class ThreadCC(Thread):
    """Thread chargé simplement d'afficher une letre dans la console."""
    def __init__(self, nombres):
        Thread.__init__(self)
        self.nombres = nombres

    def run(self):
        """Code à exécuter pendant l'exécution du thread"""
        self.calcul_cube()
    def calcul_cube(self):
        for i in range(0, len(self.nombres)):
            cube = self.nombres[i] * self.nombres[i]* self.nombres[i]
            text=(str(self.nombres[i])+" au cube = ",str(cube))
            with verrou:
                for lettre in text:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
                sys.stdout.write("\n")

thread_1 = ThreadCS([2, 3, 8, 9, 12])
thread_2 = ThreadCC([2, 3, 8, 9, 12])
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()


#Exo 2
from multiprocessing import Lock,Process
import random
import time
import sys

def calcul_square(nombres,lock):
        for i in range(0, len(nombres)):
            carre = nombres[i] * nombres[i]
            text = (str(nombres[i]) + "² = ", str(carre))
            lock.acquire()
            try:
                for lettre in text:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
                sys.stdout.write("\n")
            finally:
                lock.release()

def calcul_cube(nombres,lock):
        for i in range(0, len(nombres)):
            cube = nombres[i] * nombres[i] * nombres[i]
            text = (str(nombres[i]) + " au cube = ", str(cube))
            lock.acquire()
            try:
                for lettre in text:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
                sys.stdout.write("\n")
            finally:
                lock.release()
def main():
    lock=Lock()
    nombres =[2, 3, 8, 9, 12]
    procesesses = []
    proc1=Process(target=calcul_square, args=(nombres,lock))
    proc2=Process(target=calcul_cube, args=(nombres,lock))
    procesesses.append(proc1)
    procesesses.append(proc2)
    proc1.start()
    proc2.start()

    for proc in procesesses:
        proc.join()

if __name__=="__main__":
    main()