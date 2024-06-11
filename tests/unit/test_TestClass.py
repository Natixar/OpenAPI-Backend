""" Test module tests/unit

    © CalCool Studios 2024 2024
    © Natixar SAS 2024
    All rights reserved.
    
    Written by jm on 02/05/2024
    
    [What is tested?}
"""
import pytest


class TestClass:
    @pytest.fixture
    def word(self):
        return "this"
    
    def test_woke(self):
        assert False is True
    
    def test_truism(self, word):
        assert "h" in word

    def test_using_lambda_api(self):
        import boto3
        from botocore.config import Config
        from botocore import UNSIGNED
        
        lambda_client = boto3.client(
            'lambda',
            endpoint_url="http://127.0.0.1:3001",
            use_ssl=False,
            verify=False,
            config=Config(
                signature_version=UNSIGNED,
                   read_timeout=1,
                   retries={'max_attempts': 0}
                   )
            )
        lambda_client.invoke(FunctionName="HelloWorldFunction")