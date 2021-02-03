import requests

cities = [i.strip() for i in input().split(',')]
result = ("bla bla", 200.00)

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493" \
                   "-4b70-98ba-98533de7710b&format=json&geocode="

for i in cities:
    response = requests.get(geocoder_request + i)
    if response:
        json_response = response.json()
        name = json_response["response"]["GeoObjectCollection"][
            "metaDataProperty"]["GeocoderResponseMetaData"]["request"]
        pos = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]["Point"]["pos"]
        print(name,pos)
        if float(pos.split()[1]) < result[1]:
            result = name, float(pos.split()[1])
    else:
        print('Something goes wrong :(')

print(result[0])