from openai import OpenAI
import keyboard
from langchain_community.chat_message_histories import ChatMessageHistory

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

history = ChatMessageHistory()

while True:

    query = input(
        "\nUser (Enter to Continue || Type 'exit' or press ESC to exit): "
    )

    if keyboard.is_pressed('esc') or query.lower() == 'exit':
        print("\nExiting...")
        print("Program Finished.")
        break

    print("User Input: " + query)
    print('- ' * 50)

    if not query.strip():
        continue

    history.add_user_message(query)

    messages_with_history = []

    for m in history.messages:

        role = "user" if m.type == "human" else "assistant"

        messages_with_history.append({
            "role": role,
            "content": m.content
        })

    stream = client.chat.completions.create(
        model="llama-3.2-3b-instruct",
        messages=messages_with_history,
        stream=True
    )

    full_ai_response = ""

    for chunk in stream:

        if chunk.choices[0].delta.content:

            content = chunk.choices[0].delta.content

            print(content, end="", flush=True)

            full_ai_response += content

    history.add_ai_message(full_ai_response)

    print('\n')
    print('=' * 100)
    print(' ')