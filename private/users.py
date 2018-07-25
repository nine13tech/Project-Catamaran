from ..utils import API


class User(object):
    """
    Class to access Bungie.net User API
    """

    def __init__(self):
        pass

    @staticmethod
    def get_membership_data_for_current_user(uid):
        this_api = API()
        req = API.bungie_api + '/User/GetMembershipsForCurrentUser/'
        return this_api.call_bungie_private_api_automated(uid, req)
