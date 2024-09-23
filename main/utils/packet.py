import json

def unpacking(request, input_type):
    """ 
        Convert http request data into json data
    """
    if input_type == 'json':
        request_body_data = request.body
        request_json_data = json.loads(request_body_data)
        return request_json_data
    elif input_type == 'file':

        form_data_dict = {key: value for key, value in request.POST.items()}

        uploaded_file = request.FILES['file']

        return uploaded_file, form_data_dict
