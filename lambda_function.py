import requests
import logging

import json

def get_logger(logger_name):
    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)
    root = logging.getLogger(name=logger_name)
    root.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    root.addHandler(stream_handler)
    return root


def lambda_handler(event, context):

    logging.getLogger().setLevel(logging.INFO)

    logging.info(get_logger('holi'))

    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":"MSFT","datatype":"json","output_size":"compact"}

    headers = {
        "X-RapidAPI-Key": "89bc9142damsh5d187bc9020f7e6p180050jsnb8ffa5f5755b",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }
    logging.warning('Watch out!')

    response = requests.request("GET", url, headers=headers, params=querystring)
    

    
    return {
        'statusCode': 200,
        'body': json.dumps(logging.info(get_logger(response.text)))
    }

