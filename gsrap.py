import gspread
from oauth2client.service_account import ServiceAccountCredentials

def insert_data(data):
    scope = [
        "https://spreadsheets.google.com/feeds",
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
        ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\jarek\OneDrive\Dokumenty\learning\Projects\python\ck_raporty\client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('CK_raporty').sheet1
    
    row_num = 2
    data['random_sets'] = '\n'.join([f'{no}x komplet - {price} zł' for price, no in data['random_sets'].items() ])
    data = list(data.values())
    sheet.insert_row(data, row_num)

