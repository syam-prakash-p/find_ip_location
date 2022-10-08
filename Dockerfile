FROM python:alpine3.15
RUN pip install flask requests redis
COPY app app
ENV REDIS_HOST "localhost"
ENV REDIS_PORT 6379
WORKDIR app
EXPOSE 5000
ENTRYPOINT ["python3","main.py"]
