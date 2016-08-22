FROM python:2

RUN pip2 install flask

ADD app.py .

CMD python2 app.py
