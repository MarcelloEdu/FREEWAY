import pygame
from pygame import mixer
import random
import os
# Inicialização do pygame
pygame.init()
#posiçao inicial da galinha
x = 500
y = 660
#cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
#importação dos assets externos usando caminho relativo
caminho_atual = os.path.abspath(os.path.dirname(__file__))
img_fundo_ret = os.path.join(caminho_atual, 'assets/estrada.jpg')
galinha_ret = os.path.join(caminho_atual, 'assets/galinha.png')
azul_d_ret = os.path.join(caminho_atual, 'assets/carro_azul_d.png')
azul_e_ret = os.path.join(caminho_atual, 'assets/carro_azul_e.png')
vermelho_d_ret = os.path.join(caminho_atual, 'assets/carro_vermelho_d.png')
vermelho_e_ret = os.path.join(caminho_atual, 'assets/carro_vermelho_e.png')
verde_d_ret = os.path.join(caminho_atual, 'assets/carro_verde_d.png')
verde_e_ret = os.path.join(caminho_atual, 'assets/carro_verde_e.png')
fonte_ret = os.path.join(caminho_atual, 'assets/quadriculada.ttf')
musica_ret = os.path.join(caminho_atual, 'assets/poze_80.mp3')

#nomeando os assets externos
imagem_fundo = pygame.image.load(img_fundo_ret)
galinha_img = pygame.image.load(galinha_ret)
carro_azul_d = pygame.image.load(azul_d_ret)
carro_verde_d = pygame.image.load(verde_d_ret)
carro_vermelho_d = pygame.image.load(vermelho_d_ret)
carro_azul_e = pygame.image.load(azul_e_ret)
carro_verde_e = pygame.image.load(verde_e_ret)
carro_vermelho_e = pygame.image.load(vermelho_e_ret)
fonte = pygame.font.Font(fonte_ret, 32)
fonte_p = pygame.font.Font(fonte_ret, 16)
fonte_g = pygame.font.Font(fonte_ret,64)
musica = pygame.mixer.music.load(musica_ret)
#velocidade dos carros
vel = [50, 40, 30]
#"sorteio" das velocidades//k e o numero de vezes que sera feita a escolha
velocidades_carros = random.choices(vel, k=6)
#velocidade da galinha
vel_galinha = 10
# Posições de spawn dos carros
rectx_1 = 1300
rectx_2 = 100
rectx_3 = 1300
rectx_4 = 1000
rectx_5 = 650
rectx_6 = 650
recty = 55
#musica de fundo
mixer.music.play(-1)#-1 significa que a musica vai tcar infinitamente
#tamanho da janela
janela = pygame.display.set_mode((1000, 700))
# Número de vidas iniciais
vidas = 3
# Função para reiniciar o jogo
def reiniciar_jogo():
    global vidas, x, y
    vidas = 3
    #posiçao de respawn da galinha
    x = 500
    y = 660
