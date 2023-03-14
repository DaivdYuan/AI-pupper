from api import *
from constants import *
import os, re

SCRIPT_FOLDER = "outputs"
doc_path = "api.txt"
conversation = []

def save_script(txt):
    index = len(os.listdir(SCRIPT_FOLDER))
    with open(os.path.join(SCRIPT_FOLDER, f"script_{index}.py"), "w") as f:
        # capture parts within ''' '''
        parts = re.findall(r"```(.*?)```", txt, re.DOTALL)
        for part in parts:
            f.write(part)
            f.write("\n")


def main():
    for _, message in enumerate(BASELINE_MESSAGES):
        if _==0:
            with open(doc_path, "r") as f:
                apis = f.read()
            message = message + apis            
        get_response(message, conversation)
        if _>1:
            save_script(conversation[-1]["content"])
    while True:
        message = input("User: ")
        if message == "exit":
            break
        get_response(message, conversation)
        save_conversation(conversation)
        if message == "exit":
            break

if __name__ == "__main__":
    main()