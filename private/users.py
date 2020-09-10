from utils import API


class User(object):
    """
    Class to access Bungie.net User API
    """

    def __init__(self):
        self.public_api = API()

    @staticmethod
    def get_membership_data_for_current_user(self, uid):
        req = API.bungie_api + '/User/GetMembershipsForCurrentUser/'
        return self.public_api.call_bungie_private_api_automated(uid, req)
