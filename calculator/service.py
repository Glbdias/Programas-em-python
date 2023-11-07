# -*- coding: UTF-8 -*-

from PySimpleGUI import PySimpleGUI as sg


class Calculator:
    def __init__(self, usuario):
        self.opcao = None
        self.usuario = usuario
        self.get_informacoes()

    def get_informacoes(self):
        print(" Seja bem-vindo %s" % self.usuario)
        print("------------ Informações Calculadora ---------------")
        print('A calculadora está prepara para executar as 4 operações básicas, sendo elas:')
        print('     * Soma')
        print('     * Subtração')
        print('     * Divisão')
        print('     * Multiplicação')

