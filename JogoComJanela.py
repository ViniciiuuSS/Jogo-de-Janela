import pygame
from random import randint
from time import sleep

pygame.init()

#----------------------------------------------------variaveis globais--------------------------------------------------
x = 30
y = 150 #Max 300 #Min 0
pos_x = 800
pos_y = 100
pos_x_1 = 1000
pos_y_1 = 200
pos_atual_y = 300
velocidade = 10
velocidade_Inimigo = 10
Moeda = 800
vida = 100
Nivel = 0
xp = 0
PocaoVida = 0
PocaoVida_Preco = 100
PocaoXP = 0
PocaoXP_Preco = 100
#-----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------Armas e preço de armas---------------------------------------------
EspadaDeDiamante_atri = randint(2, 9)
EspadaDeDiamante_preço = 400
Espada_Do_Fin_atri = randint(3,10)
Espada_Do_Fin_preço = 600
EspadaDePedra_atri = randint(5,11)
EspadaDePedra_preço = 200

Arma_atual_num = 0
#-----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------imagens------------------------------------------------------------
fundo = pygame.image.load("PlanoComCoisas.png")
PersonagemImage = pygame.image.load("personagem.png")
PersonagemComEspada_diamante = pygame.image.load("PersonagemComEspada.png")
PersonagemComEspada_fin = pygame.image.load("PersonagemComEspada_fin.png")
PersonagemComEspada_pedra = pygame.image.load("PersonagemComEspada_Pedra.png")
Inimigo = pygame.image.load("inimigo.png")
Inimigo1 = pygame.image.load("inimigo2.png")
perder = pygame.image.load("perder.png")
BarraDeNivel = pygame.image.load("BarraDeNivel.png")
BarraDeNivel1 = pygame.image.load("BarraDeNivel1.png")
BarraDeNivel2 = pygame.image.load("BarraDeNivel2.png")
BarraDeNivel3 = pygame.image.load("BarraDeNivel3.png")
BarraDeNivel4 = pygame.image.load("BarraDeNivel4.png")
BarraDeNivel5 = pygame.image.load("BarraDeNivel5.png")
BarraDeNivel6 = pygame.image.load("BarraDeNivel6.png")
BarraDeNivel7 = pygame.image.load("BarraDeNivel7.png")
BarraDeNivel8 = pygame.image.load("BarraDeNivel8.png")
BarraDeNivel9 = pygame.image.load("BarraDeNivel9.png")
FundoBarraDeNivel = pygame.image.load("FundoBarraDeNivel.png")
FundoLoja = pygame.image.load("FundoLoja.png")
#-----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------tempo e money------------------------------------------------------
font = pygame.font.SysFont("arial black", 20)
texto = font.render("Nivel: "+str(Nivel), True, (0,0,0), (46,139,87))
pos_Nivel = texto.get_rect()
pos_Nivel = (660,527)

font = pygame.font.SysFont("arial black", 20)
moeda_texto = font.render("Money: "+str(Moeda), True, (0,0,0), (255,215,0))
pos_texto_moeda = texto.get_rect()
pos_texto_moeda = (660,483)

font = pygame.font.SysFont("arial black", 20)
Vida_texto = font.render("Vida: "+(str(vida)), True, (0,0,0), (255,69,0))
pos_texto_Vida = texto.get_rect()
pos_texto_Vida = (660,443)

font = pygame.font.SysFont("arial black", 20)
PocaoVida_texto = font.render("POCAO: "+(str(PocaoVida)), True, (0,0,0), (255,69,0))
pos_texto_PocaoVida = texto.get_rect()
pos_texto_PocaoVida = (589,479)

font = pygame.font.SysFont("arial black", 20)
PocaoXP_texto = font.render("POCAO: "+(str(PocaoXP)), True, (0,0,0), (255,69,0))
pos_texto_PocaoXP = texto.get_rect()
pos_texto_PocaoXP = (589,550)
#-----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------Programa rodando---------------------------------------------------
janela = pygame.display.set_mode ((800,600))

