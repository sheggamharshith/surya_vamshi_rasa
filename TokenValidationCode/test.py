from requests.auth import HTTPBasicAuth
import requests
import json
import os
from Naked.toolshed.shell import execute_js, muterun_js
import wapitest as tk

def create_Request(response_token,EmailId):
    request_url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/generic/create_request_generic"

    # Note: Wrong input from Documentation: Content-Type
    os.remove("C:\\Users\harsh\\Desktop\\ai intern\\ai intern\\TokenValidationCode\\final_prg\\input_db.json")
    print("File Removed!")
    headers = {"userEmail":EmailId,"wolken_token":response_token,"Content-Type":"application/json"}
    with open('C:\\Users\harsh\\Desktop\\ai intern\\ai intern\\TokenValidationCode\\final_prg\\input_db.json', "w") as write_file:
        json.dump(headers, write_file)
    success = execute_js('.\\final_prg.js')
    with open("C:\\Users\harsh\\Desktop\\ai intern\\ai intern\\TokenValidationCode\\final_prg\\outpt.json", "r") as read_file:
        data = json.load(read_file)
    print(data)
    return data


res = tk.login_module()
data = create_Request(res,"poornima@wolkensoftware.com")
generatedJson = tk.create_Request("sdasdasd" , "email")
            #json_format = generatedJson.json()
            #file_saving.file_saver(json_format)
dispatcher.utter_message(text="now geting the json for you this {}".format(generatedJson))
