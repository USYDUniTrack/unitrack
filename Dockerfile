FROM python:3.12.1

RUN mkdir -p /home/app

# create the app user
RUN adduser app

ENV HOME=/home/app
RUN mkdir $HOME/staticfiles

WORKDIR $HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# chown all the files to the app user
RUN chown -R app:app $HOME
EXPOSE 8000

USER app:app
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
