class WeatherService:
    def barometer(self):
        # Some unpredictable result (live weather)
        pass


class Forecaster:
    def __init__(self):
        # Now I can't injec a mock into the constructor!
        self.weather_service = WeatherService()

    def forecast(self):
        reading = self.weather_service.barometer()
        forecasts = dict(rising="Going to rain", falling="Looks clear")
        return forecasts[reading]
