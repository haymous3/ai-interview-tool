
# //////////////////////////////////////////////

# INITIALIZING AN OPENAI CLIENT

# ///////////////////////////////////////////////

# Since we already have the Streamlit package prepared, we'll only need to install OpenAI.

# We do this by opening a new terminal and writing the following command pip install OpenAI.

# Next, we must create a new folder called dot streamlit in a project directory.

# This folder will hold configuration files for Streamlit.

# We now need to create a new file in this folder called secrets dot Toml.

# In this file, we'll store our OpenAI API key.

# Inside the secrets file, we enter the following line.

# Open API key T equals to double quotation marks.

# We'll paste our API key here.

# To do that we first need to generate a new API key.

# So go to your OpenAI profile.

# Navigate to view API keys.

# Under the API section.

# Click on Create New Secret key and give it a name of your choice.

# Then click Create Secret Key to generate it.

# Copy and store your API key in a secure place.

# After this step, you won't be able to view it again.

# Once you have your API key, go back to VS code and paste it between the quotation marks in the secrets

# file.

# For the next step, we need to return to the main directory and create a new file called app dot Pi.

# We'll write our code here.

# We'll begin by importing the Streamlit library and the open eye class from the library of the same name.

# Here's how you do it.

# Now let's set up the configuration for our Streamlit page.

# Use Streamlit set page configuration method to set the page title to Streamlit chat and the page icon

# to a chat emoji.

# Next, let's set the title of our app to Chat bot.

# Let's run the code to ensure our app runs well without any problems.

# For now, we should only see the title returning to the source code.

# Let's initialize the open AI client using the API key stored securely in Streamlit Secrets Management.

# So we add the following line to do this.

# This line creates an instance of the open AI class.

# The API key argument securely pulls the API key from Streamlit Secrets file, ensuring it's not exposed

# in the code.

# All right, we've now set up the client to interact with OpenAI's API.

# Next, we'll set up our model by creating a session state.

# First, we check if the session state already contains a variable for the model.

# So we write if OpenAI model not in start session state.

# If the session state doesn't contain the OpenAI model variable, we create one and assign it to the

# value GPT for zero.

# We can do this by writing st dot session state square brackets OpenAI model equals two GPT four zero.

# If we want to use a different OpenAI model, we change the name in the last string.

# It's important to note that you must provide the exact name of the model as specified in OpenAI's documentation.

# Otherwise it would result in an error.

# In the next lesson, we'll take this setup to the next level by creating a fully functional chat application.

# Stay tuned.



# /////////////////////////////////////////////////////

# IMPLEMENTING THE CHAT FUNCTIONALITY

# //////////////////////////////////////////////////////


# Welcome back.

# Now that we've set up our libraries and API key, we can start working on the logic.

# First, we must initialize the chat history and check if a key, which we'll call messages already exists

# in the session state.

# The messages key stores the entire history of our chat, including all messages sent by the user and

# the assistant.

# It acts as a container that keeps track of the conversation as it evolves.

# If messages is not a key in the session state dictionary, it means that we haven't started storing

# any messages yet.

# In this case, we initialize it by setting session state dot messages to an empty list.

# All right, let's create the chat.

# First, we start with an input field for the user to type their message.

# The chat input method creates an input box with a placeholder text.

# Reading your answer.

# When the user submits a message, it's stored in the prompt variable.

# The syntax if prompt colon equals, is a compact way to assign the value to the prompt object and check

# if the input is not empty.

# Once we have the user's input, we append it to our session state that we called messages.

# With the role being user and the content being the user's input.

# Then we display the user's message in the chat interface using the chat message function to create a

# message block.

# Next, we use the markdown function to render the message content.

# Now we prepare to get the chatbots response.

# We create another chat message block for the assistance response and call the OpenAI API to generate

# the response.

# We do that with this code.

# We first use the with statement to create a context block.

# This is followed by the chat message method in which we pass the string assistant as an argument.

# This creates a dedicated block to display the assistance response in the chat interface.

