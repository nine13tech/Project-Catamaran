from utils import API


class User(object):
    """
    Class to access Bungie.net User API
    """

    def __init__(self):
        pass

    @staticmethod
    def get_bungie_net_user_by_id(uid: int):
        this_api = API()
        req = API.bungie_api + '/User/GetBungieNetUserById/' + str(uid) + '/'
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def search_users(display_name: str):
        this_api = API()
        req = API.bungie_api + '/User/SearchUsers/?q=' + display_name
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_membership_data_by_id(uid: int, membership_type: int = 254):
        this_api = API()
        req = API.bungie_api + '/User/GetMembershipsById/' + str(uid) + '/' + str(membership_type) + '/'
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_partnerships(uid: int):
        this_api = API()
        req = API.bungie_api + '/User/' + str(uid) + '/Partnerships/'
        return this_api.call_bungie_public_api(req)
