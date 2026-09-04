# sistema-de-suporte-pedagogico
# Sistema de Suporte Pedagógico

Projeto pessoal desenvolvido com o objetivo de praticar desenvolvimento de software a partir de um problema observado em um ambiente educacional.

A proposta do sistema é permitir que professores solicitem suporte durante a aula sem precisar se deslocar até o setor responsável pelo atendimento.

## 🎯 Problema

Durante uma aula, professores podem precisar de suporte para situações como problemas com projetor, climatização ou solicitação de materiais.

Em um fluxo tradicional, o professor pode precisar sair da sala ou procurar pessoalmente alguém responsável pelo suporte.

A proposta deste projeto é tornar esse processo mais rápido e organizado por meio da abertura e acompanhamento de solicitações.

## 💡 Solução proposta

O sistema permitirá que uma solicitação seja criada a partir de uma sala e de sua respectiva alocação.

Cada solicitação possui um fluxo de atendimento:

AGUARDANDO → EM ATENDIMENTO → CONCLUÍDO

O sistema também registra os horários de abertura, início do atendimento e conclusão da solicitação.

## ✅ Funcionalidades implementadas

Atualmente, o protótipo em Python permite:

- Criar uma solicitação;
- Selecionar o tipo de problema;
- Validar entradas do usuário;
- Associar a solicitação a professor, turma, disciplina e sala;
- Registrar automaticamente o horário de abertura;
- Alterar o status para "EM ATENDIMENTO";
- Registrar o horário de atendimento;
- Finalizar uma solicitação;
- Registrar o horário de conclusão;
- Impedir transições de estado inválidas;
- Tratar entradas não numéricas utilizando try/except.

## 🧠 Conceitos utilizados

Nesta primeira etapa do projeto foram utilizados:

- Python;
- Funções;
- Dicionários;
- Dicionários aninhados;
- Condicionais;
- Laços de repetição;
- Tratamento de exceções;
- datetime;
- Modelagem de regras de negócio;
- Git e GitHub.

## 🏗️ Estrutura atual dos dados

O protótipo trabalha atualmente com as seguintes entidades:

Professor  
Turma  
Disciplina  
Sala  
Alocação  
Solicitação

Uma alocação relaciona:

Professor + Turma + Disciplina + Sala

Uma solicitação é criada a partir de uma alocação.

## 🚦 Estados da solicitação

### AGUARDANDO

Solicitação criada e ainda não atendida.

### EM ATENDIMENTO

O responsável pelo suporte iniciou o atendimento.

### CONCLUÍDO

O atendimento foi finalizado.

## 🛠️ Tecnologias

### Atualmente

- Python

### Planejadas

- SQLite
- Flask
- HTML
- CSS
- QR Code

## 🗺️ Roadmap

- [x] Modelagem inicial das entidades
- [x] Criação de solicitações
- [x] Controle dos estados da solicitação
- [x] Registro automático de horários
- [x] Validação das entradas
- [x] Tratamento de exceções
- [ ] Persistência de dados com SQLite
- [ ] Cadastro de professores
- [ ] Cadastro de turmas
- [ ] Cadastro de disciplinas
- [ ] Cadastro de salas
- [ ] Gerenciamento de alocações
- [ ] Interface web com Flask
- [ ] Página de solicitação do professor
- [ ] Painel de atendimento
- [ ] Identificação das salas por QR Code
- [ ] Deploy da aplicação

## 📌 Status do projeto

🚧 Em desenvolvimento

A versão atual é um protótipo executado pelo terminal e tem como objetivo validar as principais regras de negócio antes da implementação do banco de dados e da interface web.

## 🔄 Fluxo principal

Professor solicita suporte  
↓  
Solicitação criada  
↓  
AGUARDANDO  
↓  
Atendimento iniciado  
↓  
EM ATENDIMENTO  
↓  
Atendimento finalizado  
↓  
CONCLUÍDO

## 📚 Objetivo de aprendizado

Além de desenvolver uma solução para um problema real, este projeto está sendo utilizado como forma de consolidar conhecimentos de programação, modelagem de dados, desenvolvimento backend, testes e versionamento de código.

O projeto será evoluído gradualmente, mantendo no GitHub o histórico das diferentes etapas de desenvolvimento.

## 👨‍💻 Autor

Kleber Montenegro

GitHub: @MonteKleber
