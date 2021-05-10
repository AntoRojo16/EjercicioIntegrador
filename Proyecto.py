class Proyecto:
    __idProyecto=0
    __Titulo=""
    __palabra=""
    __puntos=0
    
    def __init__ (self,i,tit,pa,pun=0):
        self.__idProyecto=i
        self.__Titulo=tit
        self.__palabra=pa
        self.__puntos=pun
        
        
    def getId (self):
        return self.__idProyecto
    
    
    def getTitulo (self):
        return self.__Titulo
    
    
    def getpalabra (self):
        return self.__palabra
    
        
    def agregarPuntos (self,pun):
        self.__puntos=pun
        
    def getPuntos (self):
        return self.__puntos
        
        
    def __gt__ (self, otroProyecto):
        if self.__puntos>otroProyecto.getPuntos():
            return True
        else:
            return False
        
        
    
    
    

