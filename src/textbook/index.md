# Giáo trình

Mỗi chương theo cùng một khung: **phát biểu chính xác → dẫn xuất đầy đủ → điều kiện hiệu lực → kiểm chứng số → bài tập**. Nội dung giữ đúng trọng tâm của luận án; không có phần dẫn nhập chung. Các ghi chú ở Phần A–G là sổ tay tra cứu; giáo trình là lời giải thích đầy đủ từng khái niệm, theo thứ tự phụ thuộc.

| Chương | Khái niệm | Trạng thái | Mã kiểm chứng |
|---|---|---|---|
| 1 | Hiệu ứng Josephson, $E_J$, điện cảm phi tuyến | ✅ | tích phân $\pi^2\Delta$ |
| 2 | Lượng tử hoá mạch (Lagrange → Hamilton, fluxoid, $\mathbf C$ suy biến) | ✅ | — |
| 3 | Biến tuần hoàn/mở rộng, Bloch, độ tán sắc điện tích | ✅ | `hpq.transmon`, `test_transmon.py` |
| 4 | Transmon: $\omega_{01}$, $\alpha$, $\epsilon_m$, phần tử ma trận | ✅ | `hpq.transmon` |
| 5 | Fluxonium | ⏳ | |
| 6 | BdG, phản xạ Andreev, hiệu ứng lân cận | ⏳ | |
| 7 | ABS, Beenakker, CPR, điều hòa, gatemon | ⏳ | `hpq.andreev` |
| 8 | Nguyên lý bảo vệ bằng đối xứng | ⏳ | |
| 9 | cQED, tán sắc, nhiễu bắn photon | ⏳ | `hpq.dephasing` |
| 10 | Qubit 0-π, rối loạn, mode ζ | ⏳ | `hpq.zeropi` |
| 11 | Nhiễu: phổ, quy tắc vàng, 1/f | ⏳ | |
| 12 | Phần tử cos2φ, chẵn lẻ số cặp | ⏳ | |
| 13 | Điều khiển cổng và chi phí QEC | ⏳ | |

Ký hiệu thống nhất: $\hbar$ giữ tường minh khi có điện áp/dòng, đặt $\hbar=1$ khi chỉ có năng lượng; $R_K=h/e^2$; $\Phi_0=h/2e$; $\varphi=2\pi\Phi/\Phi_0$; $\hat n$ đếm số cặp, $[\hat\varphi,\hat n]=i$; $E_C=e^2/2C$.
