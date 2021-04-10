rain = {}

while True:
    city = input("City: ").strip()

    if not city:
        break

    mm_rain = input("Please provide rainfall in mm: ").strip()
    rain[city] = rain.get(city, 0) + int(mm_rain)

for city, mm_rain in rain.items():
    print(f'{city}: {mm_rain}')
