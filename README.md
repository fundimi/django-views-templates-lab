# Django Views and Templates Lab

Projeto desenvolvido durante prática de Django com foco em views, templates, rotas, formulários, redirecionamento e estilização com CSS.

## O que o projeto faz

A aplicação exibe uma lista de cursos populares, permite simular matrícula em um curso e redireciona o usuário para uma página de detalhes com as lições do curso.

## Tecnologias usadas

- Python
- Django
- SQLite
- HTML
- CSS

## Funcionalidades praticadas

- Criação de views baseadas em função
- Renderização de templates HTML
- Uso de contexto com `render()`
- Busca de dados com Django ORM
- Ordenação de cursos por número de matrículas
- Formulário com método POST
- Proteção com CSRF token
- Redirecionamento com `HttpResponseRedirect`
- Uso de `reverse()`
- Página de detalhes de curso
- Exibição de relacionamento Course → Lesson
- Uso de arquivos estáticos CSS

## Como rodar o projeto localmente

Clone ou baixe o projeto e acesse a pasta onde está o arquivo `manage.py`.

Crie um ambiente virtual:

```powershell
py -3.11 -m venv djangoenv

Ative o ambiente virtual:

.\djangoenv\Scripts\Activate.ps1

## Caso o PowerShell bloqueie a ativação, use:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\djangoenv\Scripts\Activate.ps1

Instale as dependências:

pip install -r requirements.txt

Aplique as migrations:

python manage.py migrate

Rode o servidor:

python manage.py runserver

Acesse no navegador:

http://127.0.0.1:8000/onlinecourse/
Estrutura principal do projeto
lab3_template/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── onlinecourse/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   ├── static/
│   └── migrations/
└── static/
Principais arquivos
onlinecourse/views.py

Contém as funções responsáveis por processar as requisições HTTP, buscar dados no banco e retornar páginas HTML.

Exemplos de views usadas no projeto:

popular_course_list
enroll
course_details
onlinecourse/urls.py

Define as rotas do app onlinecourse.

Exemplos:

/onlinecourse/
/onlinecourse/course/<id>/
/onlinecourse/course/<id>/enroll/
onlinecourse/templates/

Contém os arquivos HTML renderizados pelo Django.

Principais templates:

course_list.html
course_detail.html
db.sqlite3

Banco de dados SQLite usado no projeto.

Neste lab, o banco contém dados de cursos e lições usados para testar a aplicação.

Resultado da prática

Ao final da prática, a aplicação permite visualizar cursos, clicar em Enroll, atualizar o número de matrículas e acessar a página de detalhes do curso com suas respectivas lições.

Aprendizado

Esta prática ajudou a entender como o Django conecta rotas, views, templates, models e banco de dados para criar páginas web dinâmicas.