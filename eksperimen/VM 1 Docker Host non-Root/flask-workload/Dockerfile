# Menggunakan base image Python yang ringan
FROM python:3.10-slim

# Menentukan direktori kerja
WORKDIR /app

# Menyalin semua file ke dalam container
COPY . .

# Instal dependensi Flask & Gunicorn
RUN pip install flask gunicorn

# Menentukan command default untuk menjalankan app
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]


