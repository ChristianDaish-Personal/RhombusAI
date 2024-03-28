# tests.py
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

class FileUploadAndProcessTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_file_upload_and_processing(self):
        with open('test-data/sample_data.csv', 'rb') as fp:
            response = self.client.post(reverse('file-upload'), {'file': fp}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions here to validate the response content

    def test_invalid_file_upload(self):
        # Simulating an attempted file upload with an empty file
        empty_file = SimpleUploadedFile(name='empty_file.csv', content=b'', content_type='text/csv')
        response = self.client.post(reverse('file-upload'), {'file': empty_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DataProcessingTests(APITestCase):
    def test_data_processing(self):
        """
        Ensure we can submit a file for processing and receive expected output.
        """
        upload_url = reverse('file-upload')  #
        process_url = reverse('view_data')  #

        # Assuming the upload and processing are done together
        upload_data = {
            'file': SimpleUploadedFile('sample_data.csv', b'Name,Value\nTest,123\nTest2,456', content_type='text/csv')}
        upload_response = self.client.post(upload_url, upload_data, format='multipart')

        # The response now contains the processing results directly
        self.assertEqual(upload_response.status_code, status.HTTP_200_OK)
