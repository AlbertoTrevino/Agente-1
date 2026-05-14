# Agente-1

Estructura mínima para crear un agente en **Python** usando el **SDK de Claude (Anthropic)**.

## Estructura

```text
.
├── agente/
│   ├── __init__.py
│   └── main.py
├── .env.example
├── requirements.txt
└── README.md
```

## Instalación

Requiere **Python 3.10+**.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuración

1. Copia `.env.example`:
   ```bash
   cp .env.example .env
   ```
2. Configura `ANTHROPIC_API_KEY`.
3. (Opcional) Define `CLAUDE_MODEL`.

## Uso

```bash
python -m agente.main "Hola Claude, ¿puedes presentarte?"
```
