# FROM ike-docker-local.artifactory.internetbrands.com/ib/ikenv:0.11.0 as ikenv
FROM webmd-docker-local.artifactory.internetbrands.com/consumer/baseimages/python3.10
# COPY --from=ikenv /usr/local/bin/ikenv /usr/local/bin/ikenv
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
# ENTRYPOINT [ "ikenv", "exec", "--" ]
CMD ["uvicorn", "main:app", "--port", "80", "--host", "0.0.0.0"]