#definição das telas que vão ser chamadas posteriormente
exibir_tela_lose = 'lose'
exibir_tela_lose = False
exibir_tela_win = 'win'
exibir_tela_win = False
exibir_menu = 'menu'
exibir_menu = False
exibir_instrucoes = 'instruções'
exibir_instrucoes = False
# Renderizar texto
texto_game_over_l =fonte_g.render("GAME OVER", True, (BRANCO))
texto_win = fonte_g.render("VOCE VENCEU!!!", True, (BRANCO))
texto_jogar_novamente = fonte.render("Deseja jogar novamente?", True, (BRANCO))
texto_sim = fonte.render("Sim", True, (BRANCO))
texto_nao = fonte.render("Não", True, (BRANCO))
texto_titulo = fonte_g.render("FREEWAY", True, (BRANCO))
texto_jogar = fonte.render("JOGAR", True, (BRANCO))
texto_instrucoes = fonte.render("INSTRUÇÕES", True, (BRANCO))
texto_sair = fonte.render("SAIR", True, (BRANCO))
texto_instrucoes1 = fonte_p.render("O objetivo do jogo é guiar a galinha até o outro lado da rua", True, (BRANCO))
texto_instrucoes2 = fonte_p.render("  sem ser atropelada pelos carros em alta velocidade", True, (BRANCO))
texto_instrucoes3 = fonte_p.render("Use as teclas de seta para mover a galinha.", True, (BRANCO))
texto_instrucoes4 = fonte.render("          Boa sorte!", True, (BRANCO))
texto_voltar = fonte.render('voltar', True, (BRANCO))
# Loop do menu inicial
exibir_menu = True
while exibir_menu:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            #coordenadas do clique do mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #qual opção foi selecionada
            if 410 <= mouse_x <= 410 + texto_jogar.get_width() and 330 <= mouse_y <= 330 + texto_jogar.get_height():
                exibir_menu = False
            elif 335 <= mouse_x <= 335 + texto_instrucoes.get_width() and 400 <= mouse_y <= 400 + texto_instrucoes.get_height():
                exibir_instrucoes = True
                while exibir_instrucoes:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif evento.type == pygame.KEYDOWN:
                            if evento.key == pygame.K_ESCAPE:
                                pygame.quit()
                                quit()
                        elif evento.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                        elif 0 <= mouse_x <= 0 + texto_jogar.get_width() and 0 <= mouse_y <= 0 + texto_jogar.get_height():
                            exibir_instrucoes = False
                    janela.fill((0, 0, 0))#fundo preto
                    janela.blit(texto_instrucoes1, (20, 200))
                    janela.blit(texto_instrucoes2, (100, 250))
                    janela.blit(texto_instrucoes3, (200, 300))
                    janela.blit(texto_instrucoes4, (50, 350))
                    janela.blit(texto_voltar, (0, 0))
                    pygame.display.update()
            elif 430 <= mouse_x <= 430 + texto_sair.get_width() and 470 <= mouse_y <= 470 + texto_sair.get_height():
                pygame.quit()
                quit()
    janela.fill((0, 0, 0))
    # Exibir os textos do menu inicial
    janela.blit(texto_titulo, (280, 200))
    janela.blit(texto_jogar, (410, 330))
    janela.blit(texto_instrucoes, (335, 400))
    janela.blit(texto_sair, (430, 470))
    pygame.display.update()
