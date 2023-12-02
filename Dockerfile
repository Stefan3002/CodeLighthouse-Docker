FROM python

WORKDIR /app

COPY './assertions.py' /app

CMD ["python", "-m", "unittest", "assertions.py"]