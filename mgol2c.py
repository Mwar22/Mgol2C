#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import lexic
import sintatic

#-------------------------------------------------TESTE-----------------------------------------------------
#

# Cria uma instância de analizador léxico, passando como parametro o arquivo 'fonte'
f = open('texto.alg', 'rb+')
la = lexic.LexicAnalyser(f)

#testa sintatico

st = sintatic.Sintatico(la)
st.sintatico()

