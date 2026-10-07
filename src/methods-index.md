# Bảng tra phương pháp

Mỗi dòng: phương pháp → bài toán trong luận án → miền hiệu lực / khi nào hỏng → tài liệu chuẩn → ghi chú.

## Giải tích

| Phương pháp | Dùng cho | Miền hiệu lực / bẫy | Tài liệu chuẩn | Ghi chú |
|---|---|---|---|---|
| Lượng tử hoá chính tắc mạch (cây khung, fluxoid) | Mọi Hamiltonian mạch | Mạch tập trung (kích thước ≪ λ vi sóng); bỏ qua mode thừa khi ma trận điện dung suy biến | Devoret 1997; Vool & Devoret 2017; Rasmussen 2021 | [A1](a-circuit/a1-circuit-quantization.md) |
| Gauge từ thông phụ thuộc thời gian (irrotational) | Điều khiển bằng từ thông, cổng nhanh | Phân bổ $\Phi_{ext}$ sai → số hạng ghép $\dot\Phi_{ext}\hat Q$ giả | You, Sauls, Koch 2019; Riwar & DiVincenzo 2022 | [A3](a-circuit/a3-time-dependent-flux.md) |
| Định lý Bloch cho biến tuần hoàn | Độ tán sắc điện tích, Aharonov–Casher | Phân biệt biến compact vs extended — xem A2 | Koch 2007; Koch et al. 2009 | [A2](a-circuit/a2-compact-extended.md) |
| BdG + ma trận tán xạ (Beenakker) | Phổ ABS, CPR | Mối nối ngắn $L\ll\xi$, $s$ không phụ thuộc năng lượng | Beenakker 1991, 1997 RMP | [B2](b-microscopic/b2-scattering-abs.md) |
| Điều kiện lượng tử hoá Bohr–Sommerfeld Andreev | Mối nối dài/trung gian | Bán cổ điển; cần cả đóng góp continuum vào $E_{GS}$ | Bagwell 1992; Kulik 1970 | [B3](b-microscopic/b3-beyond-short.md) |
| Lý thuyết nhiễu loạn suy biến / Schrieffer–Wolff | $\chi$, ghép hiệu dụng giữa mode | Hỏng gần cộng hưởng $|\Delta_{ll'}\pm\omega|\lesssim |g|$ | Bravyi, DiVincenzo, Loss 2011 | [DV3](derivations/dv3-zeta-coupling.md) |
| WKB / instanton | Tách mức thung lũng, phần tử ma trận | Rào cao so với $\hbar\omega$ cục bộ; đa chiều cần đường tác dụng cực tiểu | Coleman; Dempster 2014 | [C2](c-protected/c2-zero-pi.md) |
| Quy tắc vàng Fermi với $S(\omega)$ | $T_1$ từng kênh | Ghép yếu, nhiễu Markov tại $\omega_{01}$ | Schoelkopf 2003; Clerk RMP 2010 | [D1](d-noise/d1-framework.md) |
| Mất pha 1/f bậc hai tại sweet spot | $T_\varphi$ | Phân rã không hàm mũ; phụ thuộc cắt tần thấp $\omega_{ir}$ | Ithier 2005; Groszkowski 2018 | [D1](d-noise/d1-framework.md) |
| Nhiễu bắn photon (Clerk–Utami) | Mất pha do mode ζ / bộ cộng hưởng | Công thức đầy đủ cho mọi $\chi/\kappa$, $\bar n$ | Clerk & Utami 2007; Sears 2012 | [D2](d-noise/d2-channels.md) |

## Số

| Phương pháp | Dùng cho | Miền hiệu lực / bẫy | Công cụ | Ghi chú |
|---|---|---|---|---|
| Cơ sở điện tích (biến tuần hoàn) | $\theta$ trong 0-π, transmon | Cắt $|n|\le n_{cut}$; hội tụ hàm mũ khi thế trơn | scqubits, `hpq.zeropi` | [E1](e-numerics/e1-diagonalization.md) |
| Lưới sai phân / DVR (biến mở rộng) | $\varphi$ trong 0-π, fluxonium | Biên $\pm\varphi_{max}$ phải xa vùng hàm sóng; sai số $O(h^2)$ | scqubits, `hpq.zeropi` | [E1](e-numerics/e1-diagonalization.md) |
| Cơ sở dao động tử điều hòa | ζ, mode tuyến tính | Chọn tần số tham chiếu đúng để hội tụ nhanh | scqubits | |
| Chéo hoá phân cấp (hierarchical) | Mạch ≥ 3 mode | Cắt mức của hệ con phải kiểm hội tụ riêng | Kerman 2020; Chitta 2022 | |
| Lanczos/Arnoldi thưa (shift-invert) | Không gian $10^4$–$10^6$ | Suy biến gần → cần nhiều trị riêng hơn yêu cầu | `scipy.sparse.linalg.eigsh` | |
| Tight-binding BdG (Kwant) | $E_{GS}(\varphi; V_g)$, phổ ABS | Hằng số mạng $a\ll\lambda_F$; Al phải mô tả tường minh hoặc self-energy | Kwant | [E2](e-numerics/e2-kwant-bdg.md) |
| Lindblad / Bloch–Redfield | Động lực học cổng | Lindblad: Born–Markov + secular; Redfield cho phổ nhiễu có cấu trúc | QuTiP, dynamiqs | [F1](f-control/f1-protected-gates.md) |
| GRAPE / Krotov | Tối ưu xung | Ràng buộc băng thông AWG / RC đường cổng | QuTiP-qtrl, Qiskit Dynamics | |
| Tối ưu Bayes / surrogate | Quét không gian thiết kế | Hàm mục tiêu nhiễu số → cần kiểm hội tụ | BoTorch | |

## Thực nghiệm (để đọc hiểu dữ liệu)

| Phép đo | Cho biết gì | Bẫy diễn giải |
|---|---|---|
| Phổ hai tần số | Tần số chuyển dời ngoài cộng hưởng | Nhận diện sai chuyển dời khi có nhiều mức gần |
| $T_1$ theo $\Phi_{ext}$, $V_g$ | Kênh hồi phục chủ đạo | Hệ số chất lượng điện môi phụ thuộc tần số |
| Ramsey vs echo | Mất pha tần thấp vs tần cao | $T_2^*$ với nhiễu 1/f không hàm mũ |
| Nhảy chẵn lẻ (parity switching) | Tốc độ ngộ độc QP | Phân biệt QP bị bẫy trong ABS vs ở đảo |
| CPR qua SQUID bất đối xứng / RF | $E_{J,M}$ trực tiếp | Điện cảm vòng ảnh hưởng hình dạng CPR |
