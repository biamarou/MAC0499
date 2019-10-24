
Para testar a fila retroativa rode o script 'RtrQueue.py'
e insira operações válidas no seguinte formato:

    <operação> <instante de tempo: t> <opcional: valor>

    Exemplo: insert_enqueue 7 5 (insere a operação 'enqueue 5' no instante 7)

Lista de operações:
    - insert_enqueue <t> <valor>
    - delete_enqueue <t>
    - insert_dequeue <t>
    - delete_dequeue <t>
    - query_kth <t> <k>
    - query_first <t>