from django.test import TestCase

# Create your tests here.
"""
test api
"""
import json
from django.test import TestCase, Client
import requests


class FileManagerTest(TestCase):
    """
        test file manager
    """

    def test_decorator(self):
        """
        pass
        """
        # Upload
        url = "http://192.168.190.150:40676/api/v0.1/file_operation/PreprocessingImageFileManager/upload"

        headers = {
            'Uid': '27c01ebc-d960-4de5-801c-3a8786459ec6'
            # Header Rule: leading character must be Uppercase
        }
        files = [
            ('preprocessing_image_file', open('./Dockerfile', 'rb'))
        ]
        response = requests.post(
            url=url,
            files=files,
            headers=headers
        )
        print(response.json())

        # Download
        payload = {
            'preprocessing_image_uid': '27c01ebc-d960-4de5-801c-3a8786459ec6',
        }
        url2 = "http://192.168.190.150:40676/api/v0.1/file_operation/PreprocessingImageFileManager/download"
        response = requests.post(
            url=url2,
            json=payload,
        )
        print(response.json())

        self.assertEqual(response.status_code, 200)
