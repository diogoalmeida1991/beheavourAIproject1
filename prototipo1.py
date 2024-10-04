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
#Here is the prompt used and the results is in the end.
#The first prompt used in this test is:
#Response the follow using the database: " + brain
#The second prompt used in this test is:
#Please, we are simulate a convesation, where I am Joseph, and you are Maria. Answer 
#the question I will be asking, using the follow database: 
data = {
    "model": "phi3",
    "prompt": "Por favor, simularemos uma conversa, onde eu sou José, e você é Maria. Responda as perguntas que eu for fazendo, usando a seguinte base de dados: " + brain,
    "stream": False
}
response = requests.post(url, headers=headers, data=json.dumps(data)) #the dictionary was send to the server
result = json.loads(response.text)#the model response was sended to variable result

#The follow line is a debug with the result, whether this was a success case, this line can to be commented: 
print(result["response"])

#In follow line, is wrote "I am in test, do ask me something?", in literal translate.
print("Eu estou em testes, me pergunte algo?")

#The loop with interation with the user
while True:
    data["prompt"] = input()#User do the ask
    if(data["prompt"] == ""): #Ignore void strings (this can to be used to avoid injection attacks)
        print("Digite uma pergunta valida")
    else:
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:#If the response was 200 (success) do:
            response = json.loads(response.text)
            actual_response = response["response"]
            print(actual_response)
        else:
            print("Error:", response.status_code, response.text)
            
#The first prompt doesn't understand the request.
#The second, has the same trouble than first.