# Next, we call the OpenAI API to generate the assistance response.

# The OpenAI create function used here takes several parameters.

# The first is model, which specifies the model we're using, which we defined earlier as GPT four.

# Zero messages is the parameter that takes the entire chat history as the context for the assistance

# response.

# To provide this chat history.

# We loop through the messages list in the session state using a list comprehension.

# List comprehension is a concise way to create a new list by iterating over an existing one.

# In this case, it takes each message in the messages list, extracts its role and content, and reformats

# it as a dictionary.

# This structure gives the assistant all the necessary context for generating a meaningful reply.

# Each message is represented as a dictionary with two keys role, which indicates who sends the message

# and content the actual message.

# Finally, we set the stream parameter to true to receive the response as a stream, which allows for

# more user friendly interaction.

# This would then allow us to use the write stream method we discussed in a previous lesson, displaying

# the response in a dynamic and visually appealing way.

# We captured the response in a variable named accordingly, and we append it to the messages list.

# We've made good progress.

# Let's save the code, refresh the page and greet our chat bot.

# Amazing!

# We have a response, but notice that we can't view the entire chat history on screen.

# Instead, we get only one box for the user's message and one for the assistance response.

# The messages are still saved in the chat message list in the session state, but we can't see them.

# The application displays only the last user message and the last assistant response.

# Our next task is to display the chat messages in our Streamlit application.

# Here's how we do this.

# Let's break it down.

# The loop goes over each message in the session.

# State messages.

# If the role of the message is not system, we create a chat message block that can take one of two roles

# assistant or user.

# Using the markdown function, we put the content of the message so the code goes through all the messages

# and displays them.

# Note that we do not include system messages, since we don't want the users to see our prompt.

# Save the code, refresh the page, and let's test it to see if it works with a couple of inputs.

# First, I'll type.

# Hello, how are you doing?

# And we have a response.

# I'll add another input.

# Tell me a fun fact.

# And again the assistant responds dynamically with a fun fact.

# Great!

# We now have a ChatGPT like chatbot.

# Let's review one more point before we wrap up the lesson to include a system message where we write

# our prompt, we just need to append an additional element to the messages list.

# So we go to the top of the code, where we initialize the messages session state and modified the line

# like this.

# In this code, we add a role to the message, setting it to system and adding the prompt.

# You are a helpful tool that talks like a pirate.

# Go ahead and save the file, then run the code.

# Now let's ask our chatbot to tell a joke and see how it responds.

# Wow, what a response!

# We now have a ChatGPT clone that speaks like a true pirate.

# Great!

# In the next lesson, we'll set up a configuration stage for our prototype.

# See you there.


# ////////////////////////////////////////////////

# BUILDING THE SETUP PAGE

# ////////////////////////////////////////////////


# Now that we have our simple chatbot up and running, let's enhance it by adding a setup.

# This will allow the user to input personal information, which we can use to personalize the chat experience.

# In the setup, the user should be able to write their name, experience and skills and select from given

# options for level, position, and company.

# Let's start by adding a Subheader to indicate where the personal information should be added.

# We do this by writing st dot Subheader.

# We'll label it as personal information to make it more visually pleasing.

# We can add a divider at the end to do that.

# Write divider equals to rainbow.

# Save the changes in VS code and switch to the browser.

# It looks good to add a text box for the user's name.

# We write the following line.

# Let's break down what this line of code does.

# The label parameter sets the label of the text input field to name the max characters.

# Parameter limits the number of characters the user can enter.

# For now, we will set it to none, which means there is no limit, and the placeholder parameter displays

# a hint within the input field, asking the user to enter their name.

# Let's save the application and check our UI in the browser and we see our textbox on the screen.

# Next, we must create input fields for the user's experience and skills.

# Since these fields require more space for longer entries, we'll use text areas instead of text inputs.

# Here's how we can set them up.

# These text areas function similarly to the name input field, but offer a larger space.

# The value parameter sets the default value of the input field, which will leave as an empty string.

