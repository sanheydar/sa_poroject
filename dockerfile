FROM python:3.12.3

WORKDIR /var/www

COPY ./requirements.txt/var/www

RUN pip install -r requirements.txt

COPY  ./var/www

CMD ["fastapi", "run", "main.py"]