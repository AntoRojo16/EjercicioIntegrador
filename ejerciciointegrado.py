from ManejadorIntegrantes import ManejadorIntegrantesProyecto
from ManejadorProyecto import ManejadorProyecto

def test ():
    unManejadorIn=ManejadorIntegrantesProyecto()
    unManejadorPr=ManejadorProyecto()
    unManejadorIn.testIntegrantes()
    unManejadorPr.testProyecto()
    unManejadorIn.calcular(unManejadorPr)
    unManejadorPr.listar()
    
if __name__=="__main__":
    test()
    