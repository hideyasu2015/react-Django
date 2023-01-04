# 参考 https://docs.docker.jp/compose/django.html#id2

# ================= Build =================

FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /back_code

# # Install System dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
#   # clean up
   && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /back_code/
RUN pip install -r requirements.txt

COPY . /back_code/


