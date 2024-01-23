import random
from os import system, name

# função para limpar a tela

def limpa_tela():
    #windows
    if name == 'nt':
        _ = system('cls')
    #mac ou linux
    else:
        _ = system('clear')

def display_hangman(chances):
    stages = [
        """
             ______        
            |      |
            |      0
            |    - | -
            |      |
            |     / \\
            -
        """,
        """
             ______        
            |      |
            |      0
            |    - | -
            |      |
            |     / 
            -
        """,
        """
             ______        
            |      |
            |      0
            |    - | -
            |      |
            |      
            -
        """,
        """
             ______        
            |      |
            |      0
            |    - |
            |      |
            |      
            -
        """, 
        """
             ______        
            |      |
            |      0
            |      |
            |      |
            |      
            -
        """,
        """
             ______        
            |      |
            |      0
            |    
            |      
            |      
            -
        """,
        """
             ______        
            |      |
            |      
            |    
            |      
            |      
            -
        """,
    ]
    return stages[chances]
    
# definindo função do jogo
def game():

    limpa_tela()
    
    print('\nBem vindo ao jogo da forca')
    print('Adivinhe o filme do oscar 2021 ou você não é ciníefilo de verdade\n')

    #lista de palavras
    filmes = [
    'nomadland',
    'minari',
    'mank',
    'soundofmetal',
    'judasandtheblackmessiah',
    'promisingyoungwoman',
    'thetrialofthechicago7',
    'thefather',
    'da5bloods',
    'Theshapeofwater',
    ]
    filme = random.choice(filmes)

    # List comprehesion (Loop for em uma lista)
    tabuleiro = ["_"] * len(filme)

    #Número de tentativas
    chances = 6

    #Número de letras erradas
    letras_erradas = []

    while chances > 0:

        #print
        print(display_hangman(chances))
        print("Filme: ", tabuleiro)
        print('\nChances Restantes:', chances)
        print('Letras erradas:'," ".join(letras_erradas))

        #input
        tentativa = input('\nDigite uma letra: '.lower())

     #verificar se possui a letra
        if tentativa in filme:
            index = 0
            for letra in filme:
                if tentativa == letra:
                    tabuleiro[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        if "_" not in tabuleiro:
            print('\nParabéns você ganhou! A palara era: ', filme)
            break

    if "_" in tabuleiro:
        print("Você perdeu a palavra era: ", filme)

if __name__ == "__main__":
    while True:
        game()
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break
    


