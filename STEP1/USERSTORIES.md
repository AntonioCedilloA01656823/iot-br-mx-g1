# Challenge: User Stories and Acceptance requirements 


## User Story

According to the situation description and motivations, we accorded to use the following user story:

- "As a flood survivor, I want the system to be able to pinpoint my location and severity of my situation and send a message to the Crisis Management Center - CMC, so that the help team can send the team that can help me and the ones around me accordingly."

- "As an operator, I want to be able to see a dashboard containing all of the messages sent by the the survivors, their locations, and severity levels, so that I can plan for the rescue operations in an effective way."

- "As a flood survivor, I want the system to be able to determine which course of action is best for my situation, sending the appropriate resources depending on the type of damages that occurred."


## Dashboard Requirements

-"As a flood survivor, I want a system that is efficient and easy to use, that work at 100% when is used"

-"As a rescuer, I want a system that shows me in a way i can understand the severity of the survivor and their locations."

-"As an operator, I want the system to have a clear interface that lets me view the current rescue signals, as well as past ones in order to more effectively understand the cause for these disasters."


## Acceptance Criteria

- The system should be able to communicate from the application to the help team, telling the location and severity of the distress call.
- The system should be sent using IoT concepts such as MQTT protocol (mosquitto, central and local brokers)
- The message should contain the severity of the distress call, and the location of the caller with coordinates (latitude, altitude).
- The system should be usable to any Android mobile devices.
- The dashboard will show in a formal and understandable manner all the data recompiled in a database from the android app. 
