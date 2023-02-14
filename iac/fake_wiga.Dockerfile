FROM python:3.11.0-bullseye
WORKDIR /code
COPY be/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY /be/api /code/be/api
COPY /be/controllers /code/be/controllers
EXPOSE 8080
CMD ["uvicorn", "be.api.main:api", "--host", "0.0.0.0", "--port", "8080"]