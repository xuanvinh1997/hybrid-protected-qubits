# C2. Qubit 0-π

## 1. Hamiltonian đầy đủ (Groszkowski et al. 2018)

$$
\begin{aligned}
H &= H_{0\text{-}\pi} + H_\zeta + H_{int},\\
H_{0\text{-}\pi} &= -2E_{CJ}\partial_\varphi^2+2E_{C\Sigma}(i\partial_\theta-n_g)^2+2E_{C\Sigma}\,dC_J\,\partial_\varphi\partial_\theta\\
&\quad-2E_J\cos\theta\cos\!\Big(\varphi-\tfrac{\varphi_{ext}}2\Big)+E_L\varphi^2+2E_J+E_J\,dE_J\,\sin\theta\sin\!\Big(\varphi-\tfrac{\varphi_{ext}}2\Big),\\
H_\zeta &= \hbar\omega_\zeta a^\dagger a,\\
H_{int} &= 2E_{C\Sigma}\,dC\,\partial_\theta\partial_\zeta + E_L\,dE_L\,\varphi\,\zeta .
\end{aligned}
$$
(Quy ước theo `scqubits.ZeroPi` / `FullZeroPi`; hệ số trước $dE_J$ phụ thuộc định nghĩa $dE_J$ — đề cương dùng $2E_J\,dE_J$ với $dE_J=(E_J^A-E_J^B)/(E_J^A+E_J^B)$. Thống nhất quy ước trước khi so số.)

Bốn tham số rối loạn: $dE_J$ (mối nối), $dC_J$ (điện dung mối nối), $dC$ (tụ chéo), $dE_L$ (điện cảm). **Chỉ $dC$ và $dE_L$ ghép ζ.**

## 2. Cấu trúc thế và trạng thái logic

$V(\theta,\varphi)=-2E_J\cos\theta\cos\varphi+E_L\varphi^2$ (tại $\varphi_{ext}=0$):
- $\theta=0$: giếng đơn sâu tại $\varphi=0$ ⇒ $\ket{0}$ định xứ quanh $(0,0)$.
- $\theta=\pi$: $+2E_J\cos\varphi+E_L\varphi^2$ ⇒ giếng đôi tại $\varphi\approx\pm\pi$ ⇒ $\ket\pi$ = tổ hợp đối xứng.
- $\ket0,\ket\pi$ gần suy biến nhờ $E_L\pi^2$ nhỏ; cân bằng chính xác bằng chọn $\varphi_{ext}$ hoặc tham số.

## 3. Ba cơ chế bảo vệ

| Cơ chế | Đối xứng | Đại lượng triệt | Tham số phá |
|---|---|---|---|
| Tách miền định xứ | — (hình học thế) | $\bra\pi\hat n_\theta\ket0$, $\bra\pi\hat\varphi\ket0$ | không cần đối xứng chính xác |
| Sweet spot từ thông | $(\theta,\varphi)\to(-\theta,-\varphi)$ hoặc $\varphi\to-\varphi$ | $\partial\omega/\partial\Phi_{ext}$ | $\varphi_0^A\neq\varphi_0^B$, $dE_J$ khi $\varphi_{ext}\neq0$ |
| Aharonov–Casher | Bloch theo $\theta$ | $\partial\omega/\partial n_g^\theta$ | — (tô pô), nhưng độ lớn triệt phụ thuộc $E_J/E_{C\Sigma}$ |

## 4. Chế độ cứng vs mềm

Cứng: $E_{CJ}\gg E_J\gg E_L,\,E_{C\Sigma}$. Ví dụ Brooks–Kitaev–Preskill; đòi hỏi $C_J$ cực nhỏ + điện cảm cực lớn + tụ chéo cực lớn — ngoài tầm chế tạo.
Mềm (Gyenis 2021): $E_{CJ}$ vừa phải ⇒ hàm sóng $\ket0,\ket\pi$ chồng lấn theo $\varphi$ nhiều hơn; bảo vệ $T_1$ chủ yếu nhờ tách theo $\theta$. Đo (tóm tắt bài gốc, arXiv:1910.07542): $T_1\approx1{,}6$ ms, thời gian mất pha ≈ 25 µs. Khi đọc L4: ghi rõ điểm làm việc, loại phép đo (Ramsey/echo), và kênh mà tác giả quy cho giới hạn $T_2$.

## 5. Vai trò của ζ

ζ là dao động tử tần số thấp (thường vài trăm MHz) với $\bar n_\zeta$ nhiệt không nhỏ. Ghép qua $dE_L\varphi\zeta$ và $dC\,\partial_\theta\partial_\zeta$ sinh dịch chuyển tán sắc $\chi_{q\zeta}$ ⇒ nhiễu bắn photon nhiệt ([D2](../d-noise/d2-channels.md)). Chi tiết và kiểm chứng số: [DV3](../derivations/dv3-zeta-coupling.md).

## 6. Phương pháp tính

- $(\theta,\varphi)$: cơ sở điện tích × lưới; kích thước $(2n_{cut}+1)N_\varphi\sim10^4$.
- ζ: hoặc nhiễu loạn bậc hai qua $g_{ll'}$ (nhanh, cho $\chi$), hoặc chéo hoá phân cấp $H_{0\text{-}\pi}\otimes H_\zeta$ với $l\le12$, $n_\zeta\le10$.
- Phần tử ma trận cực nhỏ ($10^{-3}$–$10^{-6}$) ⇒ cần sai số trị riêng/vectơ riêng tương ứng; kiểm hội tụ **phần tử ma trận**, không chỉ trị riêng.

## 7. Tự kiểm tra

1. Tái lập Groszkowski 2018 Fig. 2 (phổ theo $\varphi_{ext}$) bằng `hpq.zeropi` và `scqubits.ZeroPi`; hai cách phải khớp.
2. Tìm tham số soft 0-π của Gyenis 2021 và tính $|\bra\pi\hat n_\theta\ket0|$.
3. Chứng minh $\bra0\hat\varphi\ket0=\bra\pi\hat\varphi\ket\pi=0$ tại $\varphi_{ext}=0$ với mọi $dE_J$ (dùng đối xứng $(\theta,\varphi)\to(-\theta,-\varphi)$).

## 8. Đọc

1. Brooks, Kitaev, Preskill 2013 PRA 87, 052306. ★ L2
2. Dempster, Fu, Ferguson, Schuster, Koch 2014 PRB 90, 094518. ★ L3
3. Groszkowski et al. 2018 New J. Phys. 20, 043053. ★ L4
4. Gyenis et al. 2021 PRX Quantum 2, 010339. ★ L4
5. Di Paolo et al. 2019 New J. Phys. 21, 043002 (điều khiển 0-π). ★ L2
6. "The tunable 0-π qubit: dynamics and relaxation" (arXiv:2211.09333) — 0-π dưới từ thông phụ thuộc thời gian, xử lý gauge-invariant; nối [A3](../a-circuit/a3-time-dependent-flux.md) với ND3. L2
