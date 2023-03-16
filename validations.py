import json


class Validations:

    @staticmethod
    def valid_status_code(response, status_code):
        assert status_code == response.status_code, "Status code not as expected."
        print(f"Status code ({status_code}) is valid.")

    @staticmethod
    def valid_json_keys(response, expected_keys):
        response_keys = (json.loads(response.text)).keys()
        assert list(response_keys) == expected_keys, "The expected set of keys does not match the actual one."
        print("All keys are available.")

    @staticmethod
    def valid_json_values(response, expected_keys):
        response_values = (json.loads(response.text)).values()
        assert expected_keys in list(response_values) or expected_keys == list(response_values), \
            "The expected values do not match the actual one."
        print("All values are available.")

    @staticmethod
    def valid_response_time(response, expected_time):
        assert round(response.elapsed.total_seconds() * 1000) < expected_time, \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {expected_time}ms."
        print(f"Response time({round(response.elapsed.total_seconds() * 1000)}) is less than {expected_time}ms.")
