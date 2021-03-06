#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import semantic_lib
from lexic import Token
from semantic_lib import sem

#Gramática
G = ["P' -> P", "P -> inicio V A", "V -> varinicio LV","LV -> D LV", "LV -> varfim;",
"D -> id TIPO;", "TIPO -> int", "TIPO -> real", "TIPO -> lit", "A -> ES A",
     "ES -> leia id;", "ES -> escreva ARG;", "ARG -> literal", "ARG -> num", "ARG -> id", 
     "A -> CMD A", "CMD -> id rcb LD;", "LD -> OPRD opm OPRD", "LD -> OPRD", "OPRD -> id", 
     "OPRD -> num", "A -> COND A", "COND -> CABEÇALHO CORPO", "CABEÇALHO -> se (EXP_R) entao",
     "EXP_R -> OPRD opr OPRD", "CORPO -> ES CORPO", "CORPO -> CMD CORPO", "CORPO -> COND CORPO", 
     "CORPO -> fimse", "A -> fim"]


# |betha| (numero de símbolos à direita de cada produção)
betha_sz = [3, 2, 2, 2, 3, 1, 1, 1, 2, 3, 3, 1, 1, 1, 2, 4, 3, 1, 1, 1, 2, 2, 5, 3, 2, 2, 2, 1,1]


#Vetor cujo index codifica o lado esquerdo (o termo A, de A-> betha) de cada regra
#de produção da gramática com o numero das colunas correspondente da tabela GOTO
trans_tbl = [0, 1, 3, 3, 4, 5, 5, 5, 2, 6, 6, 7, 7, 7, 2, 8, 9, 9, 10, 10, 2, 11, 12, 14, 13, 13, 13, 13, 2 ]



#Linhas codificam os estados (0 à 58)
GOTO = [
[1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,5,-1,-1,-1,6,-1,7,-1,-1,8,13,-1,-1],
[-1,-1,-1,15,16,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,19,-1,-1,-1,6,-1,7,-1,-1,8,13,-1,-1],
[-1,-1,20,-1,-1,-1,6,-1,7,-1,-1,8,13,-1,-1],
[-1,-1,21,-1,-1,-1,6,-1,7,-1,-1,8,13,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,23,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,29,-1,30,-1,-1,31,13,28,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,34,16,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,36,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,42,43,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,29,-1,30,-1,-1,31,13,46,-1],
[-1,-1,-1,-1,-1,-1,29,-1,30,-1,-1,31,13,47,-1],
[-1,-1,-1,-1,-1,-1,29,-1,30,-1,-1,31,13,48,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,50,-1,-1,-1,49],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,56,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,58,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]



#Vetor cujo index codifica as colunas da matrix ACTION.
Term=["inicio","varinicio","varfim","PTV","id","int","real","lit","leia","escreva",
      "Literal", "Num","RCB","OPM","se","AB_P","FC_P","entao","OPR","fimse","fim","$"]

