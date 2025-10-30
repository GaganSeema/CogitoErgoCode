# CogitoErgoCode: AI Text-to-Image Generator

A web application that generates images from text prompts using cutting-edge AI models. This project, curated by Gagan P, showcases the application of Python, machine learning, and web development to create a fun and interactive AI tool.

## About The Project

This project is a full-stack web application that allows users to bring their ideas to life by generating images from simple text descriptions. It's built to be a high-quality portfolio piece, demonstrating modern development practices including API integration, containerization, and secure configuration.

## Features

*   **Text-to-Image Generation:** Convert any text prompt into a unique image.
*   **Web-based UI:** A simple and intuitive interface for entering prompts and viewing results.
*   **Secure API Handling:** Manages API keys securely using environment variables.
*   **Deployable with Docker:** Easily run the application in a containerized environment for consistent and reliable deployment.

## Technologies Used

*   **Frontend:** HTML, CSS, JavaScript
*   **Backend:** Python, Flask
*   **AI Model:** Stable Diffusion (via Hugging Face Inference API)
*   **Containerization:** Docker, Docker Compose

## Getting Started

To run this project locally, you will need Docker and Docker Compose installed.

### Prerequisites

*   **Docker:** [Installation Guide](https://docs.docker.com/get-docker/)
*   **Hugging Face API Token:** You can get a free token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

### Installation & Running

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Gagan-P/CogitoErgoCode.git
    cd CogitoErgoCode
    ```

2.  **Set up your API Token:**
    You need to provide your Hugging Face API token as an environment variable. You can do this by exporting it in your terminal session:
    ```bash
    export HF_TOKEN="your_api_token_here"
    ```

3.  **Run with Docker Compose:**
    With the environment variable set, run the application:
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker image and start the application.

4.  **Access the application:**
    Open your web browser and navigate to `http://localhost:5000`. You can now start generating images!

## About the Author

This project was created by **Gagan P** to showcase applications of Python, machine learning, and data analytics to drive technological advancements and foster creative solutions.
