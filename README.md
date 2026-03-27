 HEAD
# CaliperWeb
UI for customers 
# CaliperAI Demo Booking App

An interactive Streamlit web application for showcasing CaliperAI products and allowing users to book product demos.

---

## Features

- Product demo video integration  
- Product selection dropdown  
- Demo scheduling using date picker  
- User input form for use case, company, and contact details  
- PostgreSQL database integration  
- Custom UI with background image and styling  
- Interactive drag-to-pan background  

---

## Tech Stack

- Frontend: Streamlit  
- Backend: Python  
- Database: PostgreSQL  
- Styling: Custom CSS, HTML, JavaScript  
- Deployment: Streamlit Cloud  

---

## Project Structure

```
.
├── app.py
├── Background.png
├── first_logo.png
├── requirements.txt
└── README.md
```

---

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/caliperai-demo.git
cd caliperai-demo
```

---

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run the Application

```bash
streamlit run app.py
```

---

## Database Setup (PostgreSQL)

### Create Database and Table

```sql
CREATE DATABASE caliper;

\c caliper;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    product TEXT,
    email TEXT,
    phone TEXT,
    demo_date DATE,
    request TEXT,
    institution TEXT
);
```

---

## Environment Variables (Recommended)

Instead of hardcoding credentials, use environment variables:

```python
import os

DATABASE_URL = os.getenv("DATABASE_URL")
```

---

## Deployment (Streamlit Cloud)

1. Push the code to GitHub  
2. Go to https://streamlit.io/cloud  
3. Create a new app  
4. Select the repository  
5. Set main file as `app.py`  
6. Add secrets:

```toml
DATABASE_URL = "your_postgresql_connection_string"
```

---

## Future Improvements

- Email notifications on form submission  
- Admin dashboard for viewing submissions  
- Authentication system  
- Multi-page app structure  
- API integration  

---

## Contributing

Contributions are welcome. Fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Author

Built using Streamlit
 ae8b89b (First commit)
