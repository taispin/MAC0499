# -*- coding: utf-8 -*-

matematica = []
humanidades = []
ciencias = []
especial = []

nmat = 15
nhum = 15
ncie = 15
nesp = 5
nniveis = 3


#def __init__ (self, disciplina, titulo, nivel, pont, enunciado, a, b, c, d, e, r):
bd_matematica = [
["Matemática", "Divisores e Multiplos",0,2, "Quais dos números a seguir estão entre os divisores de 148?","4, 7 e 8","4, 8 e 37","2, 4, 37 e 148","2, 8 e 37","2, 4, 7 e 37","c"],
["Matemática", "Divisores e Multiplos",0,2,"Um conjunto possui 18 elementos. Quantas são as possibilidades existentes para se dividir esse conjunto em grupos com quantidades iguais de elementos?","6","5","4","3","2","a"],
["Matemática", "Divisores e Multiplos",0,2,"O número cuja fatoração completa é igual a 2 x 3 x 5 é divisível pelo números abaixo, exceto :","2","6","15","18","1","d"],
["Matemática", "Divisores e Multiplos",0,2,"Utilizando a fatoração completa do número 204 podemos dizer que ele é divisível pelo números abaixo, exceto :","4","12","17","9","1","d"],
["Matemática", "Fracoes",0,2.5,"Qual das frações abaixo é equivalente a 2/5?","4/10","4/12","5/10","5/8","19/2","a"],
["Matemática", "Equação do 1 grau",1,4, "Em uma determinada região do mar, foi contabilizado um total de 340 mil animais, entre lontras marinhas, ouriços do mar e lagostas. Verificou-se que o número de lontras era o triplo do de ouriços e que o número de lagostas excedia em 20 mil unidades o total de lontras e ouriços. Pode-se dizer que o número de ouriços dessa região é","30 mil.","35 mil","40 mil","45 mil","50 mil.","c"],
["Matemática", "inequação",1,4,"Determine o valor de x na inequação a seguir: 2x + 5 < x +10.","x < 5","x < 6","x < 7","x < 8","todas anteriores","a"],
["Matemática", "Equação do 1 grau",1,4,"Qual o resultado da equação 6x = 2.(x-4)?","x=2","x=-2","x=3","x=-3","x = 0","b"],
["Matemática", "Equação do 1 grau",1,4,"Pensei em um número e multipliquei-o por 5. Depois, somei o resultado com 3 e obtive 23. Pensei em qual número?","3","4","5","6","0","b"],
["Matemática", "inequação",1,4,"Qual o resultado que encontraremos ao resolver a seguinte inequação: 4m-14+4m-14+3m+5+3m+5<38","m < 4","m < 5","m < 6","m < 7","m = 0","a"],
["Matemática", "Geometria",2,5,"Um cilindro com base circular de raio igual a 6 cm, tem volume igual à 180 cm³. Qual o valor da sua altura em metros? Adote pi=3","4","5","2","6","18","b"],
["Matemática", "Geometria",2,5,"Seja um trapézio de bases iguais a 10 e 20 metros respectivamente. Sendo sua altura, raiz da equação: 4x+3=2x+5 . O valor de sua área vale em metros quadrados?","400","200","100","20","500","c"],
["Matemática", "Geometria",2,5,"O total de poliedros de platão são?","1","2","3","4","5","e"],
["Matemática", "Probabilidade",2,6,"Qual é a probabilidade em porcentagem de, no lançamento de 4 moedas, obtermos cara em todos os resultados?","2","2,2","6,2","4","4,2","c"],
["Matemática", "Probabilidade",2,6,"Duas moedas e dois dados, todos diferentes entre si, foram lançados simultaneamente. Qual é o número de possibilidades de resultados para esse experimento?"," 146","142","133","144","155","d"]]

