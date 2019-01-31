
import getpass

users = []

class Aluno:
    def __init__ (self, cpf, passwd, nome, idade, email, cidade, age, escola):
        self.cpf = cpf
        self.senha = passwd
        self.nome = nome
        self.idade = int(idade)
        self.email = email
        self.cidade = cidade
        self.age = int(age)
        self.escola = escola
        self.mdone = []
        self.hdone = []
        self.cdone = []
        self.especiais = []
        self.merros = [0,0,0]
        self.herros = [0,0,0]
        self.cerros = [0,0,0]
        self.ultimo = []
        self.M = 0
        self.H = 0
        self.C = 0
        self.E = 0
           
    def get_cpf(self):
        return self.cpf

    def get_senha(self):
        return self.senha
       
    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_email(self):
        return self.email

    def get_cidade(self):
        return self.cidade

    def get_age(self):
        return self.age

    def get_escola(self):
        return self.escola

    def get_mdone(self):
        return self.mdone

    def get_hdone(self):
        return self.hdone
        
    def get_cdone(self):
        return self.cdone

    def get_merros(self):
        return self.merros

    def get_herros(self):
        return self.herros

    def get_cerros(self):
        return self.cerros

    def get_especiais(self):
        return self.especiais

    def get_ultimo(self):
        return self.ultimo

    def get_M(self):
        return self.M

    def get_H(self):
        return self.H

    def get_C(self):
        return self.C

    def get_E(self):
        return self.E

    def set_M(self, valor):
        self.M = valor

    def set_H(self, valor):
        self.H = valor

    def set_C(self, valor):
        self.C = valor

    def set_E(self, valor):
        self.E = valor

    def set_merros(self, pos):
        self.merros[pos] +=1

    def set_herros(self, pos):
        self.herros[pos] +=1

    def set_cerros(self, pos):
        self.cerros[pos] +=1

    def set_ultimo(self, questao):
        self.ultimo = questao

    def update_mdone(self, valor):
        self.mdone.append(valor)

    def update_hdone(self, valor):
        self.hdone.append(valor)

    def update_cdone(self, valor):
        self.cdone.append(valor)

    def update_especiais(self, valor):
        self.especiais.append(valor)


def show_users():
    for i in range(len(users)):
        show_user(users[i])

def show_user(user):
    print '-------------'
    print 'Nome:' + str(user.get_nome())
    print 'Idade:' + str(user.get_idade())
    print 'Email:' + str(user.get_email())
    print 'Ano escolar:' + str(user.get_age())
    print 'Escola:' + str(user.get_escola())
    print ''


def cadastra():
    stop = 0
    print "Nos Informe alguns dados:"
    cpf = (raw_input('CPF: '))
    if cpf == '':
        stop = 1
    senha = (getpass.getpass())
    if senha == '':
        stop = 1
    nome = (raw_input('Nome: '))
    if nome == '':
        stop = 1
    idade = (raw_input('Idade: '))
    if idade == '':
        stop = 1
    email = (raw_input('Email: '))
    if email == '':
        stop = 1
    cidade = (raw_input('Cidade: '))
    if cidade == '':
        stop = 1
    age = (raw_input('Ano Escolar: '))
    if age == '':
        stop = 1
    escola = (raw_input('Escola de Origem: '))
    print ''

    if stop == 0:
        novo = Aluno(cpf, senha, nome, idade, email, cidade, age, escola)
        users.append(novo)
        return 0
    else:
        return 1

    

def check_login(cpf, senha):
    for i in range(len(users)):
        if users[i].get_cpf() == cpf:
            if users[i].get_senha() == senha:
                return 0
    return 1

def get_aluno(cpf):
    for i in range(len(users)):
        if users[i].get_cpf() == cpf:
            return users[i]

def get_similar(aluno):
    for i in range(len(users)):
        if users[i].get_age() == aluno.get_age():
            return users[i]
    return []