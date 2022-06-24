import json
import os

from cerberus import Validator

from src.Customer import Customer


class Api:
    def create_customer(self, payload: dict) -> Customer:
        """
        validates payload and - only if valid - instantiates a Customer
        :param payload: payload containing Customer details
        :return: newly instantiated Customer if payload is valid
        """
        self.validate_payload(payload)

        return Customer(**payload)

    @staticmethod
    def validate_payload(payload: dict):
        """
        validate payload against a Cerberus schema
        :param payload: payload to be validated
        :return: nothing
        """
        with open(os.path.abspath("resources/schema.json")) as f:
            schema = json.loads(f.read())

        validator = Validator()
        validator.validate(payload, schema)

        if validator.errors:
            exit(f"Validation failed: {validator.errors}")
