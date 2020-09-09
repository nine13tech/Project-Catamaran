from utils import API


class GroupsV2(object):
    """
    Class to access Bungie.net User API
    """

    def __init__(self):
        pass

    @staticmethod
    def get_group(group_id: int) -> str:
        this_api = API()
        req = API.bungie_api + '/GroupV2/' + str(group_id) + '/'
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_group_by_name(group_name: str, group_type: int) -> str:
        """GroupType: 0=General, 1=Clan"""
        this_api = API()
        req = API.bungie_api + '/GroupV2/Name/' + group_name + '/' + str(group_type) + '/'
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_members_of_group(group_id: int, current_page: int = 1) -> str:
        """GroupType: 0=General, 1=Clan"""
        this_api = API()
        req = API.bungie_api + '/GroupV2/' + str(group_id) + '/Members/?currentPage=' + str(current_page)
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_andmins_and_founder_of_group(group_id: int) -> str:
        """GroupType: 0=General, 1=Clan"""
        this_api = API()
        req = API.bungie_api + '/GroupV2/' + str(group_id) + '/AdminsAndFounder/'
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_banned_members_of_group(group_id: int) -> str:
        this_api = API()
        req = API.bungie_api + '/GroupV2/' + str(group_id) + '/Banned/'
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_groups_for_member(membership_type: int, membership_id: int, search_filter: int, group_type: int) -> str:
        """filter: 0 all, 1 founded, 2 non-founded"""
        this_api = API()
        req = API.bungie_api + '/GroupV2/User/' + str(membership_type) + '/' + str(membership_id) + '/' + str(
            search_filter) + '/' + str(group_type) + '/'
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_potential_groups_for_member(membership_type: int, membership_id: int, search_filter: int, group_type: int) -> str:
        this_api = API()
        req = API.bungie_api + '/GroupV2/User/Potential/' + str(membership_type) + '/' + str(membership_id) + '/' + str(
            search_filter) + '/' + str(group_type) + '/'
        return this_api.call_bungie_public_api(req)
