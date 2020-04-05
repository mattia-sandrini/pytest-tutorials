import pytest
from mock import Mock
from forecaster import WeatherService, Forecaster


@pytest.fixture
def mock_ws():
    return Mock(spec=WeatherService)


# def test_rain_when_barometer_rising(mock_ws):
#     forecaster = Forecaster(mock_ws)
#     mock_ws.barometer.return_value = 'rising'
#     assert forecaster.forecast() == 'Going to rain'
#     # Passes
#
# def test_rain_when_barometer_falling(mock_ws):
#     forecaster = Forecaster(mock_ws)
#     mock_ws.barometer.return_value = 'falling'
#     assert forecaster.forecast() == 'Looks clear'
#     # Passes

# Parametrizing the test, this results equivalent to the code above
@pytest.mark.parametrize(
    "reading,expected_forecast",
    [("rising", "Going to rain"), ("falling", "Looks clear")],
)
def test_forecast(reading, expected_forecast, mock_ws):
    forecaster = Forecaster(mock_ws)
    mock_ws.barometer.return_value = reading
    assert forecaster.forecast() == expected_forecast
