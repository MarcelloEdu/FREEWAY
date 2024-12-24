@echo off
:: Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python não encontrado. Instalando...
    echo Baixe e instale o Python manualmente em https://www.python.org/downloads/
    pause
    exit /b
)

:: Garantir que pip esteja atualizado
echo Instalando dependências...
python -m pip install --upgrade pip
python -m pip install pygame --quiet

:: Executar o jogo
echo Iniciando o jogo...
python freeway.py
pause
