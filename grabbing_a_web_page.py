import requests

URL = 'https://www.python.org'

try:
    response = requests.get(URL)
except requests.HTTPError as err:
    print(err)
else:
    page_source = response.text   #  response.content  (binary)
    page_headers = response.headers

    for header, value in page_headers.items():
        print(header, value)
    print('-' * 60)

    print(page_source)

