## meeting + yes
*greet
  - utter_start
*meetings {"option": "New Employee"} 
  - utter_name
*name {"name":"Isabelle Ng"}
  - slot{"name":"Isabelle Ng"}
  - utter_meeting_who
*poc_name {"poc_name":"Marilyn"}
  - slot{"poc_name":"Marilyn"}
  - utter_correct
*affirm
  - utter_inform_poc
  - action_inform_poc
*affirm OR goodbye
  - utter_goodbye
  - action_restart

## meeting + yes
*greet
  - utter_start
*meetings {"option": "Delivery"} 
  - utter_name
*name {"name":"GrabFood"}
  - slot{"name":"GrabFood"}
  - utter_meeting_who
*poc_name {"poc_name":"Wai Foong"}
  - slot{"poc_name":"Wai Foong"}
  - utter_correct
*affirm
  - utter_inform_poc
  - action_inform_poc
*affirm OR goodbye
  - utter_goodbye
  - action_restart

## meeting + no
*greet
  - utter_start
*meetings {"option": "Interview"} 
  - utter_name
*name {"name":"William Quek"}
  - slot{"name":"William Quek"}
  - utter_meeting_who
*poc_name {"poc_name":"San Lin"}
  - slot{"poc_name":"San Lin"}
  - utter_correct
*deny
  - utter_type
  - utter_input
*user_input
  - action_replace_slots
  - utter_inform_poc
  - action_inform_poc
*affirm OR goodbye
  - utter_goodbye
  - action_restart

## meeting + no
*greet
  - utter_start
*meetings {"option": "Servicing"} 
  - utter_name
*name {"name":"Daylight Electrician"}
  - slot{"name":"Daylight Electrician"}
  - utter_meeting_who
*poc_name {"poc_name":"Wai Foong"}
  - slot{"poc_name":"Wai Foong"}
  - utter_correct
*deny
  - utter_type
  - utter_input
*user_input
  - action_replace_slots
  - utter_inform_poc
  - action_inform_poc
*affirm OR goodbye
  - utter_goodbye
  - action_restart


## course registration happy path 
*greet
  - utter_start
*course_registration
  - utter_course_type
*course_type {"course_type":"Artificial Intelligence"}
  - slot{"course_type": "Artificial Intelligence"}
  - utter_check
  - action_find_course
*choose_course {"course_name":"Introduction to Artificial Intelligence"} OR affirm
  - slot{"course_name": "Introduction to Artificial Intelligence"}
  - action_check_advanced
*affirm
  - utter_get_info
*user_info {"user_number":"91234567"}
  - slot{"user_number":"98765432"}
  - utter_registered
  - action_send_sms

## course registration + not avail + yes
*greet
  - utter_start
*course_registration
  - utter_course_type
*course_type {"course_type":"Python Programming"}
  - slot{"course_type": "Python Programming"}
  - utter_check
  - action_find_course
*choose_course {"course_name":"Advanced Python Programming"} OR affirm
  - slot{"course_name": "Advanced Python Programming"}
  - action_check_advanced
  *affirm
  - utter_get_info
*user_info {"user_number":"91234567"}
  - slot{"user_number":"98765432"}
  - utter_registered
  - action_send_sms

## course registration + not avail + no
*greet
  - utter_start
*course_registration
  - utter_course_type
*course_type {"course_type":"machine learning"}
  - slot{"course_type": "machine learning"}
  - utter_check
  - action_find_course
*deny OR not_interested
  - utter_not_interested

## course registration + found + other course + avail + yes
*greet
  - utter_start
*course_registration
  - utter_course_type
*course_type {"course_type":"artificial intelligence"}
  - slot{"course_type": "artificial intelligence"}
  - utter_check
  - action_find_course
*alternate_course {"course_type":"Genetic Algorithms"}
  - slot{"course_type": "Genetic Algorithms"}
  - utter_check
  - action_find_course
*choose_course {"course_name":"Introduction to Artificial Intelligence"} OR affirm
  - slot{"course_name": "Introduction to Artificial Intelligence"}
  - action_check_advanced
  *affirm
  - utter_get_info
*user_info {"user_number":"91234567"}
  - slot{"user_number":"98765432"}
  - utter_registered
  - action_send_sms

## course registration + found + other course + avail + no
*greet
  - utter_start
*course_registration
  - utter_course_type
*course_type {"course_type":"python programming"}
  - slot{"course_type": "python programming"}
  - utter_check
  - action_find_course
*alternate_course {"course_type": "Genetic Algorithms"}
  - slot{"course_type": "Genetic Algorithms"}
  - utter_check
  - action_find_course
*deny OR not_interested
  - utter_not_interested

