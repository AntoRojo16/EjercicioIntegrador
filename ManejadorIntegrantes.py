from Integrantes import integrantesProyecto

import csv
class ManejadorIntegrantesProyecto:
    
    def __init__ (self):
        self.__lista=[]
        
      
    def agregar (self,unIntengrante):
        self.__lista.append(unIntengrante)
    def testIntegrantes (self):
        archivo=open("IntegrantesProyecto.csv")
        reader=csv.reader(archivo,delimiter=";")
        band=True
        for fila in reader:
            if band:
                band=not band
            else:
                i=fila[0]
                ap=fila[1]
                DNI=fila[2] 
                cat=fila[3]
                rol=fila[4]
                
                unIntegrante=integrantesProyecto(i,ap,DNI,cat,rol)
                self.agregar(unIntegrante)
      
    def CalcularPuntos (self,ip):
        print("PROYECTO CON ID: {} " .format(ip))
        cont=0
        sd=False
        direc=False
        cod=False
        sc=False
        for  integrante in self.__lista:
            if integrante.getId()==ip:
                if integrante.getRol()=="integrante":
                    cont=cont+1
                if integrante.getRol()=="director":
                    sd=True
                    if integrante.getCat()=="II" or integrante.getCat()=="I":
                        direc=True
                if integrante.getRol()=="codirector":
                    sc=True
                    if integrante.getCat()=="II" or integrante.getCat()=="I" or integrante.getCat()=="III":
                        cod=True
        
        puntos=0    
        if cont>=3:
            puntos=puntos+10
        else:
            puntos-20
            print("El Proyecto debe tener como mínimo 3 integrantes")
        if direc==True:
            puntos=puntos+10
        else:
            print("El Director del Proyecto debe tener categoría I o II")
            puntos=puntos-5
            
        if cod==True:
            puntos=puntos+10
        else:
            print("El Codirector del Proyecto debe tener como mínimo categoría III")
            puntos=puntos-5
        if sd==False:
            print ("El Proyecto debe tener un Director")
            puntos=puntos-5
        if sc==False:
            print("El Proyecto debe tener un Codirector")
            puntos=puntos-5
            
            
        print("La cantidad de puntos para el proyecto con ID {}, es :{} " .format(ip,puntos))
        return puntos           
                
            
                
    def calcular (self,proyectos):
        i=0
        for i in range(3):
            iP=proyectos.Getproyecto(i)
            p=self.CalcularPuntos(iP)
            proyectos.cargarPuntos(i,p)
            
        
    
            
            
        
        
    
            
        
