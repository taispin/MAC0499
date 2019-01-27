matematica = []
fisica = []
ciencias = []
especial = []
inc = 0

nmat = 15
nfis = 15
ncie = 15
nesp = 5
nniveis = 3

#classe page: representa uma questao de uma disciplina na lista de questoes
class Questao:
    def __init__ (self, disciplina, titulo, nivel, pont, enunciado, a, b, c, d, e, r):
        self.disciplina = disciplina
        self.titulo = titulo
        self.nivel = nivel
        self.pont = pont
        self.enunciado = enunciado                
        self.a = a                
        self.b = b                
        self.c = c
        self.d = d
        self.e = e
        self.correct = r
        self.set_id(disciplina,nivel)
   
    def set_id(self,disciplina, nivel):
        c = 0
        inc = inc  + 1
        if disciplina == "matematica":
            c = 1
        if disciplina == "fisica":
            c = 2
        else:
            c = 3
        self.id =  (100*c + 10* nivel + (inc-1))

    def get_disciplina(self):
        return self.disciplina

    def get_titulo(self):
        return self.titulo

    def get_nivel(self):
        return self.nivel

    def get_pont(self):
        return self.pont

    def get_id(self):
        return self.id

    def get_enunciado(self):
        return self.enunciado

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def get_d(self):
        return self.d

    def get_e(self):
        return self.e 

    def get_correta(self) :
        return self.correct

#mostra uma questão para o usuário             

def show_listas():
    print matematica
    print fisica
    print ciencias

def num_mat():
    return nmat

def num_fis():
    return nfis

def num_cie():
    return ncie

def num_esp():
    return nesp

def num_niveis():
    return nniveis

def qst_nivel():
    return nmat/nniveis

def inicia_matriz(disciplina):
    for y in range(4):
        linha = []
        for x in range(5):
            linha.append(0)
        disciplina.append(linha)

def inicia_matrizes():
    inicia_matriz(matematica)    
    inicia_matriz(fisica)
    inicia_matriz(ciencias)

def show_questao(questao):

    print '-------------------'
    print 'Questão de ' + str(questao.get_disciplina())
    print str(questao.get_titulo())
    print 'Nivel ' + str(questao.get_nivel())
    print 'Pontuacão ' + str(questao.get_pont()) + '\n'
    print '-------------------'
    print str(questao.get_enunciado()) + '\n'
    print '[a]' + str(questao.get_a())
    print '[b]' + str(questao.get_b())
    print '[c]' + str(questao.get_c())
    print '[d]' + str(questao.get_d())
    print '[e]' + str(questao.get_e())
    
    escolha = (raw_input('Informe a alternativa correta.'))

    if questao.get_correta() == escolha:
        return 0
    else:
        return 1

def get_questao(disciplina, linha, coluna):

    if disciplina == 1:
        return matematica[linha][coluna]
    elif disciplina == 2:
        return fisica[linha][coluna]
    else: 
        return ciencias[linha][coluna]

def get_especial(item):
    return especial[item]