#  New York Real Estate Valuation Model Backend

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

A high-performance, production-ready inference server for predicting real estate prices. Built with **FastAPI** for low-latency request handling and **Scikit-learn** for robust predictive modeling.

---

##  Overview

This repository serves as the backbone for a real estate valuation engine. It provides a RESTful API that accepts property characteristics and returns a predicted market price using a pre-trained machine learning model.

### Key Architectural Highlights
- **High Throughput**: Leverages FastAPI's asynchronous capabilities for efficient request processing.
- **Type Safety**: Uses Pydantic for strict data validation and automated documentation.
- **Microservices Ready**: Optimized for containerization and horizontal scaling.
- **Real-time Inference**: Low-latency model serving using serialized pipelines.

---

##  Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast (high-performance) web framework.
- **Machine Learning**: [Scikit-learn](https://scikit-learn.org/) - Industry-standard library for predictive data analysis.
- **Data Validation**: [Pydantic](https://docs.pydantic.dev/) - Data validation using Python type hints.
- **Server**: [Uvicorn](https://www.uvicorn.org/) - ASGI server implementation for Python.

---

##  Project Structure

```text
├── main.py              # Entry point: FastAPI app & route definitions
├── schema.py            # Pydantic models for request/response validation
├── house_price_model.pkl # Serialized Scikit-learn model
├── requirements.txt      # Project dependencies
└── README.md            # You are here!
```

---

##  Getting Started


### Prerequisites
- Python 3.8+
- Virtual Environment (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aryama02/House_price_prediction_Backend.git
   cd House_price_prediction_Backend
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

Start the development server with auto-reload:
```bash
python main.py
```
The API will be available at `http://localhost:8000`.

---

##  API Documentation

Once the server is running, you can access the interactive Swagger UI at:
 [http://localhost:8000/docs](http://localhost:8000/docs)

### Endpoints

#### `POST /predict-price`
Predicts the price of a house based on input features.

**Request Body (`application/json`):**
```json
{
    "BathroomsFull": 2,
    "BathroomsHalf": 1,
    "BedroomsTotal": 3,
    "LivingArea": 1500.5
}
```

**Response (`application/json`):**
```json
{
    "predicted_price": 450000.0
}
```

---

##  Model Details

The backend utilizes a serialized `.pkl` file (`house_price_model.pkl`) containing a trained regression model. 

### Input Features:
1. `BathroomsFull`: Number of full bathrooms.
2. `BathroomsHalf`: Number of half bathrooms.
3. `BedroomsTotal`: Total number of bedrooms.
4. `LivingArea`: Total living area in square feet.

---

##  Best Practices & Quality Assurance

- **CORS Configured**: CORS middleware enabled to allow seamless integration with frontend applications.
- **Modular Schema**: Input validation logic is decoupled into a dedicated `schema.py` for maintainability.
- **Error Handling**: Built-in FastAPI mechanisms handle malformed requests with descriptive 422 Unprocessable Entity errors.

---

## Future Roadmap

- [ ] Implement Redis-based caching for frequent identical prediction requests.
- [ ] Add Prometheus/Grafana integration for monitoring inference latency.
- [ ] Dockerize the application for Kubernetes deployment.
- [ ] Integrate a database (PostgreSQL) for logging and feedback loop data collection.

---

##  Author
**Aryan**  
*Aspiring AI Engineer*

---

