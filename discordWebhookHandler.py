import requests

baseURL = "https://discord.com/api/webhooks/"

class webhook:
    def __init__(self, webhookURL):
        self.webhookURL = webhookURL
        response = requests.get(webhookURL)
        
        self.jsonResponse = response.json()
        self.webhookToken, self.webhookID = self.jsonResponse["token"], self.jsonResponse["id"]

    def delete(self):
        return requests.delete(f"{baseURL}{self.webhookID}/{self.webhookToken}")
    
    def sendMessage(self, message):
        return requests.post(self.webhookURL, json={"content":message})
    
    def modifyName(self, newName):
        return requests.patch(f"{baseURL}{self.webhookID}/{self.webhookToken}", json={"name": newName})

    def modifyAvatar(self, avatar):
        return requests.patch(f"{baseURL}{self.webhookID}/{self.webhookToken}", json={"avatar": avatar})

