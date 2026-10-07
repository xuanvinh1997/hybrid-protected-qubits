# C4. Các thiết kế khác — đọc để định vị

Mục tiêu ở đây là **L1–L2**: biết mỗi thiết kế dùng đối xứng gì, phá vỡ bởi gì, để trả lời câu hỏi "vì sao chọn 0-π/cos2φ trên nền lai mà không phải X".

| Thiết kế | Đối xứng / cơ chế | Kết quả tiêu biểu | Liên quan nền lai? | Tài liệu |
|---|---|---|---|---|
| Fluxonium | tách miền định xứ tại $\Phi_0/2$, tần số thấp | $T_1,T_2$ > 1 ms | gatemon-fluxonium đã có (dây nano) | Manucharyan 2009; Somoroff 2023 |
| Bifluxon | chẵn lẻ fluxon + CPB | bảo vệ $T_1$ khi chuyển chẵn lẻ | ít | Kalashnikov 2020 |
| KITE | đồng xuyên hầm cặp đôi | $\cos2\varphi$ hiệu dụng | — | Smith 2020, 2022 |
| Mèo Kerr / mèo tiêu tán | lỗi lật bit triệt hàm mũ, nhiễu thiên lệch | bias noise → mã lặp | gián tiếp | Grimm 2020; Lescanne 2020 |
| Unimon | một JJ trong bộ cộng hưởng | bất điều hòa lớn, miễn nhiễm điện tích | — | Hyyppä 2022 |
| Qubit Andreev / Andreev spin | trạng thái vi mô của mối nối | điều khiển trực tiếp ABS | **chính nền lai** | Janvier 2015; Hays 2021 |
| Qubit chẵn lẻ dây vỏ toàn phần | Little–Parks + chẵn lẻ | đề xuất lý thuyết | **chính nền lai** | Giavaras et al. 2025 (arXiv:2503.05284) |
| Qubit Majorana / tetron | bảo vệ tô pô | tranh luận về bằng chứng | cùng vật liệu | Aghaee 2023 (TGP); Lutchyn 2018 |

**Bài tập định vị (viết 1 trang):** so sánh 0-π lai với gatemon-fluxonium và với cos2φ lai theo ba trục: (i) số tham số phá vỡ điều khiển được, (ii) kênh nhiễu không bảo vệ được, (iii) độ phức tạp chế tạo. Đây sẽ là đoạn "định vị" trong phần mở đầu bài báo 1.
