import random    #Importo la librería "random".

def guess_number(is_replay = False, game_start = ""):     #Creo la función principal que contiene el código del juego con los parámetros is_replay y game_start para implementar rejugabilidad.
    try:
        if is_replay == False:         #Si el usuario desea volver a jugar, no le saltará esta línea de diálogo.
            game_start = input("Do you want to play a guessing game? type y for yes, n for no: ")

        #El bucle principal que contiene el juego.
        if game_start == "y" or is_replay == True:
            #Defino todas las variables necesarias para el juego, como por ejemplo el rango mínimo y máximo, el número secreto, étc..
            minimum = int(input("Please enter the minimum integer for the guessing game: "))
            maximum = int(input("Please enter the maximum integer for the guessing game: "))
            secret_number = random.randint(minimum, maximum)
            user_guess = int(input(f"Guess the number between {minimum} and {maximum} with both ends included: "))
            attempts = 1
            
            #Creo un bucle while para que se ejecute hasta que el usuario adivine el número secreto.
            while user_guess != secret_number:
                attempts += 1
                if user_guess > maximum or user_guess < minimum:
                    print(f"Please enter a number between {minimum} and {maximum}")
                    user_guess = int(input(" "))
                elif user_guess < secret_number:
                    print("The number is higher.")
                    user_guess = int(input(" "))
                else:
                    print("The number is lower")
                    user_guess = int(input(" "))

            #Una vez el usuario haya acertado el número, se sale del bucle while y le sale un breve mensaje y tiene la opción de volver a jugar.
            print(f"Congratulations! You guessed the correct number: {secret_number}, and took {attempts} attempts!")
            game_replay = input("Do you wish to play again? type y for yes, n for no: ")

            #Implemento una serie de "if" statements para preguntarle al usuario si desea volver a jugar.
            if game_replay == "y":
                guess_number(is_replay=True)
            elif game_replay == "n":
                print("See you soon!")
                exit
            else:
                exit

        else:
            print("See you soon!")
            exit

    except ValueError:      #El "except ValueError" se utiliza en caso de que el input del usuario no sea un número entero.
        print("Please enter a valid input")
        guess_number(is_replay=True)

if __name__ == "__main__":      #Llamo la función.
    guess_number()


