# Real-Time Chat App with Django Channels

This is a simple real-time chat application built by Potato Power Team using Django Channels for the backend and HTML, CSS, and Vanilla JavaScript for the frontend. It allows users to engage in real-time chat conversations with others.


## Team Members:
- Choyee Myae
- Nhan Ha
- Nitisuk Tatiyasuntorn
- Tan Dao


## Features

- Real-time chat with WebSocket support.
- User authentication and registration.
- Chat rooms for organizing conversations.
- Simple and intuitive user interface.

## Technologies Used
  - [Django](https://www.djangoproject.com/)
  - [Python](https://www.python.org/)
  - [HTML5](https://html.spec.whatwg.org/)
  - [CSS](https://www.w3.org/Style/CSS/)
  - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - [sqlite](https://www.sqlite.org/index.html)

## Prerequisites

Before running this application, ensure you have the following prerequisites installed:

- Python 3.9 or higher
- Django
- Channels
- Redis (for WebSocket support)

## Getting Started

1. Clone and setup
    1. Clone the project's repository
        Run ``git clone https://github.com/your-username/chat-app.git``
    2. Set up a virtual environment
        1. Install "virtualenv" library
            Run ``pip install virtualenv``
        2. Create a virtual environment
            ``virtualenv <env_name>`` (replace <env_name> with the name you'd like to give to your virtual environment)
        3. Activate the virtual environment by running the following command:
        
               ``<env_name>\Scripts\activate`` for Window

                ``source <env_name>/bin/activate`` for Unix or Linux
        4. Install dependencies 
            ``pip install -r requirements.txt``
       5. Run the application:
        > **Note:** Make sure you are in the folder contains the file called "manage.py"
      
        ```sh
          python manage.py runserver
        ```