bd_humanidades = [
["Geografia", "Distribuição da população mundial e deslocamentos populacionais", 0, 2, "A distribuição populacional não ocorre de forma homogênea. Esse fenômeno é constatado através das disparidades nos números de habitantes de diferentes continentes, países, regiões, estados e cidades. Indique a alternativa que corresponde ao país mais populoso do planeta.","Estados Unidos.","China.","Índia.","Brasil.","Rússia.","b"],
["Geografia", "Distribuição da população mundial e deslocamentos populacionais",0, 2,"De acordo com dados divulgados em 2009 pelo Fundo de População das Nações Unidas (FNUAP), o planeta Terra é habitado por 6,826 bilhões de pessoas. Essa população está distribuída de forma desigual pelos continentes. Nesse sentido, marque a alternativa que corresponde ao continente mais populoso.","África.","América.","Ásia.","Europa.","América do Norte.","c"],
["Geografia", "Distribuição da população mundial e deslocamentos populacionais",0, 2,"A migração pode ser definida como:","A entrada de migrantes em um determinado país.","A saída de migrantes de um determinado país para outro.","O deslocamento populacional pelo território de um país.","As políticas públicas de controle de natalidade implantadas pelo governo para controlar o crescimento populacional.","Qualquer deslocamento espacial realizado por uma pessoa ou por parte de uma população.","e"],
["Geografia", "Distribuição da população mundial e deslocamentos populacionais",0, 2,"Quando um indivíduo sai de um país em busca de melhores condições de vida, ele recebe o nome de:","emigrante.","forasteiro.","imigrante.","peregrino.","gringo.","a"],
["Geografia", "Distribuição da população mundial e deslocamentos populacionais",0, 2,"Migração é o deslocamento espacial de um indivíduo ou de parte da população de um lugar para outro. A principal causa da migração no mundo e no Brasil tem origem:","econômica.","política.","cultural.","ambiental.","religiosa.","a"],
["Geografia", "Diversidade e dinâmica da população mundial e local",1, 4,"De acordo com o Censo Demográfico de 2010, realizado pelo Instituto Brasileiro de Geografia e Estatística (IBGE), o Brasil alcançou uma população de 190.755.799 pessoas, totalizando 22.4 habitantes por km². Diante desses números, podemos concluir que o país é:","densamente povoado","populoso","homogeneamente povoado","proporcionalmente adensado","pesados","b"],
["Geografia", "Diversidade e dinâmica da população mundial e local",1, 4,"Um dos principais tipos de migrações internacionais existentes é a chamada “fuga de cérebros”, que consiste:","na perda de trabalhadores com baixa qualificação técnica para países estrangeiros, geralmente mais desenvolvidos.","na migração sazonal de pesquisadores universitários e estudantes, como em intercâmbios e cursos de capacitação.","na adoção de políticas internacionais para facilitar o deslocamento dos profissionais de alta capacidade e boa formação escolar.","no deslocamento em massa de profissionais especializados e de grande conhecimento para outros países.","no tráfico internacional de órgãos e pessoas, responsável pela morte de muitos imigrantes, geralmente ilegais.","d"],
["História", "Brasil: Primeiro Reinado",1, 5, "Sobre o processo de Independência deflagrado no Brasil em 1822, que implementou o Primeiro Reinado, é possível dizer que:","Dom Pedro antecipou-se à estratégia de seu irmão, D. Miguel, que também queria ser imperador do Brasil.","foi um processo deflagrado no Brasil após a morte de D. João VI.","foi um processo coordenado pelos revolucionários latino-americanos, como Bartolomé Mitre e Simon Bolívar.","foi um processo articulado por Napoleão Bonaparte, que fugiu da ilha de Santa Helena para o Brasil em 1819.","foi um reflexo da Revolução Liberal do Porto (1820), que exigiu o retornou de D. João VI para Portugal.","e"],
["História", "Brasil: Primeiro Reinado", 1, 5,"Entre as causas da abdicação do trono por parte de D. Pedro I, está:","a União Ibérica, entre Portugal e Espanha.","revoltas locais, como Revolução Farroupilha.","a crise financeira de 1829, que ocasionou o fechamento do Banco do Brasil.","a crise de legitimidade pelo não uso do Poder Moderador.","o processo de Impeachment protocolado por senadores da época.","c"],
["História", "Brasil: Primeiro Reinado",1, 5,"O acontecimento ocorrido na cidade do Rio de Janeiro, quando do regresso de D. Pedro I de Minas Gerais, que contribuiu para a abdicação foi:","A morte da rainha Leopoldina","A prisão do padre Feijó","A Guerra do Paraguai","A noite das garrafadas","a Insurreição Fluminense","d"],
["História", "Brasil: Segundo Reinado",2, 6,"Além de pertencer, por herança, à casa de Bragança, família aristocrática portuguesa da linhagem de João VI, Dom Pedro II também tinha o sangue aristocrático da:","Casa de Hanover","Casa de Habsburgo","Casa de Médice","Casa de Hohestaufen","Casa de Richtohfen","b"],
["História", "Brasil: Segundo Reinado",2, 6,"Dom Pedro II, após a abdicação de seu pai, em 1831, passou a ser Príncipe Regente do Brasil. Essa fase durou até o ano de 1840, quando foi formalizada a sua situação como imperador, quando ele tinha apenas 14 anos de idade. Essa formalização ficou conhecida como:","Regência Una.","Regência Trina","Soberania Clandestina","Nepotismo","Golpe da Maioridade","e"],
["História", "Brasil: Segundo Reinado",2, 6,"Como era apenas uma criança de cinco anos no ano em que seu pai abdicou do trono em seu favor (1831), Dom Pedro II passou cerca de nove anos sendo preparado para cumprir as suas obrigações de monarca. Esse período ficou conhecido como “Regencial”. O fim do Período Regencial ocorreu com:","a morte de Deodoro da Fonseca","a morte de Leopoldina","o Golpe da Maioridade","a Revolta de Juazeiro","o Golpe Republicano","c"],
["História", "Partilha da África",2, 7,"A chamada “Partilha da África” deu-se no fim do século XIX, em um contexto em que as potências nacionalistas europeias tinham expandido os seus domínios pelos continentes asiático e africano. Sobre o processo de “Partilha da África”, é INCORRETO afirmar que:","A Conferência de Berlim foi decisiva para organizar os domínios europeus sobre o território africano.","A França foi o único país a não estabelecer domínios coloniais em território africano.","O Congo passou a ser um território submetido ao domínio particular do rei Leopoldo II, da Bélgica.","A “Partilha da África” pode ser enquadrada no fenômeno mais abrangente denominado “Neocolonialismo”.","Muitas tribos e etnias africanas diferentes ficaram circunscritas a um mesmo território na ocasião em que o continente africano foi dividido.","b"],
["História", "Partilha da África",2, 7,"A “Partilha da África” suscitou uma grande discussão ideológica e científica que procurava justificar a “inferioridade” dos povos africanos e a “missão civilizatória” que a Europa desempenhava em seu processo de colonização. A corrente ideológica com bases cientificistas que mais se destacou nessa época foi:","a microbiologia","a antropologia cultural","o existencialismo","o darwinismo social","a sociobiologia","d"]]

