from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import BotUttered
import sqlite3
path_to_db = "data.db"


class OrderStatus(Action):
    def name(self) -> Text:
        return "action_order_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # connect to DB
        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()

        # get email slot
        order_email = (tracker.get_slot("email"),)

        # retrieve row based on email
        cursor.execute("SELECT * FROM orders WHERE order_email=?", order_email)
        data_row = cursor.fetchone()

        if data_row:
            # convert tuple to list
            data_list = list(data_row)

            # respond with order status
            dispatcher.utter_message(template="utter_order_status", status=data_list[5])
            connection.close()
            return []
        else:
            # db didn't have an entry with this email
            dispatcher.utter_message(template="utter_no_order")
            connection.close()
            return []

class CancelOrder(Action):
    def name(self) -> Text:
        return "action_cancel_order"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # connect to DB
        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()

        # get email slot
        order_email = (tracker.get_slot("email"),)

        # retrieve row based on email
        cursor.execute("SELECT * FROM orders WHERE order_email=?", order_email)
        data_row = cursor.fetchone()

        if data_row:
            # change status of entry
            status = [("cancelled"), (tracker.get_slot("email"))]
            cursor.execute("UPDATE orders SET status=? WHERE order_email=?", status)
            connection.commit()
            connection.close()

            # confirm cancellation
            dispatcher.utter_message(template="utter_order_cancelled")
            return []
        else:
            # db didn't have an entry with this email
            dispatcher.utter_message(template="utter_no_order")
            connection.close()
            return []


class ReturnOrder(Action):
    def name(self) -> Text:
        return "action_return"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # connect to DB
        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()

        # get email slot
        order_email = (tracker.get_slot("email"),)

        # retrieve row based on email
        cursor.execute("SELECT * FROM orders WHERE order_email=?", order_email)
        data_row = cursor.fetchone()

        if data_row:
            # change status of entry
            status = [("returning"), (tracker.get_slot("email"))]
            cursor.execute("UPDATE orders SET status=? WHERE order_email=?", status)
            connection.commit()
            connection.close()

            # confirm return
            dispatcher.utter_message(template="utter_returned")
            return []
        else:
            # db didn't have an entry with this email
            dispatcher.utter_message(template="utter_no_order")
            connection.close()
            return []

class SurveySubmit(Action):
    def name(self) -> Text:
        return "action_survey_submit"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_open_feedback")
        dispatcher.utter_message(template="utter_survey_end")
        return [SlotSet("survey_complete", True)]


class ActionMenuSearch(Action):
    def name(self) -> Text:
        return "action_menu_search"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # connect to DB
        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()

        # get slots 
        food = [(tracker.get_slot("food"))]

        # place cursor on correct row based on search criteria
        cursor.execute("SELECT * FROM inventory WHERE food=?",food)
        
        # retrieve sqlite row
        data_row = cursor.fetchone()

        if data_row:
            # provide in menu
            dispatcher.utter_message(template="utter_in_menu")
            connection.close()
            slots_to_reset = ["food"]
            return [SlotSet(slot, None) for slot in slots_to_reset]
        else:
            # provide not in menu
            dispatcher.utter_message(template="utter_no_menu")
            connection.close()
            slots_to_reset = ["food"]
            return [SlotSet(slot, None) for slot in slots_to_reset]

class GiveName(Action):
    def name(self) -> Text:
        return "action_give_name"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        evt = BotUttered(
            text = "my name is bot? idk", 
            metadata = {
                "nameGiven": "bot"
            }
        )

        return [evt]

