# URL Shortener Project

This project is a URL shortener application built with Django and Django REST Framework. It allows users to shorten long URLs and redirect to the original URL using a shorter link.

## Getting Started

To run this project locally, you need to use Docker and Docker Compose. Follow the instructions below to get started:

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine
- [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine

### Running the Application

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Build and start the application using Docker Compose:

    ```bash
    sudo docker compose up --build
    ```
- This command will build the Docker image and start the application, which will be accessible on port 80 of your local machine.

### Accessing the Application
- Open a web browser and navigate to `http://localhost` to access the application.


### Project Structure
- `Dockerfile`: Defines the Docker image for the application.
- `docker-compose.yml`: Configures the Docker Compose setup for running the application.
- `url_shortner/`: Contains the Django project and application code.

### Technologies Used
- `Django`: A high-level Python web framework for building web applications.
- `Django REST Framework`: A powerful toolkit for building Web APIs.
- `Gunicorn`: A Python WSGI HTTP Server for UNIX, used to serve the Django application.

### License
 - This project is licensed under the [MIT License](https://opensource.org/license/mit). See the [LICENSE](LICENSE) file for details.

### Contact
- For any questions or issues, please open an issue on the GitHub repository.
