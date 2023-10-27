FROM python

WORKDIR /app

COPY . /app

CMD ["python", "assertions.py"]