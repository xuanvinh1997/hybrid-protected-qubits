# G1. Từ thời gian kết hợp đến chi phí QEC

## 1. Công thức chuẩn và giới hạn của nó

Surface code khoảng cách $d$, lỗi logic mỗi chu kỳ (Fowler 2012; Google 2025):
$$\epsilon_L(d)\approx A\Big(\frac{p}{p_{th}}\Big)^{(d+1)/2},\qquad N_{phys}\approx2d^2 .$$
Ví dụ: $p/p_{th}=0{,}1$ ⇒ mỗi $+2$ trong $d$ giảm $\epsilon_L$ 10×.

**Bẫy diễn giải:** $p$ là lỗi **mỗi chu kỳ đo hội chứng** gồm cổng 2 qubit, đo, reset, rò rỉ — không phải $t_{cycle}/T_2$. Qubit bảo vệ có $T_2$ dài nhưng cổng chậm/đo chậm có thể làm $p$ **tăng**. Một phân tích nghiêm túc phải mô hình hoá ít nhất cổng 2 qubit và đo.

## 2. Đánh giá trung thực cho luận án

- Mức tối thiểu (khả thi trong ND3): bảng "nếu $p$ giảm từ $p_0$ xuống $p_1$ thì $d$ và $N_{phys}$ cần cho $\epsilon_L=10^{-12}$ thay đổi ra sao", với $p$ tính từ ngân sách lỗi một qubit + giả định rõ ràng cho cổng 2 qubit và đo. Ghi rõ đây là ước lượng điều kiện.
- Mức có đóng góp: nhiễu **thiên lệch** — nếu qubit bảo vệ có lỗi lật bit ≪ lỗi pha, dùng mã XZZX hoặc mã lặp + mã ngoài cho chi phí thấp hơn nhiều. Câu hỏi: 0-π lai có nhiễu thiên lệch không, và cổng có bảo toàn thiên lệch không?

## 3. Đọc

1. Fowler, Mariantoni, Martinis, Cleland 2012 PRA 86, 032324. ★ L2
2. Google Quantum AI 2025 Nature 638, 920 (dưới ngưỡng). L1
3. Bonilla Ataides et al. 2021 Nat. Commun. 12, 2172 (XZZX). L2
4. Puri et al. 2020 Sci. Adv. 6, eaay5901 (cổng bảo toàn thiên lệch). L1
