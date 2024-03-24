# AFDatividade

Explicação e exemplos da atividade:

Um AFD cujo o objetivo é aceitar somente números pares de 1, onde o alfabeto é {0, 1}, seu estado inicial é q0 e o final q1!

q0 0 q0
q0 1 q1 
q1 0 q1
q1 1 q0

Entradas para rejeitar:
* "010": Aqui, o número total de '1's é ímpar.
* "1001": Aqui, o número total de '1's é ímpar.

Entradas para aceitar:
* "101": O número total de '1's é par.
* "110": O número total de '1's é par.
* "000": Não há '1's na entrada.
