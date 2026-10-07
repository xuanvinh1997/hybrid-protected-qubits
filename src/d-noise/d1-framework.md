# D1. Khung lý thuyết: mật độ phổ, quy tắc vàng, nhiễu 1/f

## 1. Ghép tuyến tính và mật độ phổ

$H=H_q+\hat O\otimes\hat X+H_{bath}$ hoặc nhiễu cổ điển $\lambda(t)$: $H=H_q(\lambda_0)+\delta\lambda(t)\,\partial_\lambda H_q$.
Mật độ phổ $S_\lambda(\omega)=\int dt\,e^{i\omega t}\langle\delta\lambda(t)\delta\lambda(0)\rangle$.

**Hồi phục (quy tắc vàng):**
$$\Gamma_1=\frac1{\hbar^2}\,|\bra1\partial_\lambda H\ket0|^2\,\big[S_\lambda(\omega_{01})+S_\lambda(-\omega_{01})\big].$$
Với bể cân bằng: $S(-\omega)=e^{-\hbar\omega/k_BT}S(\omega)$.

**Mất pha thuần (nhiễu trắng tần thấp):** $\Gamma_\varphi=\frac{1}{2}\left(\partial_\lambda\omega_{01}\right)^2S_\lambda(0)$ (quy ước $S$ hai phía; kiểm thừa số 2 theo tài liệu).

## 2. Nhiễu 1/f

$S_\lambda(\omega)=2\pi A_\lambda^2/|\omega|$ trên $[\omega_{ir},\omega_{uv}]$. Phân rã Ramsey không hàm mũ:
- **Bậc nhất** (xa sweet spot): $\langle e^{i\phi(t)}\rangle\approx\exp[-t^2(\partial_\lambda\omega)^2A_\lambda^2\ln(1/\omega_{ir}t)]$ — Gauss.
- **Bậc hai** (tại sweet spot, $\partial_\lambda\omega=0$): $\delta\omega=\tfrac12\partial^2_\lambda\omega\,\delta\lambda^2$ ⇒ phân rã có đuôi đại số. Dạng ước lượng thông dụng (lấy hệ số chính xác từ Groszkowski 2018 §4 khi đọc L3 — đừng dùng công thức dưới đây để báo số):
$$\Gamma_\varphi^{(2)}\approx\big|\partial^2_\lambda\omega_{01}\big|\,A_\lambda^2\big[\ln^2(\omega_{uv}/\omega_{ir})+2\ln^2(\omega_{ir}t)\big]^{1/2}.$$

Điểm cần ghi nhớ: tại sweet spot, **độ cong** $\partial^2\omega$ mới là đại lượng thiết kế. Kết quả sơ bộ "độ cong giảm 13%" của đề cương thuộc loại này.

## 3. Định nghĩa thời gian

$T_2^{-1}=(2T_1)^{-1}+\Gamma_\varphi$ chỉ đúng cho phân rã hàm mũ. Với 1/f phải báo cáo **dạng** phân rã (hàm mũ/Gauss) và cách lấy $T_2$ (thời điểm $1/e$). So sánh $T_{2R}$ giữa các bài cần cùng quy ước.

## 4. Phương trình chủ

| Phương pháp | Giả thiết | Khi nào dùng |
|---|---|---|
| Lindblad | Born–Markov + secular | ước lượng nhanh, cổng chậm so với $1/\Delta\omega$ |
| Bloch–Redfield | Born–Markov, không secular | phổ nhiễu có cấu trúc, mức gần suy biến (tách mức thung lũng π chỉ ~20–30 MHz!) |
| Filter function | nhiễu cổ điển Gauss, mất pha thuần | chuỗi xung, echo, DD |
| Cumulant / TCL bậc cao | ghép trung bình | 1/f mạnh, non-Markov |

Ghi chú 0-π: mức $\ket{\pi'}$ (tách mức thung lũng π) nằm rất gần — secular approximation có thể hỏng; dùng Bloch–Redfield hoặc kiểm bằng mô phỏng không secular.

## 5. Đọc

1. Clerk, Devoret, Girvin, Marquardt, Schoelkopf 2010 RMP 82, 1155 "Introduction to quantum noise..." §II–III. ★ L3
2. Ithier et al. 2005 PRB 72, 134519. ★ L3
3. Schoelkopf, Clerk, Girvin, Lehnert, Devoret 2003 "Qubits as spectrometers of quantum noise" (arXiv:cond-mat/0210247). L2
4. Groszkowski et al. 2018 §4 (công thức cho từng kênh). ★ L4
5. Breuer & Petruccione, *The Theory of Open Quantum Systems*, ch. 3. L2
