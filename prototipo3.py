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
#The prompt used in this test is: I would like a summary of the text: '" + brain + "', and we will have a conversation based on the topics from that summary. You will be Morgana, and I will be José. Every conversation you start must begin with 'Morgana:', and you should continue the dialogue until I write 'goodbye'. If there are questions about places or preferences, you can use what you summarized or go for a random choice. Understood?
data = {
    "model": "llama3.1",
    "prompt": "Eu gostaria que fosse feito um resumo do texto: '" + brain + "' e com os assuntos desse resumo iremos conversar, sendo que você será a Morgana e eu serei o José, toda conversa que você inciar deve começar com 'Morgana:' e você deve manter o diálogo até eu escrever tchau, caso haja perguntas sobre locais ou gostos você pode utilizar o que você resumiu ou ir para o aleatório, entendeu?",
    "stream": False,
    "context": [1,2,3] 
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
            data["context"] = response["context"]#Mantain a memory of a conversation
            print(actual_response)
        else:
            print("Error:", response.status_code, response.text)
            
#This LLM works with text with a high performance, but the subject limitation is a great problem, maybe the use with a bussines information as code numbers and names can't work. Your prompt must had adaptation for some situations and is necessary use the variable context to maintain the conversation.
#Sometimes, the LLM "forget" the conversation and in this case a regex with response must to be created, comparing the genereted string and checking if the string 'Morgana:' exists in its composition and generated a warning or resend a string warning to LLM.