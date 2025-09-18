FROM python:3.11
WORKDIR /customer-app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["uvicorn", "customer_main:app", "--reload" ,"--host", "0.0.0.0","--port", "8000"]
