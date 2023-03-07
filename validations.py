import json


class Validations:

    @staticmethod
    def valid_status_code(response, status_code):
        assert status_code == response.status_code, "Status code not as expected"
        print(f"Status code ({status_code}) is valid.")

    @staticmethod
    def check_json_keys(response, expected_keys):
        response_keys = (json.loads(response.text)).keys()
        assert list(response_keys) == expected_keys, "The expected set of keys does not match the actual one."
        print("All keys are available.")

    @staticmethod
    def response_time(response, expected_time):
        assert round(response.elapsed.total_seconds() * 1000) < expected_time, \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {expected_time}ms."
        print(f"Response time({round(response.elapsed.total_seconds() * 1000)}) is less than {expected_time}ms.")

    @staticmethod
    def check_json_value(response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print("Value is wright")