## course registration + found + other course + not avail + yes
*greet
  - utter_start
*course_registration
  - utter_course_type
*course_type {"course_type": "Machine Learning"}
  - slot{"course_type": "Machine Learning"}
  - utter_check
  - action_find_course
*alternate_course {"course_type": "Genetic Algorithms"}
  - slot{"course_type": "Genetic Algorithms"}
  - utter_check
  - action_find_course
*choose_course {"course_name": "Introduction to Artificial Intelligence"} OR affirm
  - slot{"course_name": "Introduction to Artificial Intelligence"}
  - action_check_advanced
  *affirm
  - utter_get_info
*user_info {"user_number": "91234567"}
  - slot{"user_number": "98765432"}
  - utter_registered
  - action_send_sms

## course registration + found + other course + not avail + no
*greet
  - utter_start
*course_registration
  - utter_course_type
*course_type {"course_type": "Artificial Intelligence"}
  - slot{"course_type": "Artificial Intelligence"}
  - utter_check
  - action_find_course
*alternate_course {"course_type": "Genetic Algorithms"}
  - slot{"course_type": "Genetic Algorithms"}
  - utter_check
  - action_find_course
*deny OR not_interested
  - utter_not_interested

## course registration + found + more info + yes
*greet
  - utter_start
*course_registration
  - utter_course_type
*course_type {"course_type": "Python Programming"}
  - slot{"course_type": "Python Programming"}
  - utter_check
  - action_find_course
*more_information 
  - utter_more_information
*choose_course {"course_name": "Introduction to Python Programming"} OR affirm
  - slot{"course_name": "Introduction to Python Programming"}
  - action_check_advanced
  *affirm
  - utter_get_info
*user_info {"user_number": "91234567"}
  - slot{"user_number": "98765432"}
  - utter_registered
  - action_send_sms

## course registration + found + more info + no
*greet
  - utter_start
*course_registration
  - utter_course_type
*course_type {"course_type": "Machine Learning"}
  - slot{"course_type": "Machine Learning"}
  - utter_check
  - action_find_course
*more_information 
  - utter_more_information
*deny OR not_interested
  - utter_not_interested

## course registration + found + recommendations + yes
*greet
  - utter_start
*course_registration
  - utter_course_type
*course_type {"course_type": "artificial intelligence"}
  - slot{"course_type": "artificial intelligence"}
  - utter_check
  - action_find_course
*bot_pick
  - utter_pick
  - utter_more_information
*choose_course {"course_name": "Intermediate Artificial Intelligence"} OR affirm
  - action_check_advanced
  *affirm
  - utter_get_info
*user_info {"user_number": "91234567"}
  - slot{"user_number": "98765432"}
  - utter_registered
  - action_send_sms

## course registration + found + recommendations + no
*greet
  - utter_start
*course_registration
  - utter_course_type
*course_type {"course_type": "python programming"}
  - slot{"course_type": "python programming"}
  - utter_check
  - action_find_course
*bot_pick
  - utter_pick
  - utter_more_information
*deny OR not_interested
  - utter_not_interested

## skillsfuture
*skillsfuture
  - action_check_slot_skillsfuture
  - action_repeat

## price
*price
  - action_check_slot_price
  - action_repeat

## date
*start_date
  - action_check_slot_date
  - action_repeat

## online
*online
  - utter_online
  - action_repeat

## cancel
*cancel
  - utter_cancel
  - action_repeat

## certification
*certification
  - utter_certified
  - action_repeat

## skillsfuture claim
*skillsfuture_claim
  - utter_skillsfuture_claim
  - action_repeat

## payment
*payment_modes
  - utter_payment
  - action_repeat

## number of lessons
*number_of_lessons
  - utter_lessons
  - action_repeat

## prerequisites
* prerequisites
 - utter_prerequisites

## not_interested
*not_interested
- utter_not_interested

## book rooms happy path
*greet
  - utter_start
*book_room{"book_room": "Book room"}
  - utter_employee_id
*employee_id {"id":"YZ1234"}
  - action_check_id
*room_name
  - meeting_room_form
  - form{"name": "meeting_room_form"}
  - form{"name": null}
*affirm
  - utter_confirm_booking
*affirm OR goodbye
  - utter_goodbye
  - action_restart
  #- action_facial_recognition

## book rooms happy path 2
*greet
  - utter_start
*book_room {"book_room": "Book room"}
  - utter_employee_id
*employee_id {"id":"YZ1234"}
  - action_check_id
*room_name
  - meeting_room_form
  - form{"name": "meeting_room_form"}
  - form{"name": null}
*deny
  - action_clear_slots
 - utter_employee_id
