import requests
import property_reader as properties

# to get a application deployment and status info from runtime manager
# by providing application id as uri parameters


def get_application(application_id, authorization_header, ORG_ID, ENV_ID):
    url = properties.get('runtime_manager_url') + \
        '/applications/{}'.format(application_id)
    headers_dict = {
        "authorization": authorization_header,
        "X-ANYPNT-ORG-ID": ORG_ID,
        "X-ANYPNT-ENV-ID": ENV_ID
    }
    response = requests.get(url, headers=headers_dict)
    if response.status_code == 200:
        return response.json()
    return
