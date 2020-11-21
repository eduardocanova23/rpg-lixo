import random
class Personagem:
    def __init__(self, classe):
        self.classe = classe
        self.hp = self.stats()[2] * 10
        self.nome = self

    def stats(self):
        # força, inteligencia, vida, agilidade, furtividade, sorte
        if self.classe == 'assassino':
            return [4, 6, 5, 8, 9, 5]

        elif self.classe == 'barbaro':
            return [10, 1, 9, 2, 0, 2]

        elif self.classe == 'cavaleiro':
            return [7, 5, 8, 1, 0, 2]

        elif self.classe == 'mago':
            return [1, 12, 4, 5, 4, 3]

        elif self.classe == 'arqueiro':
            return [2, 7, 5, 10, 6, 3]

        elif self.classe == 'goblin':
            return [2, 0, 2, 2, 1, 5]

        elif self.classe == 'orc':
            return [4, 1, 3, 1, 0, 2]

        elif self.classe == 'troll':
            return [3, 2, 3, 3, 0, 3]

        elif self.classe == 'necromante':
            return [1, 6, 2, 2, 1, 4]

        elif self.classe == 'fênix':
            return [3, 5, 3, 6, 0, 1]

    def equipamento(self):
        self.equipamento = dict()
        if self.classe == 'assassino':
            self.equipamento['arma'] = ['adaga', 1]
            self.equipamento['roupa'] = ['tunica', 1]
            self.equipamento['especial'] = 'smoke'
            self.equipamento['moedas'] = 0
            return self.equipamento

        elif self.classe == 'arqueiro':
            self.equipamento['arma'] = ['arco', 1]
            self.equipamento['roupa'] = ['manto', 2]
            self.equipamento['especial'] = 'headshot'
            self.equipamento['moedas'] = 0
            return self.equipamento

        elif self.classe == 'barbaro':
            self.equipamento['arma'] = ['machadao', 3]
            self.equipamento['roupa'] = ['tanga', 0]
            self.equipamento['especial'] = 'grito amedontrador'
            self.equipamento['moedas'] = 0
            return self.equipamento

        elif self.classe == 'cavaleiro':
            self.equipamento['arma'] = ['espada', 2]
            self.equipamento['roupa'] = ['armadura de metal', 3]
            self.equipamento['especial'] = 'cura'
            self.equipamento['moedas'] = 0
            return self.equipamento

        elif self.classe == 'mago':
            self.equipamento['arma'] = ['cajado', 1]
            self.equipamento['roupa'] = ['tunica magica', 1]
            self.equipamento['especial'] = 'dano em area'
            self.equipamento['moedas'] = 0
            return self.equipamento

        elif self.classe == 'orc':
            self.equipamento['roupa'] = ['armadurinha', 1]
            self.equipamento['loot'] = 0

        elif self.classe == 'goblin':
            self.equipamento['roupa'] = ['trapo lixo', 0]
            self.equipamento['loot'] = 0

        elif self.classe == 'fênix':
            self.equipamento['roupa'] = ['pelada', 0]
            self.equipamento['loot'] = 0

        elif self.classe == 'troll':
            self.equipamento['roupa'] = ['armadurinha', 1]
            self.equipamento['loot'] = 0

        elif self.classe == 'necromante':
            self.equipamento['roupa'] = ['capa da uruguaiana', 1]
            self.equipamento['loot'] = 0



    def ataque(self, other):
        # formula pra calcular o dano causado -> dano do personagem menos a
        # armadura do outro
        print(self.dano())
        print(other.equipamento['roupa'][1])
        causado = self.dano() - other.equipamento['roupa'][1]

        # formula pra calcular se o hit deu miss ou nao -> baseado em furtividade
        # agilidade e sorte
        passou = True
        formula = round((other.stats()[5] + other.stats()[4] + other.stats()[3])/10)

        if random.randint(0, 10) <= formula:
            passou = False

        if passou:
            other.hp -= causado
            return('Dano causado:', causado)

        if not passou:
            return('Deu miss, se fudeu')



