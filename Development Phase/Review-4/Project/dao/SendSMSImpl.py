from dao.SendSMS import SendSMS
import requests

class SendSMSImpl(SendSMS):
    def __init__(self):
        self.url = "https://www.fast2sms.com/dev/bulkV2"
        self.phoneNumber = ["9360496526"]
        self.apiKey = "5symgGpwkfCM8oAvux4rJVLBY0njFUcQRZIP9SO3DEqazT7iN61wui790L8vBHhCVx4egylPSYEJXzjd"

    def sendMsg(self):
        numbers = ",".join(self.phoneNumber)
        
        params = {
            "authorization": self.apiKey,
            "route": "q",
            "message": "Test message",
            "language": "english",
            "flash": "0",
            "numbers": numbers
        }
        
        response = requests.get(self.url, params=params)
        print(response.text)  
        return response.status_code
    
    def addNumber(self, number):
        try:
            self.phoneNumber.append(number)
            return True
        except Exception as e:
            print(e)
            return False

    def deleteNumber(self, number):
        try:
            index = self.phoneNumber.index(number)
            self.phoneNumber.pop(index)
            return True
        except Exception as e:
            print(e)
            return False