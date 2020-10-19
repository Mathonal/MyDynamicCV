# docker run -it -p 5000:5000 -v /home/delka/work/Flask/dynaCV:/src delka/flask

FROM python:alpine

# NO apt-get on alpine
#RUN apk update && apk add sqlite3
RUN apk add --update sqlite

RUN pip install flask
RUN pip install flask_sqlalchemy

COPY . /src

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
