from api_requests import ReqresInApi
from validations import Validations


def test_get_list_users():
    response = ReqresInApi.get_list_users()
    Validations.valid_status_code(response, 200)
    Validations.response_time(response, 600)
    print("Successful GET request")


def test_get_single_user():
    response = ReqresInApi.get_single_user(2)
    Validations.valid_status_code(response, 200)
    Validations.response_time(response, 600)
    print("Successful GET request")


def test_create_new_user():
    response = ReqresInApi.create_new_user("John", "QA engineer")
    Validations.valid_status_code(response, 201)
    Validations.check_json_keys(response, ["name", "job", "id", "createdAt"])
    Validations.response_time(response, 800)
    print("Successful POST request")


def test_update_user():
    response = ReqresInApi.update_user("Kevin", "Project Manager", 5)
    Validations.valid_status_code(response, 200)
    Validations.check_json_keys(response, ["name", "job", "updatedAt"])
    Validations.response_time(response, 800)
    print("Successful PUT request")


def test_delete_user():
    response = ReqresInApi.delete_user(2)
    Validations.valid_status_code(response, 204)
    Validations.response_time(response, 800)
    print("Successful DELETE request")