bd_ciencias = [
["Ciências", "Fontes de Energia",0,3,"A principal fonte de energia (para a máquina a vapor) da Revolução Industrial era:","a lenha","o vento","a água","o carvão mineral","o petróleo","d"],
["Ciências", "Fontes de Energia",0,3,"A alternativa onde as fontes de energia estão colocadas segundo uma sequência cronológica da sua utilização pelo homem é:","lenha - humana - carvão mineral - petróleo - nuclear.","humana - animal - eólica (moinhos de vento) - carvão mineral - petróleo - nuclear."," carvão mineral - lenha - petróleo - carvão mineral - nuclear.","eólica - solar - animal - hidrelétrica - carvão mineral.","petróleo - carvão mineral - nuclear - solar.","b"],
["Ciências", "Fontes de Energia",0,3,"Escolha a melhor classificação para as seguintes fontes de energia: eólica, solar, geotérmica (vulcões, gêiseres), xisto e marés.","Renováveis  ","não-renováveis","arcaicas","alternativas","escassas","d"],
["Ciências", "Fontes de Energia",0,3,"Hidráulica, solar, eólica, marés, biomassa (produtos vegetais) são exemplos de fontes de energia","renováveis","não-renováveis","arcaicas","alternativas","escassas","a"],
["Ciências", "Fontes de Energia",0,3,"A maior parte das fontes de energia originam-se:","dos vegetais","dos minerais","do Sol","do mar","do subsolo","c"],
["Ciências", "Cálculo de consumo de energia elétrica",1,5,"O chuveiro elétrico de uma residência possui potência elétrica equivalente a 5000 W. Sabendo que nessa casa moram cinco pessoas e que cada uma toma dois banhos diários de 15 min, determine o consumo de energia elétrica mensal em KWh correspondente ao chuveiro.","150 KWh","250 KWh","475 KWh","300 KWh","375 KWh","e"],
["Ciências", "Cálculo de consumo de energia elétrica",1,5,"Em uma época de intenso calor, um aparelho de ar-condicionado com potência de 1500 W ficou ligado por mais tempo, chegando à marca mensal de consumo igual a 7500 W.h. Determine por quanto tempo esse aparelho ficou ligado por dia em horas.","2","4","5","6","7,5","c"],
["Ciências", "Circuito Elétrico",1,5,"Assinale o dispositivo elétrico capaz de transformar parte da energia elétrica a ele fornecida em outras formas de energia que não sejam exclusivamente a energia térmica.","Resistor","Voltímetro","Amperímetro","Gerador","Receptor","e"],
["Ciências", "Circuito Elétrico",1,5,"Chuveiros elétricos, lâmpadas incandescentes, fios condutores e ferros elétricos possuem algo em comum: todos podem ser classificados no mesmo grupo de dispositivos elétricos. Esses dispositivos podem ser considerados como:","Receptores","Resistores","Fusíveis","Disjuntores","Geradores","b"],
["Ciências", "Circuito Elétrico",1,5,"Alguns dispositivos de segurança utilizados em circuitos elétricos possuem o intuito de interromper a passagem de grandes correntes elétricas que poderiam ser prejudiciais para o seu funcionamento. São dispositivos de segurança:","Pilhas","Resistor e varistor","Fusível e disjuntor","Interruptor","Amperímetro e voltímetro","c"],
["Ciências", "Sistema Sol, Terra e Lua",2,7,"A Terra, assim como todos os corpos celestes presentes no universo, não está parada. Ao todo, são dezenas de diferentes formas de deslocamento realizadas pelo nosso planeta. Assinale, entre as alternativas a seguir, aquela que não indica um dos fenômenos de movimentação terrestre:","rotação","nutação","precessão dos equinócios","inclinação","revolução","d"],
["Ciências", "Sistema Sol, Terra e Lua",2,7,"Entre todos os movimentos realizados pela Terra, a rotação e a translação são consideradas como os dois mais importantes, pois são os que exercem maior influência no cotidiano das sociedades. As consequências principais da rotação e da translação da Terra são, respectivamente,","a intercalação das atividades solares e a variação cíclica dos climas","a ocorrência das estações do ano e a sucessão dos dias e noites","a sucessão dos dias e noites e a ocorrência das estações do ano","a existência dos solstícios e equinócios e a duração do ano em 365 dias","a duração dos ciclos solares e a diferenciação entre climas frios e quentes.","c"],
["Ciências", "Sistema Sol, Terra e Lua",2,7,"O deslocamento do periélio é registrado como um dos movimentos da Terra, mas não é tão lembrado por dois motivos: não exerce uma influência tão grande sobre a vida no planeta e também por apresentar um ciclo muito longo, que totaliza os 21 mil anos. Mas, afinal, o que é o periélio?","é a forma com que a Terra se desloca em torno do seu próprio eixo.","é o movimento aparente da Terra ao longo do universo.","é o eixo da translação terrestre.","é a distância mínima da órbita terrestre em relação ao sol.","é a distância máxima da órbita terrestre em relação ao sol.","d"],
["Ciências", "Alterações ambientais por ação humana",2,7,"O derramamento de petróleo no mar é um problema ambiental grave que merece atenção. Um dos piores vazamentos de petróleo que já ocorreram no planeta foi no Golfo do México, em 2010, onde cerca de cinco milhões de barris de petróleo foram lançados nas águas. Baseando-se nos seus conhecimentos sobre o tema, marque a única alternativa que não indica uma consequência da poluição no mar por petróleo.","Morte de várias espécies de peixes.","Diminuição da pesca na região.","Contaminação de ecossistemas de transição entre o ambiente marinho e terrestre, como mangues.","Aumento da taxa de fotossíntese das algas.","Morte de aves marinhas.","d"],
["Ciências", "Alterações ambientais por ação humana",2,7,"Existem diversos tipos diferentes de poluição, sendo todos prejudiciais ao meio ambiente. Algumas poluições, no entanto, são pouco lembradas, como é o caso da poluição desencadeada quando o volume de determinado som é superior àqueles considerados normais. Analise as alternativas abaixo e marque o nome desse tipo de poluição:","térmica.","atmosférica","ruidosa.","visual.","sonora.","e"]]

