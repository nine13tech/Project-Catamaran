import inspect
import json
import environ
import requests
from config import *

#

if CURRENT_ENV == 'prod':
    BUNGIE_API_KEY = BUNGIE_API_KEY_PROD
    BUNGIE_ORIGIN = BUNGIE_ORIGIN_PROD
elif CURRENT_ENV == 'dev':
    BUNGIE_API_KEY = BUNGIE_API_KEY_DEVEL
    BUNGIE_ORIGIN = BUNGIE_ORIGIN_DEVEL
else:
    BUNGIE_API_KEY = ''
    BUNGIE_ORIGIN = ''


class DebugHelpers(object):
    def __init__(self):
        pass

    @staticmethod
    def debug_output():
        pass


class API(object):
    """
    Class to access Bungie.net User API
    """
    bungie = 'https://www.bungie.net'
    bungie_api = bungie + '/Platform'

    def __init__(self):
        api_key = BUNGIE_API_KEY
        origin_header = BUNGIE_ORIGIN
        # print('Warmind_D2.utils.__init__:', origin_header, api_key)
        self.api_headers = {'Origin': origin_header, "X-API-Key": api_key}
        # TODO: Add "Authorization: Bearer", access_token from social_auth_usersocialauth.extra_data

    def call_bungie_public_api(self, req: str) -> str:
        """
        Calls the Bungie API
        :param req: The request URL that is built by the calling function
        :type req: str
        :return: APi return data
        :rtype: json
        """
        # Find calling function for debug
        current_frame = inspect.currentframe()
        calling_frame = inspect.getouterframes(current_frame, 2)
        called_function = calling_frame[0][3]
        calling_function_file = calling_frame[1][1]
        calling_function_line = calling_frame[1][2]
        calling_function_name = calling_frame[1][3]
        # end debug
        request_session = requests.session()
        try:
            r = request_session.get(req, headers=self.api_headers)
            return_data = r.json()
        except Exception as e:
            return_data = {'ErrorCode': 9999, 'Message': 'API Call Failed', 'ErrorStatus': 'Failure'}
            print("Exception in " + str(called_function) + " called from " + str(calling_function_file) +
                  " @ line " + str(calling_function_line) + " ->: " + str(calling_function_name) + " \n > %s\n" % e)
        if return_data['ErrorCode'] == 1 or return_data['ErrorCode'] == 1601:
            return return_data
        else:
            print(return_data['ErrorStatus'])
            print(return_data['Message'])
            exit(return_data)  # TODO: too much?

    # def call_bungie_private_api_automated(self, uid: int, req: str) -> str:
    #     """
    #     Calls the Bungie API
    #     :param uid:
    #     :type uid:
    #     :param req: The request URL that is built by the calling function
    #     :type req: str
    #     :return: APi return data
    #     :rtype: json
    #     """
    #     # Find calling function for debug
    #     current_frame = inspect.currentframe()
    #     calling_frame = inspect.getouterframes(current_frame, 2)
    #     called_function = calling_frame[0][3]
    #     calling_function_file = calling_frame[1][1]
    #     calling_function_line = calling_frame[1][2]
    #     calling_function_name = calling_frame[1][3]
    #     # end debug
    #     # Refresh Token
    #     from social_django.models import UserSocialAuth
    #     social_user = UserSocialAuth.objects.get(uid=str(uid), provider='bungie')
    #     # social_user.refresh_token(load_strategy())
    #     self.api_headers['Authorization'] = 'Bearer ' + str(social_user.access_token)
    #     # print('HEADERS', self.api_headers)
    #     # print('REQ:', req)
    #     # Add Auth to headers
    #     request_session = requests.session()
    #     try:
    #         r = request_session.get(req, headers=self.api_headers)
    #         print('REQ:', req, '\nHEADERS: ', self.api_headers)
    #         return_data = r.json()
    #     except Exception as e:
    #         return_data = {'ErrorCode': 9999, 'Message': 'API Call Failed', 'ErrorStatus': 'Failure'}
    #         print("Exception in " + str(called_function) + " called from " + str(calling_function_file) +
    #               " @ line " + str(calling_function_line) + " ->: " + str(calling_function_name) + " \n > %s\n" % e)
    #     if return_data['ErrorCode'] == 1 or return_data['ErrorCode'] == 1601:
    #         return return_data
    #     else:
    #         print(return_data['ErrorStatus'])
    #         print(return_data['Message'])
    #         exit(return_data)  # TODO: too much?

    # def call_bungie_private_api_django(self, request, req: str) -> str:
    #     """
    #     Calls the Bungie API
    #     :param request:
    #     :type request:
    #     :param req: The request URL that is built by the calling function
    #     :type req: str
    #     :return: APi return data
    #     :rtype: json
    #     """
    #     # Find calling function for debug
    #     current_frame = inspect.currentframe()
    #     calling_frame = inspect.getouterframes(current_frame, 2)
    #     called_function = calling_frame[0][3]
    #     calling_function_file = calling_frame[1][1]
    #     calling_function_line = calling_frame[1][2]
    #     calling_function_name = calling_frame[1][3]
    #     # end debug
    #     # Refresh Token
    #     from social_django.utils import load_strategy
    #     social = request.user.social_auth.get(provider='bungie')
    #     # TODO: rewrite this for Bungie??? Isn't there a refresh token method in PythonSocialAuth
    #     # TODO: I do this already in a command!!!!
    #     # from: https://stackoverflow.com/questions/41466731/how-can-i-refresh-the-token-with-social-auth-app-django
    #     response = self.get_json('https://graph.microsoft.com/v1.0/me',
    #                              headers={'Authorization': '%s %s' % (social.extra_data['token_type'],
    #                                                                   social.get_access_token(load_strategy()))})
    #     # Add Auth to headers
    #     request_session = requests.session()
    #     try:
    #         r = request_session.get(req, headers=self.api_headers)
    #         return_data = r.json()
    #     except Exception as e:
    #         return_data = {'ErrorCode': 9999, 'Message': 'API Call Failed', 'ErrorStatus': 'Failure'}
    #         print("Exception in " + str(called_function) + " called from " + str(calling_function_file) +
    #               " @ line " + str(calling_function_line) + " ->: " + str(calling_function_name) + " \n > %s\n" % e)
    #     if return_data['ErrorCode'] == 1 or return_data['ErrorCode'] == 1601:
    #         return return_data
    #     else:
    #         print(return_data['ErrorStatus'])
    #         print(return_data['Message'])
    #         exit(return_data)  # TODO: too much?


