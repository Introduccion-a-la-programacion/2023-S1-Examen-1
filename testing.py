import Examen1;
import pytest;

#########################################################

def test_numeroHermano_1():
    assert Examen1.numeroHermano(20) == True
    
def test_numeroHermano_2():
    assert Examen1.numeroHermano(8) == False
    
def test_numeroHermano_3():
    assert isinstance(str(Examen1.numeroHermano(-8)), str) == isinstance("Error: Número debe ser positivo", str)
    
#########################################################

def test_numeroPolimax_1():
    assert Examen1.numeroPolimax(4312) == True
    
def test_numeroPolimax_2():
    assert Examen1.numeroPolimax(3267) == True
    
def test_numeroPolimax_3():
    assert Examen1.numeroPolimax(-6887) == False

def test_numeroPolimax_4():
    assert Examen1.numeroPolimax(-9) == True
        
#########################################################

def test_formarNumero_1():
    assert Examen1.formarNumero([9,15,894]) == 915894
    
def test_formarNumero_2():
    assert Examen1.formarNumero([0,2,0,-1258,0,1]) == -20125801
    
#########################################################

def test_validarSecuencia_1():
    assert Examen1.validarSecuencia(258645125, 3, 9) == True
    
def test_validarSecuencia_2():
    assert Examen1.validarSecuencia(256412, 4, 9) == False
    
def test_validarSecuencia_3():
    assert Examen1.validarSecuencia(45280731, 1, 30) == True