class Inimigo(Personagem):

    def dano(self):
        if self.classe == 'goblin':
            return 10 + random.randint(0, self.stats()[5])

        if self.classe == 'fênix':
            return 11 + random.randint(0, self.stats()[5])

        if self.classe == 'orc':
            return 15 + random.randint(0, self.stats()[5])

        if self.classe == 'troll':
            return 13 + random.randint(0, self.stats()[5])

        if self.classe == 'necromante':
            return 9 + random.randint(0, self.stats()[5])



class Jogador(Personagem):

    def dano(self):
# o ultimo numero somado se refere a propria arma, se tiver um arco mais foda
# ele vai ter um dano maior
        if self.classe == 'arqueiro':
             return random.randint(0, self.stats()[5]) + self.stats()[3]
             print(self.equipamento()['arma'][1])

        if self.classe == 'mago':
            return random.randint(0, self.stats()[5]) + self.stats()[1] + danobase

        if self.classe == 'cavaleiro':
            return random.randint(0, self.stats()[5]) + self.stats()[0] + danobase

        if self.classe == 'barbaro':
            return random.randint(0, self.stats()[5]) + self.stats()[0] + danobase

        if self.classe == 'assassino':
            return random.randint(0, self.stats()[5]) + self.stats()[3] + danobase

classes = ['assassino', 'mago', 'barbaro', 'cavaleiro', 'arqueiro']

start = True
while start:
    # todo print é uma mensagem do bot
    print('Escolha sua classe (digite)')
    classe = input().lower()

    if classe == 'sair':
        print('Você saiu do jogo')
        start = False
        continue

    if classe not in classes:
        continue

    else:
        print('sua classe é', classe)
        break



nomes = ['Bkarlos', 'Snorf', 'Jcocria', 'Bkokria', 'Halbertinho', 'Dagmar', 'Craluxo']
iniclass = ['fênix', 'orc', 'troll', 'goblin', 'necromante']


j1 = Jogador(classe)
danobase = j1.equipamento()['arma'][1]
inimigo1 = Inimigo(random.choice(iniclass))
inimigo1.nome = random.choice(nomes)
# print(j1.hp)
# print(j1.equipamento()['arma'][1])
# print(j1.classe)
# print(j1.stats()[0])
print(inimigo1.equipamento['roupa'][1])
for i in range (10):
    print('dano jogador',j1.dano())
    print('dano inimigo', inimigo1.dano())



# onde o nome ali na fstring é o nome do usuário do discord
# e o print é a mensagem do bot
# print(f'''Sua jornada começa onde a maioria das aventuras têm sua origem:
# Na taverna. Infelizmente sua aventura será fácil demais ou difícil demais
# pois esse jogo ainda está em fase de desenvolvimento.
# Você está sentado numa mesa bebendo hidromel e cuidando dos seus afazeres quando
# o taverneiro te chama: "Ei, {edu.nome} tem um cara estranho querendo falar contigo"
# E ele te aponta um homem encapuzado lá no canto da taverna. Obviamente você vai
# falar com ele porque se não você não tava jogando esse jogo. Narrativa aleatória
# que depois eu faço''')


# antes do combate criar de 2 a 4 inimigos pra batalhar com o jogador e associar
# a classe Inimigo
# for i in range(random.randint(2,4)):
#     eval(random.choice(nomes)) = Inimigo(random.choice(iniclass))


print(f'Você está enfrentando um {inimigo1.classe}, o nome dele é {inimigo1.nome}')

print(j1.equipamento['roupa'][1])
print(inimigo1.classe)

combate = True
while combate and start:

    if j1.hp <= 0:
        start = False
        combate = False
        print('Você morreu, ninguém vai chorar no seu enterro')

    if inimigo1.hp <= 0:
        combate = False
        print(f'''Você matou {inimigo1.nome}, o {inimigo1.classe}. Seu loot é
        {inimigo1.equipamento()['loot']} moedas''')

    acao = input('selecione sua ação:')
    if acao == 'atacar':
        j1.ataque(inimigo1)

    print('Seu hp:', j1.hp)
    print('hp do inimigo:', inimigo1.hp)

    inimigo1.ataque(j1)

    print('Seu hp:', j1.hp)
    print('hp do inimigo:', inimigo1.hp)

    start = False
