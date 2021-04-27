
Para testar a fila de prioridade parcialmente retroativa rode
o script 'RtrPrioQueue.py' e insira operações válidas no seguinte formato:

    <operação> <instante de tempo: t> <opcional: valor>
    <busca>    --sempre no presente, não recebe argumento

    Exemplo: add_insert 7 5 (insere a operação 'insert 5' no instante 7)

Lista de operações:
    - add_insert <t> <valor>
    - add_deleteMin <t>
    - remove_insert <t>
    - remove_deleteMin <t>
    - query_min