janela_Aberta = True
while janela_Aberta:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_Aberta = False


    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_w] and y >= 0:
        y -= velocidade
    if comandos[pygame.K_s] and y <= 300:
        y += velocidade
    if comandos[pygame.K_a] and x >= 0:
        x -= velocidade
    if comandos[pygame.K_d] and x <= 700:
        x += velocidade


    #COLISAO PARA CADA INIMIGO, QUANTIDADE ATUAL : 2
    #INIMIGO 0
    if ( x + 90 > pos_x and x  < pos_x and y - 40 < pos_y and y + 40 > pos_y): #colisao no inimigo
        pos_x = 1200
        pos_y = randint(0, 145)
        MoedaMais = randint(1, 10)
        Moeda += MoedaMais
        xp += 1
        if xp == 10:
            xp = 0
            Nivel += 1
            texto = font.render("Nivel: "+str(Nivel), True, (0,0,0), (46,139,87))
        moeda_texto = font.render("Money: "+(str(Moeda)), True, (0, 0, 0), (255, 215, 0))


    #INIMIGO 1
    if ( x + 90 > pos_x_1 and x  < pos_x_1 and y - 40 < pos_y_1 and y + 40 > pos_y_1): #colisao no inimigo
        pos_x_1 = 1200
        pos_y_1 = randint(150, 300)
        MoedaMais = randint(1, 10)
        Moeda += MoedaMais
        xp += 1
        if xp == 10:
            xp = 0
            Nivel += 1
            texto = font.render("Nivel: "+str(Nivel), True, (0,0,0), (46,139,87))
        moeda_texto = font.render("Money: " + (str(Moeda)), True, (0, 0, 0), (255, 215, 0))

    #> QUANTIDADE DE INIMIGOS ATUAL : 2
    #INIMIGO 0
    if pos_x <= -180:
        pos_x = randint(1300, 2200)
        pos_y = randint(0, 145)
        vida -= 1
        Vida_texto = font.render("Vida: " + (str(vida)), True, (0, 0, 0), (255, 69, 0))

    #INIMIGO 1
    if pos_x_1 <= -180:
        pos_x_1 = randint(1000,1400)
        pos_y_1 = randint(150, 300)
        vida -= 1
        Vida_texto = font.render("Vida: " + (str(vida)), True, (0, 0, 0), (255, 69, 0))
    #FIM QUANTIDADE DE INIMIGOS

    PocaoVida_texto = font.render(f"{(str(PocaoVida))}"  , True, (0, 0, 0))
    PocaoXP_texto = font.render(f"{(str(PocaoXP))}" , True, (0, 0, 0))
    pos_x -= velocidade_Inimigo
    pos_x_1 -= velocidade_Inimigo

    janela.blit(fundo,(0,0))
    if Arma_atual_num == 0:
        Arma_atual = janela.blit(PersonagemImage, (x, y))
    janela.blit(Inimigo,(pos_x,pos_y))
    janela.blit(Inimigo1, (pos_x_1,pos_y_1))
    janela.blit(texto, pos_Nivel)
    janela.blit(moeda_texto,pos_texto_moeda)
    janela.blit(Vida_texto,pos_texto_Vida)
    janela.blit(FundoBarraDeNivel, (0,580))
    janela.blit(PocaoVida_texto, pos_texto_PocaoVida)
    janela.blit(PocaoXP_texto,pos_texto_PocaoXP)
    #BARRA DE NIVEL
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_v]:
       if vida <= 99:
           if PocaoVida > 0:
                PocaoVida -= 1
                if vida <= 99:
                    vida += 30
    if comandos[pygame.K_TAB]:
        janela.blit(FundoLoja, (100, 0))
        if comandos[pygame.K_F1]:
            if Moeda >= 200:
                Arma_atual_num = 1
                velocidade += randint(4, 7)
                Moeda -= EspadaDeDiamante_preço
        if comandos[pygame.K_F2]:
            if Moeda >= 400:
                Arma_atual_num = 2
                velocidade += randint(5, 10)
                Moeda -= Espada_Do_Fin_preço
        if comandos[pygame.K_F3]:
            if Moeda >= 600:
                Arma_atual_num = 3
                velocidade += randint(2, 5)
                Moeda -= EspadaDePedra_preço
        if comandos[pygame.K_F4]:
            if Moeda >= 100:
                PocaoVida += 1
                Moeda -= PocaoVida_Preco
                PocaoVida_texto = font.render("POCAO: " + (str(PocaoVida)), True, (0, 0, 0), (255, 69, 0))
        if comandos[pygame.K_F5]:
            if Moeda >= 100:
                xp += 1
                Moeda -= PocaoXP_Preco
                PocaoXP_texto = font.render("POCAO: " + (str(PocaoXP)), True, (0, 0, 0), (255, 69, 0))
    if Arma_atual_num == 3:
        Arma_atual = janela.blit(PersonagemComEspada_pedra, (x, y))
    if Arma_atual_num == 1:
        Arma_atual = janela.blit(PersonagemComEspada_diamante, (x, y))
    if Arma_atual_num == 2:
        Arma_atual = janela.blit(PersonagemComEspada_fin, (x, y))

    if xp == 1:
        janela.blit(BarraDeNivel, (0, 580))
    if xp == 2:
        janela.blit(BarraDeNivel1, (0, 580))
    if xp == 3:
        janela.blit(BarraDeNivel2, (0, 580))
    if xp == 4:
        janela.blit(BarraDeNivel3, (0, 580))
    if xp == 5:
        janela.blit(BarraDeNivel4, (0, 580))
    if xp == 6:
        janela.blit(BarraDeNivel5, (0, 580))
    if xp == 7:
        janela.blit(BarraDeNivel6, (0, 580))
    if xp == 8:
        janela.blit(BarraDeNivel7, (0, 580))
    if xp == 9:
        janela.blit(BarraDeNivel8, (0, 580))
    if xp == 10:
        janela.blit(BarraDeNivel9, (0, 580))
    #vida
    if vida <= 0:
        janela.blit(perder, (0, 0))

    pygame.display.update()

pygame.quit()
