# Blog PMR3304 — Segunda entrega de laboratório

Aplicação CRUD em Django (blog) com comentários e categorias.

## Rodar localmente (Windows / PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata dados
python manage.py runserver
```

Acesse http://127.0.0.1:8000/ (blog) e http://127.0.0.1:8000/admin/ (administrador).

O comando `loaddata dados` popula o banco com 3 categorias, 3 posts, 5 comentários
e 2 usuários de exemplo (`ana` e `bruno`), atendendo à parte 4 do enunciado.
Para comentar pelo site, faça login no admin com o superusuário.

## Estrutura

- `config/` — configurações do projeto (`settings.py`, `urls.py`)
- `blog/models.py` — modelos `Post`, `Comment` e `Category`
- `blog/views.py` — views (o histórico Git tem as 3 versões pedidas)
- `templates/base.html` — template base
- `blog/templates/blog/` — templates do app
- `blog/fixtures/dados.json` — dados de exemplo
- `sql/queries.sql` — queries da parte 4

## URLs

| Nome | Caminho |
|---|---|
| `blog:post_list` | `/` |
| `blog:post_detail` | `/post/<id>/` |
| `blog:post_create` | `/post/create/` |
| `blog:post_update` | `/post/<id>/update/` |
| `blog:post_delete` | `/post/<id>/delete/` |
| `blog:comment_create` | `/post/<id>/comment/` |
| `blog:category_list` | `/categories/` |
| `blog:category_detail` | `/categories/<id>/` |

## Deploy no Render

1. Suba o repositório no GitHub.
2. No Render, crie um **Web Service** ligado ao repositório.
3. Build Command: `./build.sh`
4. Start Command: `gunicorn config.wsgi:application`
5. Variáveis de ambiente:
   - `PYTHON_VERSION` = `3.12.7`
   - `DEBUG` = `False`
   - `SECRET_KEY` = uma chave longa e aleatória
   - `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD` (opcional, cria o admin no deploy)
