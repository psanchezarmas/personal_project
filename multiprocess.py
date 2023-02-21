import sys, os
import zipfile
import requests
from multiprocessing import Pool, cpu_count
from functools import partial
from io import BytesIO
import ipdb

def get_json(stock):
    try:
        #file_name = 'whatever' #url.split("/")[-1]
        url = "https://alpha-vantage.p.rapidapi.com/query"
        querystring = {"interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":str(stock),"datatype":"json","output_size":"compact"}
        headers = {
            "X-RapidAPI-Key": "89bc9142damsh5d187bc9020f7e6p180050jsnb8ffa5f5755b",
            "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return print(response)
        '''
        sourceZip = zipfile.ZipFile(BytesIO(response.content))
        print(" Downloaded {} ".format(file_name))
        sourceZip.extractall(filePath)
        print(" extracted {}".format(file_name))
        sourceZip.close()'''          
        
    except Exception as e:
        print(e)


if __name__ == "__main__":
    filePath = os.path.dirname(os.path.abspath(__file__))
    print("filePath is %s " % filePath)
    stock = ["MSFT", "GOOG", "AAPL", "AMZN"]
    
    print(f"There are {cpu_count()} CPUs on this machine ")
    pool = Pool(cpu_count())
    #ipdb.set_trace()
    download_func = partial(get_json)
    results = pool.map(download_func, stock)
    
    pool.close()
    pool.join()
    print(results)