# Desafío Evaluado: Manejo-Excepciones //

## Descripción:

Este proyecto consiste en la creación de una excepción personalizada llamada DimensionError, que se utiliza para manejar errores relacionados con dimensiones en un programa. Además, se implementa la validación de dimensiones en una clase Foto, donde se lanzará la excepción DimensionError si se intenta establecer un ancho o alto no válido para la foto.

La excepción DimensionError permite especificar un mensaje de error, la dimensión (ancho o alto) y un valor máximo permitido para esa dimensión. Esta información ayuda a identificar y manejar mejor los errores relacionados con las dimensiones.

## Empezando 🚀

Estas instrucciones te guiarán para obtener una copia de este proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

Clonar el repositorio
bash
Copy code
git clone urlgit


### Prerrequisitos 📋
Python 3.x

#### Uso
Para utilizar la excepción DimensionError, simplemente instancie un objeto DimensionError y proporcione el mensaje de error, la dimensión y el valor máximo permitido (opcionalmente). Luego, maneje la excepción según sea necesario en su código.

En el caso de la clase Foto, puede crear una instancia de Foto y establecer el ancho y alto utilizando los métodos setter. Si se proporciona un valor no válido para el ancho o alto, se lanzará la excepción DimensionError.

### Autor ✒️
Simón Nanjarí - Desarrollador principal, Diseño y documentación, Pruebas y calidad
