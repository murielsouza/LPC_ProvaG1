# controle-de-agendas
Prova de G1, disciplina Linguagem de Programação Comercial (LPC)


Prova G1:

Questões:
Você foi contratado por uma empresa para continuar um projeto de um desenvolvedor que acabou de
entrar em licença médica. O projeto consiste no desenvolvimento de um back-end para atender a
criação de agendas para os usuários de uma intranet da empresa.
Antes de sair o desenvolvedor anterior levantou os seguintes requisitos do projeto:
- Agendas podem ser de dois tipos: PRIVADAS ou PUBLICAS
- Um usuário pode criar várias agendas;
- Os usuários podem cadastrar um ou vários “compromissos” nas suas agendas;
- Deve existir uma agenda institucional para a vinculação dos feriados (compromissos) que
impactarão no funcionamento da empresa;
1) Considere a situação apresentada acima e implemente, utilizando Framework Django, os
modelos (models.py) que atendam aos requisitos. (3,0)
2) Crie rotas (urls) e respectivas visões (views) para atender as seguintes situações:
a) Uma rota que retorna todas as agendas cadastradas; (1,0)
b) Uma rota que retorna as agendas públicas de um usuário pelo seu identificador (id).
Se eu digitar na url /agendas/usuario/1 deve ser apresentado todas as agendas do
usuário com identificador 1. (1,0)
c) Uma rota que apresente todos os compromissos (feriados) da agenda institucional;
(1,0)

Avaliação 2:

Ainda no contexto de Agendas (aplicado na G1), foram solicitados mais requisitos funcionais:

Um usuário pode compartilhar suas agendas com outros usuários;
Um usuário pode convidar os demais para um compromisso especifico;
Os usuários convidados podem confirmar ou declinar na participação de um compromisso que foram convidados;

