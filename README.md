# 🏥 Insurance Premium Category Predictor

A full-stack machine learning application that predicts insurance premium categories based on user demographics and lifestyle factors. Built with FastAPI for the backend API and Streamlit for the interactive frontend.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Docker Deployment](#docker-deployment)
- [Development](#development)

## ✨ Features

- **RESTful API** built with FastAPI for fast, asynchronous predictions
- **Interactive Web Interface** using Streamlit for easy user interaction
- **Machine Learning Model** that classifies insurance premiums into categories (Low, Medium, High)
- **Intelligent Feature Engineering** including:
  - Automatic BMI calculation from height and weight
  - Lifestyle risk assessment based on smoking status and BMI
  - City tier classification (Tier 1, Tier 2, Others)
  - Age group categorization
- **Comprehensive Predictions** with confidence scores and class probabilities
- **Docker Support** for containerized deployment
- **Input Validation** using Pydantic models
- **Health Check Endpoint** for monitoring

## 🛠 Tech Stack

**Backend:**
- FastAPI - Modern, fast web framework for building APIs
- Pydantic - Data validation using Python type annotations
- Scikit-learn - Machine learning model training and prediction
- Pandas & NumPy - Data manipulation and processing
- Uvicorn - ASGI server for FastAPI

**Frontend:**
- Streamlit - Interactive web application framework

**Development Tools:**
- Black, YAPF, Autopep8 - Code formatting
- isort - Import sorting
- Flake8 - Code linting

## 📁 Project Structure

```
fastapi-model/
├── app/
│   ├── main.py           # FastAPI application and endpoints
│   ├── models.py         # Pydantic models for request validation
│   ├── schemas.py        # Response schemas
│   └── utils.py          # Utility functions (city tier classification)
├── model/
│   ├── ml.py             # ML model loading and prediction logic
│   └── model.pkl         # Trained scikit-learn model (pickle file)
├── frontend/
│   ├── app.py            # Streamlit web interface
│   └── .streamlit/
│       └── config.toml   # Streamlit configuration
├── data/
│   └── insurance.csv     # Training dataset
├── noteboooks/
│   └── fastapi_ml_model.ipynb  # Model training notebook
├── tests/                # Test directory
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Project configuration
└── README.md             # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.12 or higher
- pip package manager

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd fastapi-model
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running the Backend API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

- Interactive API docs: `http://127.0.0.1:8000/docs`
- Alternative docs: `http://127.0.0.1:8000/redoc`

### Running the Frontend

In a separate terminal, start the Streamlit app:

```bash
streamlit run frontend/app.py
```

The web interface will open automatically at `http://localhost:8501`

## 📚 API Documentation

### Endpoints

#### `GET /`
Welcome endpoint
- **Response:** `{"message": "Premium prediction model"}`

#### `GET /health`
Health check endpoint
- **Response:** `{"status": "ok"}`

#### `POST /predict`
Predict insurance premium category

**Request Body:**
```json
{
  "age": 30,
  "weight": 70.0,
  "height": 1.75,
  "income_lpa": 12.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Response:**
```json
{
  "predicted_category": "High",
  "confidence": 0.8758,
  "class_probabilities": {
    "Low": 0.01,
    "Medium": 0.15,
    "High": 0.84
  }
}
```

**Fields:**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| age | integer | 0 < age < 120 | User's age |
| weight | float | > 0 | Weight in kg |
| height | float | 0 < height < 2.5 | Height in meters |
| income_lpa | float | > 0 | Annual income in lakhs per annum |
| smoker | boolean | - | Smoking status |
| city | string | - | City of residence |
| occupation | string | enum | One of: retired, freelancer, student, government_job, business_owner, unemployed, private_job |

**Computed Features:**
- **BMI:** Calculated as weight / (height²)
- **Lifestyle Risk:** Categorized as high/medium/low based on smoking and BMI
- **City Tier:** Classified as Tier 1, Tier 2, or Others
- **Age Group:** Categorized into appropriate age ranges

## 🐳 Docker Deployment

### Building the Docker Image

```bash
docker build -t insurance-premium-api .
```

### Running the Container

```bash
docker run -d -p 8000:8000 --name insurance-api insurance-premium-api
```

The API will be accessible at `http://localhost:8000`

### Docker Compose (Optional)

Create a `docker-compose.yml` for easier orchestration:

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - ENVIRONMENT=production
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

## 🔧 Development

### Code Formatting

Format code with Black:
```bash
black app/ model/ frontend/
```

### Import Sorting

Sort imports with isort:
```bash
isort app/ model/ frontend/
```

### Linting

Check code quality:
```bash
flake8 app/ model/ frontend/
```

### Running Tests

```bash
pytest tests/
```

## 🎯 Model Information

The machine learning model uses the following features for prediction:

1. **BMI** - Body Mass Index calculated from height and weight
2. **Age Group** - Categorized age ranges
3. **Lifestyle Risk** - Computed from smoking status and BMI
4. **City Tier** - Metropolitan classification
5. **Income (LPA)** - Annual income in lakhs
6. **Occupation** - Professional category

The model outputs:
- **Predicted Category** - Low, Medium, or High premium
- **Confidence Score** - Model's certainty (0-1)
- **Class Probabilities** - Probability distribution across all categories



## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Streamlit for the simple yet powerful UI framework
- Scikit-learn for machine learning capabilities
