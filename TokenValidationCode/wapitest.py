from requests.auth import HTTPBasicAuth
import requests
import json

####################################### 1. login module ##########################################
def login_module():
    login_url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/login/authenticate"

    res = requests.get(login_url, auth=HTTPBasicAuth('extuse', 'wSOylMKaeTNekc1'))

    print(res.json())

    response_token = res.json()['token']

    return response_token

###################################### 2. Create Request #########################################
def create_Request(response_token,EmailId):
    request_url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/generic/create_request_generic"

    # Note: Wrong input from Documentation: Content-Type
    headers = {"userPsNo": EmailId, "wolken_token": response_token, "Content-Type": "application/json"}

    data = {"requestMasterVO": {"sourceId": 6, "requestDesc": "Test", "requestedEmail": "testFandLName@gmail.com"}, "descDetailsVO": {"descLarge": "test"}, "userDetails": {"userFname": "testFName", "userLname": "testLname"}}

    res11 = requests.post(url=request_url, data=json.dumps(data), headers=headers)
   
    print(res11)
   
    return res11

##################################### 3. Update Request ###########################################
def update_request(response_token,EmailId):
    update_request_url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/generic/update_request"

    # Note: Wrong input from Documentation: Content-Type
    headers = {"userPsNo": EmailId, "wolken_token": response_token, "Content-Type": "application/json"}

    data = {"requestId": 1513602290, "threadVO": {"resDesc": "Test"}, "otherInfoVO": {"milestoneId": 5}}

    all_request_res = requests.post(url=update_request_url, data=json.dumps(data), headers=headers)
    
    print(all_request_res)

    return all_request_res

#################################### 4. Get All Request #########################################
def get_All_Request(response_token,EmailId):
    all_request_url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/get_all_request"

    # Note: Wrong input from Documentation: Content-Type
    headers = {"userPsNo":EmailId, "wolken_token": response_token, "Content-Type": "application/json"}

    data = {"myRequestDtlCondition": "3"}

    all_request_res = requests.post(url=all_request_url, data=json.dumps(data), headers=headers)
    print(all_request_res.json())

    return all_request_res

#################################### 5. Get Case Details #########################################
def get_case_details(response_token,EmailId):
    url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/specific_request_details?requestId=1470&sections=REQUEST_MASTER"

    headers = {"userPsNo": EmailId, "wolken_token": response_token}

    case_res = requests.get(url=url, headers=headers)

    print(case_res.json())
    return case_res

#################################### 6. Close Request #########################################
def close_Request(response_token,EmailId):
    close_request_url = "https://api-wolken-demo.wolkenservicedesk.com/lur/external/generic/update_request"

    # Note: Wrong input from Documentation: Content-Type
    headers = {"userPsNo": EmailId , "wolken_token": response_token, "Content-Type": "application/json"}

    data = {"requestId": 1513602290, "threadVO": {"resDesc": "Test"}, "otherInfoVO": {"milestoneId": 7}}

    # Note: Wrong input from Documentation: Method
    close_res = requests.get(url=close_request_url, headers=headers, data = json.dumps(data))
    print(close_res.json())
    return close_res
