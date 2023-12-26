FROM python:3.7

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8502

COPY . /app

WORKDIR /app/streamlit

ENTRYPOINT ["streamlit", "run", "--server.port", "8502"]

CMD ["app.py"]
