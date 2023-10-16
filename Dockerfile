FROM python:3.7.5 

ADD ./code/gits.py .

RUN pip install pytest mock coverage flake8

CMD ["gits", "hello_world"]
