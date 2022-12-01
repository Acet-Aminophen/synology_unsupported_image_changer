FROM python

WORKDIR /usr/src/app

RUN pip install --no-cache-dir pillow

COPY . .

CMD [ "python", "./main.py" ]