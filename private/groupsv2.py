from utils import API


class GroupsV2(object):
    """
    Class to access Bungie.net User API
    """

    def __init__(self):
        self.public_api = API()

    def get_group(self, group_id: int):
        req = API.bungie_api + '/GroupV2/' + str(group_id) + '/'
        return self.public_api.call_bungie_public_api(req)

    def get_group_by_name(self, group_name, group_type):
        """GroupType: 0=General, 1=Clan"""
        req = API.bungie_api + '/GroupV2/Name/' + group_name + '/' + str(group_type) + '/'
        return self.public_api.call_bungie_public_api(req)

    def get_members_of_group(self, group_id: int, current_page: int = 1):
        """GroupType: 0=General, 1=Clan"""
        req = API.bungie_api + '/GroupV2/' + str(group_id) + '/Members/?currentPage=' + str(current_page)
        return self.public_api.call_bungie_public_api(req)

    def get_andmins_and_founder_of_group(self, group_id):
        """GroupType: 0=General, 1=Clan"""
        req = API.bungie_api + '/GroupV2/' + str(group_id) + '/AdminsAndFounder/'
        return self.public_api.call_bungie_public_api(req)

    def get_banned_members_of_group(self, group_id):
        req = API.bungie_api + '/GroupV2/' + str(group_id) + '/Banned/'
        return self.public_api.call_bungie_public_api(req)

    def get_groups_for_member(self, membership_type, membership_id, search_filter, group_type):
        """filter: 0 all, 1 founded, 2 non-founded"""
        req = API.bungie_api + '/GroupV2/User/' + str(membership_type) + '/' + str(membership_id) + '/' + str(
            search_filter) + '/' + str(group_type) + '/'
        return self.public_api.call_bungie_public_api(req)

    def get_potential_groups_for_member(self, membership_type, membership_id, search_filter, group_type):
        req = API.bungie_api + '/GroupV2/User/Potential/' + str(membership_type) + '/' + str(membership_id) + '/' + str(
            search_filter) + '/' + str(group_type) + '/'
        return self.public_api.call_bungie_public_api(req)
