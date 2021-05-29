# GET BASE IMAGE
FROM python:3.6.9

# UPDATE PIP
RUN pip install --upgrade pip

# INSTALL APP requirements.txt (python modules)
COPY app /app
WORKDIR /app
RUN export $(xargs < .env)
RUN pip install -r requirements.txt

# RUN DJANGO APP
CMD ["./run.sh"]