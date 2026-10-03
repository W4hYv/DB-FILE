# 🚀 BOT PORTOFOLIO: MANAJER PROYEK & INTERAKTIF MODAL 📊

Selamat datang di repositori **Bot Portofolio**! Sebuah bot Discord interaktif yang dibangun menggunakan **Python** dan **Discord.py** untuk membantu developer mengelola daftar proyek, keterampilan (*skills*), status pengembangan, hingga fitur formulir interaktif menggunakan Modal Windows. ✨

---

## 🌟 Fitur Utama Bot

Bot ini dirancang dengan struktur modular yang menghubungkan Discord frontend langsung dengan database **SQLite3**. Berikut fitur-fitur keren yang ada di dalamnya:

* 📁 **Manajemen Proyek:** Menambahkan (`!new_project`), melihat (`!projects`), memperbarui (`!update_projects`), dan menghapus (`!delete`) portofolio proyek kamu.
* 🛠️ **Sistem Keterampilan (Skills):** Menghubungkan berbagai keahlian teknologi (seperti *Python, SQL, API, Discord*) langsung ke proyek yang sedang dikerjakan.
* 🔄 **Pelacak Status Otomatis:** Memantau progres proyek dari tahap *Pembuatan Prototipe*, *Dalam Pengembangan*, hingga *Selesai, siap digunakan*.
* 📝 **Pencarian Instan:** Cukup ketik nama proyekmu di chat (tanpa prefix `!`), dan bot akan otomatis mencarikan detail informasinya!
* ⚡ **Formulir Interaktif (Modal):** Fitur UI modern menggunakan tombol dan pop-up formulir (`!test`) untuk input data teks pendek maupun panjang secara langsung di Discord.

---

## 🛠️ Struktur Kode Proyek

Proyek ini dibangun secara rapi dengan membagi logika menjadi beberapa file agar mudah dikembangkan:
📂 **`main.py`** — Inisialisasi awal database dan pengisian data bawaan (*default setup*).
📂 **`logic.py`** — Pengatur query database SQLite3 (CRUD proyek & keterampilan).
📂 **`bot.py`** — Logika utama bot Discord, manajemen command, dan event handling.
📂 **`modal.py`** — Implementasi komponen UI Discord seperti *Buttons* dan *Modal Windows*.
📂 **`config.py`** — Tempat menyimpan kredensial aman seperti token bot dan nama database.

---

## 🎨 Cuplikan Antarmuka (Screenshots)

Berikut adalah tampilan bagaimana bot ini bekerja di dalam server Discord:

### 📥 1. Mengisi Formulir Menggunakan UI Modal (`!test`)
![Formulir Modal](https://githubusercontent.com) *(Catatan: Ganti dengan screenshot modal milikmu)*

### 📊 2. Menampilkan Daftar Proyek (`!projects`)
![Daftar Proyek](https://githubusercontent.com) *(Catatan: Ganti dengan screenshot proyek milikmu)*

---

## 🚀 Cara Menjalankan Proyek

1. **Clone Repositori Ini**
   ```bash
   git clone https://github.com
   cd nama-repo-kamu
   ```

2. **Instal Library yang Dibutuhkan**
   ```bash
   pip install discord.py
   ```

3. **Inisialisasi Database**
   Jalankan file utama untuk membuat tabel database pertama kali:
   ```bash
   python main.py
   ```

4. **Konfigurasi Token**
   Buka `config.py` dan masukkan token bot Discord milikmu.

5. **Nyalakan Bot!**
   ```bash
   python bot.py
   ```

---

## ⚙️ Teknologi yang Digunakan

* 🐍 [Python 3.x](https://python.org) — Bahasa pemrograman utama.
* 🤖 [Discord.py](https://readthedocs.io) — Library API untuk interaksi bot Discord.
* 🗄️ [SQLite3](https://sqlite.org) — Database relasional lokal untuk menyimpan data proyek.

---

> 🎉 **Ekspresikan Dirimu:** *"Kode yang baik bukan cuma jalan tanpa error, tapi juga terdokumentasi dengan indah!"*
