#This view represents the dataprocessor app which takes the data from the API, processes it and then returns the result.
#It was written by Christian Daish 26-Mar-2024

#Import packages
from django.shortcuts import render
from .main import read_project_file


#Function to pull data from the API and pass it on to the processing modules
def your_view(uploaded_file,threshold_var=''):
    file_name, result = read_project_file(uploaded_file, uploaded_file.name.endswith('.xlsx') and 'xlsx' or 'csv',threshold_var)
    return file_name, result


