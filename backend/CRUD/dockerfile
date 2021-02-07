FROM python:3.8.5
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /usr/src/backend
WORKDIR /usr/src/backend
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000