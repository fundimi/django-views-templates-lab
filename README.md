# Online Course Django App

Aplicação web desenvolvida com Django para praticar conceitos de desenvolvimento full-stack, incluindo views, templates, rotas, ORM, class-based views, generic views e autenticação de usuários.

O projeto simula uma plataforma simples de cursos online, permitindo visualizar cursos, acessar detalhes, simular matrícula e gerenciar autenticação de usuários com login, logout e cadastro.

## Tecnologias usadas

- Python 3.11
- Django
- SQLite
- HTML
- CSS
- Git e GitHub

## Funcionalidades

- Listagem de cursos populares
- Exibição de imagem, nome, descrição e número de matrículas
- Página de detalhes do curso
- Exibição de lições relacionadas ao curso
- Simulação de matrícula em cursos
- Atualização do número de matrículas no banco de dados
- Login de usuários
- Logout de usuários
- Cadastro de novos usuários
- Exibição condicional de informações com base no usuário autenticado
- Integração com o Django Admin

## Conceitos praticados

### Views e Templates

- Function-Based Views
- Renderização de templates com `render()`
- Uso de contexto para enviar dados para o template
- Uso de variáveis, condicionais e loops nos templates
- Uso de `{% csrf_token %}`
- Uso de `{% url %}` para resolver rotas pelo nome
- Uso de arquivos estáticos com CSS

### Class-Based Views e Generic Views

- Uso de `View`
- Uso de `generic.ListView`
- Uso de `generic.DetailView`
- Método `get()`
- Método `post()`
- Método `get_queryset()`
- Uso de `.as_view()` nas rotas
- Uso de `pk` como parâmetro de URL

### Autenticação

- Criação de superusuário com `createsuperuser`
- Login pelo Django Admin
- Login pela interface da aplicação
- Logout pela interface da aplicação
- Cadastro de novos usuários
- Uso de `request.user`
- Uso de `user.is_authenticated`
- Uso de `authenticate()`, `login()` e `logout()`
- Uso do model `User`
- Sessões e cookies de autenticação

## Fluxo principal da aplicação

```text
Usuário acessa /onlinecourse/
        ↓
Django encontra a rota em onlinecourse/urls.py
        ↓
A view busca os cursos no banco de dados
        ↓
Os dados são enviados para o template
        ↓
O template renderiza a página HTML
        ↓
O navegador exibe a lista de cursos
```

## Fluxo de matrícula

```text
Usuário clica em Enroll
        ↓
Formulário envia uma requisição POST
        ↓
A view EnrollView busca o curso pelo pk
        ↓
O campo total_enrollment é incrementado
        ↓
O curso é salvo no banco
        ↓
Usuário é redirecionado para a página de detalhes
```

## Fluxo de autenticação

```text
Usuário acessa a página principal
        ↓
Template verifica user.is_authenticated
        ↓
Se estiver autenticado:
    mostra nome do usuário e opção Logout

Se não estiver autenticado:
    mostra Visitor com opções Login e Signup
```

## Estrutura do projeto

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
│   │   └── onlinecourse/
│   │       ├── course_list.html
│   │       ├── course_detail.html
│   │       ├── user_login.html
│   │       └── user_registration.html
│   ├── static/
│   └── migrations/
└── static/
```

## Principais arquivos

### `onlinecourse/views.py`

Contém as views responsáveis por processar requisições, buscar dados no banco, autenticar usuários e retornar respostas HTTP.

Principais views:

- `CourseListView`
- `CourseDetailsView`
- `EnrollView`
- `login_request`
- `logout_request`
- `registration_request`

### `onlinecourse/urls.py`

Define as rotas do app `onlinecourse`.

Rotas principais:

```text
/onlinecourse/
/onlinecourse/course/<pk>/
/onlinecourse/course/<pk>/enroll/
/onlinecourse/login/
/onlinecourse/logout/
/onlinecourse/registration/
```

### `onlinecourse/templates/onlinecourse/`

Contém os templates HTML renderizados pelo Django.

Principais templates:

- `course_list.html`
- `course_detail.html`
- `user_login.html`
- `user_registration.html`

### `db.sqlite3`

Banco de dados SQLite usado no ambiente local de desenvolvimento.

Neste projeto, ele armazena dados de cursos, lições, usuários, sessões e autenticação.

## Como rodar o projeto localmente

Clone o repositório:

```powershell
git clone URL_DO_REPOSITORIO
cd NOME_DA_PASTA
```

Crie o ambiente virtual:

```powershell
py -3.11 -m venv djangoenv
```

Ative o ambiente virtual:

```powershell
.\djangoenv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a ativação, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\djangoenv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

Aplique as migrations:

```powershell
python manage.py migrate
```

Crie um superusuário:

```powershell
python manage.py createsuperuser
```

Rode o servidor local:

```powershell
python manage.py runserver
```

Acesse a aplicação:

```text
http://127.0.0.1:8000/onlinecourse/
```

Acesse o painel administrativo:

```text
http://127.0.0.1:8000/admin/
```

## Comandos úteis

Verificar problemas no projeto:

```powershell
python manage.py check
```

Criar migrations:

```powershell
python manage.py makemigrations
```

Aplicar migrations:

```powershell
python manage.py migrate
```

Rodar servidor:

```powershell
python manage.py runserver
```

Criar superusuário:

```powershell
python manage.py createsuperuser
```

## Aprendizados principais

Este projeto consolidou o fluxo completo de uma aplicação Django:

```text
URL → View → Model/Database → Context → Template → HTML Response
```

Também foi praticada a evolução entre diferentes formas de escrever views:

```text
Function-Based View → Class-Based View → Generic View
```

Além disso, o projeto introduziu o sistema nativo de autenticação do Django, incluindo criação de usuários, login, logout, sessões e uso do objeto `request.user`.

## Status do projeto

Projeto desenvolvido para fins educacionais e prática de conceitos fundamentais do Django.