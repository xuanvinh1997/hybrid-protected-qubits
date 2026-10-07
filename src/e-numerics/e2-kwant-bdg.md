# E2. Mô hình liên kết chặt BdG với Kwant

Mục tiêu ND1: $E_{GS}(\varphi;V_g)$ và $\{E_{J,M}(V_g)\}$ cho mối nối phẳng InAs/Al, có kiểm soát sai số.

## 1. Thang bậc mô hình (xây từ dưới lên, mỗi bậc có test hồi quy)

| Bậc | Hệ | Kiểm chứng với |
|---|---|---|
| T0 | 1D S–N–S, `hpq.tightbinding` (numpy) | Beenakker, sai số $\propto L/\xi$ ✓ (đã có test) |
| T1 | 1D Kwant, cùng mô hình | T0 đến sai số máy |
| T2 | 2D dải rộng $W$, không SOC, sạch | $N$ kênh, mỗi kênh $\tau\approx1$ ⇒ $r\to-0{,}2$ |
| T3 | T2 + rối loạn Anderson | thống kê $\tau$ → Dorokhov khi $L\gg\ell_e$; $r_{eff}\to-0{,}1$ |
| T4 | T3 + Rashba + Zeeman | $\varphi_0$ khi $B\perp$ trường SOC (Yokoyama 2014), $\varphi_0=0$ khi $B=0$ |
| T5 | + lớp Al tường minh (2 lớp) | khe cảm ứng, metallization |

## 2. Rời rạc hoá

Mạng vuông hằng số $a$: $t=\hbar^2/2m^*a^2$. Với $m^*=0{,}023m_e$, $a=5$ nm: $t\approx66$ meV. Điều kiện: $\lambda_F=2\pi/k_F\approx25$ nm ≫ $a$ ✓; $\mu$ đo từ đáy vùng ≪ $4t$ để giữ tán sắc parabol.

Rashba: $\alpha_R(\sigma_xk_y-\sigma_yk_x)\to$ hopping $\pm i\frac{\alpha_R}{2a}\sigma$. Lấy $\alpha_R\sim5$–$20$ meV·nm cho InAs nông (kiểm tài liệu).

Khe: $\Delta e^{\pm i\varphi/2}$ trong vùng S; $\xi_0=\hbar v_F/\Delta$ phải ≪ độ dài vùng S mô phỏng (vùng S hữu hạn) hoặc dùng lead bán vô hạn.

## 3. Tính $E_{GS}(\varphi)$

Ba cách:
1. **Chéo hoá hệ đóng** (S hữu hạn): $E_{GS}=-\frac12\sum_{E>0}E$ — cần toàn phổ, $O(N^3)$; được với $N\lesssim10^4$.
2. **Hàm Green Matsubara với lead S bán vô hạn**: $F(\varphi)=-k_BT\sum_{\omega_n}\ln\det[\,i\omega_n-H_{scatt}-\Sigma_{leads}(i\omega_n,\varphi)]$ — chỉ cần vùng tán xạ; tổng $\omega_n$ hội tụ nhanh ở $T$ hữu hạn. Kwant cung cấp `selfenergy` của lead. Đây là phương pháp chuẩn cho mối nối dài (Furusaki–Tsukada / Brouwer–Beenakker).
3. **Từ ma trận tán xạ trạng thái thường** $s_N(E)$ (Kwant `smatrix`) + định thức Beenakker phụ thuộc năng lượng.

Kiểm chéo 1 ↔ 2 ↔ 3 ở T2.

## 4. Từ $E_{GS}$ đến mạch

FFT theo $\varphi$ trên lưới đều 64–256 điểm ⇒ $E_{J,M}$. Lưu bảng $E_{J,M}(V_g)$ dạng HDF5 kèm metadata (tham số, phiên bản mã, hash commit) — đầu vào trực tiếp cho `HybridZeroPi(EJA=..., EJB=...)`.

## 5. Bẫy

- Đếm spin: với BdG 4×4 (có SOC), dùng $-\frac12\sum_{E>0}$; với 2×2 không spin, $-\sum_{E>0}$.
- Lead S trong Kwant cần đối xứng hạt–lỗ được khai báo (`conservation_law`, `particle_hole`) để tránh lỗi trộn mode.
- Pha $\varphi$ đặt ở lead (gauge trong $\Delta$) vs vector potential trong hopping: hai cách tương đương nếu vùng S đủ dài.

## 6. Đọc

1. Groth, Wimmer, Akhmerov, Waintal 2014 New J. Phys. 16, 063065 (Kwant) + tutorial "Superconductors" trong tài liệu Kwant. ★ L4
2. Pientka et al. 2017 PRX 7, 021032 (mô hình mối nối phẳng). ★ L3
3. Furusaki & Tsukada 1991 PRB 43, 10164 (dòng Josephson từ biên độ phản xạ Andreev). L2
4. Brouwer & Beenakker 1997 Chaos, Solitons & Fractals 8, 1249 "Anomalous temperature dependence of the supercurrent through a chaotic Josephson junction" (công thức định thức theo $\omega_n$). L2
