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
        percentual = aluno.get_herros()
        pontuacao = aluno.get_H()
        disciplina = 'Humanidades'
    else:
        percentual = aluno.get_cerros()
        pontuacao = aluno.get_C()
        disciplina = 'Ciências'

    print 'A sua pontuação total em ' + disciplina + ' é de ' + str(pontuacao)

    for i in range(dm.num_niveis()):
        feedback_nivel(i, percentual[i], dm.qst_nivel())

def recomenda_conteudo(aluno,dis):
    cont = 1
    seg = 3
    # verifica se já respondeu todas as questões
    if dis == 1:
        done = len(aluno.get_mdone())
        if done < dm.num_mat():
            cont = 0
    elif dis == 2:
        done = len(aluno.get_hdone())
        if done < dm.num_hum():
            cont = 0
    else: 
        done = len(aluno.get_cdone())
        if done < dm.num_cie():
            cont = 0
    
    # se ainda não respondeu, obtem uma questao
    if cont == 0:
        linha = done/5
        coluna = done%5
        seg = 0
        questao = dm.get_questao(dis, linha, coluna)
        resposta = dm.show_questao(questao)
        #acertou a questao
        if resposta == 0:
            if dis == 1:
                aluno.update_mdone(questao.get_id())
                aluno.set_M(aluno.get_M() + questao.get_pont())
            elif dis == 2:
                aluno.update_hdone(questao.get_id())
                aluno.set_H(aluno.get_H() +questao.get_pont())
            else:
                aluno.update_cdone(questao.get_id())
                aluno.set_C(aluno.get_C() +questao.get_pont())
        else:
            if dis == 1:
                aluno.set_M(aluno.get_M() - 1)
                aluno.set_merros(linha)
                aluno.set_ultimo(questao)
            elif dis == 2:
                aluno.set_H(aluno.get_H() - 1)
                aluno.set_herros(linha)
                aluno.set_ultimo(questao)
            else:
                aluno.set_C(aluno.get_C() - 1)
                aluno.set_cerros(linha)
                aluno.set_ultimo(questao)

    else:
        done = len(aluno.get_especiais())
        if done < dm.num_esp():
            seg = 1
            questao = dm.get_especial(done)
            resposta = dm.show_questao(questao)
            if resposta == 0:
                aluno.update_especiais(questao.get_id())
                aluno.set_E(aluno.get_E() + questao.get_pont())
            else:
                aluno.set_E(aluno.get_E() - 1)
                aluno.set_ultimo(questao)

        else:
            seg = 2

    return seg

def tutoria(aluno, num):
    return recomenda_conteudo(aluno,num)