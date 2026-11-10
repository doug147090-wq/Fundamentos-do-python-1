# Criando o tabuleiro com listas de 1 a 9
tabuleiro = [' ' for _ in range(9)]


def exibir_tabuleiro():
  print(f'\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ')
  print('---|---|---')
  print(f' {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ')
  print('---|---|---')
  print(f' {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} \n')


def verificar_vencedor(tab, jogador):
  # Combinações possíveis para vencer (linhas, colunas e diagonais)
  vitorias = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],  # Linhas
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],  # Colunas
      [0, 4, 8],
      [2, 4, 6],  # Diagonais
  ]
  for condicao in vitorias:
    if tab[condicao[0]] == tab[condicao[1]] == tab[condicao[2]] == jogador:
      return True
  return False


jogador_atual = 'X'
jogadas = 0

while True:
  exibir_tabuleiro()
  print(f'Vez do jogador {jogador_atual}')

  try:
    escolha = int(input('Escolha uma posição de 1 a 9: ')) - 1
    if escolha < 0 or escolha > 8:
      print('Posição inválida! Escolha um número entre 1 e 9.')
      continue
    if tabuleiro[escolha] != ' ':
      print('Essa posição já está ocupada! Tente outra.')
      continue
  except ValueError:
    print('Por favor, digite apenas números.')
    continue

  tabuleiro[escolha] = jogador_atual
  jogadas += 1

  if verificar_vencedor(tabuleiro, jogador_atual):
    exibir_tabuleiro()
    print(f'Parabéns! O jogador {jogador_atual} venceu!')
    break

  if jogadas == 9:
    exibir_tabuleiro()
    print('Deu empate!')
    break

  # Alterna o jogador
  jogador_atual = 'O' if jogador_atual == 'X' else 'X'