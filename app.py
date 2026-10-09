# import streamlit as st
# from openai import OpenAI

# # Setting up the configuration for streamlit page

# st.set_page_config(page_title="Streamlit Chat", page_icon=":speech_balloon:")

# st.title("Chatbot")

# # Initializing openAI client.

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# # Setting up the moel by creating a session state

# if "openai_model" not in st.session_state:
#   st.session_state['openai_model'] = 'gpt-4.1'


# # IMPLEMENTING THE CHAT FUNCTIONALITY

# if  "messages" not in st.session_state:
#   st.session_state['messages'] = [{"role": "system", "content": "You are a helpful tool that talks like a pirate"}]


# # /////////////////////

# # Displaying the chat history

# for message in st.session_state.messages:
#   if message['role'] != "system":
#     with st.chat_message(message['role']):
#       st.markdown(message['content'])

# # /////////////////////////

# if prompt := st.chat_input("Your answer"):
#   st.session_state.messages.append({"role":"user", "content": prompt})
#   with st.chat_message("user"):
#     st.markdown(prompt)

#   with st.chat_message("assistant"):
#     stream = client.chat.completions.create(
#       model=st.session_state['openai_model'],
#       messages=[
#        { "role": m['role'],
#         "content": m["content"]}
#         for m in st.session_state.messages
#       ],
#       stream=True,
#     )
#     response = st.write_stream(stream)
#   st.session_state.messages.append({"role": "assistant", "content": response})




# /////////////////////////////////

# BUILDING THE SETUP PAGE

# ///////////////////////////////


# import streamlit as st
# from openai import OpenAI

# # Setting up the configuration for streamlit page

# st.set_page_config(page_title="Streamlit Chat", page_icon=":speech_balloon:")

# st.title("Chatbot")

# # /////////////////////////////////

# # Sub-header for personal innformation

# st.subheader('Personal information', divider='rainbow')

# # Textbox for users name

# name = st.text_input(label="Name", max_chars=None, placeholder="Enter your name")


# # Experience and skills (text areas)

# experience = st.text_area(label= "Experience", value="", height=None, max_chars=None, placeholder="Enter your experience")


# skills = st.text_area(label= "Skills", value="", height=None, max_chars=None, placeholder="List your skills")


# # Creatting a label to display the users input and confirm that the Textboxes function correctly

# st.write(f"**Your Name**: {name}")
# st.write(f"**Your Experience**: {experience}")
# st.write(f"**Your skills**: {skills}")


# # Field for company and Position

# st.subheader('Company and Position', divider='rainbow')

# col1, col2 = st.columns(2)

# with col1:
#   level = st.radio("Choose level", key="visibility", options=['Junior', 'Mid-level', 'Senior'])


# # Now for position


# with col2:
#   position = st.selectbox("Choose a position", options=['Data Engineer', 'Data Scientist', 'ML Engineer', 'UX Designer'])


# # for companies

# company = st.selectbox("Choose a company", ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify"))


# st.write(f"**Your information**: {level} {position} at {company}")

# # Initializing openAI client.

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# # Setting up the moel by creating a session state

# if "openai_model" not in st.session_state:
#   st.session_state['openai_model'] = 'gpt-4.1'


# # IMPLEMENTING THE CHAT FUNCTIONALITY

# if  "messages" not in st.session_state:
#   st.session_state['messages'] = [{"role": "system", "content": f"You are an HR executive that interviews an interiewee called {name} with experience {experience} and skills {skills}. You should interview them for the position {level} {position} at the company {company}"}]


# # /////////////////////

# # Displaying the chat history

# for message in st.session_state.messages:
#   if message['role'] != "system":
#     with st.chat_message(message['role']):
#       st.markdown(message['content'])

# # /////////////////////////

# if prompt := st.chat_input("Your answer"):
#   st.session_state.messages.append({"role":"user", "content": prompt})
#   with st.chat_message("user"):
#     st.markdown(prompt)

#   with st.chat_message("assistant"):
#     stream = client.chat.completions.create(
#       model=st.session_state['openai_model'],
#       messages=[
#        { "role": m['role'],
#         "content": m["content"]}
#         for m in st.session_state.messages
#       ],
#       stream=True,
#     )
#     response = st.write_stream(stream)
#   st.session_state.messages.append({"role": "assistant", "content": response})



# ///////////////////////////////////////////////////

# Enchancinig Chatbot Interaction with Session State

# ////////////////////////////////////////////////////////


