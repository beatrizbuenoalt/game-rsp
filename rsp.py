#importa as cores, o tempo e o randomizer
from colorama import init, Fore, Style
init()
import time
import random


# CONFIGURAÇÕES DO JOGO
# atalhos: permite digitar só a letra em vez da palavra inteira
SHORTCUTS = {"r": "rock", "p": "paper", "s": "scissor"}

# emojis pra deixar visual
EMOJIS = {"rock": "🪨", "paper": "📄", "scissor": "✂️"}

# regra do jogo: cada chave VENCE o valor correspondente
BEATS = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper"
}

CHOICES = ["rock", "paper", "scissor"]


# FUNÇÕES
def show_intro(): #define a introdução do jogo
    print("=" * 40)
    print(
        f"Let's play {Fore.LIGHTBLACK_EX}Rock{Style.RESET_ALL}, "
        f"{Fore.BLUE}Paper{Style.RESET_ALL} and "
        f"{Fore.LIGHTYELLOW_EX}Scissor{Style.RESET_ALL}! (Press Ctrl+C to exit)"
    )
    time.sleep(1)


def get_player_choice(): #pega a escolha do jogador 
    player_choice = input("Choose Rock, Paper or Scissor (or r/p/s): ").lower()
    player_choice = SHORTCUTS.get(player_choice, player_choice) #altera os atalhos para a sua resposta normal

    while player_choice not in CHOICES: #validação de resposta
        print("=" * 40)
        print(f"{Fore.RED}Invalid choice! Please choose Rock, Paper or Scissor.{Style.RESET_ALL}")
        print("=" * 40)
        time.sleep(1)

        player_choice = input("Choose Rock, Paper or Scissor (or r/p/s): ").lower()
        player_choice = SHORTCUTS.get(player_choice, player_choice)

    return player_choice #volta em looping caso o player não escolha a resposta certa


def determine_winner(player_choice, computer_choice): #determina o ganhador
    if player_choice == computer_choice:
        return "draw"
    elif BEATS[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"


def play_round(): #faz a rodada do jogo
    print("=" * 40)

    player_choice = get_player_choice()

    print("=" * 40)

    # tempo de espera antes da resposta do bot
    time.sleep(1)

    computer_choice = random.choice(CHOICES)

    print(f"Computer chose: {EMOJIS[computer_choice]} {computer_choice}")
    print("=" * 40)

    # tempo de espera pro resultado final
    time.sleep(1)

    winner = determine_winner(player_choice, computer_choice)

    if winner == "draw":
        print(f"{Fore.YELLOW}It's a draw!{Style.RESET_ALL}")
    elif winner == "player":
        print(f"{Fore.GREEN}You win!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}The computer wins!{Style.RESET_ALL}")

    return winner 


def show_score(player_score, computer_score): #mostra o score dos jogadores
    print("=" * 40)
    print(
        f"Score -> {Fore.GREEN}You: {player_score}{Style.RESET_ALL} "
        f"x {Fore.RED}Computer: {computer_score}{Style.RESET_ALL}"
    )
    print("=" * 40)


# ============================================================
# LOOP PRINCIPAL DO JOGO
# ============================================================

def main(): #faz o loop para que a pessoa jogue quantas vezes quiser
    show_intro()

    player_score = 0
    computer_score = 0
    play_again = True

    try:
        while play_again: 
            winner = play_round()

            if winner == "player":
                player_score += 1
            elif winner == "computer":
                computer_score += 1

            show_score(player_score, computer_score)

            answer = input("Play again? (y/n): ").lower()
            play_again = answer == "y" #se a resposta for sim, a pessoa vai jogar de novo

        print(#se a pessoa escolher 'n' o jogo acaba e mostra o placar
            f"\n{Fore.LIGHTCYAN_EX}"
            f"Thanks for playing! Final score -> "
            f"You: {player_score} x Computer: {computer_score}"
            f"{Style.RESET_ALL}"
        )

    except KeyboardInterrupt: 
        # pode sair usando Ctrl+C
        print(
            f"\n\n{Fore.LIGHTCYAN_EX}"
            f"Leaving the game... See you next time! 👋"
            f"{Style.RESET_ALL}"
        )


if __name__ == "__main__":
    main()