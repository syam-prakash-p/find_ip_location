FROM python:alpine3.15
RUN pip install flask requests
COPY app app
WORKDIR app
EXPOSE 5000
ENTRYPOINT ["python3","main.py"]
