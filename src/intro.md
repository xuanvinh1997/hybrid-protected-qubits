# Giới thiệu & giao thức đọc

## Mục đích

Sổ tay này phục vụ một việc: biến tài liệu thành **năng lực làm được** — tự dẫn xuất, tự tính, tự phản biện —
trong ba trục của luận án:

| Trục | Câu hỏi trung tâm | Nội dung luận án |
|---|---|---|
| Vi mô | $U(\varphi; V_g)$ của mối nối InAs/Al thực trông như thế nào, sai số bao nhiêu khi dùng Beenakker một kênh? | ND1 |
| Mạch | Đối xứng nào bảo vệ qubit, phá vỡ đối xứng nào điều chỉnh được bằng cổng, cái nào không? | ND2 |
| Động lực học | Làm sao điều khiển/đọc một qubit mà phần tử ma trận bị triệt tiêu theo thiết kế? | ND3 |

## Giao thức đọc 4 mức

Mỗi tài liệu được gắn một mức mục tiêu trong [danh mục đọc](papers/reading-list.md). Không "đọc xong" nếu chưa đạt mức đó.

| Mức | Tên | Sản phẩm bắt buộc |
|---|---|---|
| **L1** | Định vị | 5 dòng: câu hỏi, phương pháp, kết quả chính, giả thiết then chốt, liên hệ luận án |
| **L2** | Hiểu phương pháp | Ghi chú theo [template](papers/template.md): mọi phương trình chính được giải thích từng ký hiệu, chỉ rõ bước xấp xỉ |
| **L3** | Dẫn xuất lại | Tự làm lại các bước chính trên giấy/LaTeX, đặt trong `derivations/`; ghi chỗ bài báo nhảy bước |
| **L4** | Tái lập | Script trong `code/` tái tạo ít nhất một hình/bảng số; ghi sai lệch và nguyên nhân |

Quy tắc: tài liệu lõi (★) phải đạt L3–L4; tài liệu bối cảnh đạt L1–L2 là đủ.

## Cấu trúc mỗi ghi chú khái niệm

1. **Phát biểu** — định nghĩa chính xác, ký hiệu.
2. **Dẫn xuất tối thiểu** — đủ để tự làm lại.
3. **Giả thiết & miền hiệu lực** — khi nào công thức sai.
4. **Phương pháp** — cách tính số / cách đo trong thực nghiệm.
5. **Bẫy** — lỗi quy ước, thừa số 2, dấu.
6. **Tự kiểm tra** — bài tập có đáp án kiểm được bằng mã.
7. **Đọc theo thứ tự** — từ tài liệu dẫn nhập đến bài gốc.

## Nguyên tắc nhận thức

- Một con số trong luận án phải truy được về: mô hình → tham số → mã → test.
- Phân biệt rõ **"mô hình nói"** và **"thực nghiệm đo"**. Ví dụ: $T_1 = 1{,}6$ ms là số đo trên Al/sapphire, không phải tiên đoán cho đế III-V.
- Mỗi giả thuyết của đề cương được đưa vào [câu hỏi mở](open-questions.md) và chỉ được dùng khi đã `RESOLVED`.
