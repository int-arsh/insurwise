# Day2
 
## Improve
- create a new folder
- field validator for city + occcupation feature
- add routes
    - home -> health check
- add model version
- separation of logic
    - pydantic model
    - city tier
    - ml model
- try catch
- add confidence score
- Response model
```
fastapi-model/
│
├── app/
│   ├── main.py
│   ├── ml.py
│   ├── utils.py
│   └── models.py
│
├── data/
│   └── insurance.csv
│
├── model/
│   └── model.pkl
│
├── notebooks/
│   └── fastapi_ml_model.ipynb
│
├── requirements.txt
└── README.md
```

---
Instructions:
 1. create an EC2 instance
 2. Connect to the EC2 instance

 3. Run the following commands
  a. sudo apt-get update
  b. sudo apt-get install -y docker.io
  c. sudo systemctl start docker
  d. sudo systemctl enable docker
  e. sudo usermod -aG docker $USER
  f. exit
 
 4. Restart a new connection to EC2 instance
 5. Run the following commands
  a. docker pull tweakster24/insurance-premium-api:latest
  b. docker run -p 8000:8000 tweakster24/insurance-premium-api

 6. change security group settings
 7. Check the API 
 8. Change the frontend code


 
