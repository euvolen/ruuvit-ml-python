from influxdb import InfluxDBClient

def get_userdata(link):
    with InfluxDBClient(link) as client:
        result = client.query('SELECT "data" FROM database').raw
    return result

def erase_db(link):
    with InfluxDBClient(link) as client:
        result = client.drop_database('database')
    return result