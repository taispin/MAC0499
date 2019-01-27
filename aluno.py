
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
        self.fdone = []
        self.qdone = []
        self.especiais = []
        self.merros = [0,0,0]
        self.ferros = [0,0,0]
        self.qerros = [0,0,0]
        self.ultimo = []
        self.M = 0
        self.F = 0
        self.Q = 0
           
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

    def get_fdone(self):
        return self.fdone
        
    def get_qdone(self):
        return self.qdone

    def get_merros(self):
        return self.merros

    def get_ferros(self):
        return self.ferros

    def get_qerros(self):
        return self.qerros

    def get_especiais(self):
        return self.especiais

    def get_ultimo(self):
        return self.ultimo

    def get_M(self):
        return self.M

    def get_F(self):
        return self.F

    def get_Q(self):
        return self.Q

    def set_M(self, valor):
        self.M = valor

    def set_F(self, valor):
        self.F = valor

    def set_Q(self, valor):
        self.Q = valor

    def set_merros(self, pos):
        self.merros[pos] +=1

    def set_ferros(self, pos):
        self.ferros[pos] +=1

    def set_qerros(self, pos):
        self.qerros[pos] +=1

    def set_ultimo(self, questao):
        self.ultimo = questao

    def update_mdone(self, valor):
        self.mdone.append(valor)

    def update_fdone(self, valor):
        self.fdone.append(valor)

    def update_qdone(self, valor):
        self.qdone.append(valor)

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
    print 'Niveis:'
    user.print_niveis()
    print ''


def cadastra():

    print "Nos Informe alguns dados:"
    cpf = (raw_input('CPF: '))
    senha = (getpass.getpass())
    nome = (raw_input('Nome: '))
    idade = (raw_input('Idade: '))
    email = (raw_input('Email: '))
    cidade = (raw_input('Cidade: '))
    age = (raw_input('Ano Escolar: '))
    escola = (raw_input('Escola de Origem: '))

    novo = Aluno(cpf, senha, nome, idade, email, cidade, age, escola)
    novo.set_niveis()
    users.append(novo)

    show_users()

def check_login(cpf, senha):
    '''for i in range(len(users)):
        if users[i].get_cpf() == cpf:
            if users[i].get_senha() == senha:
                return 0
    return 1'''
    return 0

def get_aluno(cpf):
    for i in range(len(users)):
        if users[i].get_cpf() == cpf:
            return users[i]

def get_similar(aluno):
    for i in range(len(users)):
        if users[i].get_age() == aluno.get_age():
            return users[i]
    return []