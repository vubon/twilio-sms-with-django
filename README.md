# Twilio SMS with Django

You need to install twilio lib by this command. 
```bash
pip install twilio
```
After that call this in your views.py 
```python
from twilio.rest import Client

# your account sid and auth token 
account_sid = 'xxxxxx'
auth_token = 'xxxxxx'

# your twilio phone number and send message number
from_phone = 'xxxxxx'
to_phone = '+8801737388xxx'

client = Client(account_sid, auth_token)
message = client.messages.create(
    to=to_phone,
    from_=from_phone,
    body='your message here'
)

```
That's all. If you will face any problem let me know. I will help you.


