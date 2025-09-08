FROM python
WORKDIR /home/myapp/
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY callback.py .
COPY router_client.py .
COPY database.py .
COPY consumer.py .
COPY worker.py .
CMD python3 worker.py