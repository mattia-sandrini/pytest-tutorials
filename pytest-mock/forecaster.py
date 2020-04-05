class WeatherService:
    def barometer(self):
        # Some unpredictable result (live weather)
        pass


class Forecaster:
    def __init__(self, weather_service):
        self.weather_service = weather_service

    def forecast(self):
        reading = self.weather_service.barometer()
        forecasts = dict(rising="Going to rain", falling="Looks clear")
        return forecasts[reading]
