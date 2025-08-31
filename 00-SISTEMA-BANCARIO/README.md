Sistema Bancário em Python
==========================

Bem-vindo ao **Banco Python**!

Este projeto é um sistema bancário simples, desenvolvido como exercício prático para o curso de back-end com python, oferecendo operações essenciais de **Depósito**, **Saque** e **Extrato**.

Funcionalidades
---------------

-   **Depósito**: Permite adicionar valores positivos à conta. Todos os depósitos são registrados no extrato.

-   **Saque**: Permite até 3 saques diários, com limite de R$ 500,00 por saque. O valor sacado é descontado do saldo e registrado no extrato. O sistema impede saques acima do saldo ou do limite estabelecido.

-   **Extrato**: Lista todas as movimentações (depósitos e saques), com data e hora de cada operação, além do saldo atual formatado corretamente.

Como Usar
---------

-   **Execute o programa** rodando o arquivo Python:

``` Python
sistema_bancario.py
```

-   **Siga as instruções do menu exibido**:
    -   `[d]` **Depositar**: Informe o valor do depósito (deve ser positivo).
    -   `[s]` **Sacar**: Informe o valor a ser sacado (até R$ 500,00, limitado a 3 saques por sessão e ao saldo disponível).
    -   `[e]` **Extrato**: Exibe o histórico detalhado de todas transações e o saldo.
    -   `[q]` **Sair**: Encerra o sistema.

Regras do Sistema
=================

-   Apenas **valores positivos** podem ser depositados.

-   **Limite de saque**: R$ 500,00 por operação, até 3 saques por sessão.

-   Não é possível sacar valores superiores ao saldo da conta.

-   Todas as transações são exibidas no extrato com data e hora.

-   Caso não haja movimentações, o extrato informará que não foram realizadas operações.

Diferenciais do Projeto
-----------------------

-   **Organização por funções**: O código é modular, facilitando manutenção e futuras ampliações.

-   **Registro com data/hora**: Cada operação é anotada com o momento exato realizado.

-   **Mensagens de erro e sucesso claras**: O usuário é informado detalhadamente sobre cada ação.

-   **Visual moderno e amigável**: Menu estilizado, mensagens personalizadas, e feedback para o usuário a cada operação.

-   **Tratamento de exceções**: Previne falhas em casos de entradas inválidas.

Pré-Requisitos
--------------

-   Python 3.x instalado na sua máquina.

-   Nenhuma biblioteca adicional necessária.

Exemplo de Uso
--------------

========================================

```
  BANCO PYTHON v1.0

```

========================================

[d] Depositar

[s] Sacar

[e] Extrato

[q] Sair

========================================

Selecione a opção desejada: d

Informe o valor do depósito: R$ 500

Depósito de R$ 500.00 realizado com sucesso!

Selecione a opção desejada: s

Informe o valor do saque: R$ 200

Saque de R$ 200.00 realizado com sucesso!

Selecione a opção desejada: e

========== EXTRATO ==========

08/07/2025 19:00 - Depósito: R$ 500.00

08/07/2025 19:05 - Saque: R$ 200.00

Saldo atual: R$ 300.00

=============================

Licença

Este projeto é de uso livre para fins de aprendizagem.

Desenvolvido por Antônio 🐍