# import streamlit as st
# from openai import OpenAI

# # Setting up the configuration for streamlit page

# st.set_page_config(page_title="Streamlit Chat", page_icon=":speech_balloon:")

# st.title("Chatbot")

# # Here, we need to track whether the setup for the interview is complete.

# if "setup_complete" not in st.session_state:
#   st.session_state['setup_complete'] = False


# # A function that toggle the setup phase completion(cleaner)

# def complete_setup():
#   st.session_state.setup_complete = True


# # SHowing the setup form onlu if the setup is complete

# if not st.session_state.setup_complete:

#   # /////////////////////////////////

#   # Sub-header for personal innformation

#   st.subheader('Personal information', divider='rainbow')

#   if "name" not in st.session_state:
#     st.session_state["name"] = ""
#   if "experience" not in st.session_state:
#     st.session_state["experience"] = "" 
#   if "skills" not in st.session_state:
#     st.session_state["skills"] = ""
#   # Textbox for users name

#   st.session_state["name"] = st.text_input(label="Name", value=st.session_state['name'], max_chars=None, placeholder="Enter your name")


#   # Experience and skills (text areas)

#   st.session_state["experience"] = st.text_area(label= "Experience", height=None, max_chars=None, value=st.session_state['experience'], placeholder="Enter your experience")


#   st.session_state["skills"] = st.text_area(label= "Skills", value=st.session_state['skills'], height=None, max_chars=None, placeholder="List your skills")


#   # Creatting a label to display the users input and confirm that the Textboxes function correctly

#   st.write(f"**Your Name**: {st.session_state["name"]}")
#   st.write(f"**Your Experience**: {st.session_state["experience"]}")
#   st.write(f"**Your skills**: {st.session_state["skills"]}")


#   # Field for company and Position

#   st.subheader('Company and Position', divider='rainbow')

#   # Initializing session state for company and postion

#   if "level" not in st.session_state:
#     st.session_state['level'] = "Junior"
#   if "position" not in st.session_state:
#     st.session_state['position'] = "Data Scientist"
#   if "company" not in st.session_state:
#     st.session_state['company'] = "Amazon"

#   col1, col2 = st.columns(2)

#   with col1:
#     st.session_state['level']  = st.radio("Choose level", key="visibility", options=['Junior', 'Mid-level', 'Senior'])


#   # Now for position


#   with col2:
#      st.session_state['position'] = st.selectbox("Choose a position", options=['Data Engineer', 'Data Scientist', 'ML Engineer', 'UX Designer'])


#   # for companies

#   st.session_state['company'] = st.selectbox("Choose a company", ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify"))


#   st.write(f"**Your information**: {st.session_state['level']} {st.session_state['position']} at {st.session_state['company']}")

#   if st.button("Start Interview", on_click=complete_setup):
#     st.write("Setup complete. Starting interview....")



# # Now, when setup is set to true, our chatbox should run

# if st.session_state.setup_complete:

#   # Adding an info box to make it more engaging

#   st.info(
#     '''
#     Start by introducing yourself
# ''',
# icon=""
#   )


#   # Initializing openAI client.

#   client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

#   # Setting up the moel by creating a session state

#   if "openai_model" not in st.session_state:
#     st.session_state['openai_model'] = 'gpt-4.1'


#   # IMPLEMENTING THE CHAT FUNCTIONALITY

#   if  "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "system", "content": f"You are an HR executive that interviews an interiewee called {st.session_state["name"]} with experience {st.session_state["experience"]} and skills {st.session_state["skills"]}. You should interview them for the position {st.session_state["level"]} {st.session_state["position"]} at the company {st.session_state["company"]}"}]


#   # /////////////////////

#   # Displaying the chat history

#   for message in st.session_state.messages:
#     if message['role'] != "system":
#       with st.chat_message(message['role']):
#         st.markdown(message['content'])

#   # /////////////////////////

#   if prompt := st.chat_input("Your answer"):
#     st.session_state.messages.append({"role":"user", "content": prompt})
#     with st.chat_message("user"):
#       st.markdown(prompt)

#     with st.chat_message("assistant"):
#       stream = client.chat.completions.create(
#         model=st.session_state['openai_model'],
#         messages=[
#         { "role": m['role'],
#           "content": m["content"]}
#           for m in st.session_state.messages
#         ],
#         stream=True,
#       )
#       response = st.write_stream(stream)
#     st.session_state.messages.append({"role": "assistant", "content": response})


