# maquina_cafe.py

class VasoInvalidoError(Exception):
    """Excepción lanzada cuando se selecciona un tamaño de vaso inválido."""
    pass

class AzucarInvalidaError(Exception):
    """Excepción lanzada cuando se selecciona una cantidad de azúcar inválida."""
    pass

class SinRecursosError(Exception):
    """Excepción lanzada cuando faltan recursos (vasos, azúcar, café)."""
    pass

class MaquinaCafe:
    def __init__(self, cantidad_cafe, cantidad_azucar, vasos):
        """
        Inicializa la máquina dispensadora de café con los recursos disponibles.

        :param cantidad_cafe: Cantidad de café disponible en Oz.
        :param cantidad_azucar: Cantidad de azúcar disponible en cucharadas.
        :param vasos: Diccionario con los tamaños de vasos y su cantidad.
        """
        self.cantidad_cafe = cantidad_cafe  # en Oz
        self.cantidad_azucar = cantidad_azucar  # en cucharadas
        self.vasos = vasos  # diccionario con tamaños y cantidad
        self.tamano_vaso = None
        self.cucharadas_azucar = 0

    def seleccionar_vaso(self, tamano):
        """
        Permite seleccionar el tamaño del vaso.

        :param tamano: Tamaño del vaso ("Pequeño", "Mediano", "Grande").
        :raises VasoInvalidoError: Si el tamaño del vaso no es válido.
        """
        if tamano not in self.vasos:
            raise VasoInvalidoError("Tamaño de vaso inválido.")
        self.tamano_vaso = tamano
        print(f"Vaso seleccionado: {tamano}")

    def seleccionar_azucar(self, cucharadas):
        """
        Permite seleccionar la cantidad de azúcar.

        :param cucharadas: Número de cucharadas de azúcar.
        :raises AzucarInvalidaError: Si la cantidad de azúcar es negativa.
        """
        if cucharadas < 0:
            raise AzucarInvalidaError("La cantidad de azúcar no puede ser negativa.")
        self.cucharadas_azucar = cucharadas
        print(f"Cucharadas de azúcar seleccionadas: {cucharadas}")

    def recoger_vaso(self):
        """
        Procesa la solicitud de recoger el vaso, verificando la disponibilidad de recursos.

        :raises SinRecursosError: Si faltan vasos, azúcar o café.
        """
        if self.tamano_vaso is None:
            raise SinRecursosError("No se ha seleccionado el tamaño del vaso.")

        # Verificar existencia de vaso
        if self.vasos[self.tamano_vaso] <= 0:
            raise SinRecursosError("No hay vasos disponibles.")

        # Verificar existencia de azúcar
        if self.cucharadas_azucar > self.cantidad_azucar:
            raise SinRecursosError("No hay azúcar disponible.")

        # Determinar la cantidad de café requerida
        cantidad_necesaria = self.obtener_cantidad_cafe(self.tamano_vaso)
        if cantidad_necesaria > self.cantidad_cafe:
            raise SinRecursosError("No hay café disponible.")

        # Deduct resources
        self.vasos[self.tamano_vaso] -= 1
        self.cantidad_azucar -= self.cucharadas_azucar
        self.cantidad_cafe -= cantidad_necesaria

        # Reset selections
        self.reset_selecciones()

        print("¡Vaso de café listo para recoger!")

    def obtener_cantidad_cafe(self, tamano_vaso):
        """
        Retorna la cantidad de café necesaria según el tamaño del vaso.

        :param tamano_vaso: Tamaño del vaso seleccionado.
        :return: Cantidad de café en Oz.
        """
        tamanos = {
            "Pequeño": 3,
            "Mediano": 5,
            "Grande": 7
        }
        return tamanos.get(tamano_vaso, 0)

    def reset_selecciones(self):
        """Reinicia las selecciones de vaso y azúcar."""
        self.tamano_vaso = None
        self.cucharadas_azucar = 0

    def recargar_cafe(self, cantidad):
        """
        Permite recargar café en la máquina.

        :param cantidad: Cantidad de café a recargar en Oz.
        :raises ValueError: Si la cantidad es negativa.
        """
        if cantidad < 0:
            raise ValueError("La cantidad a recargar no puede ser negativa.")
        self.cantidad_cafe += cantidad
        print(f"Café recargado. Cantidad actual: {self.cantidad_cafe} Oz.")

    def recargar_azucar(self, cantidad):
        """
        Permite recargar azúcar en la máquina.

        :param cantidad: Cantidad de azúcar a recargar en cucharadas.
        :raises ValueError: Si la cantidad es negativa.
        """
        if cantidad < 0:
            raise ValueError("La cantidad a recargar no puede ser negativa.")
        self.cantidad_azucar += cantidad
        print(f"Azúcar recargada. Cantidad actual: {self.cantidad_azucar} cucharadas.")

    def recargar_vasos(self, tamano, cantidad):
        """
        Permite recargar vasos en la máquina.

        :param tamano: Tamaño del vaso a recargar.
        :param cantidad: Cantidad de vasos a recargar.
        :raises VasoInvalidoError: Si el tamaño del vaso no es válido.
        :raises ValueError: Si la cantidad es negativa.
        """
        if tamano not in self.vasos:
            raise VasoInvalidoError("Tamaño de vaso inválido.")
        if cantidad < 0:
            raise ValueError("La cantidad a recargar no puede ser negativa.")
        self.vasos[tamano] += cantidad
        print(f"Vasos {tamano} recargados. Cantidad actual: {self.vasos[tamano]} unidades.")