# Great.

# Now let's run the app.

# Nice.

# We have our text boxes in place, but we're not sure if they work as expected.

# Let's create a label to display the user's input and confirm that the Textboxes function correctly.

# We'll use the right method and an f string as an argument to format our message.

# Each variable name, experience, and skills is placed inside curly braces, which tells Python to substitute

# those placeholders with the actual values provided by the user.

# We can also add two asterisks at the beginning and the end of our text to make our labels bold.

# Let's test it for the name field.

# We'll type Alex for experience.

# Let's enter two years as a data scientist and for skill we'll add Python and it works.

# Next we need to add the fields for company and position separately.

# To start, let's add another Subheader.

# And again we can add our signature divider to enhance the user interface.

# Let's organize our layout into two columns.

# To do this, we index them as one and two and use the columns function to specify the number of columns

# we want.

# In our case, we'll create two.

# In the first one, we'll add radio buttons for the position level junior, mid or senior.

# Will you say with statement to access it and define its radio button logic within it?

# Here's how it looks in this setup.

# The level variable will store the selected option.

# We called the radio function to initialize the radio buttons.

# Inside this function, the first parameter choose level is a label displayed above the options to prompt

# the user.

# Next, we use the key parameter and set it to visibility, which can help maintain the widget's state

# across interactions.

# Finally, the options parameter provides the list of choices available for selection.

# Junior, mid-level or senior for the position selector.

# Let's create a dropdown menu in the second column.

# Once again, we'll use a width statement to access the second column.

# This time we'll assign the selected position to the variable position using the select box function.

# Now we'll define more choices.

# This will allow users to select their position from a predefined list of options.

# These are data scientist, Data engineer, ML engineer, BI analyst, and Financial Analyst.

# Finally, let's add another drop down menu to select a company.

# This time we won't place it inside a column.

# Once again, we'll use the select box function and enter a few company names as options.

# Let's go with Amazon, meta, Udemy 365 company, Nestlé, The LinkedIn and Spotify.

# Looks great!

# Let's test if it works once more by displaying the selected values with the label.

# Great!

# Now that we have the setup, let's connect it to the chatbot.

# Head back to the code where we initialized the system message, also known as the prompt.

# Remember the prompt template?

# We defined and tested a couple of lessons back.

# We can replace the existing system message with that template here.

# Good job.

# Let's test the application first.

# Save the file and refresh the page.

# The complete layout looks great.

# Now let's test the setup by entering some dummy data.

# Again, our name will be Alex.

# We have two years of experience and her skills include SQL and Python.

# We'll select Senior financial analyst and the company Spotify.

# The setup appears to work as expected because the labels display all the variables we've defined.

# Now let's test the chat by asking what is my name?

# Unfortunately, the chat doesn't know our name, so the setup information hasn't been passed to the

# system message.

# The model has no knowledge about our setup.

# This is because the user inputs for name, experience, skills, level, position, and company are

# not dynamically updated or incorporated into the session state after they're initially set.

# In other words, while they're captured and displayed in the setup stage, they're not actively passed

# to the session state or the chatbot during the conversation.

# Therefore, we must store the user's input in the session state and update it dynamically.

# We'll do this in the next lesson.


# ///////////////////////////////////////////////////

# Enchancinig Chatbot Interaction with Session State

# ////////////////////////////////////////////////////////


# In the previous lesson, we set up a basic chatbot and a page that collects user information.

# But we encountered an issue where the chatbot did not recognize the information provided during the

# setup stage.

# In this lesson, we'll address this problem and enhance our chatbot to ensure it effectively utilizes

# user input.

# So first let's think about how we can solve this.

# We need to track whether the setup for the interview is complete.

# To do this we can initialize a session state for the setup stage.

# We'll name it Setup Complete and initially set its value to false.

# This time, instead of directly changing the session state within a button, we'll create a cleaner

# version by defining a function to toggle the setup phase completion.

# Later, we'll attach this function to the button using an onClick event.

