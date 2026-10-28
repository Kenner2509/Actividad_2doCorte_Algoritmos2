class Nodo:
    """Representa a un miembro de la familia dentro del árbol."""

    def __init__(self, nombre):
        self.nombre = nombre   # Dato que guarda el nodo
        self.hijos = []        # Lista de hijos (árbol general, no solo binario)

    def agregar_hijo(self, hijo):
        """Inserta un nodo hijo debajo de este nodo."""
        self.hijos.append(hijo)
        return hijo            # Se retorna para poder encadenar inserciones


def postorden(nodo, resultado=None):
    """
    Recorre el árbol en postorden de forma recursiva:
      1) Recorre cada hijo de izquierda a derecha.
      2) Al terminar con los hijos, visita el nodo actual (la raíz).
    """
    if resultado is None:
        resultado = []
    for hijo in nodo.hijos:          # Izquierda -> derecha
        postorden(hijo, resultado)   # Se baja primero a los descendientes
    resultado.append(nodo.nombre)    # La raíz se visita al final
    return resultado


def mostrar_arbol(nodo, nivel=0):
    """Imprime el árbol con sangría según el nivel (1 = raíz)."""
    print("    " * nivel + f"- {nodo.nombre} (Nivel {nivel + 1})")
    for hijo in nodo.hijos:
        mostrar_arbol(hijo, nivel + 1)

# NIVEL 1: raíz (abuelo)
abuelo = Nodo("Abuela Alba")

# NIVEL 2: hijos del abuelo
padre = abuelo.agregar_hijo(Nodo("Madre Socorro"))
tia = abuelo.agregar_hijo(Nodo("Tía Luz Estela"))
madre_tio = abuelo.agregar_hijo(Nodo("Tío Alí"))

# NIVEL 3: nietos del abuelo
padre.agregar_hijo(Nodo("Yo"))
padre.agregar_hijo(Nodo("Hermano Jose Daniel"))
tia.agregar_hijo(Nodo("Prima Camila"))
madre_tio.agregar_hijo(Nodo("Prima Melany"))

# ---------------- Ejecución ----------------
print("ÁRBOL FAMILIAR:")
mostrar_arbol(abuelo)

print("\nRECORRIDO EN POSTORDEN (hijos -> raíz):")
orden = postorden(abuelo)
print(" -> ".join(orden))