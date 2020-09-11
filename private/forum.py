from utils import API


class Forum(object):
    """
    Class to access Bungie.net User API
    """

    def __init__(self):
        self.public_api = API()

    def get_bungie_net_user_by_id(self, uid: int):
        req = API.bungie_api + '/User/GetBungieNetUserById/' + str(uid) + '/'
        return self.public_api.call_bungie_public_api(req)

    def search_users(self, display_name: str):
        req = API.bungie_api + '/User/SearchUsers/?q=' + display_name
        return self.public_api.call_bungie_public_api(req)

    def get_membership_data_by_id(self, uid: int, membership_type: int = 254):
        req = API.bungie_api + '/User/GetMembershipsById/' + str(uid) + '/' + str(membership_type) + '/'
        return self.public_api.call_bungie_public_api(req)

    def get_partnerships(self, uid: int):
        req = API.bungie_api + '/User/' + str(uid) + '/Partnerships/'
        return self.public_api.call_bungie_public_api(req)