# This is an additional parameter that lets us specify a function that runs when the button is clicked.

# This allows us to trigger action like updating the state in a clear, organized way.

# Now we must show the setup form only if the setup is incomplete.

# We do that by wrapping the whole setup form in an if statement that looks like this.

# This line checks if the setup complete session state variable is false.

# If it is, the form will be displayed allowing the user to input their details.

# Once the setup is complete and set up, complete is set to true, the form will no longer be shown.

# Next, we must initialize session state variables for the user's personal information.

# This will allow us to keep track of the user's inputs across interactions, and ensure the data is persistent

# throughout the session.

# Here's how we do that for each piece of personal information.

# Name.

# Experience and skills.

# We first check if a corresponding key exists in the session state.

# If the key does not exist, the session state for that variable hasn't been initialized.

# In this case, we create the key and set its default value to an empty string.

# Now that we have our variables, we'll update the personal information input fields to save the values

# directly into the session state, making the data available across interactions.

# We add start session state followed by a set of square brackets, and pass the variable's name as a

# string.

# The same steps for the company and position information.

# First, we initialize session state variables for each input, and notice how we ensure each variable

# has a default value selected when the user starts the interview.

# This gives a starting point for each dropdown or selection input.

# Next, we again need to update the input fields to pull from the session state.

# In the previous version of the code, the selected values for level, position, and company were stored

# in regular variables.

# Now we're integrating these fields with the session states we've just created.

# We rewrite the variables by adding state session state square brackets and the name of the variable.

# We also set the index parameter to the session state.

# We apply this change to all variables to fully integrate the input fields with the session state.

# And finally, we need to add the button to complete the setup phase and trigger the session state update.

# Remember the onClick parameter that we mentioned earlier?

# It will call the complete setup function.

# This button will turn the setup complete session state to true, causing the setup form to disappear.

# This ensures the user completes the setup phase before moving on to the interview phase.

# We handled the transition similarly by checking if the setup complete session state is set to true.

# We then wrap our chatbot code inside this if statement.

# Now let's move on to our chatbot.

# One thing we can do to make it more engaging is by adding an info box to guide the user.

# Providing a friendly prompt to start the conversation.

# To do this, we'll introduce a new function the info function.

# Here's how we use it.

# We write start info, then the message we want to display.

# In our case it will be.

# Start by introducing yourself.

# We can also place an icon parameter which allows us to add a visual element such as an emoji.

# Before we wrap up this lesson, one last step is to connect the session state variables with the prompt.

# This ensures the chatbot can access the information collected in the setup phase.

# We achieve this by passing the session state variables into the prompt message.

# To reference a session state variable, we use the syntax state session state square brackets followed

# by the variable name.

# This approach dynamically inserts the user provided data into the prompt message.

# Let's test the interview to make sure everything works as intended.

# We'll start by filling out the setup fields with dummy data for the name.

# Let's enter Alex.

# In the experience field, we'll type two years of experience as a Junior Data Scientist at Globalnet.

# Then we'll complete the level company and position information.

# Once that's done, we click on Start Interview.

# Now let's begin with the simple introduction.

# As you can see, the model recognizes our name and even remarks on our background, just like an actual

# interview.

# Great job everyone!

# In the next lesson, we'll take the app to the next level by adding a feedback feature and making overall

# improvements to the project.

# See you then!



# /////////////////////////////////////////////////

# REFINING OUR PROKECT FOR THE FEEBACK

# ///////////////////////////////////////////

# Now that we have the working setup and chat, we can start creating the post interview feedback.

# We'll work on building better session management.

# Right now our application doesn't track the number of messages exchanged, so the interview could go

# on infinitely, or at least until we run out of tokens in our account.

# To manage this, we'll initialize a session state variable to keep track of the user's messages.

# We'll call it user message count and set its default value to zero.

# We might also need a session state similar to the one for the setup complete.

# That indicates whether the user has been shown feedback for the interview.

# Initially, it should be set to false, but change once the feedback is generated and shown to keep

