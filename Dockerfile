FROM lambci/lambda:build-python3.8

RUN mkdir /src
WORKDIR /src

RUN pip install -U pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY fixtures fixtures
COPY tests.py tests.py

CMD python -m app.main run
