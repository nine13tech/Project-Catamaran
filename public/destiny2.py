from ..utils import API


class Destiny2(object):
    """
    Class to access Bungie.net User API
    All GET requests done
    """

    def __init__(self):
        pass

    @staticmethod
    def get_destiny_manifest() -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/Manifest/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_destiny_entity_definition(entity_type: int, this_hash: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/Manifest/" + str(entity_type) + "/" + str(this_hash)
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def search_destiny_player(membership_type: int, display_name: str) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/SearchDestinyPlayer/" + str(membership_type) + "/" + display_name + "/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_profile(membership_type: int, membership_id: int, raw_components: list) -> str:
        components = ','.join(str(e) for e in raw_components)
        this_api = API()
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Profile/" + str(membership_id) \
              + "/?components=" + str(components)
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_character(membership_type: int, membership_id: int, character_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Profile/" + str(
            membership_id) + "/Character/" + str(character_id) + "/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_clan_weekly_reward_state(clan_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/Clan/" + str(clan_id) + "/WeeklyRewardState/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_item(membership_type: int, membership_id: int, item_instance_hash: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Profile/" + str(membership_id) + "/Item/" + \
              str(item_instance_hash) + "/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_vendors(membership_type: int, membership_id: int, character_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Profile/" + str(
            membership_id) + "/Character/" + str(
            character_id) + "/Vendors/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_vendor(membership_type: int, membership_id: int, character_id: int, vendor_hash: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Profile/" + str(
            membership_id) + "/Character/" + str(
            character_id) + "/Vendors/" + str(vendor_hash) + "/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_post_game_carnage_report(activity_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/Stats/PostGameCarnageReport/" + str(activity_id) + "/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_clan_leaderboards(clan_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/Stats/Leaderboards/Clans/" + str(clan_id) + "/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_clan_aggregate_stats(clan_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/Stats/AggregateClanStats/" + str(clan_id) + "/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_leaderboards(membership_type: int, membership_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Account/" + str(
            membership_id) + "/Stats/Leaderboards/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_leaderboards_for_character(membership_type: int, membership_id: int, character_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/Stats/Leaderboards/" + str(membership_type) + "/" + str(membership_id) + "/" + \
              str(character_id) + "/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_historical_stats(membership_type: int, membership_id: int, character_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Profile/" + str(
            membership_id) + "/Character/" + str(
            character_id) + "/Stats/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_historical_stats_for_account(membership_type: int, membership_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Account/" + str(membership_id) + "/Stats/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_activity_history(membership_type: int, membership_id: int, character_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Account/" + str(
            membership_id) + "/Character/" + str(
            character_id) + "/Stats/Activities/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_unique_weapon_history(membership_type: int, membership_id: int, character_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Account/" + str(
            membership_id) + "/Character/" + str(
            character_id) + "/Stats/UniqueWeapons/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_destiny_aggregate_activity_stats(membership_type: int, membership_id: int, character_id: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Account/" + str(
            membership_id) + "/Character/" + str(
            character_id) + "/Stats/AggregateActivityStats/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_public_milestones_content(milestone_hash: int) -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/Milestones/" + str(milestone_hash) + "/Content/"
        return this_api.call_bungie_public_api(req)

    @staticmethod
    def get_public_milestones() -> str:
        this_api = API()
        req = API.bungie_api + "/Destiny2/Milestones/"
        return this_api.call_bungie_public_api(req)

    # Milestone Helper
    @staticmethod
    def milestone_types(this_type: int) -> str:
        """
        Returns the correct English Language Milestone Type
        :param this_type: The milestone type from the milestone definition
        :type this_type: int
        :return: English Language Milestone Type
        :rtype: str
        """
        if this_type == 1:
            return 'Tutorial'
        elif this_type == 2:
            return 'OneTime'
        elif this_type == 3:
            return 'Weekly'
        elif this_type == 4:
            return 'Daily'
        elif this_type == 5:
            return 'Special'
        else:
            return 'UNKNOWN'
