# This is for accessing Anypoint platform - Runtime manager API

import requests
import property_reader as properties
from applications import view_applications
from applications import view_application
from applications import delete_application
from applications import add_application
from applications import update_application

# for login using username and password


def fetch_access_token(username, password):
    login_path = properties.get('base_url') + '/accounts/login'
    post_data = {"username": username, "password": password}
    r = requests.post(url=login_path, data=post_data)
    if r.status_code == 200:
        return r.json()['access_token']
    return


def fetch_organization_id(authorization_header):
    path = properties.get('base_url') + '/accounts/api/profile'
    headers_dict = {"Authorization": authorization_header}
    r = requests.get(url=path, headers=headers_dict)
    if r.status_code == 200:
        return r.json()['organizationId']
    return


def fetch_environment_id(authorization_header):
    path = properties.get('base_url') + '/accounts/api/profile'
    headers_dict = {"Authorization": authorization_header}
    r = requests.get(url=path, headers=headers_dict)
    if r.status_code == 200:
        return r.json()['organization']['environments'][2]['id']
    return


if __name__ == '__main__':

    # do login
    access_token = fetch_access_token(
        properties.get('username'), properties.get('password'))
    if access_token:
        print("Login successful")
    else:
        print("Incorrect username or password.")

    # fetching header components
    authorization_header = 'Bearer ' + access_token
    ORG_ID = fetch_organization_id(authorization_header)
    ENV_ID = fetch_environment_id(authorization_header)

    # to get applications list
    # applications_list = view_applications.get_applications(
    #     authorization_header, ORG_ID, ENV_ID)
    # print(applications_list)

    # to get application detail based upon application id
    # application_id = 0
    # application_detail = view_application.get_application( application_id, authorization_header, ORG_ID, ENV_ID)
    # print(application_detail)

    # to add an application
    # body = """{
    #     "applicationSource": {
    #         "source": "EXCHANGE",
    #         "groupId": "com.mulesoft.hybrid",
    #         "artifactId": "testApp",
    #         "version": "0.0.2"
    #     },
    #     "targetId": 1,
    #     "artifactName": "myApp"
    # }"""
    # application_detail = add_application.post_application(body, authorization_header, ORG_ID, ENV_ID)
    # print(application_detail)

    # to delete a deployment
    # application_id = 0
    # is_deleted = delete_application.delete_application(
    #     application_id, authorization_header, ORG_ID, ENV_ID)
    # if is_deleted:
    #     print("deleting deployment...")
    # else:
    #     print("failed request to delete deployment")

    # to update a deployment with specific attributes
    # application_id = 0
    # data = """{
    #     "desiredStatus": "STOPPED"
    #     }"""
    # updated_application = update_application.patch_application(
    #     application_id, data, authorization_header, ORG_ID, ENV_ID)
    # print(updated_application)
