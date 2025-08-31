Sistema Bancário em Python
==========================

Bem-vindo ao Banco Python!\
Este projeto é um sistema bancário simples e modular, desenvolvido como exercício prático para estudos de back-end com Python. Agora ainda mais completo, o sistema oferece as operações essenciais de Depósito, Saque, Extrato, e também inclui o cadastro de usuários e contas bancárias.

Funcionalidades
---------------

-   Depósito: Permite adicionar valores positivos à conta; todos os depósitos são registrados no extrato.
-   Saque: Permite até 3 saques diários, com limite de R$ 500,00 por saque. O valor é descontado do saldo e registrado no extrato. O sistema impede saques acima do saldo ou do limite estipulado.
-   Extrato: Exibe todas as movimentações (depósitos e saques) com data e hora de cada operação, além do saldo atual formatado.
-   Cadastro de Usuário: Permite registrar e buscar usuários via CPF, incluindo nome, data de nascimento e endereço.
-   Abertura de Conta Corrente: Cria contas vinculadas a usuários existentes, gerando número da conta e associando agência, titular e demais informações.
-   Listagem de Contas: Exibe as contas cadastradas, junto ao titular e outros dados.

Como Usar
---------

-   **Execute o programa** rodando o arquivo Python:

``` Python
sistema_bancario.py
```

Siga as instruções do menu:

-   `[d]` Depositar: Informe o valor do depósito (apenas valores positivos).

-   `[s]` Sacar: Informe o valor a ser sacado (até R$ 500, limitado a 3 saques por vez e ao saldo disponível).

-   `[e]` Extrato: Exibe o histórico detalhado de todas as transações e o saldo.

-   `[nu]` Novo usuário: Cadastre um novo cliente no sistema.

-   `[nc]` Nova conta: Crie uma nova conta vinculada a um usuário já cadastrado.

-   `[lc]` Listar contas: Exibe todas as contas já criadas.

-   `[q]` Sair: Encerra o sistema.

Regras do Sistema
-----------------

-   Apenas valores positivos podem ser depositados.

-   Limite de saque: R$ 500,00 por operação, até 3 saques por sessão.

-   Não é possível sacar valores superiores ao saldo da conta.

-   Todas as transações exibem data/hora.

-   Se não houver movimentações, o extrato informará a ausência de operações.

-   Cada usuário é identificado unicamente pelo CPF.

-   Contas sempre vinculadas a um usuário já criado.

Diferenciais do Projeto
-----------------------

-   Organização modular: O código é dividido em funções para facilitar a manutenção e aprimoramentos futuros.

-   Registro de data/hora: Todas as operações bancárias ficam registradas com o horário exato.

-   Mensagens claras e feedback ao usuário: O sistema informa detalhadamente sucesso ou falha de cada ação.

-   Menu amigável: Visual organizado e comandos autoexplicativos.

-   Tratamento de exceções: Previne travamentos frente a entradas inválidas.

-   Gestão de usuários e contas: Simula a lógica de um banco real, com cadastro de pessoas e suas contas.

Pré-Requisitos
--------------

-   Python 3.x instalado na sua máquina.

-   Não é necessário instalar nenhuma biblioteca extra.

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

[nu] Novo usuário

[nc] Nova conta

[lc] Listar contas

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
-------

Projeto livre para fins de aprendizagem.

*Desenvolvido por Antônio 🐍*

Gostaria de acrescentar exemplos para cadastro de usuário e conta, prints de tela, ou mais instruções para contribuições?