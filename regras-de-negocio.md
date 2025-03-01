# Regras de Negócio 

## RN Geral 

- [x] Separar as funcionalidades existentes de saque, depósito e extrato em funções.

- [x] Criar duas novas funções: criar usuário (cliente) e criar conta corrente.

- [x] Cada função deve ter uma regra na passagem de argumentos.

## RN Saque

- [x] A função saque deve receber os argumentos apenas por nome (keyword only). 

## RN Depósito

- [x] A função de depósito deve receber os argumentos apenas por posição (positional only). 

## RN Extrato 

- [x] A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). 

## RN Criar usuário (cliente)

- [x] O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimeto,
cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser
armazenado somente os números do CPF. Não permitir cadastrar 2 usuários com o mesmo CPF.

## RN Criar conta corrente

- [x] O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e 
usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode 
ter mais de uma conta, mas uma conta só pode pertencer a um único usuário.