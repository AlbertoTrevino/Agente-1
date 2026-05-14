import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def main() -> None:
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hola, ¿estás funcionando?"}
        ],
    )
    print(message.content[0].text)


if __name__ == "__main__":
    main()
