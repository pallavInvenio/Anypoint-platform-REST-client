import requests
import property_reader as properties
import view_application

# Redeploys the app with a new artifact.


def patch_application(application_id, body, authorization_header, ORG_ID, ENV_ID):
    url = properties.get('runtime_manager_url') + \
        '/applications/{}'.format(application_id)
    headers_dict = {
        "authorization": authorization_header,
        "X-ANYPNT-ORG-ID": ORG_ID,
        "X-ANYPNT-ENV-ID": ENV_ID
    }
    response = requests.patch(url, headers=headers_dict, data=body)
    if response.status_code == 200:
        return view_application.get_application(application_id, authorization_header, ORG_ID, ENV_ID)
    elif response.status_code == 202:
        return response.json()
    return