bd_especial = [
["Especial", "Matemática",2,10,"Um escritório utiliza uma fragmentadora de papéis, que corta em tiras muito finas documentos cujo conteúdo não se deseja tornar público. Suponha que a fragmentadora desse escritório só aceite uma folha por vez, sendo capaz de fazer sua função a uma velocidade de 3 metros por minuto. Sendo assim, para que um documento com 25 folhas seja fragmentado, levando em consideração que cada folha desse documento tem comprimento de 30 cm, o tempo mínimo para realizar a completa fragmentação desse documento é de","1 min 40 s.","2 min 20 s.","2 min 30 s.","3 min 50 s","3 min 40 s.","c"],
["Especial", "Matemática",2,10,"No munícipio de São Paulo, segundo dados do Instituto Brasileiro de Geografia e Estatística (IBGE), existem 12 milhões de habitantes e, segundo o Repositório de Dados Eleitorais do Tribunal Superior Eleitoral (TSE), no mesmo município, existem 9 milhões de eleitores registrados. Nessas condições, pode-se afirmar que, no munícipio de São Paulo, para cada 3 eleitores registrados, existem ","75 habitantes","40 habitantes.","30 habitantes.","4 habitantes.","3 habitantes.","d"],
["Especial", "História",2,10,"A República do Suriname localiza-se no norte da América do Sul e faz fronteira com a Guiana, com a Guiana Francesa e com o Brasil. Conta com uma área de aproximadamente 163 820 km2 e uma população de aproximadamente 560 000 habitantes. Sua capital é a cidade de Paramaribo. Sobre esse país é correto afirmar que","foi a única colônia europeia na América a não adotar mão de obra escrava.","era colônia holandesa e tornou-se um país independente em meados da década de 1970.","sua língua oficial é o inglês, mas o espanhol é bastante utilizado, assim como alguns dialetos locais.","é banhado pelo Oceano Pacífico e seu relevo é marcado pela existência da Cordilheira dos Andes, que corta o país de norte a sul.","seu principal produto de exportação é a banana, o que torna sua economia estável devido às pequenas variações no mercado de commodities","b"],
["Especial", "Geografia",2,10,"As rochas são agregados naturais de um ou mais minerais. Existem diferentes tipos de rochas, cada um deles formado por processos distintos. Sobre os tipos de rochas, podemos afirmar corretamente que aquelas formadas pela transformação de outras rochas existentes no interior da Terra, submetidas a enormes pressões e altas temperaturas, são conhecidas como","ígneas.","plutônicas.","magmáticas.","sedimentares.","metamórficas.","e"],
["Especial", "Ciências",2,10,"Os primeiros animais surgiram nos mares e eram invertebrados de corpo mole. À medida que o tapete verde desenvolvia-se sobre a Terra, outro grupo de criaturas vivas – os artrópodes – chegava do mar para desfrutar dessa nova e enorme massa de alimentos. Os primeiros artrópodes que emergiram foram talvez os miriápodes primitivos, que atingiam aproximadamente dois metros de comprimento e apresentavam até duzentas patas. Depois vieram as lacraias, as aranhas e os escorpiões. Tempos depois, surgiram as libélulas gigantes, um dos primeiros insetos a voar, com até setenta centímetros de envergadura. O voo foi, talvez, desenvolvido para que esses insetos escapassem dos animais predadores, que os espreitavam no chão. As baratas, os gafanhotos e os grilos também faziam parte dos conjuntos de primeiros insetos que apareceram. Considerando os animais citados no texto, podemos afirmar que ","todos possuem asas, corpo mole e segmentado","as lacraias apresentam endoesqueleto calcário e patas articuladas.","os gafanhotos, os grilos e as aranhas possuem um par de antenas e quatro pares de patas","as libélulas possuem exoesqueleto, três pares de patas e corpo segmentado em cabeça, tórax e abdome.","as baratas, as aranhas e os escorpiões apresentam glândulas de veneno, exoesqueleto e corpo não segmentado.","d"]]

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
        if disciplina == "matematica":
            c = 1
            i = len(matematica[nivel])
        if disciplina == "humanidades":
            c = 2
            i = len(humenidades[nivel])
        else:
            c = 3
            i = len(ciencias[nivel])
        self.id =  (100*c + 10* nivel + i)

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
    print humanidades
    print ciencias

