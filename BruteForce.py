from Crack import Crack
import string   

import time






    

class BruteForce(Crack):
        liste = list(string.ascii_letters+string.digits+string.punctuation)

         
        def  cracker(self,password) :
                debut = time.time()
                for i in self.liste:
                    ch= str()
                    ch = i
                    for j in self.liste:
                        ch = i+j
                        for k in self.liste:
                          ch =  i+j+k
                          for l in self.liste:  
                                ch = i+j+k+l
                                if ch == password:
                                    dure = time.ctime(time.time()-debut)[11:19]
                                    self.showPassword(ch)
                                    print(f"Mot de pass trouvé en : {dure} s")
                                    break
            
              
                        






