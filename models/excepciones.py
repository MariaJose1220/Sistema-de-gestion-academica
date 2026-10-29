"""Excepciones personalizadas del Sistema de Gestión Académica.

Cada clase representa una situación excepcional del proceso de matrícula
o de búsqueda. Todas heredan de SistemaAcademicoError, de modo que el
programa principal puede capturarlas una por una o todas juntas.
"""


class SistemaAcademicoError(Exception):
    """Clase base de todas las excepciones propias del sistema."""


class EstudianteYaMatriculadoError(SistemaAcademicoError):
    """Se lanza al intentar matricular un estudiante que ya está en el grupo."""


class CapacidadMaximaError(SistemaAcademicoError):
    """Se lanza al intentar matricular un estudiante en un grupo lleno."""


class EstudianteNoMatriculadoError(SistemaAcademicoError):
    """Se lanza al intentar retirar un estudiante que no está en el grupo."""


class AsignaturaNoEncontradaError(SistemaAcademicoError):
    """Se lanza cuando se busca una asignatura que no está registrada."""


class ProgramaNoEncontradoError(SistemaAcademicoError):
    """Se lanza cuando se busca un programa académico que no está registrado."""
