import logging
import requests
import json


logger = logging.getLogger(__name__)


class Scrapper(object):
    def __init__(self, skip_objects=None):
        self.skip_objects = skip_objects

    def scrap_process(self, storage):

        # You can iterate over ids, or get list of objects
        # from any API, or iterate throught pages of any site
        # Do not forget to skip already gathered data
        # Here is an example for you
        url = "https://api.nasa.gov/DONKI/CME?startDate=2000-01-03&endDate=2018-08-31&api_key=DEMO_KEY"
        response = requests.get(url)

        if not response.ok:
            logger.error(response.text)
            # then continue process, or retry, or fix your code

        else:
            # Note: here json can be used as response.json
            data = json.loads( response.text )

            # save scrapped objects here
            # you can save url to identify already scrapped objects
            storage.write_data(data)
