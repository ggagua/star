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
Our website offers an immersive horizontal scrollable navigation bar that dynamically responds to mouse input, providing an engaging user experience.

![Responsive Navigation](https://github.com/ggagua/star/assets/117936056/413e2c6b-2de1-4653-9258-bb2247a45140)

## Login Page

### Secure Authentication
The login page is meticulously designed using Flask's login system, incorporating modules like Flask-Login and WTForms. User passwords are securely encrypted using bcrypt, ensuring their confidentiality. We're utilizing SQLAlchemy and SQLite for the current project.

![Secure Authentication](https://github.com/ggagua/star/assets/117936056/b7fa9cbf-5581-488b-bc6e-5a287691d4b2)

## Rate Limiting

### Jedi-Like Resilience
To maintain a high level of security, we've implemented a sophisticated rate limiting mechanism. It temporarily restricts access to the login page if users exceed the maximum threshold, much like the Jedi's resilience guiding users back to the path of exploration.

![Rate Limiting](https://github.com/ggagua/star/assets/117936056/your-image-url-here)

## Data Exploration

### Star Wars Grid Layout
Within the Star Wars-themed grid layout, users can delve into a treasure trove of captivating information. Navigating the site is made easy with arrow buttons, seamlessly integrated using Jinja2 templates. Info about characters is accessed through an API. Text is randomized to make interaction less repetitive. More about this could be found in `swapi.py` file.

![Star Wars Grid Layout](https://github.com/ggagua/star/assets/117936056/abf452d7-8668-43fb-aea9-1d1239fa825d)

## Error Handling

### Graceful Handling
Our code expertly handles errors, and logic is implemented to avoid out-of-bound and dictionary errors. Also, we've made custom-made error screens, which occur if a user tries to manually change something in the link section. In the given example, we can see that the user tried to manipulate the dashboard and instead of indexes, they wrote a completely different word. We've made two different versions of the error screen to make it less repetitive.

![Error Handling](https://github.com/ggagua/star/assets/117936056/your-image-url-here)

## API Integration

### Hidden Knowledge Unveiled
Our project expertly extracts data from various APIs, unveiling hidden knowledge locked within JSON. These sacred texts reveal numerous dictionaries, each holding a piece of the Star Wars puzzle. With meticulous logic, we traverse these celestial archives, extracting vital information and presenting it in a format that would make even Master Yoda nod in approval.

![API Integration](https://github.com/ggagua/star/assets/117936056/your-image-url-here)

## ChatGPT Integration

### Unleash the Force of Knowledge
Discover the Star Wars magic on our website! Powered by ChatGPT 3.5 Turbo API, we bring you up-to-date information through function-calling. Our database holds the secrets of Star Wars series, ensuring accurate and personalized responses.

![ChatGPT Integration](https://github.com/ggagua/star/assets/117936056/your-image-url-here)

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
   

