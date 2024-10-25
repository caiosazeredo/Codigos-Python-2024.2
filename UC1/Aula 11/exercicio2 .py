inventario = ["espada", "escudo", "poção"]
print("Inventário inicial:", inventario)
pergunta = input("Você encontrou um arco em uma clareira. Deseja adicioná-lo ao inventário? (S/N): ").lower()

if pergunta == "s":
  
    print("Você precisa remover um item do inventário para carregar o arco.") 

    item = input("Qual item você deseja remover do inventário? ").lower()
    
    # Verificando se o item existe no inventário
    if item in inventario:
        inventario.remove(item)
        inventario.append("arco")
        print(f"Você removeu {item} e agora está carregando um arco.")
    else:
        print(f"O item '{item}' não está no inventário. Nada foi removido.")
else:
    print("Você decidiu não pegar o arco e continuou sua jornada.")


print("\nEnquanto você segue seu caminho pela floresta, um bandido armado surge e exige que você entregue sua poção!")

# Verificando se o jogador tem a espada para lutar
acao = input("O que você fará? (1 - Usar a espada, 2 - Entregar a poção): ")

if acao == "1":
    if "espada" in inventario:
        print("Você saca sua espada e enfrenta o bandido!")
        print("Após uma luta feroz, você derrota o bandido e continua sua jornada.")
    else:
        print("Você não tem uma espada! Sem defesa, o bandido te derrota facilmente.")
        print("Fim de jogo!")
elif acao == "2":
    if "poção" in inventario:
        inventario.remove("poção")
        print("Você entrega a poção ao bandido, e ele vai embora satisfeito.")
        print("Você perdeu a poção, mas está a salvo.")
    else:
        print("Você não tem uma poção para entregar!")
        print("Furioso, o bandido te ataca e você não consegue escapar.")
        print("Fim de jogo!")
else:
    print("Decisão inválida. O bandido aproveita sua hesitação e te derrota.")
    print("Fim de jogo!")

