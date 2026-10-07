# DV3. Ghép mode ζ và dịch chuyển tán sắc

Mức: L3 + L4. Script: `code/scripts/check_zeta_coupling.py`. Liên quan: [OQ-1](../open-questions.md).

## 1. Lập luận cấu trúc

Biến đổi $(\varphi_1,\ldots,\varphi_4)\to(\theta,\varphi,\zeta,\Sigma)$ là tuyến tính, **cố định** (chọn theo mạch đối xứng danh định). Mối nối A nối hai nút cố định ⇒ $\varphi_A$ là một tổ hợp cố định của các $\varphi_k$ ⇒ trong tọa độ mới $\varphi_A=\theta+\varphi$ (và $\varphi_B=\theta-\varphi$) **không chứa ζ**, độc lập với mọi giá trị tham số.

Vậy rối loạn chỉ có thể sinh ghép ζ qua:
- **động năng**: ma trận $\mathbf C^{-1}$ không còn chéo khối khi $dC\neq0$ ⇒ $\propto dC\,\hat n_\theta\hat n_\zeta$;
- **thế điện cảm**: $\frac{E_{L1}}{2}(\ldots)^2+\frac{E_{L2}}{2}(\ldots)^2$ với $E_{L1}\neq E_{L2}$ ⇒ $\propto dE_L\,\varphi\zeta$.

$dE_J$ (và $d_M$ mọi bậc) chỉ nằm trong khối $(\theta,\varphi)$. Đây chính là Hamiltonian của Groszkowski 2018 / `scqubits.FullZeroPi`:
$$H_{int}=2E_{C\Sigma}\,dC\,\partial_\theta\partial_\zeta+E_L\,dE_L\,\varphi\,\zeta .$$

## 2. Dịch chuyển tán sắc bậc hai

$H_{int}=\sum_{ll'}g_{ll'}\ket l\bra{l'}(a+a^\dagger)$. Năng lượng bậc hai của $\ket{l,n}$:
$$E^{(2)}_{l,n}=\sum_{l'\ne l}|g_{ll'}|^2\Big[\frac{n}{\Delta_{ll'}+\omega_\zeta}+\frac{n+1}{\Delta_{ll'}-\omega_\zeta}\Big],\quad\Delta_{ll'}=E_l-E_{l'}$$
⇒ hệ số của $n$: $\chi_l=\sum_{l'}|g_{ll'}|^2\frac{2\Delta_{ll'}}{\Delta_{ll'}^2-\omega_\zeta^2}$, và $\chi_{q\zeta}=\chi_1-\chi_0$ (quy ước "toàn bộ dịch chuyển mỗi photon"; trong công thức Clerk–Utami dùng $\chi_{CU}=\chi_{q\zeta}/2$).

$dE_J$ vào $\chi$ chỉ gián tiếp qua $\{\Delta_{ll'},g_{ll'}\}$ (vectơ riêng của khối $(\theta,\varphi)$), nên ở bậc thấp nhất $\chi_{q\zeta}\propto dE_L^2,\,dC^2,\,dE_L\,dC$ và phụ thuộc yếu vào $dE_J$.

## 3. Kiểm chứng số (tham số minh họa, GHz)

$E_J=10$, $E_L=0{,}04$, $E_{CJ}=20$, $E_C=0{,}04$; $\omega_{01}/2\pi\approx36$ MHz, $\omega_\zeta/2\pi\approx113$ MHz.

| $dE_J$ | $dE_L=dC$ | $\chi_{q\zeta}$ (kHz) |
|---|---|---|
| 0,00 | 0,05 | −15,74 |
| 0,10 | 0,05 | −15,84 |
| 0,10 | 0,02 | −2,53 |
| 0,10 | 0,01 | −0,63 |
| 0,10 | 0,00 | 0,000 |
| 0,00 | $dE_L$=0,05, $dC$=0 | −15,74 |
| 0,00 | $dE_L$=0, $dC$=0,05 | −0,008 |

Đọc bảng: $\chi_{q\zeta}$ thay đổi 0,6% khi $dE_J$ đi 0 → 0,1; tỉ lệ $dE_L^2$ (0,01→0,02: ×4); ở tham số này $dE_L$ chi phối, $dC$ không đáng kể.

## 4. Hệ quả cho đề cương và việc tiếp theo

1. Với mô hình Groszkowski, **cân bằng $E_J$ bằng cổng không làm giảm mất pha do ζ**. Lập luận "$\chi_{q\zeta}\propto dE_J^2$ ⇒ $T_{2R}$: 24 µs → 1,08 ms" cần được đối chiếu lại với mô hình trong [20].
2. Cần kiểm ở tham số soft 0-π của Gyenis 2021 (thay `BASE` trong script) và với chéo hoá đầy đủ $H_{0\text{-}\pi}\otimes H_\zeta$ (không nhiễu loạn).
3. Câu hỏi mới có giá trị: có thể dùng $dE_J$ (điều khiển được) để **bù** $\chi_{q\zeta}$ do $dE_L$ không? Từ §2, $\chi_{q\zeta}(dE_J)$ có đạo hàm khác 0 nhưng rất nhỏ ở tham số này ⇒ bù khó. Ngược lại, nếu thay siêu điện cảm bằng phần tử điều chỉnh được (chuỗi gatemon/SQUID) thì $dE_L$ trở thành tham số điều khiển — một hướng thiết kế đáng xét cho ND2.
4. Phân biệt rõ: các lợi ích **khác** của gatemon (điều hòa $\cos2\varphi$, điều chỉnh $\bar E_J$, $d_M$ ảnh hưởng $T_1$ và độ cong) vẫn đứng vững độc lập với kết luận này.
