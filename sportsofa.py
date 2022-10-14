# 10 Oct 2022

import http.client

conn = http.client.HTTPSConnection("api.sofascore.com")

payload = ""

headers = {
    'authority': "api.sofascore.com",
    'accept': "*/*",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "max-age=0",
    'if-none-match': "W/^\^43b25d1b69^^",
    'origin': "https://www.sofascore.com",
    'referer': "https://www.sofascore.com/",
    'sec-ch-ua': "^\^Chromium^^;v=^\^106^^, ^\^Google"
    }

conn.request("GET", "/api/v1/sport/football/scheduled-events/2022-10-10", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))