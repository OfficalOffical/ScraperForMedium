# Dockerfile, image, Container

FROM python:3.9.5

ADD setup.py .

ADD webScraper.py .

RUN pip install beautifulsoup4==4.11.1 pandas==1.4.3 requests==2.28.1

CMD ["python", "./setup.py"]