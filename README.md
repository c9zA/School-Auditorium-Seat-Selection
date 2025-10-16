# School Auditorium Seat Selection System

A Flask-based web application for auditorium seat selection and booking.

## Features

- User authentication and login
- Interactive seat map visualization
- Real-time seat booking and cancellation
- User seat history tracking
- Responsive web interface

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript, jQuery
- **Styling**: Custom CSS

## Installation

### Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package manager)

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/c9zA/School-Auditorium-Seat-Selection.git
cd School-Auditorium-Seat-Selection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Setup MySQL Database:
```bash
# Import the database schema
mysql -u root -p < film.sql
```

4. Configure database connection in `main.py`:
```python
conn = pymysql.connect(
    host="localhost",  # Change for production
    port=3306,
    user="your_username",
    password="your_password",
    database="film",
    charset="utf8"
)
```

5. Run the application:
```bash
python main.py
```

Visit `http://127.0.0.1:5000` in your browser.

## Deployment

### Option 1: Heroku Deployment

1. Install Heroku CLI
2. Create a `Procfile`
3. Use a production WSGI server like Gunicorn
4. Configure environment variables for database

### Option 2: Railway/Render Deployment

1. Connect your GitHub repository
2. Set up environment variables
3. Configure MySQL database service

### Option 3: Traditional VPS

1. Setup a Linux server (Ubuntu/CentOS)
2. Install Python, MySQL, and Nginx
3. Use Gunicorn + Nginx for production

## Environment Variables

For production deployment, use environment variables:

- `DATABASE_HOST`: MySQL host
- `DATABASE_USER`: MySQL username  
- `DATABASE_PASSWORD`: MySQL password
- `DATABASE_NAME`: Database name
- `SECRET_KEY`: Flask secret key

## Project Structure

```
film/
├── main.py              # Flask application
├── requirements.txt     # Python dependencies
├── film.sql            # Database schema
├── static/             # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── *.png
├── templates/          # HTML templates
│   ├── index.html
│   ├── login.html
│   └── detail.html
└── README.md
```

## API Endpoints

- `GET/POST /` or `/login` - User login
- `GET /index` - Main seat selection page
- `POST /book` - Book a seat
- `POST /cancel` - Cancel seat booking
- `GET /get_detail` - Get user's booking details

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.