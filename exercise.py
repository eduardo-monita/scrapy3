def exercise_one(value):
    if value > 0:
        response = 0
        for number in range(value):
            response += number + 1
        return response
    else:
        return print("O número precisa ser maior que 0")

def exercise_two(value):
    new_phrases = []
    for phrase in value:
        remove_duplicated = ""
        phrase_len = len(phrase)-1
        for index, letter in enumerate(phrase):
            if not phrase_len == index and letter == list(phrase)[index + 1]:
                pass
            else:
                remove_duplicated= remove_duplicated + letter
        new_phrases.append(remove_duplicated)
    return new_phrases

while True:
    print("\nEscolha uma opção abaixo:")
    print("""
1 - Método de some
2 - Remover letras duplicadas""")
    escolha = int(input())

    if escolha == 1:
        value = int(input("Digite um número inteiro: "))
        print("Resultado: " + str(exercise_two(value)))
    elif escolha == 2:
        print("\nDigite uma lista de frases com letras seguidas duplicadas e precione 0 para parar:")
        array_staing = []
        while True:
            phrase = str(input("Digite uma frase: "))
            if phrase == "0":
                break
            array_staing.append(phrase)
        print("Resultado: " + str(exercise_two(array_staing)))

    print("""
Deseja Continuar?
1 - Sim
2 - Não""")
    escolha = int(input())
    
    if escolha == 2:
        break
