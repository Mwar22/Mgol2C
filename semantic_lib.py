# -*- coding: utf-8 -*-



class TempHandler:

    def __init__(self):

        #contador
        self.__x = 0

    def newT(self):
        self.__x += 1
        return self.__x

    #Retorna uma representação em texto de um temporário i
    def getTxt(self, i):
        return ("T"+str(i))




def imprimir(text):
    print(text)




#cria uma instância de TempHandler (manipulador de temporarios)
th = TempHandler()


#Retorna o tipo do elemento que ocupará o topo da pilha de tipos.
def sem (analyser, index):
    #indice do topo da pilha
    sp = analyser.getSp()

    if index == 4:
        imprimir("\n\n\n")

    elif index == 5:
        #D-> id TIPO;

        #id e TIPO são referências à objetos. id (objeto) fica armazenado 
        #(estático) na tabela de símbolos
        
        idi  = analyser.getSemStck(sp - 2)
        TIPO =  analyser.getSemStck(sp - 1)

        idi.setTipo(TIPO.getTipo())    

        #não empilha nada ao fim do reduce
        return None    

    elif index == 6:
        #TIPO->inteiro
        #TIPO.tipo = inteiro.tipo
        return Token("","", analyser.getSemStck(sp),0,0)

    elif index == 7:
        #TIPO->real
        return Token("","", analyser.getSemStck(sp),0,0)

    elif index == 8:
        #TIPO->literal
        return Token("","", analyser.getSemStck(sp),0,0)


    elif index == 10:
        #ES->leia id;
        idi  = analyser.getSemStck(sp -1)

        #obtem o tipo
        id_tipo = idi.getTipo()

        if id_tipo != "":
            if id_tipo == "literal":
                imprimir("scanf(“%s”, " + idi.getLexem() + ");")

            elif id_tipo == "inteiro":
                imprimir ("scanf(“%d”, &" + idi.getLexem() +  ");" )    
            else:
                imprimir ("scanf(“%lf”, &" + idi.getLexem() + ");" )
        else:
            print("Erro: Variável não declarada")
            print("Linha: " + str(idi.getRow()) + ", Coluna: " + str(idi.getCol()))    
        
        #não acrescenta um novo tipo de pilha
        return None

    elif index == 11:
        #ES->escreva ARG;
        ARG = analyser.getSemStck(sp -1)

        imprimir("printf(“" + ARG.getLexem() +"”);" )
        return None

    elif index == 12:
        #ARG->literal
        literal = analyser.getSemStck(sp)

        #Copia o objeto literal (efetivamente, todos os seus atributos)
        return  literal.copy()


    elif index == 13:
        #ARG->num
        num = analyser.getSemStck(sp)
        
        return num.copy()


        
    elif index == 14:
        #ARG->id
        idi = analyser.getSemStck(sp)
        
        return idi.copy()

        
    elif index == 16:
        #CMD ->id rcb LD;
        idi = analyser.getSemStck(sp - 3)
        rcb = analyser.getSemStck(sp - 2)
        LD = analyser.getSemStck(sp - 1)

        if idi.getTipo() != "":
            
            if idi.getTipo() == LD.getTipo():
                imprimir(idi.getLexem() +" "+ rcb.getTipo() + " " +LD.getLexem())

            else:
                print("Erro: Tipos diferentes para atribuição")
        else:
            print("Erro: Variável não declarada")    
            print("Linha: "+str(idi.getRow()) + ", Coluna: " + str(idi.getCol()))    
        
        return None
        






    elif index == 17:
        #LD->OPRD(2)  opm OPRD(1)

        OPRD1 = analyser.getSemStck(sp)
        opm = analyser.getSemStck(sp - 1)
        OPRD2 =  analyser.getSemStck(sp - 2)
        
        #token de retorno
        LD = None

        if (OPRD1.getTipo() == OPRD2.getTipo) and (OPRD1.getTipo() != "literal"):
            x = th.newT()
            LD = Token("", th.getText(x), 0, 0)

            imprimir(th.getText(x) + " = "+ OPRD2.getLexem() + " "+ opm.getTipo() +" "+ OPRD2.getLexem())
            
        else:
            print("Erro: Operandos com tipos incompatíveis")

            if OPRD1.getTipo() == "literal":
                print("Linha: " + str(OPRD1.getRow()) + ", Coluna: " + str(OPRD1.getCol()))
    
            else:
                print("Linha: " + str(OPRD2.getRow()) + ", Coluna: " + str(OPRD2.getCol()))
    
        return LD



    elif index == 18:
        #LD->OPRD
        OPRD = analyser.getSemStck(sp)

        LD = OPRD.copy()
        return LD
    


    elif index == 19:
        #OPRD->id
        idi = analyser.getSemStck(sp)
        OPRD = None

        if idi.getTipo() != "":
            OPRD = id.copy()
        else:
            print("Erro : Variável não declarada")
            print("Linha: " + str(idi.getRow()) + ", Coluna: " + str(idi.getCol()))
        
        return OPRD
        
    elif index == 20:
        #OPRD->num
        num = analyser.getSemStck(sp)

        OPRD = num.copy()
        return OPRD

    elif index == 22:
        #COND->CABEÇALHO CORPO

        imprimir( "}" )
        return None

    elif index == 23:
        #CABEÇALHO->se (EXP_R) então
        EXP_R = analyser.getSemStck(sp - 2)

        imprimir("if(" + EXP_R.getLexem() + "){")

        return None






    elif index == 24:
        #EXP_R->OPRD opr OPRD
    
        
        OPRD1 = analyser.getSemStck(sp)
        opr = analyser.getSemStck(sp - 1)
        OPRD2 =  analyser.getSemStck(sp - 2)
        
        #token de retorno
        EXP_R = None

        if (OPRD1.getTipo() == OPRD2.getTipo) :
            x = th.newT()
            EXP_R = Token("", setLexem(th.getText(x), "",0,0)

            imprimir(th.getText(x) + " = " + OPRD2.getLexem() +" "+opr.getTipo() +" "+ OPRD1.getLexem() )
        else:
            print("Erro: Operandos com tipos incompatíveis")
            print("Linha: "+str(OPRD2.getRow()) + ", Coluna: " + str(OPRD2.getCol()))    

        return EXP_R
    

