# Objetivo

A nossa rede de academias possui vários estabelecimentos. Cada estabelecimento possui os seus funcionários e alunos, além de vendermos produtos. Os funcionários são responsáveis por ministrar aulas, criar fichas de treino ,realizar avaliações físicas, efetuar cobranças e venderem produtos. Os alunos têm acesso à musculação, contendo fichas de treino e uma avaliação física obrigatória, além de poderem se matricular em aulas, como spinning, zumba, etc.

## Análise de Requisitos do Banco de Dados (Academia)

### 1 - Alunos
- Nome.
- Data de nascimento.
- CPF.
- Telefone.
- ID.

_Relacionamentos:_
- Possuem avaliações físicas.
- Têm fichas de treino.
- Efetuam cobranças.
- Participam de aulas.
- Podem comprar produtos.


### 2 - Funcionários
- Nome.
- Data de nascimento.
- CPF.
- Telefone.
- Cargo.
- Salário.
- ID.

_Relacionamentos:_
- Ministram aulas.
- Criam fichas de treino.
- Realizam avaliações físicas.
- Vendem produtos.
- Realizam cobranças.
- Pertencem a um estabelecimento.


### 3 - Cobrança
- Valor.
- Data de cobrança.
- Data de vencimento.
- Forma de pagamento.
- Status.
- ID.

### 4 - Ficha de Treino
- Exercícios.
- Data de início.
- Quantidade de dias.


### 5 - Estabelecimento
- Nome.
- Endereço.
- Aluguel.
- ID.

_Relacionamentos:_
- Possui produtos.


### 6 - Aulas
- Tipo de aula.
- Horário.
- Data.
- ID.

_Relacionamentos:_
- Possuem professores.
- São frequentadas por alunos.


### 7 - Avaliação Física
- Peso.
- Altura.
- Problemas médicos.
- Data.

_Relacionamentos:_
- Pertencem a alunos.
- São realizadas por funcionários.


### 8 - Produtos
- Nome.
- Tipo.
- Preço.
- Quantidade.
- ID.

### 9 - Planos:
- Nome.
- Preço.
- Tipo.
- ID.

_Relacionamentos:_
- São vendidos por funcionários.
- Podem ser comprados por clientes.
- Pertencem ao estabelecimento.


# Requisitos Funcionais:
- Média salarial por cargo.
- Gasto salarial mensal.
- Gasto total mensal.
- Receita mensal.
- Lucro mensal.
- Idade média dos alunos.
- Média de peso dos alunos.
- Quantidade de alunos por plano.
- Idade média dos funcionários.
- Receita total por forma de pagamento por mês.
- Gasto salarial mensal por estabelecimento.
- Receita por tipo de produto.
- Quantidade de alunos por aula.
- Quantidade de alunos por estabelecimento.
- Quantidade de cobranças em atraso em um mês.
- Quantidade de funcionários por cargo por estabelecimento.
- Quantidade de funcionarios de um estabelicimento.
- Quantidade de produtos por tipo.
- Quantidade de produtos por estabelecimento.
- Quantidade de produtos vendidos por mês.

