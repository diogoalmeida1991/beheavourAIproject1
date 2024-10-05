import requests
import json
import re

#This is only a test, use to study human beaheavor, historical personalities or reduce the human workload.
#It was used the portuguese language.
#Machines don't substitute humans, machines give more leisure time to humans. 
#Make download of Ollama in https://ollama.com/, install it and it to be opened in your system tray.

url = "http://localhost:11434/api/generate" #With Ollama opened use your localhost (127.0.0.1) port 11434 to host it.

headers = {
    "Content-Type": "application/json" #This is API json comunication
}
#We need load the "brain" of the system, the "brain" can to be a autobiography, social network posts of a person or a text.

brain = open('brain.txt', encoding = 'utf-8', errors = 'ignore').read()
brain = re.sub(r'\n', ' ', brain)

#Create a dictionary with the model, prompt and do stream with false attribute.
#In this case I use a manual interpretation
data = {
    "model": "llama3",
    "prompt": "Eu gostaria de simular uma conversa com você, eu sou José e você é a Maria. E você como maria terá um texto como base, preste atenção, segue o texto:" + brain,
    "stream": False
}
"""response = requests.post(url, headers=headers, data=json.dumps(data)) #the dictionary was send to the server
result = json.loads(response.text)#the model response was sended to variable result

#The follow line is a debug with the result, whether this was a success case, this line can to be commented: 
print(result["response"])"""

#In follow line, is wrote "I am in test, do ask me something?", in literal translate.
print("Eu estou em testes, me pergunte algo?")

#The loop with interation with the user
while True:
    data["prompt"] = input()#User do the ask
    if(data["prompt"] == ""): #Ignore void strings (this can to be used to avoid injection attacks)
        print("Digite uma pergunta valida")
    elif(data["prompt"] == "brain"):
        data["prompt"] = "'" + brain + "'"
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:#If the response was 200 (success) do:
            response = json.loads(response.text)
            actual_response = response["response"]
            print(actual_response)
        else:
            print("Error:", response.status_code, response.text)
    else:
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:#If the response was 200 (success) do:
            response = json.loads(response.text)
            actual_response = response["response"]
            print(actual_response)
        else:
            print("Error:", response.status_code, response.text)
            
#This LLM is perfect for dialogues with a subject or situation, but don't work with texts.