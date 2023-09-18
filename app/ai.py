import openai

from app.database import Database
from app.prompt import CHATBOT_ROLE
from app.settings import settings

database = Database()
ddl = database.get_ddl()


def get_response_openai(prompt: str) -> str:
    """
    Generates a response from OpenAI Chat API based on the given prompt.

    Parameters
    ----------
    prompt : str
        The user's input prompt.

    Returns
    -------
    str
        The generated response from OpenAI Chat API.
    """
    completion = openai.ChatCompletion.create(
        model=settings.OPENAI_MODEL,
        temperature=settings.OPENAI_TEMPERATURE,
        messages=[
            {"role": "system", "content": CHATBOT_ROLE.format(ddl=ddl)},
            {"role": "user", "content": prompt},
        ],
    )
    return completion["choices"][0]["message"]["content"]
