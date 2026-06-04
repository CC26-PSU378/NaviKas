# NaviKas — Asisten Keuangan Pribadi Berbasis AI

> **Navigasi Kas** — Kelola keuanganmu lebih cerdas dengan analitik perilaku, prediksi AI, dan chatbot finansial personal.

🌐 **Live App:** [navi-kas.vercel.app](https://navi-kas.vercel.app)
📋 **API Docs:** [navikas-production.up.railway.app/docs](https://navikas-production.up.railway.app/docs)

---

## Daftar Isi

1. [Tentang NaviKas](#tentang-navikasproject)
2. [Fitur Utama](#fitur-utama)
3. [Panduan Penggunaan](#panduan-penggunaan)
   - [Membuat Akun](#1-membuat-akun)
   - [Login](#2-login)
   - [Dashboard](#3-dashboard)
   - [Catat Transaksi](#4-catat-transaksi)
   - [Kelola Transaksi](#5-kelola-transaksi)
   - [Analitik Keuangan](#6-analitik-keuangan)
   - [Financial DNA](#7-financial-dna)
   - [NaviKas AI (NaviBot)](#8-navikasai--navibot)
   - [Pengaturan Akun](#9-pengaturan-akun)
4. [Teknologi](#teknologi)
5. [Kontribusi & Pengembangan](#kontribusi--pengembangan)
6. [Link & Sumber Daya](#link--sumber-daya)

---

## Tentang NaviKas

NaviKas adalah aplikasi web keuangan pribadi yang menggabungkan **pencatatan transaksi**, **analitik berbasis data**, **prediksi AI**, dan **chatbot finansial** dalam satu platform.

Berbeda dari aplikasi pencatat biasa, NaviKas menganalisis *pola perilaku* keuanganmu — bukan hanya saldo — sehingga kamu mendapat insight yang benar-benar personal dan actionable.

---

## Fitur Utama

| Fitur | Deskripsi |
|---|---|
| 📊 **Dashboard Real-time** | Pantau saldo, grafik, dan transaksi terkini dalam satu layar |
| 🤖 **Prediksi AI** | Estimasi kondisi keuangan akhir bulan berbasis model Keras |
| 🧬 **Financial DNA** | Profil visual kebiasaan belanjamu dari 4 dimensi perilaku |
| 💬 **NaviBot AI** | Chatbot finansial personal yang menjawab berdasarkan data transaksimu |
| 📈 **Analitik Mendalam** | Tren, rincian per kategori, dan perbandingan bulanan |
| 🔐 **Login Google** | Masuk cepat dengan akun Google — tanpa ribet isi form |
| 🌙 **Mode Gelap/Terang** | Tampilan sesuai selera |

---

## Panduan Penggunaan

### 1. Membuat Akun

Buka aplikasi di browser, lalu klik **"Mulai Gratis"** atau **"Daftar"**.

Ada dua cara mendaftar:

**Daftar dengan email:**
1. Klik tab **"Daftar"**
2. Isi nama lengkap, email, dan password
3. Klik **"Buat Akun"**

**Daftar dengan Google:**
1. Klik tombol **"Lanjutkan dengan Google"**
2. Pilih akun Google kamu — selesai, langsung masuk

---

### 2. Login

**Login dengan email:**
1. Klik **"Masuk"**
2. Isi email dan password yang sudah terdaftar
3. Klik **"Masuk"**

**Login dengan Google:**
Klik tombol **"Lanjutkan dengan Google"**, pilih akun, dan kamu langsung masuk ke dashboard.

---

### 3. Dashboard

Setelah login, kamu langsung masuk ke **Dashboard** — pusat kendali keuanganmu.

Yang bisa kamu lihat di sini:

- **Kartu Saldo** — total saldo bersih (pemasukan − pengeluaran)
- **Grafik Batang** — visual pengeluaran dan pemasukan per bulan
- **Transaksi Terbaru** — daftar aktivitas keuangan terkini
- **Prediksi AI** — estimasi kondisi keuanganmu ke depan

> 💡 Di pojok kanan bawah ada ikon **robot biru** — itu NaviBot AI. Klik kapan saja untuk bertanya soal keuanganmu.

---

### 4. Catat Transaksi

**Cara cepat dari Dashboard:**
Klik tombol **"+ Tambah"** di kartu saldo.

**Dari halaman Transaksi:**
1. Klik menu **"Transaksi"** di sidebar kiri
2. Klik tombol **"Tambah Transaksi"** di pojok kanan atas

Isi form transaksi:

| Field | Keterangan | Contoh |
|---|---|---|
| **Jumlah** | Nominal uang | `50000` |
| **Tipe** | Pengeluaran atau Pemasukan | Pengeluaran |
| **Deskripsi** | Keterangan singkat | `Makan siang` |
| **Kategori** | Pilih dari daftar tersedia | Makanan |
| **Tanggal** | Kapan transaksi terjadi | 01/06/2026 |

Klik **"Simpan"** — transaksi langsung tercatat dan saldo diperbarui.

---

### 5. Kelola Transaksi

Di halaman **Transaksi**, kamu bisa melakukan semua ini:

**Filter & Cari**
- Gunakan tombol filter di atas tabel: **Semua / Pemasukan / Pengeluaran**
- Ketik kata kunci di kolom pencarian untuk menemukan transaksi tertentu

**Edit Transaksi**
1. Temukan transaksi yang ingin diubah
2. Klik ikon **pensil ✏️** di baris tersebut
3. Ubah data yang perlu direvisi
4. Klik **"Simpan"**

**Hapus Transaksi**
1. Klik ikon **tempat sampah 🗑️** di baris transaksi
2. Konfirmasi penghapusan di dialog yang muncul

> ⚠️ Penghapusan transaksi tidak bisa dibatalkan.

---

### 6. Analitik Keuangan

Klik menu **"Analitik"** di sidebar untuk melihat laporan mendalam:

- **Tren Pengeluaran** — grafik pergerakan pengeluaran dari waktu ke waktu
- **Rincian per Kategori** — proporsi pengeluaran per jenis (makan, transport, hiburan, dll.)
- **Prediksi Bulan Depan** — estimasi pengeluaran berdasarkan pola historis
- **Perbandingan Bulanan** — bulan ini vs bulan lalu, lengkap dengan persentase perubahan

Semakin banyak transaksi yang tercatat, semakin akurat analitiknya.

---

### 7. Financial DNA

Klik menu **"Financial DNA"** di sidebar.

Financial DNA adalah **profil perilaku keuangan personal** kamu — dihitung dari 4 dimensi:

| Dimensi | Yang Diukur |
|---|---|
| Konsistensi | Seberapa rutin kamu mencatat dan mengelola keuangan |
| Kontrol Impulsif | Seberapa sering kamu melakukan pengeluaran tidak terencana |
| Kebiasaan Menabung | Proporsi pemasukan yang tidak dihabiskan |
| Perencanaan | Seberapa baik pengeluaranmu sesuai anggaran |

Hasil skormu masuk ke salah satu dari tiga profil:

- 🟢 **Smart Saver** (skor ≥ 85) — disiplin dan terencana
- 🟡 **Balanced Planner** (skor 70–84) — cukup terencana dengan ruang perbaikan
- 🟠 **Impulsive Optimizer** (skor 55–69) — rentan impulsif, butuh perhatian ekstra

> 💡 Profil DNA kamu diperbarui otomatis setiap kali ada transaksi baru.

---

### 8. NaviKas AI — NaviBot

NaviBot adalah asisten keuangan AI yang menjawab pertanyaan **berdasarkan data transaksi pribadimu** — bukan jawaban generik.

**Cara membuka NaviBot:**
- Klik ikon **robot 🤖** di pojok kanan bawah layar, atau
- Pilih menu **"NaviBot AI"** di sidebar

**Contoh pertanyaan yang bisa kamu tanyakan:**

```
"Berapa total pengeluaranku bulan ini?"
"Kategori apa yang paling banyak kuhabiskan?"
"Apakah keuanganku sehat bulan ini?"
"Beri saran cara hemat bulan depan"
"Kapan terakhir kali aku mencatat pemasukan?"
"Bandingkan pengeluaranku bulan ini dengan bulan lalu"
```

NaviBot didukung oleh **Google Gemini** dan memiliki akses ke riwayat transaksimu, sehingga setiap jawaban disesuaikan dengan kondisi keuanganmu secara langsung.

> 💡 Chip saran pertanyaan tersedia di bagian bawah chat — klik untuk langsung bertanya tanpa ketik.

---

### 9. Pengaturan Akun

Klik menu **"Pengaturan"** di sidebar untuk mengatur:

| Opsi | Fungsi |
|---|---|
| **Nama Profil** | Ubah nama tampilan akun kamu |
| **Anggaran Bulanan** | Set batas pengeluaran yang ingin dijaga |
| **Tema Tampilan** | Pilih mode gelap atau terang |
| **Reset Data** | Hapus semua transaksi *(tidak bisa dibatalkan!)* |

**Keluar dari aplikasi:**
Di bagian bawah sidebar, klik nama/foto profil kamu → klik **"Keluar"**.

---

## Teknologi

| Layer | Teknologi |
|---|---|
| Frontend | React 18 + Vite |
| Backend | FastAPI (Python 3.12) |
| Database | PostgreSQL |
| ORM | SQLAlchemy + Alembic |
| AI/ML | TensorFlow / Keras |
| Chatbot AI | Google Gemini API |
| Auth | JWT + Google OAuth 2.0 |
| DevOps | Docker & Docker Compose |

---

## Menjalankan Secara Lokal

### Prasyarat
- Python 3.12
- Node.js 18+
- PostgreSQL

### 1. Clone Repository
```bash
git clone https://github.com/CC26-PSU378/NaviKas.git
cd NaviKas
```

### 2. Setup Backend
```bash
cd backend

# Buat virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Salin dan isi file environment
cp .env.example .env
# Edit .env — isi DATABASE_URL, SECRET_KEY, GROQ_API_KEY, GOOGLE_CLIENT_ID
```

### 3. Setup Frontend
```bash
cd frontend

# Install dependencies
npm install

# Salin dan isi file environment
cp .env.example .env
# Edit .env — isi VITE_API_URL=http://localhost:8000
```

### 4. Jalankan Aplikasi

**Terminal 1 — Backend:**
```bash
cd backend
.venv\Scripts\activate
uvicorn app.main:app --reload
```

**Terminal 2 — Frontend:**
```bash
cd frontend
npm run dev
```

Buka **http://localhost:5173** di browser.

## Link & Sumber Daya

| Resource | Link |
|---|---|
| 🌐 Aplikasi NaviKas | [navikasproject.vercel.app](https://navikasproject.vercel.app) |
| 📖 Dokumentasi API | [navikasproject.vercel.app/api/docs](https://navikasproject.vercel.app/api/docs) |
| 🤖 Model AI (Google Drive) | [Download Model Keras](https://drive.google.com/drive/folders/1rPTvN-7g-ZKWWVL-mzU-9kZF2C7jzxoP?usp=sharing) |

---
