# Contacts API

This is a simple Contacts API built with Flask and several popular extensions, including Flask-RESTful, Flask-SQLAlchemy, Flask-Marshmallow, Flask-Bcrypt, Flask-CORS, Flask-JWT-Extended, and more. The API allows users to manage their contact lists and provides user authentication to ensure privacy and security.

## Features

- User registration and authentication using JWT (JSON Web Tokens)
- Create, read, update, and delete operations for contacts
- User-specific contact lists to maintain privacy
- Secure password hashing using Flask-Bcrypt
- Cross-Origin Resource Sharing (CORS) support for handling cross-domain requests
- Data serialization and deserialization using Flask-Marshmallow
- Persistent storage and querying of contacts using Flask-SQLAlchemy
- Consistent RESTful API design and error handling using Flask-RESTful

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TheDayDreamer01/Contacts-Flask-API.git
   cd contacts-flask-api
   ```

2. Create and activate a virtual environment:

   ```bash
   virtualenv env
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the application by modifying the `config.py` file.

5. Start the server:

   ```bash
   python server.py
   ```

   The API will be accessible at `http://localhost:5000`.

## API Endpoints

### Authentication

- `POST /api/auth/register`: Register a new user. Required fields: `username`, `password`.
- `POST /api/auth/login`: Log in with an existing user. Required fields: `username`, `password`.
- `POST /api/auth/logout`: Log out the currently logged-in user.

### Contacts

- `GET /api/contacts`: Retrieve all contacts for the authenticated user.
- `GET /api/contacts/<contact_id>`: Retrieve a specific contact by ID.
- `POST /api/contacts`: Create a new contact. Required fields: `name`, `phone`, `email`.
- `PUT /api/contacts/<contact_id>`: Update an existing contact by ID. Required fields: `name`, `phone`, `email`.
- `DELETE /api/contacts/<contact_id>`: Delete a contact by ID.

## Error Handling

The API provides consistent error responses with appropriate status codes and error messages in case of any issues. Make sure to handle errors and exceptions in your client application.

## Security

User authentication is implemented using JSON Web Tokens (JWT). Each request to protected endpoints requires the inclusion of a valid JWT token in the `Authorization` header. Unauthorized requests will be denied access.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for both commercial and non-commercial purposes.
