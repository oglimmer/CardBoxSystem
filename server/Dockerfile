FROM python:3

WORKDIR /opt/server

COPY . /opt/server

RUN pip install fastapi "uvicorn[standard]" pydantic

CMD ["uvicorn", "server:app", "--host", "0.0.0.0"]
