# -*- coding: UTF-8 -*-

import platform
from service import Calculator


def perform_calculation():
    nome_usuario = platform.node()

    Calculator(nome_usuario)


perform_calculation()
