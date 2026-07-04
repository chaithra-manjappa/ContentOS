"""Groq client."""

from groq import Groq

from app.clients.base_llm import BaseLLM


class GroqClient(BaseLLM):
    """Groq implementation."""

    def __init__(
        self,
        api_key: str,
        model: str,
    ) -> None:

        self._client = Groq(api_key=api_key)
        self._model = model

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self._client.chat.completions.create(
            model=self._model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content.strip()