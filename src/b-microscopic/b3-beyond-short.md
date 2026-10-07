# B3. Vượt ra ngoài giới hạn ngắn một kênh

Bốn hiệu chỉnh mà ND1 phải định lượng, theo thứ tự ảnh hưởng dự kiến lên $\{E_{J,M}\}$.

## 1. Độ dài hữu hạn $L/\xi_0$

Kênh ballistic, $\tau=1$, pha động học $EL/\hbar v_F$ thêm vào điều kiện lượng tử hoá (Bagwell 1992):
$$\arccos\frac{E}{\Delta}-\frac{EL}{\hbar v_F}=\pm\frac{\varphi}{2}+\pi m .$$
- $L\ll\xi_0$: một cặp ABS / kênh (Beenakker).
- $L\gtrsim\xi_0$: nhiều ABS / kênh, năng lượng ABS thấp nhất giảm $\sim\Delta/(1+L/\xi_0)$; **continuum đóng góp vào $E_{GS}(\varphi)$** — không thể chỉ cộng ABS.
- $L\gg\xi_0$: CPR răng cưa (Ishii/Kulik), $E_J\sim\hbar v_F/L$ thay cho $\Delta$.

Với kênh $\tau<1$ cần ma trận tán xạ phụ thuộc năng lượng $s_N(E)$ ⇒ giải định thức số.

**Phương pháp tính $E_{GS}$ không bỏ sót continuum:** $E_{GS}(\varphi)=-\frac{1}{2}\sum_{E_n>0}E_n$ trên hệ hữu hạn (tight-binding, có cắt năng lượng) hoặc dùng hàm Green: $E_{GS}=-k_BT\sum_{\omega_n}\ln\det[\ldots]$ (Matsubara) — ổn định số hơn với hệ lớn.

## 2. Nhiều kênh và trộn kênh

Đã ở [B2](b2-scattering-abs.md). Trong 2DEG phẳng: kênh ngang của dải rộng $W$, tán xạ bờ và tạp trộn kênh. Mô hình hoá tối thiểu: tight-binding với thế ngẫu nhiên, trung bình mẫu → thăng giáng mesoscopic của $E_J$ và $r$ (thăng giáng toàn cục kiểu UCF): $\delta E_J/E_J\sim1/\sqrt N$ trong chế độ diffusive.

**Ý nghĩa cho cân bằng cổng:** $E_J(V_g)$ có cấu trúc ngẫu nhiên theo $V_g$ → $\partial E_J/\partial V_g$ thay đổi dấu và độ lớn → độ nhạy nhiễu cổng thay đổi mạnh từ điểm làm việc này sang điểm khác.

## 3. Tương tác spin–quỹ đạo và Zeeman

- $B=0$: đối xứng nghịch đảo thời gian $\Rightarrow E(\varphi)=E(-\varphi)$. SOC đơn thuần **không** sinh $\varphi_0$; chỉ tách spin của ABS trong mối nối dài/đa kênh có $L\neq0$ (Chtchelkatchev & Nazarov 2003; Béri 2008).
- $B_\parallel\neq0$ vuông góc với trường SOC: $\varphi_0$-junction, $U(\varphi)=U_0(\varphi-\varphi_0)$ + hiệu ứng diode (Yokoyama, Eto, Nazarov 2014). Đo trên Al/InAs: Mayer et al. 2020, $\varphi_0$ điều chỉnh bằng cổng.
- Cho qubit 0-π: $\varphi_0^A\neq\varphi_0^B$ tương đương một từ thông ngoài hiệu dụng **khác dấu giữa hai nhánh** → phá $\varphi\to-\varphi$. Xem OQ-6.

## 4. Metallization, band bending, cổng

$\tau_i(V_g)$ không chỉ do mật độ hạt tải: cổng thay đổi hình dạng sóng theo phương $z$ → thay đổi trọng số trong Al → thay đổi $\Delta^*$, $\alpha_R$ đồng thời. Mô hình tối thiểu: Schrödinger–Poisson 1D theo $z$ + tight-binding 2D (Antipov 2018; Winkler et al. 2019 PRB 99, 245408 cho cách tiếp cận thống nhất).

## 5. Tóm tắt thứ bậc mô hình cho ND1

| Mức | Mô hình | Có được gì | Chi phí |
|---|---|---|---|
| M0 | Beenakker 1 kênh, $\tau$ cố định | $\{E_{J,M}(\tau)\}$ | giải tích |
| M1 | Beenakker nhiều kênh, $\rho(\tau)$ | $r_{eff}$, độ nhạy phân bố | giây |
| M2 | Định thức $s_N(E)$, $L$ hữu hạn | hiệu chỉnh $L/\xi_0$ | phút |
| M3 | Tight-binding BdG (Kwant), có Al | $E_{GS}(\varphi;V_g)$, SOC, $B$, rối loạn | giờ |
| M4 | M3 + Schrödinger–Poisson | $V_g$ thực | ngày |

Nguyên tắc: mỗi mức trên phải tái lập mức dưới trong giới hạn tương ứng (test hồi quy).

## 6. Đọc

1. Bagwell 1992 PRB 46, 12573 "Suppression of the Josephson current through a narrow, mesoscopic, semiconductor channel by a single impurity". ★ L3
2. Golubov, Kupriyanov, Il'ichev 2004 RMP — §III–IV. L2
3. Yokoyama, Eto, Nazarov 2014 PRB 89, 195407 "Anomalous Josephson effect induced by spin-orbit interaction and Zeeman effect in semiconductor nanowires". L2
4. Mayer et al. 2020 Nat. Commun. 11, 212 (arXiv:1905.12670). ★ L2
5. Pientka et al. 2017 PRX 7, 021032 "Topological superconductivity in a planar Josephson junction" — mô hình chuẩn mối nối phẳng 2DEG. ★ L2
6. Danilenko et al. 2023 "Few-mode to mesoscopic junctions in gatemon qubits" (arXiv:2209.03688). ★ L2
