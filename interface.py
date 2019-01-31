# -*- coding: utf-8 -*-

import os
import sys
import getpass
import tutor as tt
import dominio as dm
import aluno as al
import readline


### MAIN
def main ():
    if len(sys.argv) == 1: 
        terminal()  # Executar sem argumentos passa a ser um terminal
    else:
        help()      # Executar sem todos os argumentos necessários mostra ajuda
        sys.exit()

# Funções
def help(): 
    print """[USO STI] python sti.py sair responder

    sair - Finaliza a execução
    responder - inicia a execução do STI para o aluno"""


def going(aluno,command):

    cont = True
    while cont:
        step = tt.tutoria(aluno,command)
        if step == 0:
            print 'O que fazer em seguida?'
            print """
            [1] Continuar
            [2] Parar
            """
            resp = int(raw_input('Informe uma das opções: '))
            if (resp == 2):
                cont = False
                resp = 3  
        else:
            cont = False
            resp = step

    return resp


def responder():

    cpf = (raw_input('Informe CPF: '))
    print 'Informe sua senha'
    senha = getpass.getpass()

    #verificar id e senha
    if al.check_login(cpf, senha) == 0:

        aluno = al.get_aluno(cpf)
        cont = 0
        print 'Escolha uma Disciplina:'
        print """
            [1] Questões de Matemática
            [2] Questões de Humanidades
            [3] Questões de Ciências
            """
        command = (raw_input('Informe uma das opções: '))

        step = going(aluno,command)
        

        if step == 1:
            print 'Você respondeu uma questão especial.'
            print """
            [1] Obter Feedback
            [2] Não Obter Feedback
            """
            prox = (raw_input('Informe uma das opções: '))
            if prox == 1:
                tt.feedback(aluno,command)

        elif step == 2:
            print 'Questões regulares respondidas.'
            print """
            [1] Obter Feedback
            [2] Não Obter Feedback
            """
            prox = (raw_input('Informe uma das opções: '))
            if prox == 1:
                tt.feedback(aluno,command)

    else:
        print 'Login desconhecido! Tente novamente.'


def cadastrar():
    check = al.cadastra()
    if check == 1:
        print 'Informações Inválidas!\n'
    else:
        print 'Cadastro efetuado com sucesso!\n'

# modo terminal
def terminal():
    dm.prepara_bds()
    dm.prepara_bd_especial()

    while(True):
        print ''
        print 'Você tem as seguintes opções:'
        print '[r]: responder questões'
        print '[c]: cadastrar um novo aluno'
        print '[s]: sair'
        print ''
        command = (raw_input('[STI - Pré-ETEC]: ')).strip().split()
        print ''
        if command:
            if command[0] == "s": 
                sys.exit(0)
            if command[0] == "c": 
                cadastrar()
            if command[0] == "r":
            	responder()
            else:
            	help()


if __name__ == "__main__":
    main()
