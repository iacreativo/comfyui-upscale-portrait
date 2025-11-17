FROM python:3.10
WORKDIR /src
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV PORT 8080
EXPOSE 8080
CMD ["python", "main.py", "--listen", "--port", "8080"]