# /////////////////////////////////////////////////

# REFINING OUR PROKECT FOR THE FEEBACK

# ///////////////////////////////////////////


# import streamlit as st
# from openai import OpenAI

# # Setting up the configuration for streamlit page

# st.set_page_config(page_title="Streamlit Chat", page_icon=":speech_balloon:")

# st.title("Chatbot")

# # Here, we need to track whether the setup for the interview is complete.

# if "setup_complete" not in st.session_state:
#   st.session_state['setup_complete'] = False

# # Keep track of no of user's message

# if "user_message_count" not in st.session_state:
#   st.session_state['user_message_count'] = 0

# # Session state tracking to show if the user has been given feedback in the inyerview

# if "feedback_shown" not in st.session_state:
#   st.session_state['feedback_shown'] = False


# # Messages Initialization (storing the conversation historu)

# if "messages" not in st.session_state:
#   st.session_state.message = []


# #  State to manage completion of interview

# if "chat_complete" not in st.session_state:

#   st.session_state.chat_complete = False

# # A function that toggle the setup phase completion(cleaner)

# def complete_setup():
#   st.session_state.setup_complete = True


# # Function to toggle the feedback display

# def show_feedback():
#   st.session_state.feedback_shown = True

# # SHowing the setup form onlu if the setup is complete

# if not st.session_state.setup_complete:

#   # /////////////////////////////////

#   # Sub-header for personal innformation

#   st.subheader('Personal information', divider='rainbow')

#   if "name" not in st.session_state:
#     st.session_state["name"] = ""
#   if "experience" not in st.session_state:
#     st.session_state["experience"] = "" 
#   if "skills" not in st.session_state:
#     st.session_state["skills"] = ""
#   # Textbox for users name

#   st.session_state["name"] = st.text_input(label="Name", value=st.session_state['name'], max_chars=40, placeholder="Enter your name")


#   # Experience and skills (text areas)

#   st.session_state["experience"] = st.text_area(label= "Experience", height=None, max_chars=200, value=st.session_state['experience'], placeholder="Enter your experience")


#   st.session_state["skills"] = st.text_area(label= "Skills", value=st.session_state['skills'], height=None, max_chars=200, placeholder="List your skills")


#   # Creatting a label to display the users input and confirm that the Textboxes function correctly

#   st.write(f"**Your Name**: {st.session_state["name"]}")
#   st.write(f"**Your Experience**: {st.session_state["experience"]}")
#   st.write(f"**Your skills**: {st.session_state["skills"]}")


#   # Field for company and Position

#   st.subheader('Company and Position', divider='rainbow')

#   # Initializing session state for company and postion

#   if "level" not in st.session_state:
#     st.session_state['level'] = "Junior"
#   if "position" not in st.session_state:
#     st.session_state['position'] = "Data Scientist"
#   if "company" not in st.session_state:
#     st.session_state['company'] = "Amazon"

#   col1, col2 = st.columns(2)

#   with col1:
#     st.session_state['level']  = st.radio("Choose level", key="visibility", options=['Junior', 'Mid-level', 'Senior'])


#   # Now for position


#   with col2:
#      st.session_state['position'] = st.selectbox("Choose a position", options=['Data Engineer', 'Data Scientist', 'ML Engineer', 'UX Designer'])


#   # for companies

#   st.session_state['company'] = st.selectbox("Choose a company", ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify"))


#   st.write(f"**Your information**: {st.session_state['level']} {st.session_state['position']} at {st.session_state['company']}")

#   if st.button("Start Interview", on_click=complete_setup):
#     st.write("Setup complete. Starting interview....")



# # Now, when setup is set to true, our chatbox should run

# if st.session_state.setup_complete:

#   # Adding an info box to make it more engaging

#   st.info(
#     '''
#     Start by introducing yourself
# ''',
# icon=""
#   )


#   # Initializing openAI client.

#   client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

#   # Setting up the moel by creating a session state

#   if "openai_model" not in st.session_state:
#     st.session_state['openai_model'] = 'gpt-4.1'


#   # IMPLEMENTING THE CHAT FUNCTIONALITY

#   if  "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "system", "content": f"You are an HR executive that interviews an interiewee called {st.session_state["name"]} with experience {st.session_state["experience"]} and skills {st.session_state["skills"]}. You should interview them for the position {st.session_state["level"]} {st.session_state["position"]} at the company {st.session_state["company"]}"}]


#   # /////////////////////

#   # Displaying the chat history

