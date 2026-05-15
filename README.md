# ProfChoice.IA

**Conversas inteligentes. Futuros personalizados.**

ProfChoice.IA é uma plataforma web de orientação vocacional baseada em Inteligência Artificial, desenvolvida no âmbito da Prova de Aptidão Profissional (PAP). O objetivo principal da aplicação é ajudar utilizadores a descobrirem o seu perfil profissional através de conversas dinâmicas e análises personalizadas baseadas no modelo psicológico RIASEC.

A aplicação combina tecnologias modernas de desenvolvimento web com modelos de IA generativa, permitindo criar uma experiência mais humana, interativa e adaptativa quando comparada com questionários vocacionais tradicionais.

---

# Funcionalidades

* Sistema de autenticação com Firebase Authentication
* Conversas persistentes guardadas na cloud
* Integração com Inteligência Artificial através da OpenRouter API
* Geração dinâmica de perguntas vocacionais
* Relatórios personalizados baseados no modelo RIASEC
* Armazenamento de resultados no Firestore
* Interface moderna e responsiva
* Gestão de histórico de chats
* Renomear e apagar conversas
* Eliminação de resultados guardados
* Visualização gráfica dos resultados RIASEC

---

# Tecnologias Utilizadas

## Frontend

* React
* Vite
* React Router DOM
* Recharts

## Backend

* Node.js
* Express.js

## Base de Dados e Autenticação

* Firebase Authentication
* Cloud Firestore
* Firebase Hosting

## Inteligência Artificial

* OpenRouter API
* Modelos GPT

## Controlo de Versões

* Git
* GitHub


---

# Funcionamento da Aplicação

O utilizador começa por criar conta ou iniciar sessão na plataforma através do Firebase Authentication. Após autenticação, pode iniciar uma conversa com a IA vocacional.

Durante a conversa, o backend envia o histórico da interação para a OpenRouter API, onde um modelo de Inteligência Artificial analisa as respostas e gera perguntas personalizadas de forma dinâmica.

Após um determinado número de respostas, o sistema gera automaticamente um relatório RIASEC detalhado, contendo:

* Perfil dominante
* Ranking completo RIASEC
* Relatório psicológico personalizado
* Áreas recomendadas
* Cursos sugeridos
* Profissões compatíveis

Todos os resultados ficam armazenados no Firestore, permitindo acesso posterior.

---

# Segurança

O projeto implementa vários mecanismos de segurança, incluindo:

* Autenticação de utilizadores
* Proteção de rotas privadas
* Utilização de variáveis de ambiente
* Separação entre frontend e backend
* Armazenamento seguro na cloud
* Ocultação de chaves API

Por razões de segurança, o ficheiro `.env` não se encontra incluído publicamente no repositório.

---

# Inteligência Artificial

A Inteligência Artificial representa o núcleo principal do projeto.

Ao contrário de sistemas tradicionais baseados em perguntas fixas, a aplicação utiliza IA generativa para adaptar dinamicamente a conversa ao perfil do utilizador.

Através de prompts estruturados, o sistema consegue:

* Fazer perguntas contextualizadas
* Evitar repetições
* Analisar padrões de personalidade
* Gerar relatórios personalizados
* Interpretar perfis RIASEC

---

# Objetivos do Projeto

* Desenvolver uma plataforma moderna de orientação vocacional
* Integrar Inteligência Artificial num sistema real
* Criar uma experiência personalizada e dinâmica
* Aplicar conhecimentos de frontend e backend
* Implementar persistência de dados na cloud
* Desenvolver uma arquitetura modular e escalável

---

# Dificuldades Encontradas

Durante o desenvolvimento surgiram vários desafios técnicos, especialmente relacionados com:

* Integração da IA com o frontend
* Estruturação de prompts eficazes
* Gestão do contexto das conversas
* Persistência de dados em tempo real
* Organização da arquitetura do projeto

Inicialmente o projeto utilizava Flask + React, mas posteriormente a arquitetura foi alterada para uma stack totalmente JavaScript utilizando Node.js + Express, permitindo maior consistência tecnológica e melhor integração entre frontend e backend.

---


## Instalar dependências

### Frontend

```bash
cd react
npm install
```

### Backend

```bash
cd api-server
npm install
```

---

# Executar o Projeto

## Frontend

```bash
npm run dev
```

## Backend

```bash
node server.js
```

---

# Autora

**Lara Pires**

Projeto desenvolvido no âmbito da Prova de Aptidão Profissional (PAP).

---

# Licença

Este projeto foi desenvolvido para fins académicos e edu
