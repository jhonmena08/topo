
__author__ = 'Jhon E. Mena Hurtado'
__title__= 'TopoCalc'
__date__ = '24/10/2025'


import math
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Point:
    # clase para representar un Punto 2D
    # ejemplo: Point(133.41, 96.12) 
    
    # variables de instancia
    x: float = 0.0
    y: float = 0.0
    descripcion: str = ''

    # variable de clase
    counter: ClassVar[int] = 0

    def __post_init__ (self) -> None:
        Point.counter += 1

        if self.descripcion == '':
            self.descripcion = 'p'+ str(Point.counter)


    def __str__(self) -> str:
        return f"Point x:{self.x:.4f}, y:{self.y:.4f}, {self.descripcion}"
    

    def to_tuple(self) -> tuple[float]:
        return(self.x, self.y, 0.0)

    
# end class


def acimut(a: Point, b: Point) -> float:
    # calcular el acimut de Dos puntos
    # ejemplo: acimut(a, b) -> 30.5466739988

    angulo = None
    if a != None and b != None:
        if isinstance(a, Point) and isinstance(b, Point):
            dx = b.x - a.x
            dy = b.y - a.y

            if dy != 0: angulo = abs(math.degrees(math.atan(dx/dy)))

            if dx > 0.0 and dy < 0.0:
                # cuadrante 2
                return 180 - angulo
            
            elif dx < 0.0 and dy < 0.0:
                # cuadrante 3
                return 180 + angulo

            elif dx < 0.0 and dy > 0.0:
                # cuadrante 4
                return 360 - angulo

            elif dx == 0.0 and dy > 0.0:
                return 0.0

            elif dx > 0.0 and dy == 0.0:
                return 90.0
                
            elif dx == 0.0 and dy < 0.0:
                return 180.0

            elif dx < 0.0 and dy == 0.0:
                return 270.0
            
    return angulo

# fin funccion


def distancia(a: Point, b: Point) -> float:
    # calcular la distancia entre 2 puntos
    resultado = None

    if a != None and b != None:
        if isinstance(a, Point) and isinstance(b, Point):
            dx = a.x - b.x
            dy = a.y - b.y
            resultado = math.sqrt(dx**2 + dy**2)

    return resultado

# fin de la funcion


def gms(angulo: float) -> str:
    # convertir a grados-min-seg
    # formato de salida -> 304-25-12

    try:
        grados: int = int(angulo)
        minutos: float = (angulo - int(angulo)) * 60
        segundos: float = (minutos - int(minutos)) * 60

        return f"{grados:03}-{int(minutos):02}-{int(round(segundos, 0)):02}"
    except(ValueError):
        print('Los valores deben ser numericos !!')
    except:
        print("Ufff, ocurrio un error..")
# fin de la funcion


def degree(fmt: str) -> float:
    # convertir el formato 334-25-10.46 a grados decimales

    if isinstance(fmt, str):
        try:
            array = fmt.split('-')
            grados = float(array[0])
            minutos = float(array[1]) / 60.0
            segundos = float(array[2]) / 3600.0

            return grados + minutos + segundos
        
        except(ValueError):
            print('los valores deben ser numerico !!')
        except:
            print("Ufff, ocurrio un error..")

# fin de la funcion


def acimut_dist(a: Point, b: Point) -> tuple[str, float]:
    # ejemplo: acimut_dist(a, b) -> ('62-39-43', 119.9804)

    az: str = None
    dist: float = None

    if a != None and b != None:
        if isinstance(a, Point) and isinstance(b, Point):
            az= gms(acimut(a, b))
            dist = round(distancia(a, b), 4)

    return (az, dist) 

# fin de la funcion



def punto_linea(a: Point, b: Point, desfases= list[float]) -> None:
    if isinstance(a, Point) and isinstance(b, Point):
        # convertir a radianes
        angulo = math.radians(acimut(a, b))

        for valor in desfases:
            e = a.x + math.sin(angulo) * valor
            n = a.y + math.cos(angulo) * valor
            print(f'{valor:.4f} -> {Point(e, n)}')
# fin de la funcion


def get_punto(a: Point, azimut: float, dist: float) -> Point:
    try:
        azimut = math.radians(azimut)
        e = a.x + math.sin(azimut) * dist
        n = a.y + math.cos(azimut) * dist

        return Point(e, n)

    except ValueError:
        print('Error de valores')