# all session state variables organized in one place.

# We can move the initialization of the message state to the top.

# It will store the conversation history, including all messages sent by the user and the assistant.

# This way, we ensure we have a place to store and access all the interactions and seamlessly manage

# and reference the conversation history across all stages of the chatbots flow.

# Next, we need another session state, similar to the one that tracks the completion of the setup stage,

# which will track the completion of the interview.

# We'll call it Chat Complete and once again set its default value to false.

# Great.

# Now we have our system for controlling the application's flow to ensure a smooth transition between

# the different stages.

# Set up interview and feedback.

# We already have a function that toggles the completion of the setup phase.

# Now let's add another function to toggle the feedback display.

# We'll name it Show Feedback.

# When it's called, it will set the feedback session state to true.

# Before we wrap up this lesson, here's an important note.

# We should always impose word or character limits on any input field that goes into the LM.

# This ensures that the model doesn't receive excessively long inputs, which can lead to inefficient

# processing and potential issues.

# For the name input field, 40 characters should be enough so we can add the following for the skills

# and experience we can set.

# Let's say 200 characters.

# Great.

# On to the next lecture where we'll implement the feedback functionality.


# /////////////////////////////////////////////////

# Implementing Feedback Functionality: Part 2

# /////////////////////////////////////////////////


# Welcome back.

# Let's continue with our development.

# The next task on our list is to implement the feedback feature.

# To start, we need a button that when clicked, will display the feedback.

# Here's how we can achieve that.

# First, we must ensure that the button is displayed only after the chat is complete and the feedback

# has not yet been shown.

# We do this with an if statement where the first part checks if the interview has reached its message

# limit and is marked as complete.

# In the second part, we use the Not operator to confirm that the feedback has not already been displayed.

# Together, these conditions control when the Get feedback button appears.

# When the button is clicked, it triggers the show feedback function that we created earlier.

# This function sets both the feedback button clicked and the feedback shown to true.

# We'll add a line after the button is clicked to let the users know that the feedback generation process

# has started.

# Next, we create the feedback screen.

# We start by checking if feedback shown is true.

# If it is, we display a new section with the Subheader titled feedback.

# In this if statement, we create a new variable called Conversation History that joins all session state

# messages from the session state messages list into a single string.

# Each message is formatted to show the role, user or assistant, and the content of the message, separated

# by a newline character represented by slash n.

# Now we need to set up another model to serve as a evaluator following the same steps.

# We initialize a new OpenAI client instance.

# Notice that we reference the same API key stored in the secrets file.

# And again we add our model name and messages.

# First we have our system message.

# Here we'll tell the LM that it's a helpful tool that provides feedback on an interviewee's performance.

# We'll also specify the format we need detailed feedback and an overall score from 1 to 10.

# Additionally, we'll include specific instructions to ensure the model gives early feedback and doesn't

# continue the conversation because models sometimes hallucinate and add unnecessary information.

# We can add can add a user message where we pass the chat history and says, this is the interview you

# need to evaluate.

# You are only a tool and shouldn't engage in conversation.

# This ensures that the LLM focuses solely on providing feedback and does not continue interacting with

# the user.

# Next, we extract the first message generated by the new model with the following line of code.

# This step is necessary because the output of the feedback completion function is a structured object

# containing a list of potential responses, which are referred to as choices.

# It would look something like this.

# Each item in the choices list represents a possible reply from the model, and includes details such

# as our well-known roles.

# So with this code, we ensure that we extract the first message from the list, which is the feedback.

# Let's test our application again.

# Let's skip ahead to the most exciting part.

# I've already completed the interview, and now I'm posting the final answer to wrap things up and finalize

# the interview process.

# Now, at the end of the of the interview, we should see a Get Feedback button.

# When you click it, the application processes the chat history and generates feedback.

# After the application loads, you'll see an overall score out of ten, followed by detailed feedback

# formatted as we specified in the prompt.

# Alright, this looks nice.

# Another enhancement we can add is navigation back to the setup page, allowing users to start the interview

