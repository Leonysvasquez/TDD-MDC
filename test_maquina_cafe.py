# test_maquina_cafe.py

import unittest
from maquina_cafe import MaquinaCafe, VasoInvalidoError, AzucarInvalidaError, SinRecursosError

class TestMaquinaCafe(unittest.TestCase):
    
    def setUp(self):
        # Inicializamos la máquina con recursos
        self.maquina = MaquinaCafe(
            cantidad_cafe=100, 
            cantidad_azucar=50, 
            vasos={"Pequeño": 10, "Mediano": 10, "Grande": 10}
        )
    
    # Pruebas de selección de tamaño de vaso
    def test_seleccionar_vaso_pequeno(self):
        self.maquina.seleccionar_vaso("Pequeño")
        self.assertEqual(self.maquina.tamano_vaso, "Pequeño")
    
    def test_seleccionar_vaso_mediano(self):
        self.maquina.seleccionar_vaso("Mediano")
        self.assertEqual(self.maquina.tamano_vaso, "Mediano")
    
    def test_seleccionar_vaso_grande(self):
        self.maquina.seleccionar_vaso("Grande")
        self.assertEqual(self.maquina.tamano_vaso, "Grande")
    
    def test_seleccionar_vaso_invalido(self):
        with self.assertRaises(VasoInvalidoError):
            self.maquina.seleccionar_vaso("Extra Grande")
    
    # Pruebas de selección de azúcar
    def test_seleccionar_azucar_cero(self):
        self.maquina.seleccionar_azucar(0)
        self.assertEqual(self.maquina.cucharadas_azucar, 0)
    
    def test_seleccionar_azucar_positiva(self):
        self.maquina.seleccionar_azucar(2)
        self.assertEqual(self.maquina.cucharadas_azucar, 2)
    
    def test_seleccionar_azucar_negativa(self):
        with self.assertRaises(AzucarInvalidaError):
            self.maquina.seleccionar_azucar(-1)
    
    # Pruebas de recoger vaso
    def test_recoger_vaso_exitoso(self):
        self.maquina.seleccionar_vaso("Pequeño")
        self.maquina.seleccionar_azucar(1)
        self.maquina.recoger_vaso()
        self.assertEqual(self.maquina.vasos["Pequeño"], 9)
    
    def test_recoger_vaso_sin_vasos(self):
        self.maquina.vasos["Pequeño"] = 0
        self.maquina.seleccionar_vaso("Pequeño")
        with self.assertRaises(SinRecursosError):
            self.maquina.recoger_vaso()
    
    def test_recoger_vaso_sin_azucar(self):
        self.maquina.cantidad_azucar = 0
        self.maquina.seleccionar_vaso("Pequeño")
        self.maquina.seleccionar_azucar(1)
        with self.assertRaises(SinRecursosError):
            self.maquina.recoger_vaso()
    
    def test_recoger_vaso_sin_cafe(self):
        self.maquina.cantidad_cafe = 0
        self.maquina.seleccionar_vaso("Pequeño")
        self.maquina.seleccionar_azucar(1)
        with self.assertRaises(SinRecursosError):
            self.maquina.recoger_vaso()
    
    # Pruebas de mensajes de error
    def test_mensaje_sin_vasos(self):
        self.maquina.vasos["Pequeño"] = 0
        self.maquina.seleccionar_vaso("Pequeño")
        with self.assertRaises(SinRecursosError) as context:
            self.maquina.recoger_vaso()
        self.assertEqual(str(context.exception), "No hay vasos disponibles.")
    
    def test_mensaje_sin_azucar(self):
        self.maquina.cantidad_azucar = 0
        self.maquina.seleccionar_vaso("Pequeño")
        self.maquina.seleccionar_azucar(1)
        with self.assertRaises(SinRecursosError) as context:
            self.maquina.recoger_vaso()
        self.assertEqual(str(context.exception), "No hay azúcar disponible.")
    
    def test_mensaje_sin_cafe(self):
        self.maquina.cantidad_cafe = 0
        self.maquina.seleccionar_vaso("Pequeño")
        self.maquina.seleccionar_azucar(1)
        with self.assertRaises(SinRecursosError) as context:
            self.maquina.recoger_vaso()
        self.assertEqual(str(context.exception), "No hay café disponible.")

if __name__ == '__main__':
    unittest.main()
