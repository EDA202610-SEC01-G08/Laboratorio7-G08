from DataStructures.Tree import bst_node
def new_map():
    return {"root": None}

def put(my_bst, key, value):
    """
    Agrega un nuevo nodo al árbol binario. Si la llave ya existe, se actualiza el valor del nodo.
    """
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst
    
def insert_node(node, key, value):
    if node is None:
        return bst_node.new_node(key, value)
    
    if key < node["key"]:
        node["left"] = insert_node(node["left"], key, value)
    elif key > node["key"]:
        node["right"] = insert_node(node["right"], key, value)
    else:
        node["value"] = value
    
    node["size"] = 1 + size(node["left"]) + size(node["right"])
    return node

def size(node):
    return node.get("size", 0)

def get(my_bst, key):
    """
    Busca un nodo en el árbol binario por su llave y devuelve su valor, si la llave no existe, devuelve None.
    """
    return get_node(my_bst["root"], key)

def get_node(root, key):
    if root is None:
        return None
    
    if key < root["key"]:
        return get_node(root["left"], key)
    elif key > root["key"]:
        return get_node(root["right"], key)
    else:
        return root["value"]


    
    
    
    
    