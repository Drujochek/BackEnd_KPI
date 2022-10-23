FROM python:3.8.3

ENV FLASK_APP=projectfiles

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY projectfiles /opt/projectfiles

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT