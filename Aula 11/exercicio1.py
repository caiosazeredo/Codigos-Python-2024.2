inventario = ["espada", "escudo", "poção"]

print("Inventário inicial:", inventario)
pergunta = input("Você encontrou um arco, deseja adicionar? S/N:").lower()
if pergunta == "s":
    item = input("Qual item remover? ").lower()
    inventario.remove(item)
    inventario.append("arco")
    print("Inventário após encontrar um novo item:", inventario)
else:
    print("Nada acontece")