ACTION = [
[102,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,0],
[-3,104,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3],
[-4,-4,-4,-4,112,-4,-4,-4,110,111,-4,-4,-4,-4,114,-4,-4,-4,-4,-4,109,-4],
[-5,-5,117,-5,118,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5],
[-6,-6,-6,-6,-6,-6,-6,-6,-6,-6,-6,-6,-6,-6,-6,-6,-6,-6,-6,-6,-6,201],
[-7,-7,-7,-7,112,-7,-7,-7,110,111,-7,-7,-7,-7,114,-7,-7,-7,-7,-7,109,-7],
[-8,-8,-8,-8,112,-8,-8,-8,110,111,-8,-8,-8,-8,114,-8,-8,-8,-8,-8,109,-8],
[-9,-9,-9,-9,112,-9,-9,-9,110,111,-9,-9,-9,-9,114,-9,-9,-9,-9,-9,109,-9],
[-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,229],
[-11,-11,-11,-11,122,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11],
[-12,-12,-12,-1,126,-12,-12,-12,-12,-12,124,125,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12],
[-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,127,-13,-13,-13,-13,-13,-13,-13,-13,-13],
[-14,-14,-14,-14,112,-14,-14,-14,110,111,-14,-14,-14,-14,114,-14,-14,-14,-14,132,-14,-14],
[-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,133,-15,-15,-15,-15,-15,-15],
[-16,-16,-16,-16,202,-16,-16,-16,202,202,-16,-16,-16,-16,202,-16,-16,-16,-16,-16,202,-16],
[-17,-17,117,-17,118,-17,-17,-17,-17,-17,-17,-17,-17,-17,-17,-17,-17,-17,-17,-17,-17,-17],
[-18,-18,-18,135,-18,-18,-18,-18,-18,-18,-18,-18,-18,-18,-18,-18,-18,-18,-18,-18,-18,-18],
[-19,-19,-19,-19,-19,137,138,139,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19],
[-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,209],
[-21,-21,-21,-21,-21,-21,-21,-21,-21,-21,-21,-21,-21,-21,-21,-21,-21,-21,-21,-21,-21,215],
[-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,221],
[-23,-23,-23,140,-23,-23,-23,-23,-23,-23,-23,-23,-23,-23,-23,-23,-23,-23,-23,-23,-23,-23],
[-24,-24,-24,141,-24,-24,-24,-24,-24,-24,-24,-24,-24,-24,-24,-24,-24,-24,-24,-24,-24,-24],
[-25,-25,-25,212,-25,-25,-25,-25,-25,-25,-25,-25,-25,-25,-25,-25,-25,-25,-25,-25,-25,-25],
[-26,-26,-26,213,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26],
[-27,-27,-27,214,-27,-27,-27,-27,-27,-27,-27,-27,-27,-27,-27,-27,-27,-27,-27,-27,-27,-27],
[-28,-28,-28,-28,144,-28,-28,-28,-28,-28,-28,145,-28,-28,-28,-28,-28,-28,-28,-28,-28,-28],
[-29,-29,-29,-29,222,-29,-29,-29,222,222,-29,-29,-29,-29,222,-29,-29,-29,-29,222,222,-29],
[-30,-30,-30,-30,112,-30,-30,-30,110,111,-30,-30,-30,-30,114,-30,-30,-30,-30,132,-30,-30],
[-31,-31,-31,-31,112,-31,-31,-31,110,111,-31,-31,-31,-31,114,-31,-31,-31,-31,132,-31,-31],
[-32,-32,-32,-32,112,-32,-32,-32,110,111,-32,-32,-32,-32,114,-32,-32,-32,-32,132,-32,-32],
[-33,-33,-33,-33,228,-33,-33,-33,228,228,-33,-33,-33,-33,228,-33,-33,-33,-33,228,228,-33],
[-34,-34,-34,-34,144,-34,-34,-34,-34,-34,-34,145,-34,-34,-34,-34,-34,-34,-34,-34,-34,-34],
[-35,-35,-35,-35,203,-35,-35,-35,203,203,-35,-35,-35,-35,203,-35,-35,-35,-35,-35,203,-35],
[-36,-36,-36,-36,204,-36,-36,-36,204,204,-36,-36,-36,-36,204,-36,-36,-36,-36,-36,204,-36],
[-37,-37,-37,151,-37,-37,-37,-37,-37,-37,-37,-37,-37,-37,-37,-37,-37,-37,-37,-37,-37,-37],
[-38,-38,-38,206,-38,-38,-38,-38,-38,-38,-38,-38,-38,-38,-38,-38,-38,-38,-38,-38,-38,-38],
[-39,-39,-39,207,-39,-39,-39,-39,-39,-39,-39,-39,-39,-39,-39,-39,-39,-39,-39,-39,-39,-39],
[-40,-40,-40,208,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40],
[-41,-41,-41,-41,210,-41,-41,-41,210,211,-41,-41,-41,-41,210,-41,-41,-41,-41,210,210,-41],
[-42,-42,-42,-42,211,-42,-42,-42,211,211,-42,-42,-42,-42,211,-42,-42,-42,-42,211,211,-42],
[-43,-43,-43,152,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43,-43],
[-44,-44,-44,218,-44,-44,-44,-44,-44,-44,-44,-44,-44,153,-44,-44,-44,-44,-44,-44,-44,-44],
[-45,-45,-45,219,-45,-45,-45,-45,-45,-45,-45,-45,-45,219,-45,-45,219,-45,219,-45,-45,-45],
[-46,-46,-46,220,-46,-46,-46,-46,-46,-46,-46,-46,-46,220,-46,-46,220,-46,220,-46,-46,-46],
[-47,-47,-47,-47,225,-47,-47,-47,225,225,-47,-47,-47,-47,225,-47,-47,-47,-47,225,225,-47],
[-48,-48,-48,-48,226,-48,-48,-48,226,226,-48,-48,-48,-48,226,-48,-48,-48,-48,226,226,-48],
[-49,-49,-49,-49,227,-49,-49,-49,227,227,-49,-49,-49,-49,227,-49,-49,-49,-49,227,227,-49],
[-50,-50,-50,-50,-50,-50,-50,-50,-50,-50,-50,-50,-50,-50,-50,-50,154,-50,-50,-50,-50,-50],
[-51,-51,-51,-51,-51,-51,-51,-51,-51,-51,-51,-51,-51,-51,-51,-51,-51,-51,155,-51,-51,-51],
[-52,-52,205,-52,205,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52],
[-53,-53,-53,-53,216,-53,-53,-53,216,216,-53,-53,-53,-53,216,-53,-53,-53,-53,216,216,-53],
[-54,-54,-54,-54,144,-54,-54,-54,-54,-54,-54,145,-54,-54,-54,-54,-54,-54,-54,-54,-54,-54],
[-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,-55,157,-55,-55,-55,-55],
[-56,-56,-56,-56,144,-56,-56,-56,-56,-56,-56,145,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56],
[-57,-57,-57,217,-57,-57,-57,-57,-57,-57,-57,-57,-57,-57,-57,-57,-57,-57,-57,-57,-57,-57],
[-58,-58,-58,-58,223,-58,-58,-58,223,223,-58,-58,-58,-58,223,-58,-58,-58,-58,223,-58,-58],
[-59,-59,-59,-59,-59,-59,-59,-59,-59,-59,-59,-59,-59,-59,-59,-59,224,-59,-59,-59,-59,-59]]





