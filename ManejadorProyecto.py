import csv
from Proyecto import Proyecto
class ManejadorProyecto:
    
    
    def __init__ (self):
        self.__lista=[]
    
    def Getproyecto (self,i):
        return self.__lista[i].getId()
        
    
    def agregar (self,unProyecto):
        self.__lista.append(unProyecto)
        
    def testProyecto (self):
        archivo=open("proyectos.csv")
        reader=csv.reader(archivo,delimiter=";")
        band=True
        for fila in reader:
            if band:
                band=not band
                
            else:
                i=fila[0]
                T=fila[1]
                p=fila[2]
                unProyecto=Proyecto(i,T,p)
                self.agregar(unProyecto)
    def cargarPuntos (self,i,p):
        
        self.__lista[i].agregarPuntos(p)
         
    def   listar (self):
        print("RANKING DE PROYECTOS")
        i=0
        pr1=self.__lista[i]
        pr2=self.__lista[i+1]
        pr3=self.__lista[i+2]
        if pr1>pr2:
            if pr1>pr3:
                if pr3>pr2:
                    print(pr1.getId())
                    print(pr3.getId())
                    print(pr2.getId())
                else:
                    print(pr1.getId())
                    print(pr2.getId())
                    print(pr3.getId())
            else:
                print(pr3.getId())
                print(pr1.getId())
                print(pr2.getId())
        else:
            if pr2>pr3:
                if pr3>pr1:
                    print(pr2.getId())
                    print(pr3.getId())
                    print(pr1.getId())
                else:
                    print(pr2.getId())
                    print(pr1.getId())
                    print(pr3.getId())
            else:
                print(pr3.getId())
                print(pr2.getId())
                print(pr1.getId())
                
            
            
        