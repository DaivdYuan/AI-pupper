from constants import *
from api_key import *
import openai

openai.api_key = API_KEY

def clean_print(text):
    # remove starting and ending blank characters and quotes
    text.content = text.content.strip().strip('"')
    print(text.content)

def process_result(result, conversation = [], save = True):
    msg = result.choices[0].message
    clean_print(msg)
    if save:
        conversation.append(msg)
    return msg

def make_message(message, role = "user"):
    return {"role": role, "content": message}

def get_response(message, conversation = []):
    conversation.append(make_message(message))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=conversation,
    )
    return process_result(completion, conversation)

def save_conversation(conversation, filename = "output.txt"):
    with open(filename, "w") as f:
        for msg in conversation:
            f.write(msg["role"] + ": " + msg["content"] + "\n")
    

