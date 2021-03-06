from twilio.rest import Client
import os
        

def send_msg(day_info):
    twillio_sid = os.environ.get('TWILIO_SID')
    twillio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client("sid", "auth token")

    msg= f"""
Centrum klimatyzacji Kalisz
{day_info['date']}
{day_info['no_fum']}x odgrzybianie - 50 zł
{day_info['no_leak']}x nieszczelność - 70 zł
{day_info['no_full_set']}x komplet - 200 zł"""

    for key, val in day_info['random_sets'].items():
        msg += '\n'
        msg += f'{val}x komplet - {key} zł'

    msg += f"""\n
Suma: {day_info['money_earned']} zł
Godziny pracy: {day_info['worker_name']} 10-18
         """
    client.messages.create(to="receiver",
                       from_="your phone number",
                       body=msg)