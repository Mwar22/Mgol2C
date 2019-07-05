#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Created by: Lucas de Jesus B.G
# Creation date: 13/04/2019

# Programmers: Lucas de Jesus & Welerson Assis

class Token:
    def __init__(self, token, lexema, tipo, row, col):
        self.__token = token
        self.__lexema = lexema
        self.__tipo = tipo
        self.__row = row
        self.__col = col


    #metodos getter e setter
    def getLexem(self):
        return self.__lexema

    def getTk(self):
        return self.__token

    def getRow(self):
        return self.__row

    def setRow(self, row):
        self.__row = row

    def getCol(self):
        return self.__col

    def setCol(self, col):
        self.__col = col

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo

    #funções extras

    def copy(self):
        return Token(self.__token, self.__lexema, self.__tipo, self.__row, self.__col)
    def prt(self):
        print('Lexema: ' + self.__lexema + '  Token: '+self.__token)
        

class SymbolTable:

    def __init__(self):
        self.__hash_tbl = {}


    #inseri um elemento  na tabela hash, dada uma chave e um objeto Token
    def inserir(self, key, token):
        if self.consultar(key) == False:
            self.__hash_tbl[key] = token
            return 0
        return -1
        

    #retorna um elemento (Token) dado uma chave key
    def ler(self, key):
        try:
            return self.__hash_tbl.get(key)
        except:
            print('Chave'+ str(key)+' não encontrada!')

        
    #Retorna True se existir elemento na tabela indexado pela chave key
    def consultar(self, key):
        if key in self.__hash_tbl:
            return True
        else:
            return False
    
    def excluir(self, key):
        try:
            self.__hash_tbl.pop(key)
        except:
            print('Chave'+ str(key)+' não encontrada!')

    def print_table(self):
        for i in self.__hash_tbl:
            tk = self.__hash_tbl[i]
            tk.prt()
        


