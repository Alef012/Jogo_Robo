import random
class Ponto:
    def __init__(self,x,y):
        self.x=x
        self.y =y
    def __str__(self):
        return "<%s,%s>" %(self.x,self.y)

class Robo(Ponto):


    def mover_pra_cima(self):
        if self.y<=9:
            self.y+=1
        else:
            print('Movimento Proibido!!')
    def mover_pra_baixo(self):
        if self.y > 0:
            self.y-=1
        else:
            print('Movimento Proibido!!')
    def mover_pra_esquerda(self):
        if self.x >0:
            self.x-=1
        else:
            print('Movimento Proibido!!')
    def mover_pra_direita(self):
        if self.x<10:
            self.x+=1
        else:
            print('Movimento Proibido!!')
class Recompensa(Ponto):
    def __init__(self, x, y,nome):
        super(Recompensa,self).__init__(x, y)
        self.nome=nome

    def __str__(self):
        return "<%s,%s>: %s" %(self.x,self.y,self.nome)

    def __repr__(self):
        return Ponto.__str__(self)

def conferir_recompensa(robo, recompensas):
    ok=False

    for recompensa in recompensas:

        if recompensa.x == robo.x and recompensa.y == robo.y:
            print("O robô achou a recompensa " + recompensa.nome)
            ok = True

    return ok

r1 =Recompensa(random.randint(0,10), random.randint(0,10), 'moeda')
r2 =Recompensa(random.randint(0,10), random.randint(0,10), 'gasolina')
r3=Recompensa(random.randint(0,10), random.randint(0,10), 'arma')
r4 =Recompensa(random.randint(0,10), random.randint(0,10), 'moeda')
r5 =Recompensa(random.randint(0,10), random.randint(0,10), 'gasolina')
r6=Recompensa(random.randint(0,10), random.randint(0,10), 'arma')

rewards=[r1,r2,r3,r4,r5,r6]
robo = Robo(random.randint(0,10),random.randint(0,10))
for i in range(20):
    print("O robo esta na posicao "+robo.__str__())
    move=False
    while move==False:
        movimmento = input("Digite o movimento nas teclas w a s d: ").upper()
        if movimmento == 'W':
            robo.mover_pra_cima()
            conferir_recompensa(robo,rewards)
            move=True
        elif movimmento == 'S':
            robo.mover_pra_baixo()
            conferir_recompensa(robo,rewards)
            move=True
        elif movimmento == 'A':
            robo.mover_pra_esquerda()
            conferir_recompensa(robo,rewards)
            move = True
        elif movimmento == 'D':
            robo.mover_pra_direita()
            conferir_recompensa(robo,rewards)
            move=True
        else:
            print('Movimento invalido')
            
        
    
print("Fim de jogo, as recompensas estavam nas posições: %s" % rewards.__repr__())

