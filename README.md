# Star Wars Enthusiast Website

Welcome to my Star Wars Enthusiast Website, a project that combines Flask, Python, HTML, CSS, and minimal JavaScript to create an immersive experience for Star Wars fans. 

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Login Page](#login-page)
- [Database Security](#database-security)
- [Rate Limiting](#rate-limiting)
- [Data Exploration](#data-exploration)
- [Error Handling](#error-handling)
- [API Integration](#api-integration)
- [ChatGPT Integration](#chatgpt-integration)

## Features

### Responsive Navigation
Website offers an immersive horizontal scrollable navigation bar that dynamically responds to mouse input, providing an engaging user experience.

![Responsive Navigation](https://github.com/ggagua/star/assets/117936056/413e2c6b-2de1-4653-9258-bb2247a45140)

## Login Page

### Secure Authentication
The login page is meticulously designed using Flask's login system, incorporating modules like Flask-Login and WTForms. User passwords are securely encrypted using bcrypt, ensuring their confidentiality. I'm utilizing SQLAlchemy and SQLite for the current project.

![Secure Authentication](https://github.com/ggagua/star/assets/117936056/b7fa9cbf-5581-488b-bc6e-5a287691d4b2)

## Rate Limiting

### Jedi-Like Resilience
To maintain a high level of security, I've implemented a sophisticated rate limiting mechanism. It temporarily restricts access to the login page if users exceed the maximum threshold, much like the Jedi's resilience guiding users back to the path of exploration.

![Rate Limiting](https://github.com/ggagua/star/assets/117936056/b7fa9cbf-5581-488b-bc6e-5a287691d4b2")

## Data Exploration

### Star Wars Grid Layout
Within the Star Wars-themed grid layout, users can delve into a treasure trove of captivating information. Navigating the site is made easy with arrow buttons, seamlessly integrated using Jinja2 templates. Info about characters is accessed through an API. Text is randomized to make interaction less repetitive. More about this could be found in `swapi.py` file.

![Star Wars Grid Layout](https://github.com/ggagua/star/assets/117936056/abf452d7-8668-43fb-aea9-1d1239fa825d)

## Error Handling

### Graceful Handling
Code expertly handles errors, logic is implemented to avoid out of bound and lot of dictionary errors. Also, I've made custom made error screen, which occurs if user tries to manually change something in link-section. In given example, we can see that user tried to manipulate dashboard and instead of indexes, he wrote completely different word. I've made 2 different versions of error screen, to make it less repetitive.

![Error Handling](https://github.com/ggagua/star/assets/117936056/your-image-url-here](https://github.com/ggagua/star/assets/117936056/0f0c34e3-efa6-4511-a5ec-04ffa6d97eb2))


## ChatGPT Integration

### Unleash the Force of Knowledge
Discover the Star Wars magic on our website! Powered by ChatGPT 3.5 Turbo API, I bring you up-to-date information through function-calling.Newly introduced function-calling has been utilized in the project, to not dive in source code too much, I'll showcase comparision of original and modified chat-bot. To explain the logic, based on prompt, ChatGPT understands when the function needs to be triggered and then accesses 
my SQLite DB which has information about upcoming Star Wars series/films. More about code in - chatapi.py

![ChatGPT Integration]<img width="873" alt="image" src="https://github.com/ggagua/star/assets/117936056/05a28af7-46c5-491f-9af2-1816376d58d7">
<img width="1495" alt="image" src="https://github.com/ggagua/star/assets/117936056/d68a0687-822e-4023-9a5b-e29c9f22a9e3">
Here is the SQLite base:
<img width="752" alt="image" src="https://github.com/ggagua/star/assets/117936056/9cdfe5ac-9f49-4189-997a-d8adf5c34fd6">

## Getting Started

To get a copy of this project and run it locally, follow these steps:


Rest is up to you to explore, but how do you access the project?
## Getting Started

To get a copy of this project and run it locally, follow these steps:

### Prerequisites

- You'll need Git installed on your computer. If you don't have it, you can download it [here](https://git-scm.com/).

### Cloning the Repository

1. Open your terminal or command prompt.

2. Change the current working directory to the location where you want to clone the repository.

3. Use the following command to clone the repository:

   ```sh
   git clone https://github.com/ggagua/star.git
   

