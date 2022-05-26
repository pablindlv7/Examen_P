FROM python:3.10

ENV PYTHONUNBUFFERED 1
RUN mkdir /code 

WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/ 
EXPOSE  8000


CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "veterinaria", "veterinaria.wsgi:application"]