# Student Performance Prediction
### Machine Learning Web App built with Django & HTML/CSS

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap)

## Project Overview

This is a full-stack Machine Learning web application that predicts a student's academic performance score based on key study factors. Built using **Django** (Python web framework), **scikit-learn** (Machine Learning), and a responsive **HTML/CSS** front-end with Bootstrap 5.

---

## Features

- **ML Prediction** - Predicts student exam score (0-100) using a trained regression model
- **Grade Display** - Shows grade: A+, A, B, C, D, or F with color-coded feedback
- **Input Validation** - Handles invalid inputs gracefully with error messages
- **Personalized Recommendations** - Gives tailored study tips based on your inputs
- **Animated Progress Bar** - Visual score meter with smooth animation
- **Fully Responsive UI** - Works on mobile, tablet, and desktop
- **Django MVC Architecture** - Clean separation of concerns

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 4.2 (Python) |
| Machine Learning | scikit-learn, NumPy, Pandas |
| Model Persistence | joblib |
| Frontend | HTML5, CSS3, Bootstrap 5.3 |
| Icons | Font Awesome 6.4 |
| Database | SQLite (Django default) |

---

## Input Features

| Feature | Description | Range |
|---------|-------------|-------|
| Study Hours | Daily study hours | 0 - 12 hrs |
| Attendance | Class attendance percentage | 0 - 100 % |
| Previous Score | Last exam score | 0 - 100 marks |
| Sleep Hours | Daily sleep duration | 0 - 12 hrs |
| Sample Papers | Practice papers solved | 0 - 20 papers |

---

## ML Models Used

The `ml_model.py` script trains and compares three models:
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

The best model (by R2 score) is automatically saved using `joblib`.

---

## Project Structure

```
Student-Performance-Prediction/
│
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore file
│
├── student_performance/               # Django project config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── predictor/                         # Django app
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py                       # Core prediction logic
│   ├── urls.py                        # URL routing
│   └── ml_model.py                    # ML training script
│
└── templates/
    └── predictor/
        ├── home.html                  # Input form page
        └── result.html                # Prediction result page
```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/manohar1305h/Student-Performance-Prediction.git
cd Student-Performance-Prediction
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Train the ML Model
```bash
python predictor/ml_model.py
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Start the Server
```bash
python manage.py runserver
```

### 7. Open in Browser
```
http://127.0.0.1:8000/
```

---

## Grading System

| Score Range | Grade | Performance |
|------------|-------|-------------|
| 90 - 100 | A+ | Outstanding |
| 80 - 89 | A | Excellent |
| 70 - 79 | B | Good |
| 60 - 69 | C | Average |
| 50 - 59 | D | Below Average |
| Below 50 | F | Fail |

---

## Screenshots

**Home Page** - Input form with study factor fields
**Result Page** - Score display with grade, progress bar, and personalized recommendations

---

## Author

**Manohar** | GitHub: [@manohar1305h](https://github.com/manohar1305h)

---

## License

This project is open-source and available under the [MIT License](LICENSE).
