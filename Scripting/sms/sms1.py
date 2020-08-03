from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC63700b5a646245b3a451f8bb3e8d8fd6"
auth_token = "da00fa6a36be7be2e09f8652cdf34878"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+5930983200592",
    from_="+12034336075",
    body="Hello there!")