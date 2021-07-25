FROM python:3.9
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY junior /junior
WORKDIR /junior
COPY entrypoint.sh /
RUN chmod 777 /entrypoint.sh
ENTRYPOINT ["./../entrypoint.sh"]