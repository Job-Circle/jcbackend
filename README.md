# Django Backend Setup and Running Instructions

This document provides the steps to set up and run the Django backend.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Steps to Set Up and Run the Backend](#steps-to-set-up-and-run-the-backend)
  1. [Install the Required Packages](#1-install-the-required-packages)
  2. [Navigate to the Project Directory](#2-navigate-to-the-project-directory)
  3. [Run the Django Development Server](#3-run-the-django-development-server)
  4. [Test the Routes Using Postman](#4-test-the-routes-using-postman)
- [Routes](#routes)
  - [Posts Routes](#posts-routes)
    - [Create Posts](#create-posts)

## Prerequisites

- Python installed on your machine
- Pip (Python package installer) installed

## Steps to Set Up and Run the Backend

### 1. Install the Required Packages

Open a terminal and navigate to the project directory. Run the following command to install all required packages listed in `requirements.txt`:

```sh
pip install -r requirements.txt
```

### 2. Navigate to the Project Directory

Change directory to the `app` folder:

```sh
cd app
```

### 3. Run the Django Development Server

Start the Django development server by running the following command:

```sh
python manage.py runserver
```

### 4. Test the Routes Using Postman

- Open Postman.
- Use the appropriate HTTP methods (GET, POST, PUT, DELETE, etc.) to test the API endpoints.
- The server will be running at `http://127.0.0.1:8000/` (or a different port if specified).

Ensure that you use the correct endpoints as defined in your Django project.

- Always ensure that your virtual environment is activated if you are using one.

## Routes

### Posts Routes

#### Create Posts

- **URL:** 
  - `POST /posts`

- **Function:**
  - `createPosts`

- **Description:**
  - Creates a new post with specified title, content, author, date, initial likes, and dislikes and posts it to facebook.

- **Parameters:**

| Parameter | Type   | Description                 |
|-----------|--------|-----------------------------|
| title     | string | Title of the post           |
| content   | string | Content of the post         |
| author    | string | Author of the post          |
| date      | string | Date of the post (optional) |

- **Request Body Example:**
  ```json
  {
    "title": "Sample Post",
    "content": "This is the content of the post.",
    "author": "John Doe",
    "date": "2024-06-26"
  }
  ```

- **Additional Instructions:**

  Before using the `/posts` endpoint, ensure:
  - Add your bot email and password in the `facebook_controller.py` file for authentication.
  - Note: You need to be a member of the group to post if it is private.

- **Returns:**
  - Success: JSON response with a success message and HTTP status 201 (Created).
  - Error: JSON response with an error message and HTTP status 400 (Bad Request) if the request is invalid.

