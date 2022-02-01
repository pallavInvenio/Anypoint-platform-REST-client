import requests
import property_reader as properties

# to get applications list from runtime manager


def get_applications(authorization_header, ORG_ID, ENV_ID):
    url = properties.get('runtime_manager_url') + '/applications'
    headers_dict = {
        "authorization": authorization_header,
        "X-ANYPNT-ORG-ID": ORG_ID,
        "X-ANYPNT-ENV-ID": ENV_ID
    }
    response = requests.get(url, headers=headers_dict)
    if response.status_code == 200:
        return response.json()
    return
