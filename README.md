# Django Views and Templates Lab

Projeto prático desenvolvido durante um laboratório de Django, com foco em **views**, **templates**, **rotas**, **formulários**, **redirecionamento**, **SQLite** e **estilização com CSS**.

## Sobre o projeto

A aplicação exibe uma lista de cursos populares, permite simular a matrícula em um curso e redireciona o usuário para uma página de detalhes, onde são exibidas as lições relacionadas ao curso selecionado.

Este projeto foi usado como prática para entender como o Django conecta **URL**, **view**, **template**, **model** e **banco de dados** para gerar páginas web dinâmicas.

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
- Formulário com método `POST`
- Proteção de formulário com `{% csrf_token %}`
- Redirecionamento com `HttpResponseRedirect`
- Uso de `reverse()` para resolver URLs pelo nome da rota
- Página de detalhes de curso
- Exibição do relacionamento entre `Course` e `Lesson`
- Uso de arquivos estáticos com CSS

## Como rodar o projeto localmente

Clone o repositório ou baixe o projeto e acesse a pasta onde está o arquivo `manage.py`.

### 1. Criar o ambiente virtual

```powershell
py -3.11 -m venv djangoenv
```

### 2. Ativar o ambiente virtual

```powershell
.\djangoenv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a ativação, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\djangoenv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 4. Aplicar as migrations

```powershell
python manage.py migrate
```

### 5. Rodar o servidor

```powershell
python manage.py runserver
```

### 6. Acessar no navegador

```text
http://127.0.0.1:8000/onlinecourse/
```

## Estrutura principal do projeto

```text
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
```

## Principais arquivos

### `onlinecourse/views.py`

Contém as funções responsáveis por processar as requisições HTTP, buscar dados no banco e retornar páginas HTML.

Views usadas no projeto:

- `popular_course_list`
- `enroll`
- `course_details`

### `onlinecourse/urls.py`

Define as rotas do app `onlinecourse`.

Rotas principais:

```text
/onlinecourse/
/onlinecourse/course/<id>/
/onlinecourse/course/<id>/enroll/
```

### `onlinecourse/templates/`

Contém os arquivos HTML renderizados pelo Django.

Principais templates:

- `course_list.html`
- `course_detail.html`

### `db.sqlite3`

Banco de dados SQLite usado no projeto.

Neste laboratório, o banco contém dados de cursos e lições usados para testar a aplicação.

## Fluxo da aplicação

```text
Usuário acessa /onlinecourse/
        ↓
Django encontra a rota em onlinecourse/urls.py
        ↓
A view popular_course_list busca os cursos no banco
        ↓
O template course_list.html renderiza a lista
        ↓
Usuário clica em Enroll
        ↓
A view enroll atualiza total_enrollment
        ↓
Django redireciona para a página de detalhes do curso
        ↓
A view course_details exibe o curso e suas lições
```

## Resultado da prática

Ao final da prática, a aplicação permite:

- Visualizar cursos cadastrados.
- Ver o número de matrículas de cada curso.
- Clicar em `Enroll`.
- Atualizar o número de matrículas no banco de dados.
- Acessar a página de detalhes do curso.
- Visualizar as lições associadas ao curso.

## Aprendizado

Esta prática ajudou a consolidar como o Django organiza uma aplicação web usando:

- `urls.py` para definir os caminhos da aplicação.
- `views.py` para processar requisições e respostas.
- `models.py` para representar dados do banco.
- Templates HTML para exibir conteúdo dinâmico.
- SQLite como banco de dados local.
- CSS estático para melhorar a apresentação visual.

O principal aprendizado foi entender o fluxo completo:

```text
URL → View → Model/Database → Context → Template → HTML Response
```