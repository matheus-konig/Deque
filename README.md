# Implementação de classe Deque em Python
O objetivo desse diretório é documentar minha abordagem para implementar uma estrutura de dados Deque (Double-Ended Queue) utilizando meu código de [implementação de Queues](https://github.com/matheus-konig/Queues/tree/main) como base, apenas fazendo as alterações necessárias --- Atividade proposta pelo professor Luis Claudio Leite Pereira, na disciplina Estrutura de Dados.

Código feito sem uso de arrays ou da biblioteca `collections.deque`.

## Utilização e Métodos
A seguir estão os exemplos de como utilizar os métodos presentes na classe `Deque`.

OBS: Citarei apenas os métodos novos ou modificados, visto que os outros podem ser conferidos no repositório disponibilizado.

#### Adicionar Elemento no Início da Lista

Adiciona um novo elemento no começo da fila utilizando o método `insert_first()`.
Se a fila estiver cheia irá disparar a excessão `OverflowError`.
```python

        nome_lista.insert_first("nome_elemento1")

```

#### Adicionar Elemento no Fim da Lista

Adiciona um novo elemento ao final da fila utilizando o método `insert_last()`.
Se a fila estiver cheia irá disparar a excessão `OverflowError`.
```python

        nome_lista.insert_last("nome_elemento2")

```

#### Remover Elemento no Início da Lista

Remove o elemento que está no começo da fila utilizando o método `remove_first()`.
Se a fila estiver vazia irá disparar a excessão `IndexError`.
```python

        nome_lista.remove_first()

```

#### Remover Elemento no Fim da Lista

Remove o elemento que está no final da lista utilizando o método `remove_last()`.
Se a fila estiver vazia irá disparar a excessão `IndexError`.
```python

        nome_lista.remove_last()

```
#### Visualizar o Primeiro Elemento

Retorna o valor do elemento que está no início da lista sem removê-lo utilizando o método `first()`.
Se a fila estiver vazia irá disparar a excessão `IndexError`.
```python

        nome_lista.first()

```


#### Visualizar o Último Elemento

Retorna o valor do elemento que está no final da lista sem removê-lo utilizando o método `last()`.
Se a fila estiver vazia irá disparar a excessão `IndexError`.
```python

        nome_lista.last()

```

## Código Funcionando

A seguir um print do terminal ao executar o script, contendo testes de todas as funções novas e tratamento de erros:

<img width="959" height="760" alt="image" src="https://github.com/user-attachments/assets/05300950-d432-4bd5-8a9a-39316a232e09" />

## Links

[Atividade no Google Classroom](https://classroom.google.com/c/ODI1MjIzMzA5OTEx/a/ODY3Mzg4MzEwMzQ3/details)

[Repositório Original sobre Classes Queue](https://github.com/matheus-konig/Queues/tree/main)
