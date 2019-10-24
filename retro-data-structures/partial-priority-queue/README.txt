
Para testar a fila de prioridades parcialmente retroativa rode
o script 'RtrPrioQueue.py' e insira operações válidas no seguinte formato:

    <operação> <instante de tempo: t> <opcional: valor>
    <busca>    --sempre no presente, não recebe argumento

    Exemplo: insert_enqueue 7 5 (insere a operação 'insert 5' no instante 7)

Lista de operações:
    - insert_insert <t> <valor>
    - insert_deleteMin <t>
    - delete <t>
    - query_min