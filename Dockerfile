FROM python:3.9-alpine
COPY . .
RUN pip install -U discord.py python-dotenv requests
CMD ["python", "main.py"]