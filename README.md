# Freeway Game

**Trabalho final da disciplina de Introdução à Programação (1º Período no IFPR)**

## Descrição do Projeto
jogo desenvolvido em Python utilizando a biblioteca Pygame. O jogador controla uma galinha que precisa atravessar a estrada enquanto evita carros em movimento. O objetivo é chegar ao outro lado sem ser atropelado.

---

## Estrutura do Projeto
```
meu_jogo/
├── freeway.py         # Arquivo principal do jogo (código fonte)
├── run.sh             # Script para executar o jogo no Linux/macOS
├── run.bat            # Script para executar o jogo no Windows
└── arquivos/          # Pasta contendo os recursos do jogo
    ├── estrada.jpg        # Imagem de fundo (estrada)
    ├── galinha.png        # Sprite da galinha (personagem principal)
    ├── carro_azul_d.png   # Sprite do carro azul (direção direita)
    ├── carro_azul_e.png   # Sprite do carro azul (direção esquerda)
    ├── carro_vermelho_d.png # Sprite do carro vermelho (direção direita)
    ├── carro_vermelho_e.png # Sprite do carro vermelho (direção esquerda)
    ├── carro_verde_d.png   # Sprite do carro verde (direção direita)
    ├── carro_verde_e.png   # Sprite do carro verde (direção esquerda)
    ├── quadriculada.ttf    # Fonte usada no jogo
    └── poze_80.mp3         # Trilha sonora do jogo
```

---

## Requisitos
- Python 3.8 ou superior
- Biblioteca Pygame instalada

---

## Como Executar o Jogo

### **Windows**
1. Certifique-se de ter o Python instalado no sistema.
   - Se o Python não estiver instalado, o script `run.bat` informará o link para download.
2. Clique duas vezes no arquivo `run.bat`.
3. O script:
   - Instalará automaticamente o Pygame (se ainda não estiver instalado).
   - Executará o jogo.

### **Linux/macOS**
1. Abra um terminal e navegue até o diretório do jogo.
   ```bash
   cd /caminho/para/meu_jogo
   ```
2. Certifique-se de que o script `run.sh` tem permissão de execução:
   ```bash
   chmod +x run.sh
   ```
3. Execute o script:
   ```bash
   ./run.sh
   ```
4. O script:
   - Instalará o Python e o Pygame automaticamente (se não estiverem instalados).
   - Executará o jogo.

---

## Observações
- Este projeto foi desenvolvido como trabalho final da disciplina de Introdução à Programação no 1º Período do IFPR.
- Certifique-se de que todos os arquivos da pasta `arquivos` estão presentes para evitar erros durante a execução.
- Caso encontre problemas ao executar o jogo, verifique se os requisitos estão atendidos ou entre em contato comigo.

---

**Divirta-se jogando Freeway!**