def num_mat():
    return nmat

def num_hum():
    return nhum

def num_cie():
    return ncie

def num_esp():
    return nesp

def num_niveis():
    return nniveis

def qst_nivel():
    return nmat/nniveis


def show_questao(questao):
    print '==================='
    print ''
    print '-------------------'
    print 'Questão de ' + questao.get_disciplina()
    print questao.get_titulo()
    print 'Nivel ' + str(questao.get_nivel())
    print 'Pontuacão ' + str(questao.get_pont()) + '\n'
    print '-------------------'
    print questao.get_enunciado() + '\n'
    print '[a] ' + questao.get_a()
    print '[b] ' + questao.get_b()
    print '[c] ' + questao.get_c()
    print '[d] ' + questao.get_d()
    print '[e] ' + questao.get_e()
    
    escolha = (raw_input('Informe a alternativa correta: '))

    if questao.get_correta() == escolha:
        print '\nResposta Correta!\n'
        return 0
    else:
        print '\nResposta Incorreta!\n'
        return 1

def get_questao(disciplina, linha, coluna):

    if disciplina == 1:
        return matematica[linha][coluna]
    elif disciplina == 2:
        return huminades[linha][coluna]
    else: 
        return ciencias[linha][coluna]

def get_especial(item):
    return especial[item]


def mostra_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            show_questao(matriz[i][j])

def mostra_especial(matriz):
    for i in range(len(matriz)):
        show_questao(matriz[i])


def inicia_matriz(disciplina):
    for y in range(3):
        linha = []
        disciplina.append(linha)

def inicia_matrizes():
    inicia_matriz(matematica)    
    inicia_matriz(humanidades)
    inicia_matriz(ciencias)


def monta_questao(linha):
    novo = Questao(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7],linha[8],linha[9], linha[10])
    return novo

def monta_tabela(bd, mbd):
    k = 0
    for i in range(3):
        for j in range(5):
            mbd[i].append(monta_questao(bd[k]))
            k = k + 1


def prepara_bd_especial():
    for i in range(nesp):
        especial.append(monta_questao(bd_especial[i]))
#    mostra_especial(especial)

def prepara_bds():
    inicia_matrizes()

#    print 'Matemática'
    monta_tabela(bd_matematica, matematica)
#    mostra_matriz(matematica)

#    print 'Humanidades'
    monta_tabela(bd_humanidades, humanidades)
#    mostra_matriz(humanidades)

#    print 'Ciencias'
    monta_tabela(bd_ciencias, ciencias)
#    mostra_matriz(ciencias)