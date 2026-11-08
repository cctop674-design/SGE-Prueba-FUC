"""
Sistema de Gestión de Estudiantes (SGE) básico
Aplicación por consola: agregar, mostrar, buscar por ID y salir.
"""

MAX_ESTUDIANTES = 50  # Tamaño máximo para evitar crecimiento descontrolado


def leer_entero(mensaje):
    """Pide un número entero y repite hasta que la entrada sea válida.
    Se usa while para no dejar que el programa caiga con texto inválido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida: escribe un número entero.")


def leer_texto(mensaje):
    """Pide un texto no vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Este campo no puede estar vacío.")


def leer_nota(mensaje):
    """Pide una nota entre 0.0 y 5.0 (escala colombiana)."""
    while True:
        try:
            nota = float(input(mensaje))
            if 0.0 <= nota <= 5.0:
                return nota
            print("La nota debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("Entrada inválida: escribe un número (ej. 3.8).")


def mostrar_menu():
    print("\n===== SGE - MENÚ PRINCIPAL =====")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Salir")


def mostrar_estudiante(estudiante):
    """Imprime los datos de un solo estudiante (unidad reutilizable)."""
    print(f"ID: {estudiante['id']} | Nombre: {estudiante['nombre']} | "
          f"Programa: {estudiante['programa']} | Nota: {estudiante['nota']:.1f}")


def id_existe(estudiantes, id_buscado):
    """Devuelve True si el ID ya está registrado."""
    for estudiante in estudiantes:
        if estudiante["id"] == id_buscado:
            return True
    return False


def agregar_estudiante(estudiantes, total):
    """Agrega un estudiante a la lista y devuelve el nuevo conteo."""
    if total >= MAX_ESTUDIANTES:
        print("Se alcanzó el límite máximo de estudiantes.")
        return total

    id_nuevo = leer_entero("ID del estudiante: ")
    # Decisión simple: evitar IDs duplicados
    if id_existe(estudiantes, id_nuevo):
        print("Ya existe un estudiante con ese ID.")
        return total

    nombre = leer_texto("Nombre: ")
    programa = leer_texto("Programa: ")
    nota = leer_nota("Nota final (0.0 - 5.0): ")

    estudiantes.append({
        "id": id_nuevo,
        "nombre": nombre,
        "programa": programa,
        "nota": nota,
    })
    total += 1  # Variable de conteo
    print("Estudiante agregado correctamente.")
    return total


def mostrar_estudiantes(estudiantes, total):
    """Recorre la lista con for y muestra cada registro."""
    if total == 0:
        print("No hay estudiantes registrados.")
        return
    print(f"\n--- Lista de estudiantes ({total}) ---")
    for estudiante in estudiantes:
        mostrar_estudiante(estudiante)


def buscar_estudiante(estudiantes):
    """Busca por ID recorriendo la lista; usa una bandera de encontrado."""
    id_buscado = leer_entero("ID a buscar: ")
    encontrado = False  # Bandera de búsqueda
    for estudiante in estudiantes:
        if estudiante["id"] == id_buscado:
            print("Estudiante encontrado:")
            mostrar_estudiante(estudiante)
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún estudiante con ese ID.")


def main():
    estudiantes = []        # Lista que almacena los datos
    total = 0               # Variable de conteo
    banderaSalir = False    # Bandera que controla el bucle principal

    while not banderaSalir:  # Repetición condicionada al comienzo
        mostrar_menu()
        opcion = leer_entero("Elige una opción: ")

        # Decisión múltiple para dirigir el flujo
        if opcion == 1:
            total = agregar_estudiante(estudiantes, total)
        elif opcion == 2:
            mostrar_estudiantes(estudiantes, total)
        elif opcion == 3:
            buscar_estudiante(estudiantes)
        elif opcion == 4:
            banderaSalir = True
            print("Saliendo del sistema. ¡Hasta pronto!")
        else:
            print("Opción no válida. Elige entre 1 y 4.")


if __name__ == "__main__":
    main()
