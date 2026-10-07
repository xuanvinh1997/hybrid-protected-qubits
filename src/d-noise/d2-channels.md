# D2. Danh mục kênh nhiễu cho qubit lai

Mỗi kênh: toán tử ghép, mật độ phổ, tham số thực nghiệm cần lấy, công thức. Cột cuối: có trong mô hình sơ bộ [20] không.

| # | Kênh | Toán tử | $S(\omega)$ / tham số | Có trong [20]? |
|---|---|---|---|---|
| 1 | Tổn hao điện môi (tụ) | $\hat n_\theta$, $\hat n_\varphi$ | $\propto\tan\delta_C\,\coth(\hbar\omega/2k_BT)$ | ✓ |
| 2 | Tổn hao điện cảm | $\hat\varphi$ | $\propto1/Q_L(\omega)$ | ? |
| 3 | 1/f từ thông | $\partial H/\partial\Phi_{ext}$ | $A_\Phi\sim1$–$5\,\mu\Phi_0$ | ✓ |
| 4 | 1/f điện tích | $\partial H/\partial n_g$ | $A_{n_g}\sim10^{-4}e$ | ✓ |
| 5 | Nhiễu bắn photon (ζ, bộ cộng hưởng) | $\hat a^\dagger\hat a$ qua $\chi$ | $\bar n$, $\kappa$ | ✓ |
| 6 | **1/f điện áp cổng** | $\partial H/\partial V_g$ | $A_{V_g}$ từ thực nghiệm gatemon | ✗ |
| 7 | **QP trong ABS** (ngộ độc chẵn lẻ) | nhảy telegraph $E_J\to E_J-\Delta\sqrt{1-\tau_k\sin^2}$ | tốc độ bẫy/thoát $\Gamma_{trap},\Gamma_{esc}$ | ✗ |
| 8 | **Tổn hao điện môi đế III-V** | như #1 với tỉ phần năng lượng trong đế | $\tan\delta_{III-V}\sim10^{-4}$–$10^{-3}$, tỉ phần EPR | ✗ |
| 9 | Trạng thái dưới khe | tiêu tán vào continuum mềm | DOS dưới khe | ✗ |
| 10 | QP ở đảo/điện cực (Catelani) | $\sin(\hat\varphi/2)$ qua mối nối | $x_{qp}$ | ? |
| 11 | Đường cổng như cổng tiêu tán (Johnson) | $\hat n$ qua $C_g$ | $R_{line}$, $C_g$ | ✗ |

## Kênh 5 — nhiễu bắn photon: công thức đầy đủ

Clerk & Utami 2007 (PRA 75, 042302), cho mode với tốc độ tắt $\kappa$, số photon nhiệt $\bar n$, dịch chuyển tán sắc $\chi$ (quy ước: tần số qubit dịch $2\chi$ mỗi photon):
$$
\Gamma_\varphi=\frac{\kappa}{2}\,\mathrm{Re}\!\left[\sqrt{\Big(1+\frac{2i\chi}{\kappa}\Big)^2+\frac{8i\chi\bar n}{\kappa}}-1\right].
$$
Giới hạn:
- $\chi\ll\kappa$: $\Gamma_\varphi\approx\frac{4\chi^2}{\kappa}\bar n(\bar n+1)$.
- $\chi\gg\kappa$, $\bar n\ll1$: $\Gamma_\varphi\approx\kappa\bar n$ (bão hoà — mỗi photon nhiệt đến là một sự kiện đo).

Công thức $\frac{\chi^2\bar n\kappa}{\chi^2+\kappa^2}$ trong đề cương là xấp xỉ $\bar n\ll1$ với một quy ước $\chi$ riêng. **Với ζ ở vài trăm MHz và $T_{eff}\approx20$–$50$ mK, $\bar n_\zeta$ có thể ~ 1** — phải dùng công thức đầy đủ. Cài đặt: `hpq.dephasing.photon_shot_dephasing`.

## Kênh 6 — nhiễu cổng (khung ước lượng)

$\partial\omega_{01}/\partial V_g=\sum_{j=A,B}(\partial\omega_{01}/\partial E^{(j)}_J)(\partial E^{(j)}_J/\partial V_g^{(j)})$.
- Nhiễu **chung** ($\delta V^A=\delta V^B$): thay đổi $\bar E_J$ ⇒ dịch $\omega_{01}$ ở bậc nhất (0-π mềm có $\omega_{01}$ nhạy $E_J$).
- Nhiễu **vi sai**: thay đổi $dE_J$ ⇒ tại $dE_J=0$, $\partial\omega/\partial(dE_J)=0$ do đối xứng ⇒ chỉ bậc hai.

Việc cần làm: lấy $\partial E_J/\partial V_g$ và $A_{V_g}$ từ dữ liệu gatemon 2DEG (Casparis 2018) và dây nano (Luthi 2018 PRL 120, 100502), ước lượng $\Gamma_\varphi^{gate}$. Đây là con số mà hội đồng sẽ hỏi.

## Kênh 7 — QP bị bẫy trong ABS

Khi một QP chiếm mức Andreev kênh $k$, đóng góp kênh đó vào $U(\varphi)$ triệt tiêu (trạng thái lẻ). Hệ quả:
- $E_J^{(j)}\to E_J^{(j)}-\delta_k$ ⇒ $dE_J$ nhảy telegraph với biên độ $\sim\delta_k/2\bar E_J$.
- Với kênh $\tau\approx1$, năng lượng mức gần $\varphi=\pi$ nhỏ ⇒ bẫy hiệu quả.
- Mô hình: nhiễu telegraph đối xứng/bất đối xứng ⇒ mất pha kiểu Lorentz; nếu tốc độ chuyển ≪ $\delta\omega$ ⇒ phổ tách hai đỉnh.

Đọc: Uilhoorn et al. 2021, "Quasiparticle trapping by orbital effect in a hybrid superconducting-semiconducting circuit" (xác minh arXiv ID khi tải); Hays et al. 2018 PRL 121, 047001; Janvier 2015.

## Kênh 8 — đế III-V

Tỉ phần năng lượng điện (EPR) trong lớp III-V × $\tan\delta$. Gatemon 2DEG hiện có $T_1$ cỡ µs–vài chục µs — chủ yếu do kênh này. **$T_1=1{,}6$ ms của Al/sapphire không chuyển sang được** trừ khi mạch được thiết kế để mối nối là phần duy nhất trên III-V (khắc bỏ III-V ngoài vùng mối nối — kỹ thuật đã có).

## Bài tập trung tâm (cổng G1)

Lập bảng ngân sách cho 0-π lai ở điểm làm việc của [20]: mỗi kênh một dòng, $T_1^{(k)}$, $T_\varphi^{(k)}$, tham số dùng, nguồn tham số, độ bất định. Kết luận: kênh nào chi phối, và $T_{2R}$ thực tế ước lượng.
