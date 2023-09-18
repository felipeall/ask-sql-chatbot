from time import sleep

import gradio as gr

from app.ai import get_response_openai
from app.settings import settings


def user(user_message: str, history: list):
    """
    Handles the user's input message and updates the chat history.

    Parameters
    ----------
    user_message : str
        The user's input message.
    history : list
        The chat history.

    Returns
    -------
    tuple
        An empty string and the updated chat history.
    """
    return "", history + [[user_message, None]]


def bot(history: list):
    """
    Generates the bot's response based on the chat history.

    Parameters
    ----------
    history : list
        The chat history.

    Yields
    ------
    list
        The updated chat history after each character of the bot's response is added.
    """
    bot_message = get_response_openai(prompt=history[-1][0])
    history[-1][1] = ""
    for character in bot_message:
        history[-1][1] += character
        sleep(0.01)
        yield history


with gr.Blocks() as app:
    gr.Markdown("""<h1><center>Ask SQL Chatbot</center></h1>""")
    chatbot = gr.Chatbot(height=650)
    msg = gr.Textbox()
    clear = gr.Button("Clear")
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, chatbot, chatbot)
    clear.click(lambda: None, None, chatbot, queue=False)

app.queue()
app.launch(debug=True, server_port=settings.GRADIO_SERVER_PORT, server_name=settings.GRADIO_SERVER_NAME)
