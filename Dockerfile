FROM python:3.10.6
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY myrestapi /code
CMD ["python", "manage.py", "migrate"]
EXPOSE 8080