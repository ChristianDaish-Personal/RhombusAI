#This view represents the API module that imports data from the front end and then exports processed data back.
#This was written 26-MAR-2024 by Christian Daish

#Import packages
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import FileUploadSerializer
from django.http import JsonResponse
from django.core.cache import cache
from dataprocessor.views import your_view

#This class pulls the data from the front end and pushes it to the back end.
class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            # Extract the uploaded file using validated data
            uploaded_file = file_serializer.validated_data['file']
            threshold_var = request.data.get('threshold_var','') # Extract threshold_var from request
            uploaded_file.seek(0)

            #Clear the cache so that files are not overloaded
            cache.clear()
            #Process the file
            try:
                processing_result = your_view(uploaded_file,threshold_var)

                # Converting Series indexes and values to strings and organizing them in a dictionary
                index_value_dict = {str(index): str(value) for index, value in processing_result[1].items()}

                # Extracting the key data from the dictionary
                processed_data = {"data":[index_value_dict]}
                processed_data = processed_data["data"][0]

                #Store processed data in cache
                cache.clear()
                cache.set('processed_file_data',processed_data,timeout=300)

                #return the data to the front end
                return JsonResponse(processed_data,safe=True, status=200)
            except Exception as e:
                return JsonResponse({'error':str(e)},status=400)
        else:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

    #Function to retrieve the processed data immediately after it has been uploaded.
    def get(self,request, *args, **kwargs):
        #Handle GET request: Fetch and return information
        processed_data = cache.get('processed_file_data')
        if processed_data:
            return JsonResponse(processed_data,safe=True, status=200)
        else:
            return JsonResponse({'error': 'No processed data available'}, status=400)



