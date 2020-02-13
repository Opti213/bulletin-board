#WIP!
<p align="center">
    <em>This is the simplest api for bulletin board via 
        <a href="https://github.com/tiangolo/fastapi" target="_blank">
            FastAPI
            </a>
    </em>
</p>
<p align="center">
<a href="https://github.com/wemake-services/wemake-python-styleguide" target="_blank">
    <img src="https://img.shields.io/badge/style-wemake-000000.svg" alt="Code style">
</a>
</p>

---


## Requirements

* Python 3.8+
* <a href="https://github.com/python-poetry/poetry" target="_blank">Poetry</a>

## Start

To install the dependencies, you need use poetry, which you can install through the pocket manager or directly through pip directly in venv

```bash
poetry install
```

Or no-dev variant for not install dev tools like linters

```bash
poetry install --no-dev
```

You can also user else ASGI server, for production such as <a href="https://gitlab.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.
Just use

```bash
poetry remove uvicorn
poetry add {{youre awesome ASGI server}}
```

## Tools

