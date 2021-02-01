# SISTEMA PARA RESOLVER LIMITES, DERIVADAS E INTEGRAIS




## Introdução
<p> Como trabalho final para disciplina de cálculo I foi proposto desenvolver um sistema para resolver problemas estudados ao decorrer da disciplina. Ao decorrer do semestre foi ensinado sobre funções, limites, derivadas, integrais e outros temas relacionados a cálculo I. O sistema desenvolvido, chamado Calculadora Plus Plus, foi criado para resolver o conteúdo citado. </p>

## calculadora Plus plus
<p>A Calculadora Plus Plus foi desenvolvida com a linguagem de programação Python, é utilizado das bibliotecas sympy e math para a resolução dos exercícios de cálculo especificamente e tkinter para construir toda a interface gráfica.  </p><br>

<p align="center">
    <img  src="https://github.com/mazarafa/Under-Control/blob/main/image/te.PNG" title=""><br />
    
</p>

<p align="center">
    <img  src="https://github.com/mazarafa/Under-Control/blob/main/image/fluxo.PNG" title=""><br />
    
</p>


A calculadora, ilustrada acima, realiza as seguintes operações:
  
Cálculos de limites:
* No ponto;
* Laterais.

Cálculos de derivadas:
* Sendo possível avaliar a derivada em um ponto.

Cálculos de Integrais:
* Definidas;
* Indefinidas.

<p> O objetivo do projeto é observar se o conteúdo estudado pelo acadêmico/aluno em aula está validando com aplicativo, verificando se a resposta é compatível com a solução desenvolvida pelo mesmo. A longo prazo seria a implementação de novas funções e deixar o mesmo mais consistente e intuitivo para as próximas gerações utilizarem, com possibilidades de melhorias, deixando o código aberto para quem desejar acessar e alterar no github.</p><br>
<p>O desenvolvimento pelo front-end, em específico, se iniciou pela tela maior, onde os demais componentes foram inseridos. Após foi desenvolvido o label, frase no canto superior direito, para informar a equação e o resultado completo ou se a equação é inválida. Logo abaixo foi criado um display para mostrar a equação conforme é digitada pelo usuário, ocupando toda a largura e abaixo todos os botões, sendo estes dígitos numéricos, operadores e funções para limpar display, montar a equação desejada e dar início ao cálculo para mostrar o resultado. Por último na tela foi criado um label para dicas, pois alguns símbolos são diferentes das calculadoras usuais.</p><br>
<p>Ao término de toda a parte gráfica se deu início a parte interna, chamada back-end, onde, por baixo dos panos, onde o usuário não têm noção do que ocorre, cada dígito informado pelo menos, através do teclado, ou clicks do mouse, são divididos e verificados através de condicionais para realizar operações de forma separada e juntas as mesmas aos poucos até chegar ao resultado final e retornar ao usuário final.</p><br>

<p align="center">
    <img  src="https://github.com/mazarafa/Under-Control/blob/main/image/executando.PNG" title=""><br />
    
</p>

## Ambiente

´sudo apt install python3-tk´
´sudo apt install python3-pip´

[Acesse: ](https://github.com/sympy/sympy)
´pip3 install sympy´

### Se usar o terminal ubuntu no windows seguir os passos adiante:

1 - Baixar o Xgaming X Server for Windows: https://sourceforge.net/projects/xming/?source=typ_redirect

2 - Em seguida, entrar no diretório inicial ~no terminal do Ubuntu e abrir o arquivo .bashrc executando ´vim .bashrc.´ ou abrindo via arquivo.

3 - No final do arquivo, adicionar a seguinte linha: ´export DISPLAY=:0;.´
