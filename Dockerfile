FROM python:3.8

WORKDIR /app

COPY ./app .

RUN pip3 install -R requirements.txt && jupyter nbconvert --to python main.ipynb

CMD ["python3","app/main.py"]