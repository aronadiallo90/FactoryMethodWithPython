
import time

from Crack import Crack


class Dictionnaire(Crack):

    def cracker(self,password):

          with open("dico2.txt", 'r') as filin:
              lignes = filin.read().split()
          debut = time.time()
          for ligne in lignes:
              if ligne == password :
                      dure = time.ctime(time.time()-debut)[11:19]
                      self.showPassword(ligne)
                     
                      print(f"Mot de pass trouvé en : {dure} s")
                      break