*employee_id {"id":"YZ1234"}
 - action_check_id
*room_name
 - meeting_room_form
 - form{"name": "meeting_room_form"}
 - form{"name": null}
*affirm
 - utter_confirm_booking
*affirm OR goodbye
 - utter_goodbye
 - action_restart
#- action_facial_recognition
  
## book rooms sad path
*greet
  - utter_start
*book_room {"book_room": "Book room"}
  - utter_employee_id
*employee_id {"id":"YZ1234"}
  - action_check_id
*affirm OR goodbye
  - utter_goodbye
  - action_restart
  

#not implemented yet
### office map happy path
#*greet
  #- utter_start
#*map {"map":"map"}
  #- utter_display_map
  #- utter_qr_handoff
  #- action_facial_recognition

## office map sad path 1 (fac recog fail + ID match)
* greet
  - utter_start
* map {"map": "map"}
  - utter_employee_id
* employee_id {"id":"YZ1234"}
  - action_check_id
* affirm OR goodbye
  - utter_goodbye
  - action_restart
  #- action_facial_recognition

#not implemented yet
### notifications happy path
#*greet
  #- utter_start
#*notifications {"notifications": "notifications"}
  #- action_display_notifications
  #- action_facial_recognition

## notifications sad path 1 (fac recog fail + ID match)
* greet
  - utter_start
* notifications {"notifications": "notifications"}
  - utter_employee_id
* employee_id {"id":"YZ1234"}
  - action_check_id
* affirm OR goodbye
  - utter_goodbye
  - action_restart
  #- action_facial_recognition

#not implemented yet
### attendance happy path
#*greet
  #- utter_start
#*attendance {"attendance": "attendance"}
  #- utter_confirm_attendance
  #- action_facial_recognition

## attendance sad path 1 (face recog fail + ID match)
* greet
  - utter_start
* attendance {"attendance": "attendance"}
  - utter_employee_id
* employee_id {"id":"YZ1234"}
  - action_check_id
* affirm OR goodbye
  - utter_goodbye
  - action_restart
  #- action_facial_recognition

## default fallback story
* fallback
  - action_default_fallback

## restart
* restart
  - utter_start
  - action_restart
  
## back/undo last
* undo
  - action_repeat
  - action_back


## isbot
* ask_isbot
  - utter_isbot
  - action_repeat 

## goodbye
* goodbye
 - utter_goodbye
 - action_restart



## interactive_story_1
* greet
    - utter_start
* meetings{"option": "Delivery"}
    - slot{"option": "Delivery"}
    - utter_name
* name{"name": "Grabfood"}
    - slot{"name": "Grabfood"}
    - utter_meeting_who
* poc_name{"poc_name": "Wai Foong"}
    - slot{"poc_name": "Wai Foong"}
    - utter_correct
* affirm
    - utter_inform_poc

## interactive_story_1
* booking_duration{"booking_duration": "3hi"}
    - slot{"booking_duration": "3hi"}

## meeting (new employee happy path)
* greet
    - utter_start
* meetings{"option": "New Employee"}
    - slot{"option": "New Employee"}
    - utter_name
* name{"name": "Bob"}
    - slot{"name": "Bob"}
    - utter_meeting_who
* booking_name{"poc_name": "Wai Foong"}
    - slot{"poc_name": "Wai Foong"}
    - utter_correct
* affirm
    - utter_inform_poc

## interactive_story_1
* greet
    - utter_start
* meetings{"option": "Interview"}
    - slot{"option": "Interview"}
    - utter_name
* name{"name": "Song Yun"}
    - slot{"name": "Song Yun"}
    - utter_meeting_who
* poc_name{"poc_name": "Marilyn"}
    - slot{"poc_name": "Marilyn"}
    - utter_correct
* affirm
    - utter_inform_poc

## interactive_story_1
* greet
    - utter_start
* meetings{"option": "Meeting"}
    - slot{"option": "Meeting"}
    - utter_name
* name{"name": "Luke"}
    - slot{"name": "Luke"}
    - utter_meeting_who
* booking_name{"poc_name": "San Lin"}
    - slot{"poc_name": "San Lin"}
    - utter_correct

## interactive_story_1
* greet
    - utter_start
* meetings{"option": "Servicing"}
    - slot{"option": "Servicing"}
    - utter_name
* name{"name": "Aircon Repair"}
    - slot{"name": "Aircon Repair"}
    - utter_meeting_who
* poc_name{"poc_name": "Wai Foong"}
    - slot{"poc_name": "Wai Foong"}
    - utter_correct



## interactive_story_1
* greet
    - utter_start
* meetings{"option": "Delivery"}
    - slot{"option": "Delivery"}
    - utter_name
