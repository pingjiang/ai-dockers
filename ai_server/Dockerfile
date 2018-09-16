FROM python:alpine 

LABEL maintainer="pingjiang"

RUN pip install Flask

COPY src /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
