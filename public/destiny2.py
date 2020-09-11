from utils import API


class Destiny2(object):
    """
    Class to access Bungie.net User API
    All GET requests done
    """

    def __init__(self):
        self.public_api = API()

    def get_destiny_manifest(self) -> str:
        req = API.bungie_api + "/Destiny2/Manifest/"
        return self.public_api.call_bungie_public_api(req)

    def get_destiny_entity_definition(self, entity_type: int, this_hash: int) -> str:
        req = API.bungie_api + "/Destiny2/Manifest/" + str(entity_type) + "/" + str(this_hash)
        return self.public_api.call_bungie_public_api(req)

    def search_destiny_player(self, membership_type: int, display_name: str) -> str:
        req = API.bungie_api + "/Destiny2/SearchDestinyPlayer/" + str(membership_type) + "/" + display_name + "/"
        return self.public_api.call_bungie_public_api(req)

    def get_profile(self, membership_type: int, membership_id: int, raw_components: list) -> str:
        components = ','.join(str(e) for e in raw_components)
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Profile/" + str(membership_id) \
              + "/?components=" + str(components)
        return self.public_api.call_bungie_public_api(req)

    def get_character(self, membership_type: int, membership_id: int, character_id: int) -> str:
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Profile/" + str(
            membership_id) + "/Character/" + str(character_id) + "/"
        return self.public_api.call_bungie_public_api(req)

    def get_clan_weekly_reward_state(self, clan_id: int) -> str:
        req = API.bungie_api + "/Destiny2/Clan/" + str(clan_id) + "/WeeklyRewardState/"
        return self.public_api.call_bungie_public_api(req)

    def get_item(self, membership_type: int, membership_id: int, item_instance_hash: int) -> str:
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Profile/" + str(membership_id) + "/Item/" + \
              str(item_instance_hash) + "/"
        return self.public_api.call_bungie_public_api(req)

    def get_vendors(self, membership_type: int, membership_id: int, character_id: int) -> str:
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Profile/" + str(
            membership_id) + "/Character/" + str(
            character_id) + "/Vendors/"
        return self.public_api.call_bungie_public_api(req)

    def get_vendor(self, membership_type: int, membership_id: int, character_id: int, vendor_hash: int) -> str:
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Profile/" + str(
            membership_id) + "/Character/" + str(
            character_id) + "/Vendors/" + str(vendor_hash) + "/"
        return self.public_api.call_bungie_public_api(req)

    def get_post_game_carnage_report(self, activity_id: int) -> str:
        req = API.bungie_api + "/Destiny2/Stats/PostGameCarnageReport/" + str(activity_id) + "/"
        return self.public_api.call_bungie_public_api(req)

    def get_clan_leaderboards(self, clan_id: int) -> str:
        req = API.bungie_api + "/Destiny2/Stats/Leaderboards/Clans/" + str(clan_id) + "/"
        return self.public_api.call_bungie_public_api(req)

    def get_clan_aggregate_stats(self, clan_id: int) -> str:
        req = API.bungie_api + "/Destiny2/Stats/AggregateClanStats/" + str(clan_id) + "/"
        return self.public_api.call_bungie_public_api(req)

    def get_leaderboards(self, membership_type: int, membership_id: int) -> str:
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Account/" + str(
            membership_id) + "/Stats/Leaderboards/"
        return self.public_api.call_bungie_public_api(req)

    def get_leaderboards_for_character(self, membership_type: int, membership_id: int, character_id: int) -> str:
        req = API.bungie_api + "/Destiny2/Stats/Leaderboards/" + str(membership_type) + "/" + str(membership_id) + "/" + \
              str(character_id) + "/"
        return self.public_api.call_bungie_public_api(req)

    def get_historical_stats(self, membership_type: int, membership_id: int, character_id: int) -> str:
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Profile/" + str(
            membership_id) + "/Character/" + str(
            character_id) + "/Stats/"
        return self.public_api.call_bungie_public_api(req)

    def get_historical_stats_for_account(self, membership_type: int, membership_id: int) -> str:
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Account/" + str(membership_id) + "/Stats/"
        return self.public_api.call_bungie_public_api(req)

    def get_activity_history(self, membership_type: int, membership_id: int, character_id: int) -> str:
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Account/" + str(
            membership_id) + "/Character/" + str(
            character_id) + "/Stats/Activities/"
        return self.public_api.call_bungie_public_api(req)

    def get_unique_weapon_history(self, membership_type: int, membership_id: int, character_id: int) -> str:
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Account/" + str(
            membership_id) + "/Character/" + str(
            character_id) + "/Stats/UniqueWeapons/"
        return self.public_api.call_bungie_public_api(req)

    def get_destiny_aggregate_activity_stats(self, membership_type: int, membership_id: int, character_id: int) -> str:
        req = API.bungie_api + "/Destiny2/" + str(membership_type) + "/Account/" + str(
            membership_id) + "/Character/" + str(
            character_id) + "/Stats/AggregateActivityStats/"
        return self.public_api.call_bungie_public_api(req)

    def get_public_milestones_content(self, milestone_hash: int) -> str:
        req = API.bungie_api + "/Destiny2/Milestones/" + str(milestone_hash) + "/Content/"
        return self.public_api.call_bungie_public_api(req)

    def get_public_milestones(self, ) -> str:
        req = API.bungie_api + "/Destiny2/Milestones/"
        return self.public_api.call_bungie_public_api(req)

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
