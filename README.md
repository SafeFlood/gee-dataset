# gee-dataset

Repositori ini berisi kode dan skrip untuk mengelola dataset pada Google Earth Engine (GEE).

## Cara Setup Environment

Ikuti langkah-langkah berikut untuk menyiapkan environment agar dapat menjalankan kode di repositori ini:

### 1. Clone Repositori

```bash
git clone https://github.com/SafeFlood/gee-dataset.git
cd gee-dataset
```

### 2. Membuat & Mengaktifkan Virtual Environment (Opsional tapi direkomendasikan)

**Menggunakan Python (pastikan sudah terinstall Python 3.7 atau lebih baru):**

```bash
python -m venv venv
source venv/bin/activate  # Untuk Linux/MacOS
venv\Scripts\activate     # Untuk Windows
```

### 3. Instalasi Dependencies

Pastikan Anda sudah berada di direktori utama repositori. Kemudian jalankan:

```bash
pip install -r requirements.txt
```

Jika file `requirements.txt` belum tersedia, silakan tambahkan dependensi yang dibutuhkan secara manual.

### 4. Konfigurasi Environment Variables

Buat file `.env` di direktori root (jika diperlukan) dan tambahkan variabel yang dibutuhkan, seperti API Key, credential, dll.

Contoh isi file `.env`:
```
GEE_SERVICE_ACCOUNT=your_service_account.json
ANOTHER_ENV_VAR=value
```

### 5. Autentikasi Google Earth Engine

Pastikan Anda sudah melakukan autentikasi di Google Earth Engine. Jalankan:

```bash
earthengine authenticate
```

Ikuti instruksi pada terminal untuk login dan mengizinkan akses.

---

## Catatan Tambahan

- Pastikan semua dependensi terinstall dengan baik.
- Jika ada library khusus yang dibutuhkan, tambahkan ke `requirements.txt`.
- Lihat dokumentasi atau script di dalam repositori ini untuk lebih detail.

Jika ada pertanyaan lebih lanjut, silakan buka issue di repositori ini.