#   for message in st.session_state.messages:
#     if message['role'] != "system":
#       with st.chat_message(message['role']):
#         st.markdown(message['content'])

#   # /////////////////////////

#   if prompt := st.chat_input("Your answer", max_chars=1000):
#     st.session_state.messages.append({"role":"user", "content": prompt})
#     with st.chat_message("user"):
#       st.markdown(prompt)

#     with st.chat_message("assistant"):
#       stream = client.chat.completions.create(
#         model=st.session_state['openai_model'],
#         messages=[
#         { "role": m['role'],
#           "content": m["content"]}
#           for m in st.session_state.messages
#         ],
#         stream=True,
#       )
#       response = st.write_stream(stream)
#     st.session_state.messages.append({"role": "assistant", "content": response})

# /////////////////////////////////////////////////

# Implementing Feedback Functionality: Part 1

# //////////////////////////////////////////////////


# import streamlit as st
# from openai import OpenAI

# # Setting up the configuration for streamlit page

# st.set_page_config(page_title="Streamlit Chat", page_icon=":speech_balloon:")

# st.title("Chatbot")

# # Here, we need to track whether the setup for the interview is complete.

# if "setup_complete" not in st.session_state:
#   st.session_state['setup_complete'] = False

# # Keep track of no of user's message

# if "user_message_count" not in st.session_state:
#   st.session_state['user_message_count'] = 0

# # Session state tracking to show if the user has been given feedback in the inyerview

# if "feedback_shown" not in st.session_state:
#   st.session_state['feedback_shown'] = False


# # Messages Initialization (storing the conversation historu)

# if "messages" not in st.session_state:
#   st.session_state.messages = []


# #  State to manage completion of interview

# if "chat_complete" not in st.session_state:

#   st.session_state.chat_complete = False

# # A function that toggle the setup phase completion(cleaner)

# def complete_setup():
#   st.session_state.setup_complete = True


# # Function to toggle the feedback display

# def show_feedback():
#   st.session_state.feedback_shown = True

# # SHowing the setup form onlu if the setup is complete

# if not st.session_state.setup_complete:

#   # /////////////////////////////////

#   # Sub-header for personal innformation

#   st.subheader('Personal information', divider='rainbow')

#   if "name" not in st.session_state:
#     st.session_state["name"] = ""
#   if "experience" not in st.session_state:
#     st.session_state["experience"] = "" 
#   if "skills" not in st.session_state:
#     st.session_state["skills"] = ""
#   # Textbox for users name

#   st.session_state["name"] = st.text_input(label="Name", value=st.session_state['name'], max_chars=40, placeholder="Enter your name")


#   # Experience and skills (text areas)

#   st.session_state["experience"] = st.text_area(label= "Experience", height=None, max_chars=200, value=st.session_state['experience'], placeholder="Enter your experience")


#   st.session_state["skills"] = st.text_area(label= "Skills", value=st.session_state['skills'], height=None, max_chars=200, placeholder="List your skills")


#   # Creatting a label to display the users input and confirm that the Textboxes function correctly

#   st.write(f"**Your Name**: {st.session_state["name"]}")
#   st.write(f"**Your Experience**: {st.session_state["experience"]}")
#   st.write(f"**Your skills**: {st.session_state["skills"]}")


#   # Field for company and Position

#   st.subheader('Company and Position', divider='rainbow')

#   # Initializing session state for company and postion

#   if "level" not in st.session_state:
#     st.session_state['level'] = "Junior"
#   if "position" not in st.session_state:
#     st.session_state['position'] = "Data Scientist"
#   if "company" not in st.session_state:
#     st.session_state['company'] = "Amazon"

#   col1, col2 = st.columns(2)

#   with col1:
#     st.session_state['level']  = st.radio("Choose level", key="visibility", options=['Junior', 'Mid-level', 'Senior'])


#   # Now for position


#   with col2:
#      st.session_state['position'] = st.selectbox("Choose a position", options=['Data Engineer', 'Data Scientist', 'ML Engineer', 'UX Designer'])


#   # for companies

#   st.session_state['company'] = st.selectbox("Choose a company", ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify"))


#   st.write(f"**Your information**: {st.session_state['level']} {st.session_state['position']} at {st.session_state['company']}")

#   if st.button("Start Interview", on_click=complete_setup):
#     st.write("Setup complete. Starting interview....")



# # Now, when setup is set to true, our chatbox should run

# # So here, we are adding more conditions to the if statement to determine the next phase of the application flow

