#!/bin/bash

# Atualizar repositórios e instalar Python se não estiver presente
if ! command -v python3 &> /dev/null; then
    echo "Python3 não encontrado. Instalando Python..."
    sudo apt update && sudo apt install python3 python3-pip -y
fi

# Garantir que o Pygame esteja instalado
echo "Instalando dependências..."
python3 -m pip install --upgrade pip
python3 -m pip install pygame --quiet

# Executar o jogo
echo "Iniciando o jogo..."
python3 freeway.py
