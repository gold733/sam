from openai import OpenAI

# Create OpenAI client (API key is read from environment variable)
client = OpenAI()

print("🤖 AI Agent is running. Type 'exit' to quit.\n")

conversation = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("AI: Goodbye! 👋")
        break

    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation
    )

    ai_reply = response.choices[0].message.content
    print(f"AI: {ai_reply}\n")

    conversation.append({"role": "assistant", "content": ai_reply})
