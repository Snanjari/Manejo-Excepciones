class DimensionError(Exception):
    """
    Excepción personalizada para errores relacionados con dimensiones.
    """

    def __init__(self, mensaje: str, dimension: str = None, maximo: int = None) -> None:
        """
        Inicializa una nueva instancia de DimensionError.

        Args:
            mensaje (str): Descripción del error.
            dimension (str, optional): La dimensión relacionada con el error. Por defecto es None.
            maximo (int, optional): El valor máximo permitido para la dimensión. Por defecto es None.
        """
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del error.

        Returns:
            str: La representación en cadena del error.
        """
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            return f"{self.mensaje} ({self.dimension}: {self.maximo})"
