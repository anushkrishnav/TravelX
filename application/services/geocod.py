from radar import RadarClient
from config import Config
# initialize client with your project's secret key

radar = RadarClient(Config.RSECRET_KEY)


def geocode(addr):

    address = radar.geocode.forward(query="20 jay st brooklyn")[0]
    return[f"{address.latitude}, {address.longitude}"]
