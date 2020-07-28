from twilio.rest import Client


def send_msg(date, name, no_full, no_leak, no_fum, sum):
    client = Client("your account sid", "auth token")
    msg= f"""
Centrum klimatyzacji Kalisz
{date}
{no_fum}x odgrzybianie - 50 zł
{no_leak}x nieszczelność - 70 zł
{no_full}x komplet - 200 zł

Suma: {sum}
Godziny pracy: {name} 10-18
         """
    client.messages.create(to="+48503525328",
                       from_="+18137564411",
                       body=msg)
