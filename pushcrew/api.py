from hammock import Hammock
from .services.segments import SegmentsMixin


class Api(SegmentsMixin):
    """
    Manage all the available services.
    """
    API_BASE_URL = 'https://pushcrew.com/api/v1/'

    def __init__(self, token, api_base_url=API_BASE_URL):
        self.token = token
        self.api_base_url = api_base_url

        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.pushcrew = Hammock(self.api_base_url, headers=headers)
