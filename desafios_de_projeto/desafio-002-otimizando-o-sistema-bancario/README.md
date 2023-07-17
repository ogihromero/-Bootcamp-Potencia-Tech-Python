# Desafio 002 - Otimizando o Sistema Bancário

## Descrição
- Desafio de projeto proposto pelo Bootcamp Potência Tech powered by iFood de Ciências de Dados com Python.
- O código pode ser encontrado [aqui](desafio002_otimizando_sistema_sancario.py).
- O projeot é uma continuação do [Desafio 001](../desafio-001-sistema-bancario-python/README.md).

## Instruções
- O desafio consiste em criar um sistema bancário simples, com as funções de depósito, saque e extrato.
- Deve ser criado uma conta com R$ 500,00 de saldo inicial.
- Há um limite de 3 saques diários.
- Se não houver saldo suficiente para o saque, deve ser exibida uma mensagem de erro.
- O extrato deve ser exibido com os valores no formato monetário (R$ XX,XX).
- Se não houver movimentações realizadas, deve ser exibido uma mensagem no extrato "Não foram realizadas movimentações.".
- A função de depósito deve aceitar argumentos `positional-only` e a função de saque deve aceitar argumentos `keyword-only`.
- A função extrato deve aceitar argumentos `positional-only` e `keyword-only`.
- Necessário funções para criar usuário e criar uma conta.
- Não deve ser permitido criar uma conta com o mesmo CPF.
- O programa deve  manter uma lista com todas as contas criadas.

## Observações
- Foi criado um usuário e conta com o CPF `123456` e saldo inicial de R$ 500,00.
