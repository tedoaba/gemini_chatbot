import gradio as gr

from src.chatbot import Chatbot


def chat(message, history):
    """Processes the chat message and returns the chatbot response."""
    chatbot = Chatbot()

    if not history:  
        chatbot.clear_history()
    else:
        for user_message, bot_message in history:
            chatbot.chat_history.append({"role": "user", "parts": [user_message]})
            chatbot.chat_history.append({"role": "model", "parts": [bot_message]})


    response = chatbot.process_message(message)

    return response


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def respond(message, chat_history):
        bot_message = chat(message, chat_history)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.queue().launch(share=True)