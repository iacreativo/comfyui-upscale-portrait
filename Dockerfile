FROM python:3.10
WORKDIR /src
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install cog  # Necesario para correr predict.py con Replicate
ENV PORT 8080
EXPOSE 8080
