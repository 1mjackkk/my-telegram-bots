# 1. Base Image
FROM python:3.10-slim

# 2. Working Directory
WORKDIR /app

# 3. Requirements install karna
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Saara code copy karna
COPY . .

# 5. Port open karna
EXPOSE 8080

# 6. Command: Gunicorn se Flask chalega aur python se aapki main file
CMD gunicorn 40in1:app & python 40in1.py