#Terminais esperados para cada estado 
t_esp = ["inicio", "EOF", "varinicio", "id, leia, escreva, se, fim", "varfim, id", "EOF", "id, leia, escreva, se, fim",
        "id, leia, escreva, se, fim", "id, leia, escreva, se, fim", "EOF", "id", "id, literal, num, ", "rcb",
        "id, leia, escreva, se, fimse", "(", "id, leia, escreva, se, fim", "varfim, id", ";", "int, real, lit", "EOF",
        "EOF", "EOF", ";", ";", ";", ";", ";", "id, num","id, leia, escreva, se, fimse, fim", "id, leia, escreva, se, fimse",
        "id, leia, escreva, se, fimse",  "id, leia, escreva, se, fimse", "id, leia, escreva, se, fimse, fim",
        "id, num", "id, leia, escreva, se, fim", "id, leia, escreva, se, fim", ";", ";", ";", ";", "id, leia, escreva, se, fimse, fim",
        "id, leia, escreva, se, fimse, fim", ";", "opm", "; , opm, ), opr", "; , opm, ), opr", "id, leia, escreva, se, fimse, fim",
        "id, leia, escreva, se, fimse, fim", "id, leia, escreva, se, fimse, fim", ")", "opr", "varfim, id", 
        "id, leia, escreva, se, fimse, fim", "id, num", "entao", "id, num", ";", "id, leia, escreva, se, fimse", ")"]

FOLLOWS_LEXEM = [
            ["$"],
            ["leia", "escreva", "id", "se", "fim"],
            ["$"],
            ["leia", "escreva", "id", "se", "fim"],
            ["id", "varfim"],
            [";"],
            ["leia", "escreva", "id", "se", "fimse", "fim"],
            [";"],
            ["leia", "escreva", "id", "se", "fimse", "fim"],
            [";"],
            [";", ")", "opr", "opm"],
            ["leia", "escreva", "id", "se", "fimse", "fim"],
            ["leia", "escreva", "se", "id", "fimse"],
            ["leia", "escreva", "id", "se", "fimse", "fim"],
            [")"]]


