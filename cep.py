# -*- coding: utf-8 -*-

from tkinter import *
import pprint
import requests

def obter_endereco(cep: str) -> dict:
    endpoint = f'https://viacep.com.br/ws/{cep}/json'
    resp = requests.get(endpoint)
    retorno = resp.json()
    return retorno

if __name__ == '__main__':
    pprint.pprint(obter_endereco(45807000))






