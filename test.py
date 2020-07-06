from TokenValidationCode import wapitest

import json

res_token = wapitest.login_module()

respq = wapitest.close_Request(res_token,"poornima@wolkensoftware.com")

print(respq.json())
