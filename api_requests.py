import requests
import json

base_url = "https://reqres.in/"


class ReqresInApi:

    @staticmethod
    def get_list_users():
        endpoint = "api/users?page=2"
        get_url = base_url + endpoint
        response = requests.get(get_url)
        return response

    @staticmethod
    def get_single_user(id):
        endpoint = f"api/users/{id}"
        get_url = base_url + endpoint
        response = requests.get(get_url)
        return response

    @staticmethod
    def create_new_user(user_name, user_job):
        endpoint = "api/users"
        json_body = {
            "name": f"{user_name}",
            "job": f"{user_job}"
        }
        post_url = base_url + endpoint
        response = requests.post(post_url, json_body)
        return response

    @staticmethod
    def update_user(user_name, user_job, user_id):
        endpoint = f"api/users/{user_id}"
        json_body = {
            "name": f"{user_name}",
            "job": f"{user_job}"
        }
        put_url = base_url + endpoint
        response = requests.put(put_url, json_body)
        return response

    @staticmethod
    def delete_user(user_id):
        endpoint = f"api/users/{user_id}"
        delete_url = base_url + endpoint
        response = requests.delete(delete_url)
        return response

