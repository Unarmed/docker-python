FROM python:2

RUN pip2 install flask
RUN pip2 install psycopg2

ADD app.py .

CMD python2 app.py
