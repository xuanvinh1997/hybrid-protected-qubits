# F1. Cổng trên qubit bảo vệ

## 1. Mâu thuẫn bảo vệ–điều khiển

Nếu $|\bra1\hat O\ket0|\sim\epsilon$ cho mọi $\hat O$ cục bộ thì tốc độ Rabi trực tiếp $\Omega\propto\epsilon$ trong khi rò rỉ sang mức cao không bị triệt ⇒ cổng trực tiếp chậm và bẩn. Các lối ra trong tài liệu:

| Chiến lược | Ý tưởng | Tài liệu | Điểm yếu |
|---|---|---|---|
| Raman qua mức trung gian | $\ket0\to\ket e\to\ket\pi$, mức $e$ có chồng lấn với cả hai | Di Paolo 2019 (0-π); Earnest 2018 (fluxonium Λ) | chậm, mức $e$ không bảo vệ |
| Cổng bảo vệ tô pô / hình học | ghép với dao động tử, cổng pha hình học | Brooks, Kitaev, Preskill 2013 | đòi tham số cứng |
| Điều biến tham số | điều biến $\Phi_{ext}$ hay $V_g$ ở tần số chuyển dời | | ghép tham số cũng yếu |
| **Hạ bảo vệ tạm thời** | giảm rào thế ⇒ tăng chồng lấn ⇒ cổng nhanh ⇒ khôi phục | ý tưởng của ND3 | rò rỉ không đoạn nhiệt, nhiễu khi rào thấp |

## 2. Phân tích "hạ bảo vệ" — các câu hỏi phải trả lời

1. **Tham số điều khiển là gì?** Trong 0-π lai: $\bar E_J(V_g)$ (chung) — hạ $\bar E_J$ giảm rào giữa thung lũng. Phạm vi: $\tau(V_g)$ từ ~0,5 đến ~0,95 ⇒ $\bar E_J$ đổi ~×2 (theo Bảng DV1).
2. **Đoạn nhiệt so với cái gì?** Khe nhỏ nhất dọc đường điều khiển giữa không gian tính toán và mức cao (plasmon θ ~ GHz; tách mức thung lũng π ~ 20–30 MHz — **rất nhỏ**). Tiêu chí Landau–Zener với khe ~30 MHz ⇒ thời gian ramp ≳ 100 ns.
3. **Băng thông đường cổng.** Cổng điện của gatemon thường có lọc RC ~ MHz–100 MHz ⇒ giới hạn dưới thời gian ramp; cần đường cổng băng rộng (tiêu tán thêm — kênh 11 ở [D2](../d-noise/d2-channels.md)).
4. **Mất kết hợp trong lúc rào thấp.** Tích phân $\int\Gamma(t)\,dt$ dọc xung; tối ưu hình dạng xung để cân bằng tốc độ cổng và lỗi.
5. **Pha động lực học.** Tần số qubit thay đổi theo $V_g$ ⇒ pha tích lũy phụ thuộc nhiễu $V_g$ ⇒ cần echo hoặc thiết kế sao cho $\partial\omega_{01}/\partial V_g$ nhỏ dọc đường.

## 3. Phương pháp

- Mô hình: $H(t)=H_{0\text{-}\pi}[\bar E_J(t)]$ chiếu lên $l\lesssim10$ mức tức thời; biểu diễn đoạn nhiệt + số hạng không đoạn nhiệt $\dot\lambda\bra m\partial_\lambda\ket n$.
- Mô phỏng: Lindblad với tốc độ phụ thuộc thời gian từ [D2]; kiểm bằng Bloch–Redfield vì mức gần suy biến.
- Tối ưu: GRAPE/Krotov trên $V_g(t)$ có ràng buộc băng thông; đo lỗi bằng độ trung thực cổng trung bình + rò rỉ riêng.
- Đọc trạng thái: χ với bộ cộng hưởng nhỏ ở điểm bảo vệ ⇒ đọc khi đã hạ bảo vệ, hoặc đọc qua mức phụ.

## 4. Đọc

1. Di Paolo, Grimsmo, Groszkowski, Koch, Blais 2019 New J. Phys. 21, 043002. ★ L3
2. Earnest et al. 2018 PRL 120, 150504 "Realization of a Λ system with metastable states of a capacitively shunted fluxonium". L2
3. Khaneja et al. 2005 J. Magn. Reson. 172, 296 (GRAPE). L2
4. Motzoi, Gambetta, Rebentrost, Wilhelm 2009 PRL 103, 110501 (DRAG — rò rỉ). L2
