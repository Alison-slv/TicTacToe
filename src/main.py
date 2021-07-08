#!/usr/bin/python3
# author: alison silva

import os
from time import sleep

class TicTacToe:
    """
    classe principal do jogo
    """
    def __init__(self):
        # tabuleiro do jogo, uma lista de listas ou array tridimensional.
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player = "X"

    def showBoard(self):
        """
        metodo que exibe o tabuleiro do jogo
        """
        print("\nJOGO DA VELHA AO ESTILO CLI\n")
        for slot in self.board:
            print(f"{slot[0]} | {slot[1]} | {slot[2]}")
            
    def changePlayer(self):
        """
        metodo que faz a troca dos jogadores
        """
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def verifyMove(self, move):
        """
        este metodo verifica a jogada se for valida faz a insercao da jogada no tabuleiro
        """
        if move == 1 and self.board[0][0] == " ":
            self.board[0][0] = self.player
            return True
            
        elif move == 2 and self.board[0][1] == " ":
            self.board[0][1] = self.player
            return True
        
        elif move == 3 and self.board[0][2] == " ":
            self.board[0][2] = self.player
            return True
        elif move == 4 and self.board[1][0] == " ":
            self.board[1][0] = self.player
            return True
            
        elif move == 5 and self.board[1][1] == " ":
            self.board[1][1] = self.player
            return True
            
        elif move == 6 and self.board[1][2] == " ":
            self.board[1][2] = self.player
            return True
            
        elif move == 7 and self.board[2][0] == " ":
            self.board[2][0] = self.player
            return True
            
        elif move == 8 and self.board[2][1] == " ":
            self.board[2][1] = self.player
            return True
            
        elif move == 9 and self.board[2][2] == " ":
            self.board[2][2] = self.player
            return True
            
        else:
            return False
            
    def move(self, movePlayer):
    	verificationMove = self.verifyMove(movePlayer)
    	
    	if not verificationMove:
    		print("\nja escolhido")
    		self.changePlayer()
    		sleep(.5)
            
    def verifyWinner(self):
        """
        este metodo verifica se ouve vencedor ma rodada. ele verifica cada linha do tabuleiro se é igual a letra do jogador.
        """
        # verifica as linhas
        if self.board[0][0] == self.player and self.board[0][1] == self.player and self.board[0][2] == self.player:
            return self.player
            
        elif self.board[1][0] == self.player and self.board[1][1] == self.player and self.board[1][2] == self.player:
            return self.player
            
        elif self.board[2][0] == self.player and self.board[2][1] == self.player and self.board[2][2] == self.player:
            return self.player
            
        # verifica as colunas
        if self.board[0][0] == self.player and self.board[1][0] == self.player and self.board[2][0] == self.player:
            return self.player
            
        elif self.board[0][1] == self.player and self.board[1][1] == self.player and self.board[2][1] == self.player:
            return self.player
            
        elif self.board[0][2] == self.player and self.board[1][2] == self.player and self.board[2][2] == self.player:
            return self.player
            
        elif self.board[0][0] == self.player and self.board[1][1] == self.player and self.board[2][2] == self.player:
            return self.player
            
        elif self.board[0][2] == self.player and self.board[1][1] == self.player and self.board[2][0] == self.player:
            return self.player
            
    def verifyDraw(self):
        """
        metodo que faz a verificacao de empate, se ouver claro.
        ele percorre o tabuleiro que é uma lista e procura se algum slot é igaul a ""(vazio) se tiver que dizer que ainda tem slots vazios, se nao tiver DEU VELHA!
        """
        for slot in self.board:
            if " " in slot:
                return False
        return True
            
# cria a instacia da classe do jogo
tic = TicTacToe()

#chama o metodo para exibir o tabuleiro
while True:
	os.system("clear")
	tic.showBoard()
	print(f"\nJogador da vez: {tic.player}")
	try:
	    move = int(input("sua jogada: "))
	    while move not in (1,2,3,4,5,6,7,8,9):
	        print("jogada invalida, tente denovo")
	        move = int(input("sua jogada: "))
	    tic.move(move)
	    win = tic.verifyWinner()
	    if tic.verifyDraw():
	        os.system("clear")
	        print("empate")
	        tic.showBoard()
	        print("\ntentem denovo")
	        break
	    if win == tic.player:
	        os.system("clear")
	        print(f"o jagador {tic.player} venceu")
	        tic.showBoard()
	        print("\nparabens")
	        break
	    tic.changePlayer()
	    sleep(.5)
	
	except (KeyboardInterrupt, EOFError, ValueError):
	    if ValueError:
	        print("\napenas numeros sao permitidos\n")
	    print("Bye..")
	    sleep(1)
	    break