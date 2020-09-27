from twilio.rest import Client

# Your Account SID 
account_sid = "fill in your"
# Your Auth Token 
auth_token  = "fill in your"
#Your Twilio number
twilio_number = "fill in your"
#creating the client
client = Client(account_sid, auth_token)


class TwilioHelper:
    def send(self, content, targetPhone):
        #send simple sms message
        message = client.messages.create(
        to=targetPhone, 
        from_=twilio_number,
        body=content)
        print("message was sent sucssesfully")
    
    def multipuleSend(self, content, targetPhones):
        #send massage to couple of people
        for phone in targetPhones:
            self.send(content, phone)
            print("message was sent sucssesfully")
        print("all messages were sent sucssesfully")

    def call(self, targetPhone):
        #call target phone
        call = client.calls.create(
            to = targetPhone,
            from_ =twilio_number,
            url =  "https://demo.twilio.com/docs/voice.xml"
        )
    
    def getMessageHistory(self, lim = 25):
        return client.api.messages.stream(limit = lim)
    
    def getCallsHistory(self, lim = 25):
        return client.calls.stream(limit = lim)
    
tw = TwilioHelper

tw.call(tw, '')

