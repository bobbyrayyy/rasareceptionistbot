# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet # to set a slot
from rasa_sdk.forms import FormAction  # tbc for booking rooms
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import AllSlotsReset


# Data base of courses
COURSES = {
    "introduction to artificial intelligence":
        {
            "name": "Introduction to Artificial Intelligence",
            "type": "Artificial Intelligence",
            "level": "Beginner",
            "skillsfuture": "yes",
            "date": "20 June 2020",
            "price": "$300"
        },
    "introduction to machine learning":
        {
            "name": "Introduction to Machine Learning",
            "type": "Machine Learning",
            "level": "Beginner",
            "skillsfuture": "yes",
            "date": "20 June 2020",
            "price": "$300"
        },
    "introduction to python programming":
        {
            "name": "Introduction to Python Programming",
            "type": "Python Programming",
            "level": "Beginner",
            "skillsfuture": "yes",
            "date": "20 June 2020",
            "price": "$300"
        },
    "intermediate artificial intelligence":
        {
            "name": "Intermediate Artificial Intelligence",
            "type": "Artificial Intelligence",
            "level": "Intermediate",
            "skillsfuture": "no",
            "date": "20 June 2020",
            "price": "$400"
        },
    "intermediate machine learning":
        {
            "name": "Intermediate Machine Learning",
            "type": "Machine Learning",
            "level": "Intermediate",
            "skillsfuture": "yes",
            "date": "20 June 2020",
            "price": "$400"
        },
    "intermediate python programming":
        {
            "name": "Intermediate Python Programming",
            "type": "Python Programming",
            "level": "Intermediate",
            "skillsfuture": "yes",
            "date": "20 June 2020",
            "price": "$400"
        },
    "advanced artificial intelligence":
        {
            "name": "Advanced Artificial Intelligence",
            "type": "Artificial Intelligence",
            "level": "Advanced",
            "skillsfuture": "no",
            "date": "20 June 2020",
            "price": "$500"
        },
    "advanced machine learning":
        {
            "name": "Advanced Machine Learning",
            "type": "Machine Learning",
            "level": "Advanced",
            "skillsfuture": "no",
            "date": "20 June 2020",
            "price": "$500"
        },
    "advanced python programming":
        {
            "name": "Advanced Python Programming",
            "type": "Python Programming",
            "level": "Advanced",
            "skillsfuture": "no",
            "date": "20 June 2020",
            "price": "$500"
        },
}


# Data base of meeting rooms
ROOMS = {
    "Room A":
        {
            "name": "Room A",
            "available time": "12:00-15:00",
            "pax": 10,
        },
    "Room B":
        {
            "name": "Room B",
            "available time": "9:00-17:00",
            "pax": 20,
        },
    "Room C":
        {
            "name": "Room C",
            "available time": "12:00-16:30",
            "pax": 5,
        },
    "Room D":
        {
            "name": "Room D",
            "available time": "9:00-17:00",
            "pax": 5,
        },
     "Room E":
        {
            "name": "Room E",
            "available time": "9:00-17:00",
            "pax": 8,
        },
}


# Data base of staff info
EMPLOYEEID = {
    "YZ1234":
        {
            "name": "Bob Lin",
            "employee id": "YZ1234",
            "department": "AI",
        },
    "YZ5678":
        {
            "name": "Justin Yip",
            "employee id": "YZ5678",
            "department": "AI",
        },
    "YZ0000":
        {
            "name": "Wai Foong",
            "employee id": "YZ0000",
            "department": "AI",
        },
    "YZ1111":
        {
            "name": "Marilyn",
            "employee id": "YZ1111",
            "department": "HR",
        },
     "YZ3011":
        {
            "name": "Song Yun",
            "employee id": "YZ3011",
            "department": "AI",
        },
    }