class AccountHelpers(object):

    def __init__(self):
        pass

    def profile_versions_owned_humanize(self, versions: int) -> str:
        if versions == 0:
            return 'none'
        elif versions == 1:
            return 'D2 Only'
        elif versions == 2:
            return 'D2 + DLC 1'
        elif versions == 3:
            return 'D2 + DLC 1 & 2'
        else:
            return 'unknown'

    def profile_privacy_humanize(self, privacy: int) -> str:
        if privacy == 0:
            return 'none'
        elif privacy == 1:
            return 'public'
        elif privacy == 2:
            return 'private'
        else:
            return 'unknown'

    def find_correct_account(self, display_name: str, membership_type: int):
        from .public.users import User
        d2_user_api_instance = User()
        api_response = d2_user_api_instance.search_users(display_name)
        if membership_type != 4:
            weight = []
            these_ids = []
            for idx, each in enumerate(api_response['Response']):
                weight.append(0)
                if each['displayName'] == display_name:
                    weight[idx] += +1
                else:
                    weight[idx] += -1
                if each['profilePicturePath'] == "/img/profile/avatars/default_avatar.gif":
                    weight[idx] += -1
                else:
                    weight[idx] += 1
                if each['firstAccess'] == each['lastUpdate']:
                    weight[idx] += -1
                else:
                    weight[idx] += 1
                if each['profilePicture'] == 0:
                    weight[idx] += -1
                else:
                    weight[idx] += 1
                these_ids.append(each['membershipId'])
            if these_ids.index(max(these_ids)) is None:
                correct_idx = 0000
            else:
                newest = these_ids.index(max(these_ids))
                weight[newest] += 1
                correct_idx = weight.index(max(weight))
            return api_response['Response'][correct_idx]['membershipId']
        else:
            return 0000


