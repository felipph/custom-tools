FROM python:3.12-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    TZ=America/Sao_Paulo \
    PATH="$PATH:/runtime/bin" \
    PYTHONPATH="$PYTHONPATH:/runtime/lib/python3.12/site-packages"


WORKDIR /app
RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --only main


RUN useradd -m appuser && chown appuser:appuser /app
USER appuser

ENV PATH="$PATH:/home/appuser/.local/bin/"

COPY --chown=appuser ["custom_tools", "/app"]

EXPOSE 3001

CMD python api.py


