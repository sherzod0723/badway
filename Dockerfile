FROM python:latest

WORKDIR /app
COPY . /app


RUN pip install -r req.txt

EXPOSE 8585

#ENTRYPOINT ["sh", "entrypoint.sh"]
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8585"]
