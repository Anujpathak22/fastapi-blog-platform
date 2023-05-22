<img width="904" alt="Screenshot 2023-05-22 210201" src="https://github.com/Anujpathak22/fastapi-blog-platform/assets/84982825/201ba8b2-4c7e-4532-9a20-c71479ff0a0f">
# CRUD Operations Overview

This project implements a Flask API for performing CRUD (Create, Read, Update, Delete) operations on a blog.

## Functionality

The API supports the following CRUD operations:

- **Create**: Allows users to create new blog posts by sending a POST request to the `/posts` endpoint with the necessary data.
- **Read**: Retrieves blog posts by sending a GET request to the `/posts` endpoint. Users can retrieve all posts or filter them based on specific criteria.
- **Update**: Enables users to update existing blog posts by sending a PUT or PATCH request to the `/blog/<{id}>` endpoint with the updated data.
- **Delete**: Allows users to delete a specific blog post by sending a DELETE request to the `/blog/<{id}>` endpoint.
- **Login**: Registered users can log in with their credentials to access protected resources.



## API Endpoints

The API exposes the following endpoints:

- `GET /blog/`: Retrieves all blog posts.
- `POST /blog/`: Creates a new blog post.
- `GET /blog/<{id}>`: Retrieves a specific blog post.
- `PUT /blog/<{id}>`: Updates a specific blog post.
- `DELETE /blog/<{id}>`: Deletes a specific blog post.

## Usage

To use the API, make HTTP requests to the appropriate endpoints using tools like cURL, Postman, or any other API testing tool.

Ensure you include the required data and parameters in your requests according to the specific CRUD operation you want to perform.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>


## Command to build docker image
2. 
   ```bash
   docker build -t fastapi-app 
   
Feel free to customize the content, formatting, and instructions in the README.md file to match your specific Flask app's user authentication implementation.

# future work 
1. Adding the functionality of JWT TOKENS 
2. Deployement of the APP on Vercel or Swagger UI
