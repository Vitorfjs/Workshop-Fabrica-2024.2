# 🚀 Projeto Django: API de Personagens Star Wars

Este é um projeto Django que consiste em um aplicativo que utiliza a estrutura de viewsets Django REST Framework para exibir dados e realizar outras operações CRUD. O projeto consome dados da Star Wars API (SWAPI) para gerenciar informações sobre personagens do universo Star Wars. A API permite listar, filtrar, e sincronizar dados desses personagens em um banco de dados local.

## 🌟 Funcionalidades

- **Listagem de Personagens:** Exibe uma lista de personagens obtidos da SWAPI, com informações detalhadas como altura, massa, cor dos olhos, etc.🧑‍🚀
- **Sincronização de Dados:** A API sincroniza automaticamente os dados com a SWAPI quando a listagem de personagens é acessada.🔄
- **Filtragem de Personagens:** Permite filtrar personagens por nome.🔍
- **Autenticação JWT:** A API utiliza JWT para autenticação, permitindo que os usuários obtenham e renovem tokens de acesso.🔐

## 🛠️ Tecnologias Utilizadas

- **Django:** Framework web utilizado para construir a aplicação. 🐍
- **Django REST Framework:** Biblioteca para a construção de APIs RESTful em Django. 🔧
- **SWAPI (Star Wars API):** API externa usada para obter dados dos personagens. 🌌
- **JWT (JSON Web Token):** Utilizado para autenticação e autorização. 🛡️

## 🛠️ Instalação e Configuração do Projeto 

Siga os passos abaixo para configurar e executar o projeto localmente.

### 🔄 1. Clonar o Repositório

Primeiro, clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/Vitorfjs/Workshop-Fabrica-2024.2.git
cd Workshop-Fabrica-2024.2
```
### 🧩 2. Criar e Ativar o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```
Ative o Ambiente Virtual:

- **No macOS/Linux:**

```bash
source venv/bin/activate
```

- **No Windows:**

```bash
venv\Scripts\activate
```

### 📦 3. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## 🔄 4. Aplicar as Migrações

Aplique as migrações para configurar o banco de dados:

```bash
python manage.py makemigrations
```

Depois:

```bash
python manage.py migrate
```

### 👤 5. Criar um Superusuário

Crie um superusuário para acessar a interface administrativa do Django:

```bash
python manage.py createsuperuser
```

### 🚀 6. Executar o Servidor de Desenvolvimento

Por fim, inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

## Uso da API

### 🔑 Autenticação

#### 📥 1. Obter Token de Acesso

```bash
POST /api/token/
```
Envie as credenciais (username e password) para obter um token JWT.

#### 🔄 2. Renovar Token de Acesso

```bash
POST /api/token/refresh/
```
Envie o token de refresh para obter um novo token de acesso.

### 📋 Endpoints Disponíveis

- Listar Personagens:

```bash
GET /api/characters/
```
Exibe uma lista de personagens do banco de dados sincronizado com a SWAPI.

- Filtrar Personagens por Nome:
  
```bash
GET /api/characters/?name=<nome>
```
Filtra personagens que contenham o <nome> especificado.

- Detalhar um Personagem:

```bash
GET /api/characters/<id>/
```
Retorna os detalhes de um personagem específico com base no seu <id>.

- Criar um Novo Personagem:

```bash
POST /api/characters/
```
Cria um novo personagem no banco de dados local. Observação: A criação de personagens pode ser restrita dependendo da lógica implementada.

- Atualizar um Personagem:

```bash
PUT /api/characters/<id>/
```
Atualiza completamente as informações de um personagem específico.
```bash
PATCH /api/characters/<id>/
```
Atualiza parcialmente as informações de um personagem específico.

- Deletar um Personagem:

```bash
DELETE /api/characters/<id>/
```
Remove um personagem específico do banco de dados.
