"# CodeAlpha_Chatbot" 

This is a GUI-based Rule-Based Chatbot built with Python and PyQt5.
It provides a simple and interactive graphical interface where users can type short messages and receive predefined responses from the chatbot.

The project demonstrates how to create a basic chatbot with a clean interface, input/output handling, and GUI design using PyQt5 — ideal for beginners learning GUI programming and simple rule-based logic.

Key Features:
1. Graphical Interface: Built using PyQt5 with text display, input box, and buttons.
2. Predefined Replies: Responds to greetings and basic conversational inputs like “hello”, “how are you”, or “bye”.
3. Clear Chat Button: Resets the chat to the default greeting.
4. Exit Button: Closes the application instantly.
5. Minimal and Responsive Layout: Simple design with user-friendly styling.

How It Works:
When you launch the app, it opens a window titled “Simple Rule-Based Chatbot”.

The chat window starts with the greeting:
  Chatbot: Hello!
  The user types a message (e.g., "hello", "how are you", "bye").
  The chatbot checks the message and responds with one of its predefined answers.
  If the input is not recognized, it replies with:
  Chatbot: Sorry, I didn't understand that.

You can click:
Generate → to send your message
Clear → to reset the conversation
Exit → to close the program

Installation & Usage:
Step 1: Clone the Repository
  git clone https://github.com/your-username/rule-based-chatbot.git

Step 2: Navigate to the Folder
  cd rule-based-chatbot

Step 3: Install Dependencies
  This project requires PyQt5. Install it using:
  pip install PyQt5

Step 4: Run the Application
  python Chatbot.py

Dependencies:
  PyQt5 → for GUI interface
  sys → for application control and exit functionality
