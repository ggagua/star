# Star Wars Website

Welcome to my Star Wars Enthusiast Website, a project that combines Flask, Python, HTML, CSS, and minimal JavaScript to create an immersive experience for Star Wars fans. 

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Login Page](#login-page)
- [Rate Limiting](#rate-limiting)
- [Data Exploration](#data-exploration)
- [Error Handling](#error-handling)
- [ChatGPT Integration](#chatgpt-integration)
- [How to install?](#getting-started)
- [Issues](#issues)
- [Donation](#donation)
- [Inspiration](#attribution-and-acknowledgments)

## Features

### Responsive Navigation
Website offers an immersive horizontal scrollable navigation bar that dynamically responds to mouse input, providing an engaging user experience.

![Responsive Navigation](https://github.com/ggagua/star/assets/117936056/413e2c6b-2de1-4653-9258-bb2247a45140)

## Login Page

### Secure Authentication
The login page is meticulously designed using Flask's login system, incorporating modules like Flask-Login and WTForms. User passwords are securely encrypted using bcrypt, ensuring their confidentiality. I'm utilizing SQLAlchemy and SQLite for the current project.
<img width="1512" alt="image" src="https://github.com/ggagua/star/assets/117936056/298ee4be-8556-4397-bb42-e6653818783b">


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

<img width="873" alt="image" src="https://github.com/ggagua/star/assets/117936056/05a28af7-46c5-491f-9af2-1816376d58d7">
<img width="1495" alt="image" src="https://github.com/ggagua/star/assets/117936056/d68a0687-822e-4023-9a5b-e29c9f22a9e3">
<img width="752" alt="image" src="https://github.com/ggagua/star/assets/117936056/9cdfe5ac-9f49-4189-997a-d8adf5c34fd6">

SQLite DB⬆️


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
4. Install required modules (Flask, SQLAlchemy, etc.)
5. Run app.py
6. In your web-browser access your localhost (127.0.0.1:5000).
7. If your localhost is taken by another project or service, you can modify last line of the project and add
   port = 8000. Ex : app.run(debug=True, port = 8000)

## Issues

I strive to make our Star Wars Enthusiast Website as flawless as a lightsaber. If you encounter any issues, bugs, or have suggestions for improvement, I welcome your feedback. Here's how you can help:

1. **Check Existing Issues**: Before reporting a new issue, please check our [GitHub Issues](https://github.com/ggagua/star/issues) to see if someone else has already reported the same problem or if there's an ongoing discussion about it.

2. **Create a New Issue**: If you can't find an existing issue that matches your problem or suggestion, feel free to [create a new issue](https://github.com/ggagua/star/issues/new). Be as detailed as possible, including the steps to reproduce the issue, the expected behavior, and the actual behavior you observed.

3. **Include Screenshots**: If the issue is visual or related to the user interface, it's often helpful to include screenshots. You can upload them directly to the issue you create.

4. **Provide Context**: Describe the environment in which you encountered the issue, such as your operating system, browser, or any relevant software versions.

5. **Contribute to Solutions**: If you're technically inclined and want to contribute to resolving the issue, consider submitting a pull request. I am always open to collaboration from the community. 


## Donation

If you've found my Star Wars Website valuable and want to support its continued development and maintenance, you can make a donation. 

- [Support me on Buy Me a Coffee](https://www.buymeacoffee.com/ggagua)
  

## Attribution and Acknowledgments

I believe in transparency, and as a token of my commitment, I have uploaded a PDF that lists all the sources  I've used in the development of this project. Feel free to check it out.

- [Download PDF - Sources and Acknowledgments](https://github.com/ggagua/star/files/13142988/swars-ggagua.pdf)

For inquiries or collaboration opportunities, feel free to contact me at [ggagua.tech@gmail.com](mailto:ggagua.tech@gmail.com).


**May the Force be with you!**


   

