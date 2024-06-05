# Words API

A simple project to learn a bit about Django REST Framework.

Has a simple API to manage words and their meanings and link them to a language

## Routes

Run the app:

```bash 
python manage.py runserver
```

To see the available API routes, you can go to `http://127.0.0.1:8000/swagger/` to view the Swagger documentation.

All routes are protected by JWT authentication, so you need to get a token from the `/login` route and use it in the `Authorization` header.

For example

To login, you can use the following command to return a token:

```bash
curl -L -XPOST http://localhost:8000/api/login/ -d '{"username": "nick2", "password": "password"}' -H "Content-Type: application/json"
```

And then use it in subsequent API requests:

```bash
❯ curl -L -H "Content-Type: application/json" -H "Authorization: Token <token>" localhost:8000/api/languages/
[{"id":2,"name":"Indonesian","created_at":"2024-06-05T11:45:44.453221Z","updated_at":"2024-06-05T11:45:44.453247Z"}]%
```