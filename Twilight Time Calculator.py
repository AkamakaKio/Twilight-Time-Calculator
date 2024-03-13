from datetime import datetime
import ephem

def calculate_twilight(date):
    observer = ephem.Observer()
    observer.lat = '52.5200'  # Latitude of the observer (e.g., Berlin)
    observer.lon = '13.4050'  # Longitude of the observer (e.g., Berlin)
    observer.date = date
    sunset = observer.next_setting(ephem.Sun())
    twilight_civil = observer.next_setting(ephem.Sun(), use_center=True)
    twilight_nautical = observer.next_setting(ephem.Sun(), use_center=True, horizon="-12")
    twilight_astronomical = observer.next_setting(ephem.Sun(), use_center=True, horizon="-18")
    return {
        "Sunset": sunset.datetime(),
        "Civil Twilight": twilight_civil.datetime(),
        "Nautical Twilight": twilight_nautical.datetime(),
        "Astronomical Twilight": twilight_astronomical.datetime()
    }

date = datetime(2024, 2, 14)
twilight_times = calculate_twilight(date)
for event, time in twilight_times.items():
    print(f"{event}: {time}")
