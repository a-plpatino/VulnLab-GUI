FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install flask
RUN python init_db.py
EXPOSE 5003
CMD ["python", "app.py"]
