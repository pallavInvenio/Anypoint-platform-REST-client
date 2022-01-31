# This is for accessing Anypoint platform - Runtime manager and cloudhub api

import requests

base_url = 'https://anypoint.mulesoft.com'

# for login using username and password
def fetch_access_token(username, password):
    login_path = base_url+'/accounts/login'
    post_data = {"username": username, "password": password}
    r = requests.post(url=login_path, data=post_data)
    if r.status_code == 200:
        print("Login successful")
        return r.json()['access_token']
    else:
        print("Incorrect username or password.")
        return


def fetch_organization_id(authorization_header):
    path = base_url+'/accounts/api/profile'
    headers_dict = {"Authorization": authorization_header}
    r = requests.get(url=path, headers=headers_dict)
    if r.status_code == 200:
        return r.json()['organizationId']
    return


def fetch_environment_id(authorization_header):
    path = base_url+'/accounts/api/profile'
    headers_dict = {"Authorization": authorization_header}
    r = requests.get(url=path, headers=headers_dict)
    if r.status_code == 200:
        return r.json()['organization']['environments'][1]['id']
    return


def fetch_applications(headers_dict):
    path = base_url+'/hybrid/api/v1/applications'
    headers_dict = headers_dict
    r = requests.get(url=path, headers=headers_dict)
    if r.status_code == 200:
        return r.json()
    return


if __name__ == '__main__':
    username = "m_daoud"  # externalize and secure
    password = "Invenio2021"  # externalize and secure
    authorization_header = 'Bearer ' + fetch_access_token(username, password)
    ORG_ID = fetch_organization_id(authorization_header)
    ENV_ID = fetch_environment_id(authorization_header)
    headers_dict = {
        "authorization": authorization_header,
        "X-ANYPNT-ORG-ID": ORG_ID,
        "X-ANYPNT-ENV-ID": ENV_ID
    }
    applications_list = fetch_applications(headers_dict)

    print(applications_list)
