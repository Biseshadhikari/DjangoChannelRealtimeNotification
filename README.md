# Django Friend Requests WebSocket Project

## Overview

This Django project showcases a real-time friend request system using Django Channels for WebSocket communication. The application allows users to send and receive friend requests, with the system updating in real-time. The project's frontend is built with HTML, styled using Tailwind CSS, and incorporates JavaScript for WebSocket interactions.

## Project Structure

### 1. WebSocket Consumer (`consumers.py`)

The `FriendRequestConsumer` class manages WebSocket connections, disconnections, and message exchanges. It utilizes Django Channels to facilitate group communication, enabling real-time interactions for sending and receiving friend requests.

### 2. WebSocket Routing (`routing.py`)

Defines the WebSocket URL patterns to route WebSocket connections to the `FriendRequestConsumer`.

### 3. WebSocket Frontend (`index.html`)

The webpage displays a list of users, allowing them to send friend requests. Real-time notifications are presented using Tailwind CSS for styling. JavaScript is used to manage WebSocket interactions and update the UI dynamically.

### 4. Django Views (`views.py`)

The `home` view fetches a list of users from the Django User model, excluding the currently logged-in user, and renders the HTML template.

### 5. Channel Layers

Django Channels introduces the concept of channel layers, which enables communication between different parts of your application. In this project:

- When a user connects, they are added to a WebSocket group (`friendreq_username`) based on their username.
- Disconnection from the WebSocket results in removal from the corresponding group.
- Sending and accepting friend requests involve sending messages within these WebSocket groups in real-time.

## How it Works

1. **WebSocket Connection:**
   - Users connecting to the WebSocket are added to a WebSocket group based on their username (`friendreq_username`).

2. **WebSocket Disconnection:**
   - Users are removed from the WebSocket group upon disconnection.

3. **Sending Friend Requests:**
   - Users can click the "Add Friend" button to send a friend request.
   - The frontend sends a WebSocket message to the recipient's WebSocket group, notifying them of the request.

4. **Handling Friend Requests:**
   - The recipient's WebSocket consumer receives the message and updates the UI in real-time.
   - Notifications are displayed, and the "Add Friend" button changes to an "Accept Request" button.

5. **Accepting Friend Requests:**
   - When the recipient clicks the "Accept Request" button, a message is sent to the sender's WebSocket group.
   - Both users receive notifications, and the UI is updated accordingly.

## Usage

1. **Installation:**
   - Install required packages: `pip install -r requirements.txt`.
   - Run migrations: `python manage.py migrate`.

2. **Run the Server:**
   - Start the Django development server: `python manage.py runserver`.

3. **Access the Application:**
   - Open a web browser and go to `http://localhost:8000`.

4. **Interact with WebSocket:**
   - Send friend requests and observe real-time updates.

## Note

This project is a basic demonstration and may require additional features, such as user authentication and handling multiple friend requests simultaneously. Customize and extend it as needed.

## Dependencies

- Django
- Channels
- Tailwind CSS


