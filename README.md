# 🎬 Late Show API

A RESTful backend service for managing a fictional late-night talk show. The API supports user authentication, guest and episode management, and tracks guest appearances with performance ratings.

Built with Flask, PostgreSQL, and JWT for secure access control.

---

## 🔧 Tech Stack

- **Backend:** Python, Flask, Flask SQLAlchemy, Flask-JWT-Extended
- **Database:** PostgreSQL
- **Migrations:** Flask-Migrate
- **Auth:** JWT (Token-Based Authentication)
- **Testing:** Postman
- **Architecture:** Modular MVC

---

## 🌐 API Endpoints

| Method | Endpoint              | Auth | Description                            |
|--------|-----------------------|------|----------------------------------------|
| POST   | `/register`           | ❌    | Register a new user                    |
| POST   | `/login`              | ❌    | Login and receive JWT token            |
| GET    | `/guests`             | ❌    | Retrieve all show guests               |
| GET    | `/episodes`           | ❌    | Retrieve all episodes                  |
| GET    | `/episodes/<id>`      | ❌    | Retrieve a single episode + guests     |
| POST   | `/appearances`        | ✅    | Create new guest appearance            |
| DELETE | `/episodes/<id>`      | ✅    | Delete an episode and its appearances  |

> 🔐 Protected routes require a valid JWT token in the `Authorization: Bearer <token>` header.

---

## 📁 Project Structure

late-show-api-challenge/
├── server/
│ ├── app.py
│ ├── config.py
│ ├── seed.py
│ ├── models/
│ └── controllers/
├── migrations/
├── .env
├── Pipfile
├── README.md
└── challenge-4-lateshow.postman_collection.json

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
2. Set Up Environment
Install dependencies:

bash
Copy
Edit
pipenv install
pipenv shell
Create a .env file:

ini
Copy
Edit
DB_USER=your_postgres_user
DB_PASSWORD=your_password
DB_NAME=late_show_db
DB_HOST=localhost
DB_PORT=5432
JWT_SECRET_KEY=your_secret_key
Be sure to keep your .env file out of version control.

3. Database Setup
Ensure PostgreSQL is running, then run:

bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python server/seed.py
4. Run the App
bash
Copy
Edit
flask run
App will be available at:
http://localhost:5000

🧪 Testing the API
Use Postman to test all routes.

Import the provided collection:

pgsql
Copy
Edit
challenge-4-lateshow.postman_collection.json
Authenticate using /login, then copy the JWT token and set it as a variable or use it directly in headers.

📌 Highlights
Secure route protection using JWT

Relationship modeling via SQLAlchemy ORM

Cascade deletion of related data

Modular, scalable architecture

Fully tested endpoints

✍️ Author
George Mwazuna
Backend Developer
GitHub Profile

🏁 License
This project is open-source and available under the MIT License.

markdown
Copy
Edit
