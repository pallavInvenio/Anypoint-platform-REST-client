import requests
import property_reader as properties

# Deploy an artifact to a deployment target. Initiates deployment and creates server artifacts.


def post_application(body, authorization_header, ORG_ID, ENV_ID):
    url = properties.get('runtime_manager_url') + '/applications'
    headers_dict = {
        "authorization": authorization_header,
        "X-ANYPNT-ORG-ID": ORG_ID,
        "X-ANYPNT-ENV-ID": ENV_ID
    }
    response = requests.post(url, headers=headers_dict, data=body)
    if response.status_code == 201:
        return response.json()
    return
