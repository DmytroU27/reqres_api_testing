from api_requests import ReqresInApi
from validations import Validations


class TestSuitPositive:
    def test_get_list_users(self):
        response = ReqresInApi.get_list_users()
        Validations.valid_status_code(response, 200)
        Validations.valid_response_time(response, 600)
        print("Successful GET request")

    def test_get_single_user(self):
        response = ReqresInApi.get_single_user(2)
        Validations.valid_status_code(response, 200)
        Validations.valid_response_time(response, 600)
        print("Successful GET request")

    def test_create_new_user(self):
        response = ReqresInApi.create_new_user("John", "QA engineer")
        Validations.valid_status_code(response, 201)
        Validations.valid_json_keys(response, ["name", "job", "id", "createdAt"])
        Validations.valid_response_time(response, 800)
        print("Successful POST request")

    def test_update_user(self):
        response = ReqresInApi.update_user("Kevin", "Project Manager", 5)
        Validations.valid_status_code(response, 200)
        Validations.valid_json_keys(response, ["name", "job", "updatedAt"])
        Validations.valid_response_time(response, 800)
        print("Successful PUT request")

    def test_delete_user(self):
        response = ReqresInApi.delete_user(2)
        Validations.valid_status_code(response, 204)
        Validations.valid_response_time(response, 800)
        print("Successful DELETE request")
    def test_registration(self):
        response = ReqresInApi.register("eve.holt@reqres.in", "Qwerty")
        Validations.valid_status_code(response, 200)
        Validations.valid_json_keys(response, ["id", "token"])
        Validations.valid_response_time(response, 1000)
        print("Successful POST request")

    def test_login(self):
        response = ReqresInApi.login("eve.holt@reqres.in", "Qwerty")
        Validations.valid_status_code(response, 200)
        Validations.valid_json_keys(response, ["token"])
        Validations.valid_response_time(response, 1000)
        print("Successful POST request")


class TestSuitNegative:
    def test_get_invalid_single_user(self):
        response = ReqresInApi.get_single_user(25)
        Validations.valid_status_code(response, 404)
        Validations.valid_response_time(response, 800)
        print("Single user not found. Empty response.")

    def test_registration_without_email(self):
        response = ReqresInApi.register("", "Qwerty")
        Validations.valid_status_code(response, 400)
        Validations.valid_json_keys(response, ["error"])
        Validations.valid_json_values(response, ["Missing email or username"])
        Validations.valid_response_time(response, 8000)
        print("Error: Missing email or username")

    def test_registration_without_password(self):
        response = ReqresInApi.register("eve.holt@reqres.in", "")
        Validations.valid_status_code(response, 400)
        Validations.valid_json_keys(response, ["error"])
        Validations.valid_json_values(response, ["Missing password"])
        Validations.valid_response_time(response, 8000)
        print("Error: Missing password")

    def test_login_without_email(self):
        response = ReqresInApi.login("", "Qwerty")
        Validations.valid_status_code(response, 400)
        Validations.valid_json_keys(response, ["error"])
        Validations.valid_json_values(response, ["Missing email or username"])
        Validations.valid_response_time(response, 8000)
        print("Error: Missing email or username")

    def test_login_without_password(self):
        response = ReqresInApi.login("eve.holt@reqres.in", "")
        Validations.valid_status_code(response, 400)
        Validations.valid_json_keys(response, ["error"])
        Validations.valid_json_values(response, ["Missing password"])
        Validations.valid_response_time(response, 8000)
        print("Error: Missing password")