# if st.session_state.setup_complete and not st.session_state.feedback_shown and not st.session_state.chat_complete:

#   # Adding an info box to make it more engaging

#   st.info(
#     '''
#     Start by introducing yourself
# ''',
# icon=""
#   )


#   # Initializing openAI client.

#   client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

#   # Setting up the moel by creating a session state

#   if "openai_model" not in st.session_state:
#     st.session_state['openai_model'] = 'gpt-4.1'


#   # IMPLEMENTING THE CHAT FUNCTIONALITY

#   if not st.session_state.messages:
#     st.session_state.messages = [{"role": "system", "content": f"You are an HR executive that interviews an interiewee called {st.session_state["name"]} with experience {st.session_state["experience"]} and skills {st.session_state["skills"]}. You should interview them for the position {st.session_state["level"]} {st.session_state["position"]} at the company {st.session_state["company"]}"}]


#   # /////////////////////

#   # Displaying the chat history

#   for message in st.session_state.messages:
#     if message['role'] != "system":
#       with st.chat_message(message['role']):
#         st.markdown(message['content'])

#   # /////////////////////////

#   # Checking if the user has sent 5 fewer messages

#   if st.session_state.user_message_count < 5:
#     if prompt := st.chat_input("Your answer", max_chars=1000):
#       st.session_state.messages.append({"role":"user", "content": prompt})
#       with st.chat_message("user"):
#         st.markdown(prompt)

#         # To ensure the chatbox stop responding after a specific number of user message

#       if st.session_state.user_message_count < 4:
#         with st.chat_message("assistant"):
#           stream = client.chat.completions.create(
#             model=st.session_state['openai_model'],
#             messages=[
#             { "role": m['role'],
#               "content": m["content"]}
#               for m in st.session_state.messages
#             ],
#             stream=True,
#           )
#           response = st.write_stream(stream)
#         st.session_state.messages.append({"role": "assistant", "content": response})
#       st.session_state.user_message_count += 1

#   # ///////////////////////

#   # checking if the user has sent 5 messages, indicating that the interview is complete.

#   if st.session_state.user_message_count >= 5:
#     st.session_state.chat_complete = True


# IMPLEMETING FEEDBACK FUNCTIONALITY: PART 2


import streamlit as st
from openai import OpenAI

# Importing streamlit-js-eval

from streamlit_js_eval import streamlit_js_eval

# Setting up the configuration for streamlit page

st.set_page_config(page_title="Streamlit Chat", page_icon=":speech_balloon:")

st.title("Chatbot")

# Here, we need to track whether the setup for the interview is complete.

if "setup_complete" not in st.session_state:
  st.session_state['setup_complete'] = False

# Keep track of no of user's message

if "user_message_count" not in st.session_state:
  st.session_state['user_message_count'] = 0

# Session state tracking to show if the user has been given feedback in the inyerview

if "feedback_shown" not in st.session_state:
  st.session_state['feedback_shown'] = False


# Messages Initialization (storing the conversation historu)

if "messages" not in st.session_state:
  st.session_state.messages = []


#  State to manage completion of interview

if "chat_complete" not in st.session_state:

  st.session_state.chat_complete = False

# A function that toggle the setup phase completion(cleaner)

def complete_setup():
  st.session_state.setup_complete = True


# Function to toggle the feedback display

def show_feedback():
  st.session_state.feedback_shown = True

# SHowing the setup form onlu if the setup is complete

