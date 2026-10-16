# Conjuntos

# . add()
my_set = {1, 2, 3}
my_set.add(6)
my_set.add(3)  # lo ignora
print(my_set)

# .remove()  Elimina un elemento pero da error si no existe
my_set.remove(2)
print(my_set)

# . discard() No marca error si no existe
my_set.discard(3)
print(my_set)
my_set.discard(3)  # lo ignora
print(my_set)


# .pop() Elimina un elemento al azar y lo devuelve
print(my_set.pop())
print(my_set)
