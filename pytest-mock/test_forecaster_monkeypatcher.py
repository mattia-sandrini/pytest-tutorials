import pytest
from mock import Mock
#import monkeypatch
from forecaster_monkeypatch import WeatherService, Forecaster

@pytest.fixture
def mock_ws():
    return Mock(spec=WeatherService)

# spec: This can be either a list of strings or an existing object (a class or instance) that acts as the specification
#       for the mock object. If you pass in an object then a list of strings is formed by calling dir on the object
#       (excluding unsupported magic attributes and methods).
#       Accessing any attribute not in this list will raise an AttributeError.

def test_rain_when_barometer_rising(monkeypatch, mock_ws):
    WS = Mock(return_value=mock_ws)  # WS is a class for which mock_ws is the instance

    # return_value: The value returned when the mock is called. By default this is a new Mock (created on first access).

    monkeypatch.setattr('forecaster_monkeypatch.WeatherService', WS)
    forecaster = Forecaster()
    mock_ws.barometer.return_value = 'rising'
    assert forecaster.forecast() == 'Going to rain'
    # Passes

# From: https://docs.python.org/3/library/unittest.mock.html

# return_value: The value returned when the mock is called. By default this is a new Mock (created on first access).
#               Set this to configure the value returned by calling the mock:
#
#               >>> mock = Mock()
#               >>> mock.return_value = 'fish'
#               >>> mock()
#                   'fish'
#
#               The default return value is a mock object and you can configure it in the normal way:
#               >>> mock = Mock()
#               >>> mock.return_value.attribute = sentinel.Attribute
#               >>> mock.return_value()
#                   <Mock name='mock()()' id='...'>
#               >>> mock.return_value.assert_called_with()
#
#               return_value can also be set in the constructor:
#               >>> mock = Mock(return_value=3)
#               >>> mock.return_value
#                   3
#               >>> mock()
#                   3
