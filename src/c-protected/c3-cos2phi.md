# C3. Phần tử cos2φ

## 1. Phát biểu

$H=4E_C(\hat n-n_g)^2-E_2\cos2\hat\varphi$ giao hoán với $\hat P=e^{i\pi\hat n}$ ⇒ không gian tách thành lớp $n$ chẵn / lẻ. Hai trạng thái thấp nhất: một trong mỗi lớp, định xứ (trong biểu diễn pha) quanh $\varphi=0$ và $\varphi=\pi$ (đúng hơn: tổ hợp chẵn/lẻ của hai giếng). Chuyển dời giữa chúng cần toán tử lẻ (ví dụ $e^{i\hat\varphi}$, tức một cặp Cooper đơn) — bị cấm nếu không có $E_{J,1}$.

Tách mức $\propto$ biên độ phase slip $\pi$ (không phải $2\pi$) ⇒ $\propto e^{-\sqrt{2E_2/E_C}\cdot c}$; tìm $c$ là bài tập.

## 2. Cách hiện thực

| Cách | Cơ chế | Số hạng dư phá chẵn lẻ | Tài liệu |
|---|---|---|---|
| Chuỗi hình thoi JJ ở $\Phi_0/2$ | giao thoa trong mỗi hình thoi | lệch $\Phi$, rối loạn $E_J$ | Gladchenko 2009; Bell 2014 |
| KITE | hai nhánh có điện cảm, $\Phi_0/2$ | rối loạn nhánh | Smith 2020; Smith 2022 |
| SQUID mối nối bán dẫn ở $\Phi_0/2$ | $E_{J,1}$ triệt bằng giao thoa, $E_{J,2}$ cộng | $\delta E_{J,1}$, có thể bù bằng cổng | Larsen 2020; Ciaccia 2024 |
| Mảng giao thoa kế gatemon | nhiều SQUID nối tiếp | | Schrade, Marcus, Gyenis 2022 |
| SQUID graphene / Ge phẳng | như trên, vật liệu khác | | Messelot 2024; Leblanc 2025 |

## 3. SQUID mối nối phi sin

Hai mối nối $U_j(\varphi)=-\sum_ME^{(j)}_{J,M}\cos M\varphi$, vòng có $\Phi$, điện cảm vòng bỏ qua:
$$U(\varphi)=-\sum_M\Big[E^{(1)}_{J,M}\cos M\varphi+E^{(2)}_{J,M}\cos M(\varphi-2\pi\Phi/\Phi_0)\Big].$$
Tại $\Phi=\Phi_0/2$: số hạng $M$ lẻ trừ nhau ⇒ dư $(E^{(1)}_{J,M}-E^{(2)}_{J,M})\cos M\varphi$; $M$ chẵn cộng nhau.

**Điều kiện cân bằng đầy đủ** cần $\delta E_{J,M}=0$ cho **mọi M lẻ** — với hai cổng chỉ có thể ép $\delta E_{J,1}=0$; $\delta E_{J,3}$ dư phụ thuộc phân bố kênh (cùng bản chất với OQ-2).

**Điện cảm vòng hữu hạn** $L_{loop}$: thêm bậc tự do, hiệu chỉnh $\propto\beta_L=2\pi L I_c/\Phi_0$. Phải kiểm khi điều hòa bậc hai yếu ($|E_{J,2}|\sim0{,}1E_{J,1}$) vì $L_{loop}$ có thể sinh điều hòa hiệu dụng cùng bậc.

## 4. Câu hỏi luận án

- Bảo vệ bị giới hạn bởi $\delta E_{J,1}$ dư + nhiễu cổng vi sai $\delta V_g^{(1)}-\delta V_g^{(2)}$. Tốc độ hồi phục $\Gamma_1\propto|\delta E_{J,1}|^2|\bra1\cos\hat\varphi\ket0|^2S(\omega_{01})$ — viết đầy đủ và ước lượng.
- $E_2=2|E_{J,2}|$ nhỏ (≈ 0,25$E_{J,1}$ ở $\tau=0{,}9$) ⇒ cần $E_{J,1}$ lớn ⇒ mối nối rộng, nhiều kênh ⇒ phân bố $\tau$ quyết định $r_{eff}$.

## 5. Đọc

1. Smith, Kou, Xiao, Vool, Devoret 2020 npj QI 6, 8. ★ L3
2. Larsen et al. 2020 PRL 125, 056801. ★ L3
3. Ciaccia et al. 2024 Commun. Phys. 7, 41. ★ L2
4. Schrade, Marcus, Gyenis 2022 PRX Quantum 3, 030303. ★ L3
5. Messelot et al. 2024 PRL 133, 106001 (arXiv:2405.13642). L2
6. Leblanc et al. 2025 Nat. Commun. 16 (arXiv:2405.14695) — Ge phẳng, điều chỉnh cổng + từ thông. ★ L2
7. Willsch et al. 2024 Nat. Phys. (arXiv:2302.09192) — ngay cả mối nối đường hầm AlOx cũng có điều hòa bậc cao. ★ L2
