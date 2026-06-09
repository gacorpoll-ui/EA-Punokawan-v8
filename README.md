# 🛡️ EA Punokawan V.8_MA 🛡️
### *The Ultimate Recovery & Smart Averaging Solution for MT5*

![Trading Performance](https://img.shields.io/badge/Status-Stable-brightgreen) ![Platform](https://img.shields.io/badge/Platform-MetaTrader%205-blue) ![Strategy](https://img.shields.io/badge/Strategy-Averaging%20%7C%20Scalping-orange)

**EA Punokawan V.8_MA** bukan sekadar robot trading biasa. Ini adalah mahakarya algoritma yang dirancang khusus untuk menghadapi volatilitas pasar yang ekstrem dengan sistem **Dynamic Recovery Cycle**. Dibangun untuk trader yang menginginkan keamanan aset sekaligus pertumbuhan profit yang konsisten.

---Send STAR ME On trial EA PunoKawan---

## 🌟 Mengapa Memilih Punokawan V.8_MA?

### 🔄 **1. Intelligence Recovery System**
Berbeda dengan EA averaging standar yang hanya menambah posisi, Punokawan menghitung setiap sen kerugian berjalan (`Rugi`) dan memproyeksikan titik **Break Even Point (BEP)** secara presisi. EA ini tidak akan berhenti sebelum siklus perdagangan Anda ditutup dalam kondisi profit!

### 🎯 **2. Precision Entry dengan MA Filter**
Tidak ada lagi entry "buta". EA ini menggunakan kombinasi filter **Moving Average** dan **Candlestick Pattern Analysis** untuk memastikan setiap posisi dibuka pada momentum yang tepat, mengurangi risiko *drawdown* berkepanjangan.

### 🔘 **3. Hybrid Trading Mode**
*   **Fully Automatic:** Biarkan algoritma bekerja 24/5 untuk Anda.
*   **Semi-Manual (Execution Button):** Anda pegang kendali! Gunakan tombol interaktif di chart untuk memulai siklus trading berdasarkan analisa personal Anda, dan biarkan EA yang menyelesaikan manajemen averaging-nya.

### 🛡️ **4. Advanced Risk Management**
*   **Emergency Close on BEP:** Fitur penyelamat yang akan menutup semua posisi saat akun mencapai titik impas setelah floating minus tertentu.
*   **Hidden SL/TP:** Menghindari *stop loss hunting* oleh broker dengan target harga yang tersembunyi dari server.

---

## 📊 Fitur Eksklusif Versi V.8_MA

| Fitur | Manfaat |
| :--- | :--- |
| **Static BEP Logic** | Garis target stabil, mencegah modifikasi order berlebihan (anti-ban broker). |
| **Anti Double-Entry** | Proteksi tingkat tinggi agar tidak terjadi duplikasi posisi saat volatilitas tinggi. |
| **Real-Time Dashboard** | Monitor Profit, Margin, dan status Recovery langsung di layar chart Anda. |
| **License Lock** | Keamanan penuh bagi pemilik EA untuk mengontrol masa aktif penyewa. |

---

## ⚙️ Parameter Utama (Mudah Digunakan)

*   💰 **Start Lot:** Mulai dari 0.01 untuk keamanan maksimal.
*   📈 **Multiplier:** Kendali penuh atas agresivitas averaging Anda.
*   🏁 **Target Profit:** Bisa ditentukan dalam Pips, Dollar ($), atau BEP+.
*   📉 **Max Loss Recovery:** Batas toleransi untuk mengaktifkan mode penyelamatan.

---

## 📈 Tips Sukses Penggunaan
1.  **Gunakan VPS:** Pastikan EA berjalan 24 jam tanpa gangguan koneksi.
2.  **Pilih Pair Mayor:** Sangat direkomendasikan untuk XAUUSD atau pair dengan spread rendah.
3.  **Mulai Small:** Gunakan lot kecil terlebih dahulu untuk memahami karakter recovery EA ini.

---

## ⚙️ Penjelasan Parameter (Settings) Secara Rinci

### 1. Common Settings (Pengaturan Umum)
*   **EA_NAME**: Nama EA yang akan muncul di komentar setiap transaksi.
*   **ExpertID (Magic Number)**: ID unik EA. Pastikan ID ini berbeda jika menjalankan EA yang sama pada pair berbeda di satu akun.

### 2. Trade Execution Mode
*   **StartingTradesMST**: 
    *   `Automatic`: EA membuka posisi pertama sendiri berdasarkan sinyal.
    *   `Manual / Button`: EA hanya akan mulai bekerja setelah Anda menekan tombol di chart.
*   **StartingTradesMSTBUT**: Metode eksekusi tombol.
    *   `Direct Order`: Langsung buka posisi saat tombol ditekan.
    *   `Close Candle`: Menunggu candle saat ini selesai baru membuka posisi.

### 3. Lot Management
*   **Lot**: Ukuran lot awal (posisi pertama).
*   **StartingTradesM**: 
    *   `Lot Adder`: Lot posisi selanjutnya ditambah (Lot 1 + Multiplier).
    *   `Multiplier Lot`: Lot posisi selanjutnya dikali (Lot 1 * Multiplier).
*   **Multiplier**: Nilai penambahan atau pengali untuk level averaging selanjutnya.

### 4. Takeprofit & Recovery (TP Mode)
*   **StartingTradesTP**: Metode penentuan target profit.
    *   `Pips`: Target profit murni berdasarkan jarak pips dari harga entry.
    *   `BEP + Pips`: Target profit dihitung dari titik impas (harga rata-rata) ditambah pips.
    *   `BEP + $`: Target profit dihitung dari titik impas ditambah nilai dollar.
*   **TP_Averaging**: Nilai target profit (sesuai metode yang dipilih di atas).

### 5. Hidden Protection (Proteksi Tersembunyi)
*Fitur ini digunakan agar TP/SL tidak terlihat oleh server broker.*
*   **HTPP / HTP / HTPD**: Hidden Takeprofit dalam bentuk Pips, BEP+Pips, atau BEP+$.
*   **HStoploss**: Stoploss tersembunyi dalam pips.
*   **HAutoSL**: Jika `true`, EA akan menggunakan Low/High candle sebelumnya sebagai Stoploss otomatis.

### 6. Safety & Grid Logic
*   **Max Range Open From Candle**: Jarak maksimal harga saat ini dari harga Open Candle untuk mengizinkan entry (mencegah entry saat harga sudah "lari").
*   **Min Range Next Order**: Jarak minimal (pips) antara posisi satu dengan posisi averaging selanjutnya.
*   **Min Range Next Order Start**: Level order keberapa grid minimal mulai diterapkan.

### 7. Close On Opposite Signal
*   **CloseOnOppositeSignal**: Jika `true`, EA akan menutup semua posisi jika muncul sinyal yang berlawanan arah.
*   **StartingTradesMCOS**:
    *   `All`: Tutup semua posisi (profit/loss).
    *   `Loss Only`: Hanya tutup jika posisi dalam keadaan rugi.

### 8. Emergency Exit (Close On BEP)
*   **CloseOnBEPb**: Mengaktifkan fitur "Exit Darurat".
*   **CloseOnBEP**: Batas floating minus (dalam Dollar). Jika floating minus mencapai angka ini, EA akan masuk mode siaga dan akan menutup semua posisi segera setelah grafik profit kembali menyentuh titik impas (0 atau $0.10).

### 9. Trailing Stop Settings
*   **Trailing Stop ON**: Mengaktifkan trailing stop standar.
*   **Trailing Lock Profit BEP**: Mengunci profit pada harga BEP jika harga sudah melaju jauh sesuai arah posisi.

---

## 📊 Tips Optimasi
1.  **Untuk Modal Kecil ($100-$500)**: Gunakan `StartingTradesM = Multiplier` dengan nilai `Multiplier = 1.5` atau `2.0` dan `Lot = 0.01`.
2.  **Untuk Mengunakan Modal Cent Minimal 1000cent 
3.  **Untuk Recovery Cepat**: Gunakan `StartingTradesTP = BEP + $` dengan nilai `TP_Averaging = 1` hingga `5`.
4.  **Keamanan Tinggi**: Aktifkan `MAFilter_ON` agar EA tidak melawan arus tren besar (Trend Follower).

---



## 📞 Hubungi Pengembang
Ingin mendapatkan Full Version atau akses lisensi? Hubungi kami sekarang:

*   👤 **Developer:** Afri_Kenyik
*   📧 **Support:** zeneos6@gmail.com
*   📱 **WhatsApp:** [+6285157110863](https://wa.me/6285157110863)
*   🌐 **Website:** [markaz-arshy.com](https://markaz-arshy.com)

---
> **Peringatan Risiko:** Trading Forex memiliki risiko yang signifikan. Pastikan Anda memahami strategi averaging sebelum menggunakan EA ini di akun riil. Hasil masa lalu tidak menjamin keuntungan di masa depan.
