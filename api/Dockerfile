FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app/api
COPY requirements.txt /app/api/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/api/

CMD python main.py
