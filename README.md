
# To-Do List Application

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Database Migration](#database-migration)

## Introduction

The To-Do List application is a web-based tool that allows users to manage their tasks effectively. Users can create, edit, delete, and filter tasks based on various parameters such as priority, status, and due date. This application uses Flask as the backend framework and SQLAlchemy for database interactions.

## Features

- **User Registration and Authentication**: Users can register and log in securely.
- **Task Management**: Create, read, update, and delete tasks.
- **Filters**: Search and filter tasks by content, status, priority, and due date.
- **Responsive Design**: User-friendly interface that works on both desktop and mobile devices.
- **Flash Messages**: Provides feedback on user actions (success or error).

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **SQLAlchemy**: An ORM for managing database interactions.
- **Flask-Migrate**: Database migration handling for SQLAlchemy.
- **Flask-Bcrypt**: Password hashing to secure user passwords.
- **Flask-Login**: User session management.
- **SQLite**: Lightweight database for storing user and task data.
- **HTML/CSS**: For creating the user interface.
  
**Login Page**
  ![Screenshot of To-Do List Application](https://github.com/Ruksina01/Flask-Todo-List-App/blob/main/images_output/todo1.png?raw=true)

**Registration Page**
  ![Screenshot of To-Do List Application](https://github.com/Ruksina01/Flask-Todo-List-App/blob/main/images_output/todo3.png?raw=true)

**Interface**
  ![Screenshot of To-Do List Application](https://github.com/Ruksina01/Flask-Todo-List-App/blob/main/images_output/todo2.png?raw=true)
  

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**
- **pip** (Python package installer)

### Step-by-Step Setup

1. **Clone the Repository**:

   Open your terminal and run the following command to clone the repository:

   ```bash
   git clone https://github.com/yourusername/todolistapp.git
   ```

   Replace `yourusername` with your actual GitHub username.

2. **Navigate to the Project Directory**:

   ```bash
   cd todolistapp
   ```

3. **Create a Virtual Environment**:

   It’s a good practice to create a virtual environment for your projects:

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install Required Packages**:

   Use the following command to install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. **Set Environment Variables**:

   Create a `.env` file in the root directory of the project and add the following lines:

   ```plaintext
   SECRET_KEY=your_secret_key
   ```

   Replace `your_secret_key` with a strong secret key for session management.

## Usage

1. **Run the Application**:

   After setting everything up, you can run the application with the following command:

   ```bash
   python app.py
   ```

   The application will start on `http://127.0.0.1:5000`.

2. **Access the Application**:

   Open your web browser and go to `http://127.0.0.1:5000`. You will be directed to the login page. If you don't have an account, you can register by clicking on the "Register" link.

3. **Managing Tasks**:

   - Once logged in, you can add new tasks using the provided form.
   - Edit or delete existing tasks as needed.
   - Use the search and filter options to manage your tasks more effectively.

## Configuration

- The application uses SQLite for database storage by default. You can change this to a different database by modifying the `SQLALCHEMY_DATABASE_URI` in `app.py`.

## Database Migration

To manage database migrations:

1. **Initialize Migrations**:

   ```bash
   flask db init
   ```

2. **Create a Migration Script**:

   ```bash
   flask db migrate -m "Initial migration."
   ```

3. **Apply Migrations**:

   ```bash
   flask db upgrade
   ```
   
## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [SQLAlchemy](https://www.sqlalchemy.org/) - The ORM for database interactions.
- [Bootstrap](https://getbootstrap.com/) - The CSS framework used for responsive design.