class ManifestHelpers(object):

    def __init__(self):
        pass

    def int32(self, hash_id: int) -> int:
        """
        Convert hash to unsigned 32 bit for Manifest DB Lookup
        Required to convert the integers for looking up hashes in the manifest DB
        :param hash_id: vendor, item or activity hash
        :return: unsigned 32 bit int
        """
        hash_id = int(hash_id)
        if hash_id > 0xFFFFFFFF:
            raise OverflowError
        if hash_id > 0x7FFFFFFF:
            hash_id = int(0x100000000 - hash_id)
            if hash_id < 2147483648:
                return -hash_id
            else:
                return -2147483648
        return hash_id

    def query_manifest(self, table, this_hash):
        import sqlite3
        conn = sqlite3.connect(MANIFEST_DB[0])
        cur = conn.cursor()
        this_id = self.int32(this_hash)
        query = 'SELECT json FROM ' + table + ' WHERE id = ?'
        key = (this_id,)
        cur.execute(query, key)
        this_out = cur.fetchall()
        conn.commit()
        conn.close()
        return this_out

    def refresh_manifest_db(self):
        """ """
        from .public.destiny2 import Destiny2
        destiny2 = Destiny2()
        print('Updating Manifest DB')
        api_response = destiny2.get_destiny_manifest()
        try:
            environ.os.remove(MANIFEST_DB[0])
        except Exception as e:
            print(e)
        file_name = api_response['Response']['mobileWorldContentPaths']['en']
        file_name = file_name.split('/')[5]
        mani_url = BUNGIE_URL + api_response['Response']['mobileWorldContentPaths']['en']
        import urllib.request
        import shutil
        out_path = BASE_DIR + '/data/' + file_name
        with urllib.request.urlopen(mani_url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        import zipfile
        zip_ref = zipfile.ZipFile(file_name, 'r')
        zip_ref.extractall(BASE_DIR + '/data')
        zip_ref.close()
        shutil.move(out_path, MANIFEST_DB[0])
        try:
            environ.os.remove(file_name)
        except Exception as e:
            print(e)


def query_banner_manifest(self, table, this_hash):
    import sqlite3
    conn = sqlite3.connect(BANNER_DB[0])
    cur = conn.cursor()
    this_id = self.int32(this_hash)
    query = 'SELECT json FROM ' + table + ' WHERE id = ?'
    key = (this_id,)
    cur.execute(query, key)
    this_out = cur.fetchall()
    conn.commit()
    conn.close()
    return this_out


def refresh_banner_db(self):
    """ """
    from .public.destiny2 import Destiny2
    destiny2 = Destiny2()

    print('Updating Banner DB')
    api_response = destiny2.get_destiny_manifest()
    try:
        environ.os.remove(BANNER_DB[0])
    except Exception as e:
        print(e)
    file_name = api_response['Response']['mobileClanBannerDatabasePath']
    file_name = file_name.split('/')[4]
    mani_url = BUNGIE_URL + api_response['Response']['mobileClanBannerDatabasePath']
    import urllib.request
    import shutil
    out_path = BASE_DIR + '/data/' + file_name
    with urllib.request.urlopen(mani_url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    import zipfile
    zip_ref = zipfile.ZipFile(file_name, 'r')
    zip_ref.extractall(BASE_DIR + '/data')
    zip_ref.close()
    shutil.move(out_path, BANNER_DB[0])
    try:
        environ.os.remove(file_name)
    except Exception as e:
        print(e)


class MilestonesDisplay(object):

    def __init__(self):
        pass

    def flashpoint_location(self, flashpoint_quest: int) -> str:
        if int(flashpoint_quest) == 2144675440:
            return "EDZ"
        elif int(flashpoint_quest) == 1881837031:
            return "Nessus"
        elif int(flashpoint_quest) == 1111180031:
            return "Titan"
        elif int(flashpoint_quest) == 2878046419:
            return "Io"
        elif int(flashpoint_quest) == 3786778617:
            return "Mercury"
        elif int(flashpoint_quest) == 1268260813:
            return "Mars"
        else:
            return "UNKNOWN"

    def nightfall(self, api_response: dict) -> dict:
        """
        Return JSON of Nightfall activity, variants and challenges for display or email
        EVENT TYPE: Circadian
        :param api_response: pulled from the public milestones API
        :type api_response: dictionary
        :return: dictionary of nightfall data
        :rtype: dict
        """
        # NIGHTFALL
        # print('api_response\n', api_response)
        mh = ManifestHelpers()
        # nightfall = api_response['Response']['2171429505']
        nightfall = {}
        quest_json = json.loads(
            mh.query_manifest('DestinyInventoryItemDefinition', api_response['Response']['2171429505']
            ['availableQuests'][0]['questItemHash'])[0][0])
        standard_hash = api_response['Response']['2171429505']['availableQuests'][0]['activity']['activityHash']
        nightfall['name'] = quest_json['displayProperties']['name']
        nightfall['description'] = quest_json['displayProperties']['description']
        nightfall['icon'] = quest_json['displayProperties']['icon']
        activity_json = json.loads(
            mh.query_manifest('DestinyActivityDefinition', api_response['Response']['2171429505']
            ['availableQuests'][0]['activity']['activityHash'])[0][0])
        nightfall['activity'] = activity_json['displayProperties']['name']
        nightfall['activity_desc'] = activity_json['displayProperties']['description']
        nightfall['activity_icon'] = activity_json['displayProperties']['icon']
        place_json = json.loads(mh.query_manifest('DestinyPlaceDefinition', activity_json['placeHash'])[0][0])
        nightfall['activity_place_name'] = place_json['displayProperties']['name']
        nightfall['activity_place_desc'] = place_json['displayProperties']['description']
        nightfall['variants'] = {}
        nightfall['variants']['standard'] = {}
        nightfall['variants']['prestige'] = {}
        i = 0
        for each in api_response['Response']['2171429505']['availableQuests'][0]['activity']['variants']:
            # TODO: ISSUE 550 https://github.com/Bungie-net/api/issues/550
            # We need the activityLevel and activityLightLevel from the variant
            # We need the name, desc and icon from the mode
            if each['activityHash'] == standard_hash:
                variant_json = json.loads(
                    mh.query_manifest('DestinyActivityDefinition', each['activityHash'])[0][0])
                variant_mode = json.loads(
                    mh.query_manifest('DestinyActivityModeDefinition', each['activityModeHash'])[0][0])
                nightfall['variants']['standard']['light'] = variant_json['activityLightLevel']
                nightfall['variants']['standard']['level'] = variant_json['activityLevel']
                nightfall['variants']['standard']['name'] = variant_mode['displayProperties'][
                    'name']
                nightfall['variants']['standard']['desc'] = variant_mode['displayProperties'][
                    'description']
                nightfall['variants']['standard']['icon'] = variant_mode['displayProperties'][
                    'icon']

                # print('variant_json ', i, '\n', variant_json)
                # print('variant_mode ', i, '\n', variant_mode)
            else:
                variant_json = json.loads(
                    mh.query_manifest('DestinyActivityDefinition', each['activityHash'])[0][0])
                variant_mode = json.loads(
                    mh.query_manifest('DestinyActivityModeDefinition', 532484583)[0][0])
                nightfall['variants']['prestige']['light'] = variant_json['activityLightLevel']
                nightfall['variants']['prestige']['level'] = variant_json['activityLevel']
                nightfall['variants']['prestige']['name'] = variant_mode['displayProperties'][
                    'name']
                nightfall['variants']['prestige']['desc'] = variant_mode['displayProperties'][
                    'description']
                nightfall['variants']['prestige']['icon'] = variant_mode['displayProperties'][
                    'icon']
                # print('variant_json ', i, '\n', variant_json)
                # print('variant_mode ', i, '\n', variant_mode)
        s = 0
        p = 0
        for each in api_response['Response']['2171429505']['availableQuests'][0]['challenges']:
            if each['activityHash'] == standard_hash:
                objective_json = json.loads(
                    mh.query_manifest('DestinyObjectiveDefinition', each['objectiveHash'])[0][0])
                this_challenge = 'challenge_' + str(s)
                nightfall['variants']['standard'][this_challenge] = {}
                nightfall['variants']['standard'][this_challenge]['name'] = \
                    objective_json['displayProperties']['name']
                nightfall['variants']['standard'][this_challenge]['desc'] = \
                    objective_json['displayProperties']['description']
                s += 1
            else:
                objective_json = json.loads(
                    mh.query_manifest('DestinyObjectiveDefinition', each['objectiveHash'])[0][0])
                this_challenge = 'challenge_' + str(p)
                nightfall['variants']['prestige'][this_challenge] = {}
                nightfall['variants']['prestige'][this_challenge]['name'] = \
                    objective_json['displayProperties']['name']
                nightfall['variants']['prestige'][this_challenge]['desc'] = \
                    objective_json['displayProperties']['description']
                p += 1
        return nightfall

    def raid(self, api_response: dict) -> dict:
        """
        Return JSON of Raid activity, variants and challenges for display or email
        EVENT TYPE: Circadian
        :param api_response: pulled from the public milestones API
        :type api_response: dictionary
        :return: dictionary of nightfall data
        :rtype: dict
        """
        mh = ManifestHelpers()
        raid = {}
        # raid = api_response['Response']['3660836525']
        raid = {}
        quest_json = json.loads(
            mh.query_manifest('DestinyInventoryItemDefinition', api_response['Response']['3660836525']
            ['availableQuests'][0]['questItemHash'])[0][0])
        standard_hash = api_response['Response']['3660836525']['availableQuests'][0]['activity']['activityHash']
        raid['name'] = quest_json['displayProperties']['name']
        raid['description'] = quest_json['displayProperties']['description']
        raid['icon'] = quest_json['displayProperties']['icon']
        activity_json = json.loads(
            mh.query_manifest('DestinyActivityDefinition', api_response['Response']['3660836525']
            ['availableQuests'][0]['activity']['activityHash'])[0][0])
        raid['activity'] = activity_json['displayProperties']['name']
        raid['activity_desc'] = activity_json['displayProperties']['description']
        raid['activity_icon'] = activity_json['displayProperties']['icon']
        place_json = json.loads(mh.query_manifest('DestinyPlaceDefinition', activity_json['placeHash'])[0][0])
        raid['activity_place_name'] = place_json['displayProperties']['name']
        raid['activity_place_desc'] = place_json['displayProperties']['description']
        raid['variants'] = {}
        raid['variants']['standard'] = {}
        raid['variants']['prestige'] = {}
        i = 0
        for each in api_response['Response']['3660836525']['availableQuests'][0]['activity']['variants']:
            if each['activityHash'] == standard_hash:
                variant_json = json.loads(
                    mh.query_manifest('DestinyActivityDefinition', each['activityHash'])[0][0])
                variant_mode = json.loads(
                    mh.query_manifest('DestinyActivityModeDefinition', each['activityModeHash'])[0][0])
                raid['variants']['standard']['light'] = variant_json['activityLightLevel']
                raid['variants']['standard']['level'] = variant_json['activityLevel']
                raid['variants']['standard']['name'] = variant_mode['displayProperties'][
                    'name']
                raid['variants']['standard']['desc'] = variant_mode['displayProperties'][
                    'description']
                raid['variants']['standard']['icon'] = variant_mode['displayProperties'][
                    'icon']

                # print('variant_json ', i, '\n', variant_json)
                # print('variant_mode ', i, '\n', variant_mode)
            else:
                variant_json = json.loads(
                    mh.query_manifest('DestinyActivityDefinition', each['activityHash'])[0][0])
                variant_mode = json.loads(
                    mh.query_manifest('DestinyActivityModeDefinition', each['activityModeHash'])[0][0])
                raid['variants']['prestige']['light'] = variant_json['activityLightLevel']
                raid['variants']['prestige']['level'] = variant_json['activityLevel']
                raid['variants']['prestige']['name'] = variant_mode['displayProperties'][
                    'name']
                raid['variants']['prestige']['desc'] = variant_mode['displayProperties'][
                    'description']
                raid['variants']['prestige']['icon'] = variant_mode['displayProperties'][
                    'icon']
                # print('variant_json ', i, '\n', variant_json)
                # print('variant_mode ', i, '\n', variant_mode)
        s = 0
        p = 0
        for each in api_response['Response']['3660836525']['availableQuests'][0]['challenges']:
            if each['activityHash'] == standard_hash:
                objective_json = json.loads(
                    mh.query_manifest('DestinyObjectiveDefinition', each['objectiveHash'])[0][0])
                this_challenge = 'challenge_' + str(s)
                raid['variants']['standard'][this_challenge] = {}
                raid['variants']['standard'][this_challenge]['name'] = \
                    objective_json['displayProperties']['name']
                raid['variants']['standard'][this_challenge]['desc'] = \
                    objective_json['displayProperties']['description']
                s += 1
            else:
                objective_json = json.loads(
                    mh.query_manifest('DestinyObjectiveDefinition', each['objectiveHash'])[0][0])
                this_challenge = 'challenge_' + str(p)
                raid['variants']['prestige'][this_challenge] = {}
                raid['variants']['prestige'][this_challenge]['name'] = \
                    objective_json['displayProperties']['name']
                raid['variants']['prestige'][this_challenge]['desc'] = \
                    objective_json['displayProperties']['description']
                p += 1
        return raid

    def trials_of_the_nine(self, api_response: dict) -> dict:
        """
        Return JSON of Raid activity, variants and challenges for display or email
        EVENT TYPE: Circadian
        :param api_response: pulled from the public milestones API
        :type api_response: dictionary
        :return: dictionary of nightfall data
        :rtype: dict
        """
        mh = ManifestHelpers()
        trials = {}
        quest_json = json.loads(
            mh.query_manifest('DestinyInventoryItemDefinition', api_response['Response']['3551755444']
            ['availableQuests'][0]['questItemHash'])[0][0])
        standard_hash = api_response['Response']['3551755444']['availableQuests'][0]['activity']['activityHash']
        trials['name'] = quest_json['displayProperties']['name']
        trials['description'] = quest_json['displayProperties']['description']
        trials['icon'] = quest_json['displayProperties']['icon']
        activity_json = json.loads(
            mh.query_manifest('DestinyActivityDefinition', api_response['Response']['3551755444']
            ['availableQuests'][0]['activity']['activityHash'])[0][0])
        trials['activity'] = activity_json['displayProperties']['name']
        trials['activity_desc'] = activity_json['displayProperties']['description']
        trials['activity_icon'] = activity_json['displayProperties']['icon']
        place_json = json.loads(mh.query_manifest('DestinyPlaceDefinition', activity_json['placeHash'])[0][0])
        trials['activity_place_name'] = place_json['displayProperties']['name']
        trials['activity_place_desc'] = place_json['displayProperties']['description']
        trials['variants'] = {}
        trials['variants']['standard'] = {}
        trials['variants']['prestige'] = {}
        i = 0
        for each in api_response['Response']['3551755444']['availableQuests'][0]['activity']['variants']:
            print('EACH\n', each)
            if each['activityHash'] == standard_hash:
                variant_json = json.loads(
                    mh.query_manifest('DestinyActivityDefinition', each['activityHash'])[0][0])
                variant_mode = json.loads(
                    mh.query_manifest('DestinyActivityModeDefinition', each['activityModeHash'])[0][0])
                trials['variants']['standard']['light'] = variant_json['activityLightLevel']
                trials['variants']['standard']['level'] = variant_json['activityLevel']
                trials['variants']['standard']['name'] = variant_mode['displayProperties'][
                    'name']
                trials['variants']['standard']['desc'] = variant_mode['displayProperties'][
                    'description']
                trials['variants']['standard']['icon'] = variant_mode['displayProperties'][
                    'icon']
            else:
                variant_json = json.loads(
                    mh.query_manifest('DestinyActivityDefinition', each['activityHash'])[0][0])
                variant_mode = json.loads(
                    mh.query_manifest('DestinyActivityModeDefinition', each['activityModeHash'])[0][0])
                trials['variants']['prestige']['light'] = variant_json['activityLightLevel']
                trials['variants']['prestige']['level'] = variant_json['activityLevel']
                trials['variants']['prestige']['name'] = variant_mode['displayProperties'][
                    'name']
                trials['variants']['prestige']['desc'] = variant_mode['displayProperties'][
                    'description']
                trials['variants']['prestige']['icon'] = variant_mode['displayProperties'][
                    'icon']
        s = 0
        p = 0
        for each in api_response['Response']['3551755444']['availableQuests'][0]['challenges']:
            if each['activityHash'] == standard_hash:
                objective_json = json.loads(
                    mh.query_manifest('DestinyObjectiveDefinition', each['objectiveHash'])[0][0])
                this_challenge = 'challenge_' + str(s)
                trials['variants']['standard'][this_challenge] = {}
                trials['variants']['standard'][this_challenge]['name'] = \
                    objective_json['displayProperties']['name']
                trials['variants']['standard'][this_challenge]['desc'] = \
                    objective_json['displayProperties']['description']
                s += 1
            else:
                objective_json = json.loads(
                    mh.query_manifest('DestinyObjectiveDefinition', each['objectiveHash'])[0][0])
                this_challenge = 'challenge_' + str(p)
                trials['variants']['prestige'][this_challenge] = {}
                trials['variants']['prestige'][this_challenge]['name'] = \
                    objective_json['displayProperties']['name']
                trials['variants']['prestige'][this_challenge]['desc'] = \
                    objective_json['displayProperties']['description']
                p += 1
        print('TRIALS\n', trials)
        return trials

    def meditations(self, api_response: dict) -> dict:
        mh = ManifestHelpers()
        meditations = {}
        if '3245985898' in api_response['Response']:
            meditations_quest = api_response['Response']['3245985898']['availableQuests'][0]['questItemHash']
            meditation_json = json.loads(mh.query_manifest('DestinyMilestoneDefinition',
                                                           api_response['Response']['3245985898']['milestoneHash'])[0][
                                             0])
            # print('med_json\n', meditation_json)
            meditations['desc'] = meditation_json['displayProperties']['description']
            meditations['name'] = meditation_json['displayProperties']['name']
            meditations['icon'] = meditation_json['displayProperties']['icon']
            meditations['quests'] = []
            i = 0
            for quest in api_response['Response']['3245985898']['availableQuests']:
                variant_json = json.loads(
                    mh.query_manifest('DestinyActivityDefinition', quest['activity']['activityHash'])[0][0])
                meditations['quests'].append({'name': variant_json['displayProperties']['name'],
                                              'desc': variant_json['displayProperties']['description'],
                                              'icon': variant_json['displayProperties']['icon']},
                                             )
                i += 1
        return meditations

    def strikes(self, api_response: dict) -> dict:
        """
        Return JSON of Strikes activity, variants and challenges for display or email
        EVENT TYPE: Circadian
        :param api_response: pulled from the public milestones API
        :type api_response: dictionary
        :return: dictionary of nightfall data
        :rtype: dict
        """
        mh = ManifestHelpers()
        strikes = {}
        if '3172444947' in api_response['Response']:
            strikes = api_response['Response']['3172444947']
        return strikes

    def flashpoint(self, api_response: dict) -> dict:
        """
        Return JSON of Hotspot/Flashpoint activity, variants and challenges for display or email
        EVENT TYPE: Recon Report
        :param api_response: pulled from the public milestones API
        :type api_response: dictionary
        :return: dictionary of nightfall data
        :rtype: dict
        """
        mh = ManifestHelpers()
        flashpoint = {}
        if '463010297' in api_response['Response']:
            # flashpoint = api_response['Response']['463010297']
            flashpoint_quest = api_response['Response']['463010297']['availableQuests'][0]['questItemHash']
            flashpoint['location'] = self.flashpoint_location(int(flashpoint_quest))
            fp_json = json.loads(mh.query_manifest('DestinyMilestoneDefinition',
                                                   api_response['Response']['463010297']['milestoneHash'])[0][0])
            this_quest = str(api_response['Response']['463010297']['availableQuests'][0]['questItemHash'])
            flashpoint['desc'] = fp_json['quests'][this_quest]['displayProperties']['description']
            flashpoint['name'] = fp_json['quests'][this_quest]['displayProperties']['name']
            flashpoint['icon'] = fp_json['quests'][this_quest]['displayProperties']['icon']
        return flashpoint

    def xur(self, api_response: dict) -> dict:
        """
        Return JSON of Xur, Agent of the Nine for display or email
        EVENT TYPE: Recon Report
        :param api_response: pulled from the public milestones API
        :type api_response: dictionary
        :return: dictionary of nightfall data
        :rtype: dict
        """
        mh = ManifestHelpers()
        flashpoint_quest = int(api_response['Response']['463010297']['availableQuests'][0]['questItemHash'])
        xur = {}
        if '534869653' in api_response['Response']:
            xur = api_response['Response']['534869653']
            xur_json = json.loads(mh.query_manifest('DestinyVendorDefinition',
                                                    api_response['Response']['534869653']['vendors'][0]['vendorHash'])[
                                      0][
                                      0])
            # print('xur_json\n', xur_json)
            # find location:
            if flashpoint_quest != 1268260813 or flashpoint_quest != 3786778617:
                xur['location'] = self.flashpoint_location(int(flashpoint_quest))
            else:
                xur['location'] = "Tower"
        else:
            # xur = api_response['Response']['534869653']
            xur_json = json.loads(mh.query_manifest('DestinyVendorDefinition', 2190858386)[0][0])
            # print('xur_json\n', xur_json)
            xur['name'] = xur_json['displayProperties']['name']
            xur['desc'] = xur_json['displayProperties']['description']
            xur['icon'] = xur_json['displayProperties']['icon']
            xur['location'] = "withdrawn"
        return xur
