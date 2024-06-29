DEFAULT_PASSWORD = '12345678'
DATA_GENERATION_LOCALE = 'ru_RU'
MAIL_RECEIVE_TIMEOUT = 30  # seconds

SOME_SEND_CODE_URl = ''
SOME_CHECK_CODE_URL = ''
SOME_REGISTER_URL = ''
SOME_DATA_TEMPLATE = {
    "email": '',
    "code": '',
    "name": {
        "first_name": "NAME",
        "last_name": "LAST_NAME",
        "middle_name": "MIDDLE_NAME"
    },
    "nickname": "",
    "phone": "",  # changed
    "birth_date": "",  # changed
    "gender": 1,
    "citizenship_id": 222,
    "country_id": 111,
    "role": "SOME_ROLE",
    "educational_institution": None,
    "educational_institution_rf": False,
    "educational_institution_info": {
        "grade": None,
        "post": None,
        "course": None,
        "type": None
    },
    "educational": {
        "name": "undefined",
        "legalAddress": "undefined",
        "countryId": None
    },
    "password": ""  # changed
}

SOME_HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Content-Type': 'application/json',
    'Dnt': '1',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'Omega',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}
