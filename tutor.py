# -*- coding: utf-8 -*-
import dominio as dm
import aluno as al
historico = 0

def recomenda_colaborativa(aluno):

    similiar = al.get_similar(aluno)
    if similiar == []:
        print 'Não é possível recomendar questões baseadas nos colegas de mesmo perfil'
    else:
        resposta  = dm.show_questao(similiar.get_ultimo())

def feedback_nivel(nivel, valor, total):

    media = float(valor/total)

    if media < 0.3:
        print 'Você teve bom desempenho no nível' + nivel + '.'
    elif media >= 0.3 and media < 0.5:
        print 'Você teve desempenho regular no nível' + nivel + '.'
    else:
        print 'Como um todo, o seu desempenho no nível' + nivel + 'não foi muito bom.'


def feedback(aluno, dis):
    
    if dis == 1:
        percentual = aluno.get_merros()
        pontuacao = aluno.get_M()
        disciplina = 'Matemática'
    elif dis == 2:
        percentual = aluno.get_ferros()
        pontuacao = aluno.get_F()
        disciplina = 'Física'
    else:
        percentual = aluno.get_qerros()
        pontuacao = aluno.get_Q()
        disciplina = 'Ciências'

    print 'A sua pontuação total em ' + disciplina + ' é de ' + str(pontuacao)

    for i in range(dm.num_niveis()):
        feedback_nivel(i, percentual[i], dm.qst_nivel())

def recomenda_conteudo(aluno,dis):
    #verifica se já respondeu todas as questões
    if dis == 1:
        done = len(aluno.get_mdone())
        if done < dm.num_mat():
            cont = 0
    elif dis == 2:
        done = len(aluno.get_fdone())
        if done < dm.num_fis():
            cont = 0
    else: 
        done = len(aluno.get_qdone())
        if done < dm.num_cie():
            cont = 0

    if cont == 0:
        linha = done/5
        coluna = done%5
        questao = dm.get_questao(dis, linha, coluna)
        resposta = dm.show_questao(questao)
        #acertou a questao
        if resposta == 0:
            if dis == 1:
                aluno.update_mdone(questao.get_id())
                aluno.set_M(aluno.get_M() + questao.get_pont())
            elif dis == 2:
                aluno.update_fdone(questao.get_id())
                aluno.set_F(aluno.get_F() +questao.get_pont())
            else:
                aluno.update_qdone(questao.get_id())
                aluno.set_Q(aluno.get_Q() +questao.get_pont())
        else:
            if dis == 1:
                aluno.set_M(aluno.get_M() - 1)
                aluno.set_merros(linha)
                aluno.set_ultimo(questao)
            elif dis == 2:
                aluno.set_F(aluno.get_F() - 1)
                aluno.set_ferros(linha)
                aluno.set_ultimo(questao)
            else:
                aluno.set_Q(aluno.get_Q() - 1)
                aluno.set_qerros(linha)
                aluno.set_ultimo(questao)

        return 0

    else:
        done = len(aluno.get_especiais())
        if done < dm.num_esp():
            questao = dm.get_especial(done)
            resposta = dm.show_questao(questao)
            if resposta == 0:
                aluno.update_especiais(questao.get_id())
                aluno.set_E(aluno.get_E() + questao.get_pont())
            else:
                aluno.set_E(aluno.get_E() - 1)
                aluno.set_ultimo(questao)

            return 1

        else:
            return 2

def tutoria(aluno, num):
        recomenda(aluno,num)