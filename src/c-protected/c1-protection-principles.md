# C1. Nguyên lý bảo vệ

## 1. Hai điều kiện (Douçot–Ioffe; Gyenis et al. 2021 PRX Quantum)

Cho qubit $\{\ket0,\ket1\}$, môi trường ghép qua tập toán tử cục bộ $\{\hat O_k\}$ (ví dụ $\hat n$, $\hat\varphi$, $\partial H/\partial\Phi_{ext}$, $\partial H/\partial V_g$):

- **(R) chống hồi phục:** $|\bra1\hat O_k\ket0|\to0$ — thường qua tách miền định xứ: $\mathrm{supp}\,\psi_0\cap\mathrm{supp}\,\psi_1\approx\varnothing$ trong biến mà $\hat O_k$ cục bộ.
- **(D) chống mất pha:** $|\bra1\hat O_k\ket1-\bra0\hat O_k\ket0|\to0$ — tần số phẳng theo tham số nhiễu.

Một bậc tự do khó thỏa cả hai cho cả $\hat n$ và $\hat\varphi$ đồng thời (bất đẳng thức kiểu bất định: định xứ trong $\varphi$ ⇒ trải rộng trong $n$). Lối ra: **hai bậc tự do + đối xứng rời rạc**.

## 2. Phân loại theo đối xứng

| Đối xứng | Toán tử | Bảo vệ gì | Ví dụ |
|---|---|---|---|
| Phản xạ pha | $\varphi\to-\varphi$ (tại $\varphi_{ext}=0$ hoặc $\pi$) | $\partial\omega/\partial\Phi_{ext}=0$ | flux sweet spot |
| Tịnh tiến pha (Bloch) | $\theta\to\theta+2\pi$, pha $e^{2\pi i n_g}$ | AC → độ tán sắc triệt | transmon, 0-π |
| Chẵn lẻ số cặp | $e^{i\pi\hat n}$ | cấm chuyển dời chẵn↔lẻ | cos2φ, KITE |
| Chẵn lẻ fluxon | — | | bifluxon |
| Hoán vị nhánh | $A\leftrightarrow B$ | khử ghép mode thừa (ζ) | 0-π |

**Điểm mấu chốt cho luận án:** mỗi đối xứng có một tập tham số phá vỡ riêng. Cần lập bảng "tham số phá vỡ → đối xứng bị phá → kênh nhiễu mở ra → điều chỉnh được bằng cổng?" — đây là xương sống của ND2.

## 3. Bảo vệ cứng và mềm

- **Cứng**: tỉ số năng lượng cực đoan, mọi đại lượng (R), (D) bị triệt **hàm mũ** theo một tham số lớn (ví dụ $\sqrt{E_J/E_{C\theta}}$).
- **Mềm**: tỉ số khả thi, chỉ một số kênh bị triệt mạnh; kênh còn lại triệt đại số hoặc không. Soft 0-π (Gyenis 2021) thuộc nhóm này.

## 4. Định lý "không có bữa trưa miễn phí"

- **Điều khiển**: (R) cũng triệt phần tử ma trận của xung điều khiển. Cổng phải dùng: Raman qua mức trung gian, điều biến tham số, hoặc tạm thời hạ bảo vệ (ND3).
- **Đọc**: χ của qubit với bộ cộng hưởng cũng nhỏ → đọc chậm; hoặc dùng đọc qua mức phụ.
- **Rối loạn**: đối xứng chỉ gần đúng ⇒ bảo vệ bị giới hạn bởi $\epsilon_{disorder}$; độ bền theo $\epsilon$ là tiêu chí so sánh chính (Dempster 2014).

## 5. Tự kiểm tra

1. Với fluxonium tại $\Phi_{ext}=\Phi_0/2$: chứng minh (R) cho $\hat n$ nhưng không cho $\hat\varphi$ (phần tử ma trận pha lớn) — vì sao fluxonium vẫn có $T_1$ dài? (gợi ý: tần số thấp + phụ thuộc tần số của $S(\omega)$).
2. Viết bảng §2 cho 0-π lai, thêm cột "điều chỉnh bằng $V_g$?".

## 6. Đọc

1. Gyenis, Di Paolo, Koch, Blais, Houck, Schuster 2021 PRX Quantum 2, 030101 "Moving beyond the transmon". ★ L3
2. Douçot & Ioffe 2012 Rep. Prog. Phys. 75, 072001. ★ L2
3. Kitaev 2006 (arXiv:cond-mat/0609441); Brooks, Kitaev, Preskill 2013 PRA 87, 052306. L2
