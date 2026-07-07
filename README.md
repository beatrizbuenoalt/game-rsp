# 🪨📄✂️ Rock, Paper, Scissors (Terminal)

> 🇺🇸 **English below.**  
> 🇧🇷 **Português logo abaixo.**

---

# 🇺🇸 English

A Rock, Paper, Scissors game written in Python, played in the terminal, featuring input validation, keyboard shortcuts, a persistent scoreboard, and colorful output using `colorama`.

## Features

- Input validation (prevents the game from crashing due to invalid input)
- Keyboard shortcuts: type `r`, `p`, or `s` instead of the full word
- Persistent scoreboard between rounds
- Colored terminal output for wins, losses, and ties
- Emojis representing each move
- Safe exit with `Ctrl+C`

## How to Play

### Requirements

- Python 3.8+
- `colorama`

### Installation

```bash
git clone https://github.com/beatrizbuenoalt/rock-paper-scissors.git
cd rock-paper-scissors
pip install -r requirements.txt
```

### Run

```bash
python rock_paper_scissors.py
```

## Code Structure

The project is divided into small, independent functions:

| Function | Responsibility |
|----------|----------------|
| `show_intro()` | Displays the welcome message |
| `get_player_choice()` | Reads and validates the player's input |
| `determine_winner()` | Determines the winner of the round |
| `play_round()` | Runs a complete game round |
| `show_scoreboard()` | Displays the current scoreboard |
| `main()` | Main game loop |


## Author

Made by **Beatriz Bueno** as part of her Python studies (ETEC Technical Course – Systems Development).

---

# 🇧🇷 Português

Jogo de Pedra, Papel e Tesoura em Python, jogado pelo terminal, com validação de entrada, atalhos de teclado, placar contínuo e visual colorido usando `colorama`.

## Funcionalidades

- Validação de entrada (impede que o jogo trave com valores inválidos)
- Atalhos: digite `r`, `p` ou `s` em vez da palavra completa
- Placar persistente entre rodadas
- Cores no terminal para vitória, derrota e empate
- Emojis representando cada jogada
- Saída segura com `Ctrl+C`

## Como jogar

### Pré-requisitos

- Python 3.8+
- Biblioteca `colorama`

### Instalação

```bash
git clone https://github.com/beatrizbuenoalt/rock-paper-scissors.git
cd rock-paper-scissors
pip install -r requirements.txt
```

### Execução

```bash
python pedra_papel_tesoura.py
```

## Estrutura do código

O projeto é dividido em funções pequenas e independentes:

| Função | Responsabilidade |
|--------|------------------|
| `mostrar_intro()` | Exibe a mensagem inicial |
| `pegar_escolha_jogador()` | Lê e valida a entrada do jogador |
| `descobrir_vencedor()` | Determina o vencedor da rodada |
| `jogar_rodada()` | Executa uma rodada completa |
| `mostrar_placar()` | Exibe o placar atualizado |
| `main()` | Loop principal do jogo |


## Autora

Feito por **Beatriz Bueno** como parte dos estudos de Python (Curso Técnico em Desenvolvimento de Sistemas – ETEC).
