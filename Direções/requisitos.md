# Objetivo

A nossa rede de academias possui vários estabelecimentos. Cada estabelecimento possui os seus funcionários e alunos. Os funcionários são divididos em professores e administrativos. Os professores são responsáveis por ministrar aulas, criar fichas de treino e realizar avaliações físicas. Os funcionários administrativos são responsáveis por efetuar cobranças. Os alunos têm acesso à musculação, contendo fichas de treino e uma avaliação física obrigatória, além de poderem se matricular em aulas, como spinning, zumba, etc.

## Análise de Requisitos do Banco de Dados (Academia)

### 1 - Alunos
- Nome.
- Data de nascimento.
- CPF.
- Telefone.
- ID.

_Relacionamentos:_
- Possuem professores.
- Realizam avaliações físicas.
- Têm fichas de treino.
- Efetuam cobranças.
- Participam de aulas.

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
- Podem pertencer a um estabelecimento.

### 3 - Cobrança
- Valor.
- Data de vencimento.
- Data de pagamento.
- Forma de pagamento.
- ID.

### 4 - Ficha de Treino
- Exercícios.
- Data de início.
- Quantidade de dias.
- ID.

### 5 - Estabelecimento
- Nome.
- Endereço.
- Telefone.

### 6 - Aulas
- Tipo de aula.
- Horário.
- Data.

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
