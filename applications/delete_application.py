import requests
import property_reader as properties

# Undeploy artifact from all servers in deployment target and delete the deployment.


def delete_application(application_id, authorization_header, ORG_ID, ENV_ID):
    url = properties.get('runtime_manager_url') + \
        '/applications/{}'.format(application_id)
    headers_dict = {
        "authorization": authorization_header,
        "X-ANYPNT-ORG-ID": ORG_ID,
        "X-ANYPNT-ENV-ID": ENV_ID
    }
    response = requests.delete(url, headers=headers_dict)
    if response.status_code == 204:
        return True
    return False
