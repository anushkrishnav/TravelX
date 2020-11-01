from radar import RadarClient

# initialize client with your project's secret key
SECRET_KEY = "prj_test_sk_03c606242c4792740ed602a782f59fc681e6cc57"
radar = RadarClient(SECRET_KEY)

address = radar.geocode.forward(query="20 jay st brooklyn")[0]
print(f"{address.latitude}, {address.longitude}")
