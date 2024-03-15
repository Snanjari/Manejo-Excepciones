from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        """
        Inicializa una nueva instancia de Foto.

        Args:
            ancho (int): El ancho de la foto.
            alto (int): El alto de la foto.
            ruta (str): La ruta de la foto.
        """
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta

    @property
    def ancho(self) -> int:
        """
        Obtiene el ancho de la foto.

        Returns:
            int: El ancho de la foto.
        """
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        """
        Establece el ancho de la foto y verifica si cumple con las condiciones.

        Args:
            ancho (int): El nuevo ancho de la foto.

        Raises:
            DimensionError: Si el nuevo ancho es menor o igual a cero o excede el tamaño máximo permitido.
        """
        if ancho <= 0:
            raise DimensionError("El ancho debe ser mayor que cero", dimension="Ancho", maximo=self.MAX)
        if ancho > self.MAX:
            raise DimensionError(f"El ancho excede el máximo permitido de {self.MAX}", dimension="Ancho", maximo=self.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        """
        Obtiene el alto de la foto.

        Returns:
            int: El alto de la foto.
        """
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        """
        Establece el alto de la foto y verifica si cumple con las condiciones.

        Args:
            alto (int): El nuevo alto de la foto.

        Raises:
            DimensionError: Si el nuevo alto es menor o igual a cero o excede el tamaño máximo permitido.
        """
        if alto <= 0:
            raise DimensionError("El alto debe ser mayor que cero", dimension="Alto", maximo=self.MAX)
        if alto > self.MAX:
            raise DimensionError(f"El alto excede el máximo permitido de {self.MAX}", dimension="Alto", maximo=self.MAX)
        self.__alto = alto
