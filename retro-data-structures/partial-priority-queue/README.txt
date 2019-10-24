
Para testar a fila parcialmente retroativa rode o script 'PartialQueue.py'
e insira operações válidas no seguinte formato:

    <operação> <instante de tempo: t> <opcional: valor>
    <busca>    --sempre no presente, não recebe argumento

    Exemplo: insert_enqueue 7 5 (insere a operação 'enqueue 5' no instante 7)

Lista de operações:
    - insert_enqueue <t> <valor>
    - delete_enqueue <t>
    - insert_dequeue <t>
    - delete_dequeue <t>
    - query_front
    _ query_back