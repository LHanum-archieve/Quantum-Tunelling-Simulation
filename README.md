# Quantum Tunneling Simulation (1D TDSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
![Status](https://img.shields.io/badge/Status-Active-success)

Repositori ini berisi simulasi numerik untuk fenomena Quantum Tunneling menggunakan Persamaan Schrödinger bergantung waktu (Time-Dependent Schrödinger Equation - TDSE). Simulasi ini memvisualisasikan paket gelombang Gaussian yang menabrak penghalang potensial persegi.

## Fitur Utama
Metode Numerik: 
- Menggunakan algoritma Split-Step Fourier Method yang efisien dan stabil secara energi (unitary).
- Menghasilkan animasi .gif yang menunjukkan evolusi probabilitas densitas ∣Ψ(x,t)∣
- Pengguna dapat dengan mudah mengubah tinggi penghalang (V_0), lebar penghalang, dan energi paket gelombang.


## Teori Singkat

Simulasi ini menyelesaikan Persamaan Schrödinger Bergantung Waktu (TDSE) untuk partikel non-relativistik dalam satu dimensi:

$$i\hbar \frac{\partial}{\partial t} \Psi(x,t) = \hat{H} \Psi(x,t)$$

Dimana operator Hamiltonian $\hat{H}$ didefinisikan sebagai:

$$\hat{H} = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x)$$

### Metode Split-Step Fourier

Untuk evolusi waktu numerik, kita menggunakan operator propagasi:

$$\Psi(x, t + \Delta t) \approx e^{-\frac{iV\Delta t}{2\hbar}} e^{-\frac{i\hat{T}\Delta t}{\hbar}} e^{-\frac{iV\Delta t}{2\hbar}} \Psi(x, t)$$

Simulasi ini membagi langkah waktu $\Delta t$ menggunakan teknik **Strang Splitting** karena operator energi kinetik ($\hat{T}$) dan energi potensial ($V$) tidak komutatif. Teknik ini sangat penting untuk meminimalkan galat numerik dan menjaga simulasi tetap akurat (orde kedua).
Proses satu langkah waktu ($\Delta t$) dilakukan dalam tiga tahap:

1.  **Langkah Potensial ($\Delta t/2$)**

    Memberikan kick potensial pada fungsi gelombang di ruang posisi. Langkah ini mengubah fase kompleks $\Psi$ berdasarkan nilai $V(x)$ tanpa mengubah posisi partikel.

4.  **Langkah Kinetik ($\Delta t$)**

    Pada tahap ini, partikel digerakkan. Kita menggunakan transformasi karena operator kinetik sulit dihitung di ruang posisi : 
    - FFT : Mengubah $\Psi$ dari ruang posisi ke ruang momentum ($k$-space).
    - Propagasi : Di ruang momentum, operator kinetik menjadi perkalian sederhana dengan fase $e^{-i\frac{\hbar k^2}{2m}\Delta t}$.
    - IFFT : Mengembalikan fungsi gelombang kembali ke ruang posisi.

6.  **Langkah Potensial ($\Delta t/2$)**

    Memberikan kick potensial terakhir untuk melengkapi satu siklus langkah waktu secara simetris.

> **Mengapa menggunakan FFT?**
> Menghitung turunan kedua (energi kinetik) di ruang posisi secara numerik cenderung lambat dan tidak stabil. Dengan Fast Fourier Transform (FFT), operasi turunan berubah menjadi perkalian biasa yang jauh lebih efisien secara komputasi dan menjamin hukum kekekalan probabilitas tetap terjaga.

## Parameter yang Bisa Diubah
Anda dapat bereksperimen dengan nilai berikut di dalam kode:
- `V0`= Tinggi penghalang 
- `k0`= Kecepatan/Momentum paket gelombang
- `a` = Lebar penghalang .

Hint : 
| Skenario | Energi ($E$) | Potensial ($V_0$) | Prediksi Fisika |
| :--- | :--- | :--- | :--- |
| **Tunneling** | $E < V_0$ | Tinggi | Sebagian kecil bocor lewat penghalang. |
| **Transmisi** | $E > V_0$ | Rendah | Partikel lewat dengan perubahan fase. |
| **Refleksi** | $E \ll V_0$ | Sangat Tinggi | Partikel terpantul sempurna. |

dengan energi didefinisikan sebagai:

$$E = \frac{p^2}{2m} = \frac{(\hbar k_0)^2}{2m}$$

## Cara Penggunaan
1. Salin skrip
   ```bash
   ....py.
   ```
2. Install depedensi
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan skrip
   ```bash
   python quantum_tunneling.py
   ```
5. Program akan melakukan kalkulasi langkah waktu dan menampilkan progres pembuatan frame.
6. Setelah selesai, sebuah file bernama quantum_tunneling_animation.gif akan muncul pada direktori.


