from ratelimit import limits, RateLimitException
from backoff import on_exception, expo

import requests

FIFTEEN_MINUTES = 900

@on_exception(expo, RateLimitException, max_tries=8)
@limits(calls=15, period=FIFTEEN_MINUTES)
def call_api(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response


def main():
    url = 'https://dev.to/api/articles'
    for i in range(10):
        call_api(url)
    
if __name__ == '__main__':
    main()
