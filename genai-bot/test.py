import openai

# Set your OpenAI API key
openai.api_key = "Your OpenAI API key"

#  Creating Message List 
messages= [ {"role": "system", "content": "You are a intelligent assistant."} ]


#Taking Input from the user
while True:
    message = input("User : ")
    if message :
        #If user ask something ,appending that in messages list
        messages.append(
            {"role": "user", "content":message},
        )
        # Interacting with ChatGPT model
        chat = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",messages=messages,temperature=0.5
        )
    # Api return ChatGPT response 
    reply =chat.choices[0].message.content
    print(f"ChatGPT: {reply}")

    #Appending the reply to the message list
    messages.append({"role": "assitant","content" : reply })