# process over again.

# There's a clever way of doing this with the following code.

# We first install the library called Streamlit js eval.

# This library allows us to execute JavaScript commands directly from Streamlit, enabling advanced functionality

# like refreshing the page or interacting with the browser.

# Then go to the beginning of our file and import the necessary function.

# We can then add the following code to the feedback page.

# This way we restart the interview by refreshing the page, providing a seamless experience for users

# to begin a new interview session.

# Let's test the application one final time.

# For this demonstration, we've skipped ahead to the last question of the interview.

# Once we press the Get Feedback button.

# We see the feedback generated by the model displayed on the screen.

# Now notice that we also have a new button labeled Restart Interview.

# When we click it.

# The page refreshes and we are seamlessly brought back to the setup stage, ready to start a new session.

# The next step is to remove the text labels we use to test if the text box is recorded.

# Information.

# Great.

# Looks cleaner now.

# Well done everyone!

# With this, our application is fully functional and complete.

# But if you pay close attention to the interview and the feedback output from the large language model,

# you'll notice that sometimes the responses lack depth, offer generic insights, or fail to provide

# well structured feedback.

# For your homework, I suggest you work on prompt engineering to create better prompts for both the feedback

# and the interview.

# Additionally, experiment with tweaking the settings of the model to achieve better results.

# For instance, you could revisit the scoring system mentioned earlier in the course or implement a question

# by question evaluation.

# Try adjusting parameters like temperature or top p values to observe how they affect the feedback quality.

# Feel free to build on this project.

# You can improve the design or even change the topic altogether.

# For example, you could create a debate simulator where on the setup page you decide the topic of the

# debate and the difficulty level.

# The interview screen would then turn into a debate screen instead of feedback.

# The second model would decide who wins the debate.

# All right.

# In the remaining lectures of this section, we'll cover how to upload our code to GitHub and host our

# application via Streamlit services.

# See you there.


# /////////////////////////////////////////////

# Uploading Your Project on Github

# ////////////////////////////////////////////

# Welcome back.

# Now that our project is nearly complete, it's time to upload it to GitHub.

# As you are probably already familiar, GitHub is the most popular platform for version control and collaboration,

# and it will help us manage our project and deploy it using Streamlit.

# In this lesson, we'll walk you through the steps to upload your project and explain how to commit any

# changes you make.

# But before we start, it's essential to note that you should never upload your API keys to GitHub.

# Automated bots called crawlers scan public repositories for sensitive information like API keys.

# If these keys are exposed, unauthorized users can exploit them, potentially draining your funds.

# Always ensure your sensitive information is kept secure.

# First, we must create a repository on GitHub to store our project.

# If you don't have a GitHub account, the first step is to sign up for one at github.com.

# Once you've created your account and have signed in, the next step is to create a new repository.

# Begin by clicking on the new button located on the top right corner of the GitHub homepage, or navigate

# to the repositories tab and click new.

# Next we need to choose a name for the repository.

# I'll go with Interview Tool.

# Now we must decide whether it will be public or private.

# If we choose public, anyone can view our repository, whereas private means only those you select can

# see the repository.

# For this project, we'll choose public and I'll explain the reasoning behind this choice in the following

# lesson where we discuss deploying the app.

# After making your selection, click on Create Repository.

# Now don't close this window.

# Go back to your project in VS code and open a terminal.

# In the terminal, we need to initialize a local git repository and connect it to the GitHub repository

# we just created.

# Start by navigating to your project directory.

# If you're not already there.

# You can do this using the CD command followed by the path to your project folder.

# Once in the project directory, initialize the git repository by running the command git init.

# Next, add all your project files to the staging area using the command git add dot.

# now commit these files with the message describing this as the initial commit.

# Like this.

# Git commit m and we add a message with the text initial commit.

# You might be asked for verification, so follow the steps written in the terminal.

# Before we proceed, let's quickly discuss branches.

# Branches in git allow you to work on different project versions simultaneously.

