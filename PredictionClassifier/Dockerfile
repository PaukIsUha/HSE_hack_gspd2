FROM nvcr.io/nvidia/pytorch:23.06-py3

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5623

CMD ["python", "main.py"]