class LexicAnalyser:

    #Alfabeto da linguagem e lista de estados finais, bem como o token respectivo à estes estados

    __alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/(){}<>=.;_"\t\n '
    __final_state = [1, 3, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    __token = ['Num', 'Num', 'Num', 'Literal', 'id', 'Comentario', 'OPR', 'OPR', 'OPR', 'OPR', 'RCB', 'OPM', 'AB_P', 'FC_P', 'PTV']


    #   Formato: Cada linha representa um símbolo do alfabeto e as colunas os estados atuais.
    #   Os estados seguintes são representados pelos números em cada posição. -1 indica que não há transição em um dado estado e entrada.
    #   Nesta situação estados finais são reconhecidos, ou outros são tratados como erro.

    __transition_tbl = [
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,4,-1,4,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [9,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [1,1,3,3,6,6,6,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [1,1,3,3,6,6,6,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [1,1,3,3,6,6,6,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [1,1,3,3,6,6,6,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [1,1,3,3,6,6,6,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [1,1,3,3,6,6,6,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [1,1,3,3,6,6,6,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [1,1,3,3,6,6,6,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [1,1,3,3,6,6,6,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [1,1,3,3,6,6,6,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [17,-1,-1,-1,5,-1,5,7,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [17,-1,-1,-1,5,-1,5,7,-1,-1,10,-1,16,-1,-1,-1,-1,-1,-1,-1,-1],
        [17,-1,-1,-1,-1,-1,-1,7,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [17,-1,-1,-1,-1,-1,-1,7,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [18,-1,-1,-1,-1,-1,-1,7,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [19,-1,-1,-1,-1,-1,-1,7,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [10,-1,-1,-1,-1,-1,-1,7,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,7,-1,-1,11,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [12,-1,-1,-1,-1,-1,-1,7,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [13,-1,-1,-1,-1,-1,-1,7,-1,-1,10,-1,15,-1,-1,-1,-1,-1,-1,-1,-1],
        [14,-1,-1,-1,-1,-1,-1,7,-1,-1,10,-1,14,14,-1,-1,-1,-1,-1,-1,-1],
        [-1,2,-1,-1,-1,-1,-1,7,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [20,-1,-1,-1,-1,-1,-1,7,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,7,-1,9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [7,-1,-1,-1,-1,-1,-1,8,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [0,-1,-1,-1,-1,-1,-1,7,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [0,-1,-1,-1,-1,-1,-1,7,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [0,-1,-1,-1,-1,-1,-1,7,-1,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]



    # Método construtor da classe
    def __init__(self, font_file):
        
        #file handler para o fonte especificado
        self.__font_file = font_file
        
        #informações do autômato
        self.__cur_state = 0
        self.__char_index = 0
        self.__buffer = ''

        #contadores de linha e coluna
        self.__row = 1
        self.__col = 0

        #inicializa um objeto do tipo SymbolTable e inializa as palavras reservadas (e o token das mesmas):
        self.__st = SymbolTable()

        res_words = ['inicio', 'varinicio', 'varfim', 'escreva', 'leia', 'se', 'entao', 'fimse', 'fim', 'int', 'lit', 'real']
        for rw in res_words:
            self.__st.inserir(rw, Token(rw, rw, '', 0, 0))
        

    #método que retorna a tabela de símbolos
    def getSymbolTable(self):
        return self.__st

    #Método geral da classe, retorna um objeto Token
    def lexico(self):
        

        #Lê um caractere e avança o carro
        self.__font_file.seek(self.__char_index)
        char = self.__font_file.read(1)
        self.__char_index += 1
        

        #Chegou no fim do arquivo?
        if char == '': 
            self.__cur_state = 0
            return Token('$', 'EOF','', self.__row, self.__col +1)

        else:
             


            #calcula sym_row, final e next
            sym_row = self.__in_alphabet(char)
            final = self.__is_final_state(self.__cur_state) 

            #-1 caso não exista transições
            next = -1   
            if sym_row != -1:
                next = self.__transition_tbl[sym_row][self.__cur_state]  


            #se for estado final...
            if final != -1:

                #se o caractere não pertence ao alfabeto ou não existe transição
                if sym_row == -1 or next == -1:


                    #cria um token e depois de resetar o buffer e o estado, o envia
                    tk = Token(self.__token[final], self.__buffer,'none', self.__row, (self.__col - len(self.__buffer) + 1))
                    bf = self.__buffer  #backup do valor do buffer (pois o buffer real é resetado na sequência)

                    self.__buffer = ''
                    self.__cur_state = 0


                    #caso esteja no alfabeto
                    if sym_row != -1:

                        #volta o leitor
                        self.__char_index -= 1
                         
             
                    else:
                        #atualiza as linhas e coluna (pois o retorno do token impede o procedimento segundo o fluxo padrão)
                        self.__rowcol(char) 
                        print('ERRO~ '+ str(self.__row) + ':'+ str(self.__col) + ' Caractere '+char+' é permitido apenas entre "..." ou {...} !')




                    #Seção responsável pelo manuseamento da tabela de símbolos
                    #Se o tipo do token for um id...
                    if self.__token[final] == 'id':
                        
                        #Verifica se está na tabela. Retorna o que estiver, e adiciona se não estiver
                        if self.__st.consultar(bf):
                            tk = self.__st.ler(bf)
                            tk.setRow(self.__row)
                            tk.setCol(self.__col -len(tk.getLexem()) + 1)
                            return tk
                        else:
                            #adiciona na tabela
                            self.__st.inserir(bf, tk)
                            return tk
                    #retorna o token, se não for id
                    return tk

      
                    

            #atualiza as linhas e colunas (estados não finais, fluxo padrão)
            self.__rowcol(char) 
           
            #se existe transição... (sendo estado final ou não)
            if next != -1: 
                #concatena o caractere (apenas  se não for TAB,SALTO, ESPAÇO) e muda de estado
                if char != '\t' and char != '\n' and char != ' ':
                    self.__buffer += char
                    self.__cur_state = next

            elif final == -1:#se não existe transição e não é estado final

                #caso não esteja nos estados que aceitem qualquer coisa...
                if self.__cur_state != 7 and self.__cur_state != 10:
                    
                    #se o caractere for especial (não pertencer à gramatica)
                    if sym_row == -1:
                        print('ERRO~ '+str(self.__row) + ':'+ str(self.__col) +' Caractere '+char+' é permitido apenas entre "..." ou {...} !')
                    else:
                        print('ERRO~ '+ str(self.__row) + ':'+ str(self.__col) + ' Caractere '+char+' não esperado em '+self.__buffer+char+' !')
                    
                    #reseta o buffer e começa novamente do estado inicial
                    self.__buffer = ''
                    self.__cur_state = 0
                    

                else:
                    #concatena o caractere 
                    self.__buffer += char

                 

            
                    
          

            #executa novamente (lê o próximo caractere, até reconhecer algum token)
            return self.lexico()
             

    # Faz update nas linhas/colunas
    def __rowcol(self, char):
        if char != '\n':
            self.__col += 1
        else:
            self.__row += 1
            self.__col = 0

    #   Retorna -1 se não pertencer ao alfabeto ou a posição, caso o contrário.
    def __in_alphabet(self, char):
        for i in range(0, 80):
            if self.__alphabet[i] == char:
                return i
        return -1

    #   Retorna o index se for estado final, -1 caso o contrário. (busca linear simples, poucos valores)
    def __is_final_state(self, state):
        for i in range (0,15):
            if self.__final_state[i] == state:
                return i

        return -1