# The default branch is where your main development happens and it's common practice to name it main.

# After committing your files, rename the default branch to main using the command git branch dash m

# main.

# This ensures that the primary branch of your repository is named main.

# The next step is to connect your local repository to the GitHub repository.

# To do this, we must return to the GitHub page where we created the repository.

# We then need to copy the remote repository URL.

# After that, go back to the console and write git remote add origin and add your URL address.

# This command tells git where to push your project files on GitHub.

# Finally, push your local repository to GitHub using the command git push u origin main.

# This command uploads your local repository to GitHub and sets the remote repository as the default for

# future pushes.

# Follow the instructions if you're prompted with a message asking you to sign in.

# Now return to your GitHub repository page and refresh it.

# You should see all your project files uploaded.

# Congratulations!

# Your project has now been successfully uploaded to GitHub.

# If you make any changes to your project files, you need to update your GitHub repository to reflect

# those changes.

# Here's how you can do that.

# First, we add the changes to the staging area by again writing git add all.

# We commit the changes with git commit and write a descriptive message such as.

# Updated the prompt and we again push it to GitHub.

# Great.

# In the next lesson, we'll take it a step further by deploying our application using Streamlit services.

# This will allow us to share our interactive app with others quickly and efficiently.

# See you there!


# /////////////////////////////////////////

# DEPLOYING YOUR STREAMLIT APP

# //////////////////////////////////////////


# Now that your project is uploaded to GitHub, it's time to make it accessible to others by deploying

# it.

# In this lesson, we'll walk you through the process using Streamlit Community Cloud.

# Streamlit Community Cloud is a fantastic service that allows you to host and share your Streamlit apps

# with just a few clicks, making it incredibly easy to showcase your projects to the world.

# Plus, it's free, but there's a catch you can only host Streamlit apps that are public on GitHub.

# This means that everyone will be able to see the source code of your application.

# While this might seem like a drawback, it also allows others to learn from your work and contributes

# to the open source community.

# A worthwhile trade off.

# First, we need to create a requirements.txt file.

# This file lists all the dependencies required to run your Streamlit app.

# This ensures the Streamlit cloud knows which packages it needs to install to run your app smoothly.

# To create this file, Open a text editor and create a new file named requirements.txt.

# Now we need to add the libraries we've used for our project.

# The requirements file should include Streamlit, OpenAI and Streamlit js eval.

# It's as simple as that.

# But what if you have so many libraries that you can't track them all, and you encounter errors every

# time you try to run the app on the server?

# In such cases, you can use the following command in the VSCode terminal to generate the requirements

# file automatically.

# This command will create a requirements file containing all the packages and dependencies currently

# installed in your environment.

# Once we have this file, we must commit and push it to GitHub.

# We start by writing in the terminal.

# Git add dot to add all the files.

# Then with git commit m we can write a commit message.

# For example adding the requirements file.

# Finally, push the changes to the remote repository.

# Git.

# Push.

# Origin.

# Main.

# All right.

# To deploy the app we first need to visit shared Streamlit, IO and sign in with GitHub and set up your

# account.

# Once signed in, click Create App and select deploy a public app from GitHub.

# You'll be presented with a form where you need to add information about your repository.

# In the repository field, add the link to your GitHub repository.

# We've used main for the branch, so select that.

# The main file path should point to the file you use to run the app, which in our case is app dot Pi.

# If needed, you can also customize the app URL.

# Next, click on the Advanced Settings button.

# This is where we can add the content of our secrets file.

# Paste your API key here in the following format.

# Save the changes and click deploy.

# After a few seconds, your app will be deployed.

# Let's test the application to ensure everything works perfectly.

# And it does flawlessly.

# Now we have an app that's up and running.

# You can share the link with your friends to try it out.

# We did it!

# Congratulations on deploying your first LM app.

# In the next section, you'll get an inside look at how we built the Ace interview.

# Our interview simulator that is up and running today helping thousands of students prepare for their

# job interviews.

# So stay tuned.


