# This files contains your custom actions which can be used to run
# custom Python code.


from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from TokenValidationCode import wapitest,Regex_validtor,file_saving
from requests.auth import HTTPBasicAuth
import requests
import json
from rasa_sdk.forms import FormAction


# please do follow code for you further reference  
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

######################################### This is for the initlizing the########################################### 
def file_saver(json_format):
    json_dump_out_put = json.dumps(json_format)
    requiredData = json.loads(json_dump_out_put)
    #print(requiredData["message"])
    with open("just.pdf", "w") as outfile:
        outfile.write(json_format) 
    input_string = ''
    for x in requiredData["data"]:
        print("{}".format(requiredData["data"][x])) 
    return requiredData
########################################### initlizing the custom action validation#################################


class Email(FormAction):
    """Collects Email information and adds it to the Api"""

    def name(self):
        return "Email_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [
            "Email",
            ]

    # validating the email id if you want have any custom email id regex equation 
    # already imported the module just pass tha regex patter
    # def validate_Email(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     """Validate Email value."""

    #     if Regex_validator("<patter>",value): -----> change the regex pattern
    #         # validation succeeded, if the ducker recognize it as email
    #         return {"Email": value}
    #     else:
    #         dispatcher.utter_message(template="You have provide us with an incorrect email id format please check and try-again")
    #         # validation failed, set this slot to None, meaning the
    #         # user will be asked for the slot(Email) again
    #         return {"Email": None}

    def validate_Email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate Email value."""
        print(value)
        return {"Email": value}



    def slot_mappings(self):
        """This function will map the intent of the text"""
        return {
        "Email": [self.from_entity(entity="email"),], # This maps the duckling email id
        }


    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:
        '''This function will submit the form'''
        print("I have received the Email id: {}".format(tracker.get_latest_entity_values("Email")))
        dispatcher.utter_message("Saving your email id as {}".format(tracker.get_slot("Email")))
        return []





class GenerateToken(Action):
    """ This class will do custom api and generate the token """
    def name(self) -> Text:
        return "action_Generate_Token"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            generatedToken = wapitest.login_module()
            print(generatedToken)
            dispatcher.utter_message(text="Here is you token for you validation {}".format(generatedToken))
            generatedJson = wapitest.get_All_Request(generatedToken , tracker.get_slot("Email"))
            json_format = generatedJson.json()
            file_saving.file_saver(json_format)
            dispatcher.utter_message(text="now geting the json for you [this]".format(generatedJson.json()))

        except:
            dispatcher.utter_message(text="Sorry there something wrong 😖 with the token.Please contact to the management🏢")
        return []


