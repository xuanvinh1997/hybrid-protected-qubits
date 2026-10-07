# Hybrid Protected Qubits — sổ tay nghiên cứu

Kho tài liệu phục vụ luận án *"Nghiên cứu các thiết kế đối xứng cho qubit dựa trên vật liệu 2DEG lai hoá siêu dẫn/bán dẫn"*.

Mục tiêu không phải tóm tắt tài liệu mà là **nắm phương pháp**: với mỗi khái niệm, ghi rõ
(i) phát biểu chính xác, (ii) dẫn xuất tối thiểu tự làm lại được, (iii) giả thiết và miền hiệu lực,
(iv) phương pháp tính/đo dùng để kiểm chứng, (v) bẫy thường gặp, (vi) bài kiểm tra tự đánh giá,
(vii) thứ tự đọc tài liệu gốc.

## Cấu trúc

```
src/                    # sách mdBook (đọc trực tiếp trên GitHub cũng được)
  roadmap.md            # lộ trình 4 giai đoạn, gắn với Nội dung 1–3 của luận án
  methods-index.md      # bảng tra: phương pháp → dùng ở đâu → miền hiệu lực → tài liệu
  concept-map.md        # đồ thị phụ thuộc khái niệm (Mermaid)
  a-circuit/            # A. Lượng tử hoá mạch
  b-microscopic/        # B. Lý thuyết vi mô mối nối lai (BdG, Andreev, tán xạ)
  c-protected/          # C. Qubit bảo vệ bằng đối xứng (0-π, cos2φ, ...)
  d-noise/              # D. Nhiễu và mất kết hợp
  e-numerics/           # E. Phương pháp số
  f-control/            # F. Điều khiển, cổng, đọc trạng thái
  g-architecture/       # G. Kiến trúc chịu lỗi, chi phí QEC
  derivations/          # dẫn xuất chi tiết từng bước, có kiểm chứng số
  papers/               # template ghi chú bài báo + danh mục đọc phân tầng
  open-questions.md     # sổ câu hỏi mở / giả thuyết cần kiểm chứng
code/                   # gói Python `hpq` + tests + scripts tái lập hình
refs/refs.bib           # BibTeX
```

## Dùng

```bash
# đọc dạng sách
cargo install mdbook mdbook-katex mdbook-mermaid
mdbook serve --open

# mã tái lập
cd code && pip install -e ".[dev]" && pytest -q
python scripts/fig_beenakker_harmonics.py
python scripts/check_zeta_coupling.py      # cần scqubits
```

Công thức viết bằng `$...$` / `$$...$$` (GitHub và mdbook-katex đều hiển thị được).

## Quy ước làm việc

- Mỗi bài báo đọc nghiêm túc → một file trong `src/papers/notes/` theo `src/papers/template.md`.
- Mỗi kết luận định lượng dùng trong luận án → phải có một script trong `code/scripts/` hoặc test trong `code/tests/`.
- Giả thuyết chưa kiểm chứng → ghi vào `src/open-questions.md` với trạng thái `OPEN / CHECKING / RESOLVED / REFUTED`.
- Nhánh `main` luôn build được; CI chạy `pytest` và build sách.
