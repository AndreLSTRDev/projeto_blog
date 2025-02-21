# Projeto Blog Django

Este projeto consiste em um sistema de blog desenvolvido com o framework Django, com foco na implementação do back-end e da API RESTful.

## Funcionalidades

* **Posts:**
    * Criação, edição e exclusão de posts, incluindo título, conteúdo, categoria e tags.
    * Listagem de posts com paginação e filtragem por categoria e tags.
    * Visualização de posts individuais.
* **Categorias:**
    * Criação, edição e exclusão de categorias.
    * Listagem de categorias.
* **Tags:**
    * Criação, edição e exclusão de tags.
    * Listagem de tags.
* **Usuários:**
    * Gerenciamento de usuários (autenticação e autorização).
    * Painel administrativo para gerenciamento de usuários.
* **API RESTful:**
    * API para acesso aos dados do blog, incluindo posts, categorias e tags.
    * Endpoints para criação, edição e exclusão de posts, categorias e tags.

## Tecnologias Utilizadas

* Python (versão 3.9 ou superior)
* Django (versão 4.0 ou superior)
* Django REST Framework
* Banco de dados SQLite (padrão)

## Instalação

1. Clone este repositório:

   ```bash
   git clone [https://github.com/AndreLSTRDev/projeto_blog.git](https://github.com/AndreLSTRDev/projeto_blog.git)
Crie um ambiente virtual (recomendado):

Bash

cd projeto_blog
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
Instale as dependências:

Bash

pip install -r requirements.txt
Migre o banco de dados:

Bash

python manage.py makemigrations
python manage.py migrate
Execução
Inicie o servidor de desenvolvimento:

Bash

python manage.py runserver
Acesse o painel administrativo em:

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
A API RESTful estará disponível em:

[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)
Como usar a API
A API RESTful oferece os seguintes endpoints:

Posts:
GET /api/posts/: Lista todos os posts.
GET /api/posts/{id}/: Detalhes de um post específico.
POST /api/posts/: Cria um novo post.
PUT /api/posts/{id}/: Atualiza um post existente.
DELETE /api/posts/{id}/: Exclui um post.
Categorias:
GET /api/categorias/: Lista todas as categorias.
GET /api/categorias/{id}/: Detalhes de uma categoria específica.
POST /api/categorias/: Cria uma nova categoria.
PUT /api/categorias/{id}/: Atualiza uma categoria existente.
DELETE /api/categorias/{id}/: Exclui uma categoria.
Tags:
GET /api/tags/: Lista todas as tags.
GET /api/tags/{id}/: Detalhes de uma tag específica.
POST /api/tags/: Cria uma nova tag.
PUT /api/tags/{id}/: Atualiza uma tag existente.
DELETE /api/tags/{id}/: Exclui uma tag.
Contribuição
Contribuições são sempre bem-vindas. Sinta-se à vontade para abrir issues e enviar pull requests.
