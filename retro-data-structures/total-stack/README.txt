
Para testar a pilha retroativa rode o script 'RtrStack.py'
e insira operções válidas no seguinte formato:

    <operação> <instante de tempo: t> <opcional: valor>

    Exemplo: insert_push 7 5 (insere a operação 'push 5' no instante 7)

Lista de operações:
    - insert_push <t> <valor>
    - delete_push <t>
    - insert_pop <t>
    - delete_pop <t>
    - query_top <t>