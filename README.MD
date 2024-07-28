# Projeto Django com API JWT

Este projeto é uma API desenvolvida com Django que utiliza autenticação JWT. Ele permite registrar usuários, autenticar-se usando JWT e realizar operações CRUD (Criar, Ler, Atualizar, Deletar) com usuários autenticados.

## Pré-requisitos

- Python 3.x
- Git

## Passos para Configurar e Rodar o Projeto

### 1. Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Criar e Ativar um Ambiente Virtual
Crie e ative um ambiente virtual para instalar as dependências do projeto.

Para Windows:

bash
Copiar código
python -m venv venv
venv\Scripts\activate
Para MacOS/Linux:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
3. Instalar Dependências
Instale todas as dependências listadas no arquivo requirements.txt.

bash
Copiar código
pip install -r requirements.txt
4. Configurar o Banco de Dados
Crie e aplique as migrações do banco de dados para configurar o esquema inicial.

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
5. Criar um Superusuário
Crie um superusuário para acessar a interface de administração do Django.

bash
Copiar código
python manage.py createsuperuser
6. Rodar o Servidor de Desenvolvimento
Inicie o servidor de desenvolvimento do Django.

bash
Copiar código
python manage.py runserver