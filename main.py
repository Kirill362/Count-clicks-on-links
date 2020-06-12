import requests
import os


API_BITLY_TOKEN = os.getenv("API_BITLY_TOKEN")


def create_bitlink(url, token):
  headers = {"Authorization": "Bearer {}".format(token)}
  payload = {'long_url': url}
  response = requests.post("https://api-ssl.bitly.com/v4/shorten", headers=headers, json=payload)
  response.raise_for_status()
  return response.json()['id']


def count_clicks(url, token):
  headers = {"Authorization": "Bearer {}".format(token)}
  request_url = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(url)
  response = requests.get(request_url, headers=headers)
  response.raise_for_status()
  return response.json()['total_clicks']


if __name__ == '__main__':
  your_url = input()
  try:
    if your_url.startswith("http"):
      print(create_bitlink(your_url, API_BITLY_TOKEN))
    else:
      print(count_clicks(your_url, API_BITLY_TOKEN))
  except requests.exceptions.HTTPError:
    print("Ошибка: ваша ссылка не работает")