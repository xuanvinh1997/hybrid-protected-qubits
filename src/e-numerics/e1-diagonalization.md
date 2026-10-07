# E1. Chéo hoá Hamiltonian mạch và hội tụ

## 1. Biểu diễn

| Biến | Cơ sở | Toán tử | Hội tụ |
|---|---|---|---|
| tuần hoàn $\theta$ | điện tích $\vert n\rangle$, $\vert n\vert\le n_{cut}$ | $e^{iM\theta}$: dịch $M$; $\hat n$: chéo | hàm mũ (thế giải tích) |
| mở rộng $\varphi$ | lưới đều $N$ điểm trên $[-\varphi_{max},\varphi_{max}]$ | $-\partial^2$: sai phân 3 điểm | $O(h^2)$ |
| mở rộng $\varphi$ | DVR sinc | $-\partial^2$: ma trận đặc giải tích | hàm mũ |
| dao động tử | Fock $\vert k\rangle$, $k<k_{cut}$ | $a, a^\dagger$ | phụ thuộc chọn $\omega_{ref}$ |

Tích tensor: $H=\sum_\alpha A_\alpha\otimes B_\alpha$ dựng bằng `scipy.sparse.kron`.

## 2. Giao thức hội tụ (bắt buộc cho mọi số liệu báo cáo)

1. Chọn đại lượng mục tiêu $Q$ (trị riêng, **phần tử ma trận**, độ cong, độ tán sắc).
2. Quét từng tham số cắt $c\in\{n_{cut},N,\varphi_{max},k_{cut},l_{max}\}$ độc lập, tăng gấp ~1,5 lần mỗi bước.
3. Hội tụ khi $|Q(c_{k+1})-Q(c_k)|<\epsilon_{rel}|Q|$; với phần tử ma trận cỡ $10^{-3}$–$10^{-5}$ cần $\epsilon$ tương đối, không tuyệt đối.
4. Ghi bảng hội tụ vào `code/tests/` dưới dạng test hồi quy.

Bẫy: độ tán sắc điện tích cỡ kHz–MHz trên tần số GHz ⇒ cần sai số trị riêng tương đối $<10^{-7}$; dùng hiệu $E(n_g=1/2)-E(n_g=0)$ tính ở **cùng** lưới để triệt sai số hệ thống.

## 3. Bộ giải

- `eigsh(H, k, sigma=E0, which='LM')` (shift-invert) cho vài trị riêng thấp: nhanh, cần LU của $H-\sigma$.
- `which='SA'` không shift: không cần LU nhưng hội tụ chậm khi khe nhỏ.
- Gần suy biến ($\ket0,\ket\pi$ trong 0-π): yêu cầu $k$ lớn hơn số mức cần, kiểm trực giao.
- GPU: `cupyx.scipy.sparse.linalg.eigsh` (Lanczos) — hữu ích cho quét tham số $10^3$ điểm; tránh FP32 cho phần tử ma trận nhỏ.

## 4. Chéo hoá phân cấp

Cho $H=H_A\otimes1+1\otimes H_B+V$: chéo $H_A$, $H_B$ riêng, giữ $l_A,l_B$ mức thấp, chiếu $V$ ⇒ ma trận $l_Al_B$. Kiểm hội tụ theo $l_A,l_B$. scqubits `HilbertSpace` và `Circuit(..., hierarchical_diagonalization=True)` cài sẵn.

## 5. Xác minh chéo (bắt buộc)

- `hpq.zeropi` vs `scqubits.ZeroPi` ở $r=0$ (test trong `code/tests/test_zeropi.py`).
- Phổ transmon vs nghiệm Mathieu.
- Đối xứng: tính $\partial\omega/\partial\varphi_{ext}$ tại $\varphi_{ext}=0$ phải bằng 0 đến sai số máy (không phải đến sai số cắt).

## 6. Đọc

1. Groszkowski & Koch 2021 Quantum 5, 583 (scqubits). ★ L4 — đọc mã nguồn `zeropi.py`, `zeropi_full.py`.
2. Chitta et al. 2022 New J. Phys. 24, 103020 (Circuit module). L2
3. Kerman 2020, "Efficient numerical simulation of complex Josephson quantum circuits" (arXiv). L2
