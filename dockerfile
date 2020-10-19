# DOCKER IMAGE BUILD command :
# docker build . -t delka/flask
# DOCKER RUN command : (note : modify Sqlpopulate to true in local setup)
# docker run -it -p 5000:5000 -v /home/delka/work/GitRepos/mydynamicCV:/src delka/flask

FROM python:alpine
#nota : NO "apt-get" on alpine
#RUN apk update && apk add sqlite3
#RUN apk add --update sqlite

RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install pysqlite3 

COPY . /src

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
