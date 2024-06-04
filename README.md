# Recipes Application

This project is a full-stack application for managing recipes. It features a Vue.js frontend and a Django backend. The frontend allows users to create, read, update, and delete recipes, as well as manage the ingredients for each recipe.

## Table of Contents

- [Installation](#installation)
- [Docker Setup](#docker-setup)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [API Endpoints](#api-endpoints)

## Installation

### Docker Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/jduffey1990/recipe-app.git
   cd recipe-app/recipe_app
   ``` 

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ``` 

3. Ensure Docker is installed and running on your system.

4. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ``` 

This will handle the installation of dependencies, setting up environment variables, running database migrations, and starting the development servers for both the backend and frontend.

## Usage

### Running the Application - when the above line has been completed and you server is running, it should be as easy as entering http://localhost:8080 into your browser.

1. Access the backend API at `http://localhost:8000`.
2. Access the frontend at `http://localhost:8080`.

### Creating and Managing Recipes

- The frontend provides an interface for creating, viewing, updating, and deleting recipes.
- Each recipe can have multiple ingredients associated with it.
- Use the provided forms to add ingredients to recipes.

## Technologies Used

- **Backend:** Django, Django REST framework, PostgreSQL
- **Frontend:** Vue.js, Axios
- **Docker:** For containerization of the application

## API Endpoints

- **GET** `/api/recipes/` - Retrieve a list of recipes.
- **POST** `/api/recipes/` - Create a new recipe.
- **GET** `/api/ingredients/` - Combine ingredients associated reverse ForeignKey.  Happens automatically.
- **POST** `/api/ingredients/` - Add an ingredient to a recipe.  Happens automatically after post.
- **DELETE** `/api/ingredients/delete_by_recipe/?recipe_id={id}` - Delete all ingredients associated with a recipe.
