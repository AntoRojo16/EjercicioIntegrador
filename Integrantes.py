class integrantesProyecto():
    __idProyecto=0
    __apeNom=""
    __DNI=0
    __cat=""
    __rol=""
    
    
    def __init__ (self,i,a,d,c,r):
        self.__idProyecto=i
        self.__apeNom=a
        self.__DNI=a
        self.__cat=c
        self.__rol=r
        
    def getId (self):
        return self.__idProyecto
    
    def getApe (self):
        return self.__apeNom
    
    def getDNI (self):
        return self.__DNI
    
    def getCat (self):
        return self.__cat
    
    def getRol (self):
        return self.__rol
    
    