# to repeat most recent text to drive conversation back to original path after an always on function
class ActionRepeat(Action):

    def name(self) -> Text:
        return "action_repeat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_ignore_count = 3
        count = 0
        tracker_list = []
        consecutive_msgs = False


        while user_ignore_count > 0:
            event = tracker.events[count].get('event')
            if event == 'user':
                user_ignore_count = user_ignore_count - 1
            if event == 'bot':
                tracker_list.append(tracker.events[count])
                if tracker.events[count-2].get('event') == 'bot' and tracker.latest_message.get('text') == 'Undo':
                    consecutive_msgs = True
            count -= 1

        print(tracker_list)
        last_bot_msg = tracker_list[1].get('text')

        i = 1
        if consecutive_msgs and last_bot_msg != "We have these courses. Which course would you like?" :
            i += 1
        if len(tracker_list) > i:
            data = tracker_list[i].get('data')
            if data:
                if "buttons" not in data:
                    dispatcher.utter_message(text=tracker_list[i].get('text'))
                else:
                    dispatcher.utter_message(text=tracker_list[i].get('text'), buttons=data["buttons"])
        return []

# to send message to POC about visitor and purpose of meeting
class ActionInformPoc(Action):

    def name(self) -> Text:
        return "action_inform_poc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        visitor_name = tracker.get_slot("name")
        poc_name = tracker.get_slot("poc_name")
        option = tracker.get_slot("option")

        dispatcher.utter_message(f"Hi {poc_name}! {visitor_name} is here for a {option}, please meet him at the lobby!")

        return []


# to find course with user keyword in the database
class ActionFindCourse(Action):

    def name(self) -> Text:
        return "action_find_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        course_found = []
        course_type = tracker.get_slot("course_type")

        if course_type is None:
            dispatcher.utter_message("Sorry, I didn't catch what type of courses you'll want?")

        else:
            course_info = list(COURSES.values())
            for course in course_info:
                if course_type.lower() in course["type"].lower():
                    course_found.append(course["name"])
                    
            if course_found == []:
                dispatcher.utter_message("Sorry we do not have {} courses at the moment. Try another topic?".format(course_type))

            else:
                buttons = []
                i = min(len(course_found), 3)
                for course in course_found[0:3]:
                    payload = "/choose_course{\"course_name\":\"" + course + "\"}"
                    buttons.append({"title": "{}".format(course), "payload": payload})
                dispatcher.utter_message(text="We have these courses. Which course would you like?", buttons=buttons)
            return []


# to check course level and recommend prerequisites
class ActionCheckAdvanced(Action):

    def name(self) -> Text:
        return "action_check_advanced"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        course_name = tracker.get_slot("course_name")
        
        try:
            if COURSES[course_name.lower()]["level"] == "Intermediate" or COURSES[course_name.lower()]["level"] == "Advanced":
                dispatcher.utter_message("Oh this course is an intermediate/advanced course. It'll be better if you have "
                                         "the required pre-requisites.")
            if COURSES[course_name.lower()]["level"] == "Beginner":
                dispatcher.utter_message("No problem, this course is a beginner course. So, no prerequisites are needed!")
                
        except TypeError:
            dispatcher.utter_message("Sorry, I didn't catch which course you'll want?")
            
        except KeyError:
            dispatcher.utter_message("Sorry, I didn't catch which course you'll want?")
        
        except AttributeError:
            dispatcher.utter_message("Sorry, I didn't catch which course you'll want?")
            
        return []


# to check if course choosen is under skillsfuture
class ActionCheckSlotSkillsfuture(Action):

    def name(self) -> Text:
        return "action_check_slot_skillsfuture"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        course_name = tracker.get_slot("course_name")
        if course_name is None:
            dispatcher.utter_message("Hmm, that will depend on the course that you choose.")

        else:
            if COURSES[course_name.lower()]["skillsfuture"] == "yes":
                dispatcher.utter_message("Oh nice, this course is covered by SkillsFuture. It'll be much cheaper!")
            elif COURSES[course_name.lower()]["skillsfuture"] == "no":
                dispatcher.utter_message("Oh mans, this course is not covered by SkillsFuture.")

        return []


# to check start date of course choosen
class ActionCheckSlotDate(Action):

    def name(self) -> Text:
        return "action_check_slot_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        course_name = tracker.get_slot("course_name")
        if course_name is None:
            dispatcher.utter_message("Hmm, that will depend on the course that you choose.")

        else:
            course_date = COURSES[course_name.lower()]["date"]
            dispatcher.utter_message("Let me check...{} will start on {}.".format(course_name, course_date))

        return []


