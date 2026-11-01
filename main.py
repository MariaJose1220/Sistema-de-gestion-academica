
from controllers.persona_controller import PersonaController
from controllers.programa_controller import ProgramaController
from controllers.asignatura_controller import AsignaturaController
from controllers.grupo_controller import GrupoAcademicoController

from menus.menu_principal import menu_principal


def main():

    persona_controller = PersonaController()
    programa_controller = ProgramaController()
    asignatura_controller = AsignaturaController()
    grupo_controller = GrupoAcademicoController()

    menu_principal(
        persona_controller,
        programa_controller,
        asignatura_controller,
        grupo_controller
    )


if __name__ == "__main__":
    main()
