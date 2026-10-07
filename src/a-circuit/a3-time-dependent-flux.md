# A3. Từ thông ngoài phụ thuộc thời gian

## 1. Vấn đề

Với $\Phi_{ext}$ tĩnh, mọi cách phân bổ $\Phi_{ext}$ vào các nhánh của vòng tương đương nhau (khác nhau một phép biến đổi chính tắc). Khi $\Phi_{ext}(t)$ biến thiên, phép biến đổi đó phụ thuộc thời gian và sinh số hạng $\propto\dot\Phi_{ext}\,\hat Q$. Chỉ **một** cách phân bổ khớp với điện động lực học (cảm ứng Faraday thực sự phân bố theo điện dung các nhánh).

## 2. Kết quả (You, Sauls, Koch 2019)

Điều kiện "irrotational": chọn phân bổ sao cho Lagrangian không chứa số hạng ghép $\dot\Phi_{ext}\cdot\dot\Phi_j$. Với một vòng gồm các nhánh điện dung $C_b$ mắc nối tiếp, trọng số tỉ lệ nghịch với điện dung:
$$\Phi_b^{ext} = \frac{C_b^{-1}}{\sum_{b'}C_{b'}^{-1}}\,\Phi_{ext}$$
(giống phân áp trên tụ nối tiếp). Nhánh không có điện dung (điện cảm thuần) phải được xử lý bằng giới hạn.

## 3. Vì sao quan trọng cho luận án

- **Mất kết hợp do nhiễu từ thông**: phần tử ma trận nhiễu từ thông là $\partial H/\partial\Phi_{ext}$, phụ thuộc phân bổ → $T_1^{flux}$ của fluxonium/0-π có thể sai bậc độ lớn nếu chọn gauge sai (Riwar & DiVincenzo 2022).
- **Cổng nhanh bằng xung từ thông** (ND3): số hạng $\dot\Phi_{ext}\hat Q$ gây chuyển dời không mong muốn.
- Với **điều khiển bằng điện áp cổng** của gatemon, vấn đề tương ứng nhẹ hơn ($V_g$ thay đổi $E_J$, không vào ràng buộc fluxoid) — một lợi thế cần nêu khi so sánh cổng từ thông vs cổng điện.

## 4. Tự kiểm tra

1. Với dc-SQUID $C_1\neq C_2$, viết $H(t)$ theo hai cách phân bổ; tính tốc độ chuyển dời $0\to1$ dưới xung $\Phi_{ext}(t)$ tuyến tính, so sánh.
2. Áp dụng cho 0-π: hai tụ chéo $C$ và hai $C_J$ — phân bổ irrotational là gì?

## 5. Đọc

1. You, Sauls, Koch 2019 PRB 99, 174512 (arXiv:1902.04734). ★ L3
2. Riwar, DiVincenzo 2022 npj Quantum Inf. 8, 36 "Circuit quantization with time-dependent magnetic fields for realistic geometries". L2
3. Bryon, Weiss, You, Koch et al. 2023 "Time-dependent magnetic flux in devices for circuit quantum electrodynamics" — PR Applied. L1
