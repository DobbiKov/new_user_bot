from time import sleep
import openai
import os

async def chatgpt_handler(client, message):
    text = message.text.split("#chatgpt ")[-1]
    new_mess = await client.send_message(message.chat.id, "Please, wait...")

    openai.api_key = os.getenv("CHATGPTAPIKEY")

    # Use GPT-3 to generate text
    prompt = text
    model = "text-davinci-003"
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the generated text
    response = completions.choices[0].text
    await client.send_message(message.chat.id, response)
    try:
        await client.delete_messages([str(new_mess.message_id)])
    except:
        pass