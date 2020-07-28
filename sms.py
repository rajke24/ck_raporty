from twilio.rest import Client


def send_msg(date, name, no_full, no_leak, no_fum, sum):
    client = Client("ACcaf60ae6f3dbdc0a64b387afc2178904", "4c22e5bfdcf3aa32a7ada744cba33276")
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