# Loop principal
janela_aberta = True
while janela_aberta:
    pygame.time.delay(60)#"fps" do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            janela_aberta = False
    #coontroles do jogo
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP]:
        y -= vel_galinha
    if tecla[pygame.K_DOWN]:
        y += vel_galinha
    if tecla[pygame.K_LEFT]:
        x -= vel_galinha
    if tecla[pygame.K_RIGHT]:
        x += vel_galinha
    janela.blit(imagem_fundo, (0, 0))#fundo preto
    #funçao pra os carros voltarem ao inicio
    if rectx_1 < -20:  # 1
        rectx_1 = 1000
        velocidades_carros = random.choices(vel, k=6)
    if rectx_2 > 1000:  # 2
        rectx_2 = -20
        velocidades_carros = random.choices(vel, k=6)
    if rectx_3 > 1000:  # 3
        rectx_3 = -20
        velocidades_carros = random.choices(vel, k=6)
    if rectx_4 > 1000:  # 4
        rectx_4 = -20
        velocidades_carros = random.choices(vel, k=6)
    if rectx_5 < -20:  # 5
        rectx_5 = 1000
        velocidades_carros = random.choices(vel, k=6)
    if rectx_6 > 1000:  # 6
        rectx_6 = -20
        velocidades_carros = random.choices(vel, k=6)
    galinha = janela.blit(galinha_img, (x, y))
    carro1 = janela.blit(carro_vermelho_e, (rectx_1, recty))#1
    if carro1.colliderect(galinha):#colisao
        #respawn da galinha (se colidir volta pra posiçao(x, y)
        vidas -= 1 #contador de vidas
        x = 500
        y = 650
    rectx_1 -= velocidades_carros[0]
    carro2 = janela.blit(carro_verde_d, (rectx_2, recty + 80))#2
    if carro2.colliderect(galinha):#colisao
        vidas -= 1
        x = 500
        y = 650
    rectx_2 += velocidades_carros[1]
    carro3 = janela.blit(carro_azul_d, (rectx_3, recty + 170))#3
    if carro3.colliderect(galinha):#colisao
        vidas -= 1
        x = 500
        y = 650
    rectx_3 += velocidades_carros[2]
    carro4 = janela.blit(carro_vermelho_d, (rectx_4, recty + 350)) #4
    if carro4.colliderect(galinha):#colisao
        vidas -= 1
        x = 500
        y = 650
    rectx_4 += velocidades_carros[3]
    carro5 = janela.blit(carro_verde_e, (rectx_5, recty + 440))#5
    if carro5.colliderect(galinha):#colisao
        vidas -= 1
        x = 500
        y = 650
    rectx_5 -= velocidades_carros[4]
    carro6 = janela.blit(carro_azul_d, (rectx_6, recty + 540))#6
    if carro6.colliderect(galinha):#colisao
        vidas -= 1
        x = 500
        y = 650
    rectx_6 += velocidades_carros[5]
    if y <= 15:#vitoria//chegou do outro lado
        exibir_tela_win = True
        while exibir_tela_win:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        #reiniciar o jogo
                        reiniciar_jogo()
                        exibir_tela_lose = False
                    elif evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    #coordenadas do clique
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    #Verificar se o botão 'sim' foi clicado
                    if 200 <= mouse_x <= 200 + texto_sim.get_width() and 500 <= mouse_y <= 500 + texto_sim.get_height():
                        #reiniciar o jogo
                        reiniciar_jogo()
                        exibir_tela_win = False
                        #verificar se o botão 'não' foi clicado
                    elif 700 <= mouse_x <= 700 + texto_nao.get_width() and 500 <= mouse_y <= 500 + texto_nao.get_height():
                        pygame.quit()
                        quit()
            #fundo preto
            janela.fill((PRETO))
            #posicionar o texto
            janela.blit(texto_win, (90, 200))
            janela.blit(texto_jogar_novamente, (140, 360))
            janela.blit(texto_sim, (200, 500))
            janela.blit(texto_nao, (700, 500))
            pygame.display.update()
    if vidas == 0:#perdeu todas as vidas, perdeu o jogo
        exibir_tela_lose = True
    while exibir_tela_lose:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    # Reiniciar o jogo
                    reiniciar_jogo()
                    exibir_tela_lose = False
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Obter as coordenadas do clique do mouse
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Verificar se o botão 'Sim' foi clicado
                if 300 <= mouse_x <= 300 + texto_sim.get_width() and 500 <= mouse_y <= 500 + texto_sim.get_height():
                    # Reiniciar o jogo
                    reiniciar_jogo()
                    exibir_tela_lose = False
                # Verificar se o botão 'Não' foi clicado
                elif 600 <= mouse_x <= 600 + texto_nao.get_width() and 500 <= mouse_y <= 500 + texto_nao.get_height():
                    pygame.quit()
                    quit()
        #preencher o fundo com a cor preta
        janela.fill((0, 0, 0))
        #posicionar o texto na janela
        janela.blit(texto_game_over_l, (230, 200))
        janela.blit(texto_jogar_novamente, (140, 360))
        janela.blit(texto_sim, (300, 500))
        janela.blit(texto_nao, (600, 500))
        pygame.display.update()
    texto_vidas = fonte.render("Vidas: " + str(vidas), True, (PRETO))
    janela.blit(texto_vidas, (10, 10))
    pygame.display.update()
pygame.quit()
