# DESCRIPTION: Simple flask base app, with sqlite capabilities 
# (install flask base libs from dockerfile,
# add other libs depending of project via requirements)
# AUTHORS: Alexis Mathon <mathonal@gmail.com>
# USAGE:
# DOCKER IMAGE BUILD command :
# docker build . -t delka/flask
# DOCKER RUN command :
# docker run -it -p 5000:5000 -v /home/delka/work/GitRepos/mydynamicCV:/src delka/flask
#
# NOTE : next/other version due when i have all pieces form REST API in SQLAzure 
#
FROM python:alpine
# INSTALLING  pre-requisites
RUN pip install --upgrade pip

# INSTALLING python flask libs from volume (project directory)
WORKDIR /usr/src
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
