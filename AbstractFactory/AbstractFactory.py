from abc import ABC, abstractmethod


class FabriqueAnimal():
    @abstractmethod
    def crier(self):
        pass

    @abstractmethod
    def deplacer(self):
        pass

class FabriqueHomme(FabriqueAnimal):
    def crier(self):
        return CrierHomme()
    def deplacer(self):
        return DeplacerHommme()

class FabriqueChien(FabriqueAnimal):
    def crier(self):
        return CrierChien()
    def deplacer(self):
        return DeplacerChien()

class Crier():

    @abstractmethod
    def nourir(self):
        pass
class Deplacer():

    @abstractmethod
    def deplacer(self):
        pass


class CrierHomme(Crier):
    def crier(self):
        print("L'homme parle")

class CrierChien(Crier):
    def crier(self):
        print("Le chien Aboie")


class DeplacerHommme(Deplacer):
    def deplacer(self):
        print("L'homme marche")

class DeplacerChien(Deplacer):
    def deplacer(self):
        print("Le chien cours")


class Test :
    homme = FabriqueHomme().crier().crier()
    chien = FabriqueChien().crier().crier()


    homme = FabriqueHomme().deplacer().deplacer()
    chien = FabriqueChien().deplacer().deplacer()




