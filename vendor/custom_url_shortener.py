import random
class CustomUrlShortener:
    def __init__(self):
          self.protocolHttp = 'http://'
          self.protocolHttps = 'https://'
          self.domain = 'mm.com'      
    def doShortener(self, str_url):
        """
        1 - Defines a random alphanumeric with length = 6
        2 - Build a URL string based on protocol + short domain + random alphanumeric  
        """
        str_rand_alphaNumeric =  ''.join(random.choice('0123456789ABCDEF') for i in range(6))
        short = '{}{}/{}'.format(self.protocolHttps, self.domain, str_rand_alphaNumeric)
        return {'short':short}
        