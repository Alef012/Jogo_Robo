class Ponto:
    def __init__(self,x,y):
        self.x=x
        self.y =y

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
def conferir_recompensa(robo, recompensas):
    ok=False
    for recompensa in recompensas:
        if recompensa.x == robo.x and recompensa.y == robo.y:
            print("O robô achou a recompensa " + recompensa.nome)
            ok = True
    return ok
r1=Robo(2,10)
reward1= Recompensa(2,10,'moeda')
recompensas =[reward1]
conferir_recompensa(r1,recompensas)
