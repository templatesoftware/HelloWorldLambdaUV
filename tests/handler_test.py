import os
import unittest
from unittest.mock import patch

from hello_world_lambda_uv import lambda_handler


class TestHandler(unittest.TestCase):

    @patch.dict(os.environ, {'AWS_REGION': 'us-west-2'})
    def test_region_parsing_from_env(self):
        context = {
            "function_version": "1.0",
            "aws_request_id": "123456789"
        }
        event = {
            "resource": "/example",
            "httpMethod": "GET",
            "queryStringParameters": {"key1": "value1"}
        }
        response = lambda_handler.handler(
            event,
            context
        )
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(response["headers"], {'Content-Type': 'application/json'})
        self.assertEqual(response["body"], "{\"message\": \"Hello from us-west-2.\"}")

    @patch.dict(os.environ, {'AWS_REGION': 'us-east-1'})
    def test_names_are_extracted_from_event(self):
        context = {
            "function_version": "1.0",
            "aws_request_id": "123456789"
        }
        event = {
            "resource": "/example",
            "httpMethod": "GET",
            "name": "John Smith",
        }
        response = lambda_handler.handler(
            event,
            context
        )
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(response["headers"], {'Content-Type': 'application/json'})
        self.assertEqual(response["body"], "{\"message\": \"Hello John Smith! From us-east-1.\"}")


    @patch.dict(os.environ, {})
    def test_error_code_returned_when_no_region_set(self):
        context = {
            "function_version": "1.0",
            "aws_request_id": "123456789"
        }
        event = {
            "resource": "/example",
            "httpMethod": "GET",
            "queryStringParameters": {"key1": "value1"}
        }
        response = lambda_handler.handler(
            event,
            context
        )
        self.assertEqual(response["statusCode"], 400)
        self.assertEqual(response["body"], "{\"error\": \"No configured region\"}")