class Sintatico:

    def __init__(self, lexical_obj):
        #pilha
        self.__sp = 0        #index para o topo da pilha
        self.__stack = [0]    #pilha


        #pilha auxiliar do analisador semantico.
        self.__semantic_stack = []

        #salva o objeto controlador do analizador lexico
        self.__lexical_obj = lexical_obj

        self.__old_token = None

        #Lê o token 
        self.__token = lexical_obj.lexico()


    #retorna o elemento de intex i da pilha do semantico
    def getSemStck(self, index):
        return self.__semantic_stack[index-1]

    #retorna o indice atual da pilha    
    def getSp(self):
        return self.__sp

    def printstack(self):
        print("stack:")
        for i in range (0, len(self.__stack)):
           print(str(i)+ ", ch:" +str(self.__stack[i]))
        print("\n")
                


    #Retorna o índice do token encontrado encontrado (para ter o acesso às 
    #colunas de ACTION

    def getActionIndex(self, token):
        l = token.getTk()    #string que identifica o tipo do token
        for i in range (0, len(Term)):
            if l == Term[i]:
                return i
        return -1
    
    
    #recebe como argumento um objeto do tipo analizador lexico.
    def sintatico(self):
        

        t = None;

        while (True):

            #obtem um índice(colunas) na tabela de ações
            a = self.getActionIndex(self.__token)

            #caso não encontre...
            if a == -1:
                print ("Erro, token desconhecido\n")
                return

            # s assume o valor que ocupa o topo da pilha.
            s = self.__stack[self.__sp]
            
            #obtem a ação 
            tmp = ACTION[s][a]
            
            
            #É uma operação de SHIFT
            if (tmp > 100 and tmp < 200 ):

                #t
                t = tmp%100;
                
                #empilha o estado especificado na ação (apenas a unidade e a dezena fazem parte deste numero)
                self.__stack.append(t)
                self.__sp += 1


                #clona o comportamento da pilha do sintatico (anal. semantico)
                self.__semantic_stack.append(self.__token)
                

                
                #lê o proximo token (e faz um backup do token anterior)
                self.__old_token = self.__token
                self.__token = self.__lexical_obj.lexico()

                #obtem um índice(colunas) na tabela de ações
                a = self.getActionIndex(self.__token)   
                
            
            #caso seja um REDUCE
            elif (tmp > 200): 
                
                prod = tmp%100;    #obtem o numero da produção (0 é equiv. à 2 na num. da folha)

                
                #aplica as regras semânticas
                topo = sem(self, prod);

                #token burro, apenas para ocupar um espaço na pilha e permitir seu correto funcionamento
                if topo == None:
                    topo = Token('','','',0,0)
                    
          
              
                    
                
                #Desempilha |betha| (subtrai 1 de prod pois o vetor betha_sz  começa a indexar à partir da produção 1
                for i in range(0, betha_sz[prod -1]):
                    self.__stack.pop()
                    self.__sp -= 1

                    #clona o comportamento na pilha do semantico
                    self.__semantic_stack.pop()

                
                #empilha o não terminal da redução
                self.__semantic_stack.append(topo)
             


                # faz ‘t’ ter o valor do topo da pilha
                t = self.__stack[self.__sp]
                

                #Empilha o estado a ser transitado (ind. pelo GOTO)
                self.__stack.append(GOTO[t][trans_tbl[prod-1]])
                self.__sp += 1
                 
                
                
                #Imprime a produção
                #print (G[prod])
                
                
               

            #se  reconheceu
            elif tmp ==0:
                print(G[0])
                print("Uhuuu, reconheceu!\n")
                break
            else:
                #Obtem o estado  em que ocorreu o erro (token não esperado)
                est = -1*(tmp + 1)  
                
                if (self.__old_token != None):
                    print("Erro :(" + str(self.__token.getRow()) + "," + str(self.__token.getCol())+") Esperado < " + t_esp[est]+ " >" +
                          " depois de '"+self.__old_token.getLexem() + "' do tipo '" + self.__old_token.getTk()+"'")
                else:
                    print("Erro :(" + str(self.__token.getRow()) + "," + str(self.__token.getCol())+") Esperado < " + t_esp[est]+ " >")

                print("\tPorem '" + self.__token.getLexem() + "' do tipo '" + self.__token.getTk() + "' foi lido.") 
            
                self.erro()

                #condição de parada, para quando não há mais o que ler
                if self.__token.getTk() == '$':
                    break
            
                

    def erro(self):
        #Pega o tamanho da pilha
        stk_len = len(self.__stack)

        #maior
        index_pilha = 0
        
        #não terminal
        nt = 0

        #varre, para cada não terminal...
        for n  in range (0, 15):
            
            #Para cada estado da pilha, do topo ao inicio...{ s em  (size, 0]}
            for i in range(stk_len -1, -1, -1):
                
                #se a transição para o estado que está no index 's' da pilha existe para
                #o dado não terminal indexado por 'n', e se o index for maior que o 'maior'
                #(ou seja, está mais proximo ao topo da pilha, precisando desempilhar menos no futuro):

                estado = self.__stack[i]
                #print('Indice: '+str(i)+', estado: '+str(estado)+', GOTO:'+ str(GOTO[estado][n] ))

                if ((GOTO[estado][n] != -1) and (i > index_pilha)):
                    index_pilha = i
                    nt = n
                    
                    #print('->Indice: '+str(i)+', N-Terminal:'+str(n)+'')
                    #print('->Maior: '+str(index_pilha)+', N-Term: '+str(nt))
             
                    break

        

        #----------------------------------------------------------------------------------------
        #desempilha a pilha até que seu topo tenha o valor de index_pilha (menor numero de desempilhamentos)
        for i in range (stk_len -1, index_pilha, -1):
            self.__stack.pop()
        self.__sp = index_pilha

        #joga o valor da transição na pilha
        self.__stack.append(GOTO[self.__stack[self.__sp]][nt])
        self.__sp += 1

        #Faz um um backup do token 
        self.__old_token = self.__token

        #indica se encontrou um token de sincronização
        sinchronized = False

        #enquanto não tiver...descarta tokens até encontrar um que tenha
        while(sinchronized == False):

            #Lê um novo token
            self.__token = self.__lexical_obj.lexico()

            
            #obtem o lexema
            lexema = self.__token.getLexem()

            #procura no conjunto dos seguintes para o dado não terminal
            for i in FOLLOWS_LEXEM[nt]:
                if lexema == i:
                    print("ok")
                    sinchronized = True
                    break
            #caso especial... lexema de $ é 'EOF'
            if lexema == 'EOF':
                break

         


               
        
        
        
        


        

                
  
    
        
      
        