# to check price of course choosen
class ActionCheckSlotPrice(Action):

    def name(self) -> Text:
        return "action_check_slot_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        course_name = tracker.get_slot("course_name")
        if course_name is None:
            dispatcher.utter_message("Hmm, that will depend on the course that you choose.")

        else:
            course_price = COURSES[course_name.lower()]["price"]
            dispatcher.utter_message("{} is {}."
                                     .format(course_name, course_price))
        return []


# to send confirmation message to course student
class ActionSendSms(Action):

     def name(self) -> Text:
        return "action_send_sms"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        course_name = tracker.get_slot("course_name")
        user_number = tracker.get_slot("user_number")

        dispatcher.utter_message(f"To {user_number}: You have successfully registered for {course_name}.")

        return []

# to display list of rooms and availability to user
class ActionGetAvailRooms(Action):
    
    def name(self) -> Text:
        return "action_get_avail_rooms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        
         dispatcher.utter_message("Sure! Here are the list of rooms and their availability:")
         dispatcher.utter_message(image="./src/roomAvailability.png")
         dispatcher.utter_message(template="utter_ask_room_name")
         return []

# Rasa form to get details from user for booking rooms
class BookingForm(FormAction):

    def name(self) -> Text:
        return "meeting_room_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return ["booking_name", "room_name", "booking_start_time", "booking_duration", "booking_pax"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return{"booking_name": self.from_entity(entity="booking_name", intent=["booking_name"]),
               "room_name": self.from_entity(entity="room_name", intent=["room_name"]),
               "booking_start_time": self.from_entity(entity="booking_start_time", intent=["booking_start_time"]),
               "booking_duration": self.from_entity(entity="booking_duration", intent=["booking_duration"]),
               "booking_pax": self.from_entity(entity="booking_pax", intent=["booking_pax"])}

    def submit(self,dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:

        booking_name = tracker.get_slot("booking_name")
        room_name = tracker.get_slot("room_name")
        booking_start_time = tracker.get_slot("booking_start_time")
        booking_duration = tracker.get_slot("booking_duration")
        booking_pax = tracker.get_slot("booking_pax")

        dispatcher.utter_message(f"Okay {booking_name}, you've indicated to book {room_name} from {booking_start_time} for {booking_duration} with {booking_pax} participants. Shall I go ahead and confirm?")

        return []
    
# Action to validate employee ID
class ActionCheckId(Action):

    def name(self) -> Text:
        return "action_check_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        user_id = tracker.get_slot("id")
        id_verified = False

        if user_id is None:
            dispatcher.utter_message("Sorry, I didn't catch your employee ID?")

        else:
            employee_id = list(EMPLOYEEID.keys())
            for employee in employee_id:
                if user_id == employee:
                    id_verified = True

            if id_verified == False:
                dispatcher.utter_message("Hmm, seems like your employee ID is invalid. You might want to check with HR.")
            else:
                if tracker.get_slot("map") != None:
                    dispatcher.utter_message(template="utter_display_map")
                    
                elif tracker.get_slot("attendance") != None:
                    dispatcher.utter_message(template="utter_confirm_attendance")

                elif tracker.get_slot("notifications") != None:
                    dispatcher.utter_template("utter_display_notif", tracker, False, image="https://tinyurl.com/ycw58qpk")
                    
                elif tracker.get_slot("book_room") != None:
                    booking_name = EMPLOYEEID[user_id]["name"]
                    return[SlotSet("booking_name", booking_name), FollowupAction(name="action_get_avail_rooms")]
        return []


#to replace name slots to those typed by user
class ActionReplaceSlots(Action):

    def name(self) -> Text:
        return "action_replace_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        userInput = tracker.latest_message.get('text')
        visitor_name = userInput.split(":")[1]
        poc_name = userInput.split(":")[2]

        return [SlotSet("name",name), SlotSet("poc_name",poc_name)]


# to clear slots + repeat meeting_room_form
class ActionClearSlots(Action):

     def name(self) -> Text:
            return "action_clear_slots"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("Sorry my bad, let's try again!")
         

         return [AllSlotsReset(), SlotSet("book_room", "Room-booking")]
         


# Action to undo previous step (go back one step)
#class ActionBack(Action):
#    def name(self):

#         return "utter_back"

#    def run(self,dispatcher,tracker,domain):

#        from rasa_core.event import ActionReverted

#        dispatcher,utter_template("utter_back",tracker,silent_fail=True)

#        return [ActionReverted()]

