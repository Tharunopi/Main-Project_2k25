from dao.SendSMSImpl import SendSMSImpl

msgSender = SendSMSImpl()

code = msgSender.sendMsg()
print(code)