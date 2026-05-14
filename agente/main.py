import os
import sys

try:
    from anthropic import Anthropic
except ImportError:  # pragma: no cover - depende del entorno local
    Anthropic = None


class ClaudeAgent:
    def __init__(self, api_key: str | None = None, model: str | None = None) -> None:
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.model = model or os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-latest")

    def ask(self, prompt: str, max_tokens: int = 512) -> str:
        if not prompt.strip():
            raise ValueError("El prompt no puede estar vacío")
        if Anthropic is None:
            raise RuntimeError("Falta dependencia 'anthropic'. Instala con: pip install -r requirements.txt")
        if not self.api_key:
            raise RuntimeError("Falta ANTHROPIC_API_KEY en variables de entorno")

        client = Anthropic(api_key=self.api_key)
        response = client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
        return "".join(block.text for block in response.content if hasattr(block, "text")).strip()


def main() -> int:
    prompt = " ".join(sys.argv[1:]).strip()
    if not prompt:
        print("Uso: python -m agente.main \"Tu prompt\"")
        return 1

    agent = ClaudeAgent()
    try:
        print(agent.ask(prompt))
        return 0
    except (RuntimeError, ValueError) as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