if not st.session_state.setup_complete:

  # /////////////////////////////////

  # Sub-header for personal innformation

  st.subheader('Personal information', divider='rainbow')

  if "name" not in st.session_state:
    st.session_state["name"] = ""
  if "experience" not in st.session_state:
    st.session_state["experience"] = "" 
  if "skills" not in st.session_state:
    st.session_state["skills"] = ""
  # Textbox for users name

  st.session_state["name"] = st.text_input(label="Name", value=st.session_state['name'], max_chars=40, placeholder="Enter your name")


  # Experience and skills (text areas)

  st.session_state["experience"] = st.text_area(label= "Experience", height=None, max_chars=200, value=st.session_state['experience'], placeholder="Enter your experience")


  st.session_state["skills"] = st.text_area(label= "Skills", value=st.session_state['skills'], height=None, max_chars=200, placeholder="List your skills")


  # Creatting a label to display the users input and confirm that the Textboxes function correctly

  # st.write(f"**Your Name**: {st.session_state["name"]}")
  # st.write(f"**Your Experience**: {st.session_state["experience"]}")
  # st.write(f"**Your skills**: {st.session_state["skills"]}")


  # Field for company and Position

  st.subheader('Company and Position', divider='rainbow')

  # Initializing session state for company and postion

  if "level" not in st.session_state:
    st.session_state['level'] = "Junior"
  if "position" not in st.session_state:
    st.session_state['position'] = "Data Scientist"
  if "company" not in st.session_state:
    st.session_state['company'] = "Amazon"

  col1, col2 = st.columns(2)

  with col1:
    st.session_state['level']  = st.radio("Choose level", key="visibility", options=['Junior', 'Mid-level', 'Senior'])


  # Now for position


  with col2:
     st.session_state['position'] = st.selectbox("Choose a position", options=['Data Engineer', 'Data Scientist', 'ML Engineer', 'UX Designer'])


  # for companies

  st.session_state['company'] = st.selectbox("Choose a company", ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify"))


  st.write(f"**Your information**: {st.session_state['level']} {st.session_state['position']} at {st.session_state['company']}")

  if st.button("Start Interview", on_click=complete_setup):
    st.write("Setup complete. Starting interview....")



# Now, when setup is set to true, our chatbox should run

# So here, we are adding more conditions to the if statement to determine the next phase of the application flow

if st.session_state.setup_complete and not st.session_state.feedback_shown and not st.session_state.chat_complete:

  # Adding an info box to make it more engaging

  st.info(
    '''
    Start by introducing yourself
''',
icon=""
  )


  # Initializing openAI client.

  client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

  # Setting up the moel by creating a session state

  if "openai_model" not in st.session_state:
    st.session_state['openai_model'] = 'gpt-4.1'


  # IMPLEMENTING THE CHAT FUNCTIONALITY

  if not st.session_state.messages:
    st.session_state.messages = [{"role": "system", "content": f"You are an HR executive that interviews an interiewee called {st.session_state["name"]} with experience {st.session_state["experience"]} and skills {st.session_state["skills"]}. You should interview them for the position {st.session_state["level"]} {st.session_state["position"]} at the company {st.session_state["company"]}"}]


  # /////////////////////

  # Displaying the chat history

  for message in st.session_state.messages:
    if message['role'] != "system":
      with st.chat_message(message['role']):
        st.markdown(message['content'])

  # /////////////////////////

  # Checking if the user has sent 5 fewer messages

  if st.session_state.user_message_count < 5:
    if prompt := st.chat_input("Your answer", max_chars=1000):
      st.session_state.messages.append({"role":"user", "content": prompt})
      with st.chat_message("user"):
        st.markdown(prompt)

        # To ensure the chatbox stop responding after a specific number of user message

      if st.session_state.user_message_count < 4:
        with st.chat_message("assistant"):
          stream = client.chat.completions.create(
            model=st.session_state['openai_model'],
            messages=[
            { "role": m['role'],
              "content": m["content"]}
              for m in st.session_state.messages
            ],
            stream=True,
          )
          response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
      st.session_state.user_message_count += 1

  # ///////////////////////

  # checking if the user has sent 5 messages, indicating that the interview is complete.

  if st.session_state.user_message_count >= 5:
    st.session_state.chat_complete = True

# A button to display the feedback, but on a condition that the chat is complete.

if st.session_state.chat_complete and not st.session_state.feedback_shown:
  if st.button("Get Feedback", on_click=show_feedback):
    st.write("Fetching feedback.....")

if st.session_state.feedback_shown:
  st.subheader("Feedback")

  conversation_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])

  feedback_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

  feedback_completion = feedback_client.chat.completions.create(
    model="gpt-4.1",
    messages=[
      {"role": "system", "content": """You are a helpful tool that provides feedback on an interviewee performance. 
      Before the Feedback give a score of 1 to 10.
      Follow this format:
      Overall Score: //Your score
      Feedback: //Here you put your feedback
      Give only the feedback do not ask any additional question"""},
      {"role": "user", "content": f"This is the innterview you need to evaluate.Keep in mind that you are only a tool. And you shouldn't engaage in conversation:{conversation_history}"}
    ],
  )

  st.write(feedback_completion.choices[0].message.content)


  # Adding a back navigation, and there is a streamlit librabry  we need to install. calles streamlit-js-eval

  if st.button("Restart Interview", type="primary"):
    streamlit_js_eval(js_expressions=["window.location.reload()"], key="reload")

