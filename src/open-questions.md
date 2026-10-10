# Câu hỏi mở & giả thuyết

Trạng thái: `OPEN` (chưa bắt đầu) · `CHECKING` (đang kiểm) · `RESOLVED` (đã có câu trả lời, ghi bằng chứng) · `REFUTED` (giả thuyết sai).

Nguyên tắc: mọi khẳng định của đề cương đi qua bảng này trước khi vào bài báo/luận án.

---

## OQ-1 · Mode ζ ghép với qubit qua tham số nào? — `CHECKING` · ưu tiên CAO

**Giả thuyết trong đề cương:** khi $dE_J\neq0$, ζ ghép với $(\theta,\varphi)$ với hằng số ghép $\propto dE_J$, nên $\chi_{q\zeta}\propto dE_J^2$, và cân bằng $dE_J$ bằng cổng nâng $T_{2R}$ từ 24 µs lên ≈ 1,08 ms.

**Bằng chứng ngược (sơ bộ):**
- Trong Hamiltonian đầy đủ của Groszkowski et al. 2018 (cũng là `scqubits.FullZeroPi`), số hạng ghép là
  $H_{int} = 2E_{C\Sigma}\,dC\,\partial_\theta\partial_\zeta + E_L\,dE_L\,\varphi\,\zeta$; $dE_J$ chỉ xuất hiện trong khối $(\theta,\varphi)$.
- Lý do cấu trúc: mỗi mối nối nối hai nút cố định nên pha mối nối là tổ hợp tuyến tính $\theta\pm\varphi$ **chính xác**, không chứa ζ, bất kể rối loạn. Vậy $E_J^{A,B}$ không thể sinh ghép tới ζ ở bất kỳ bậc nào trong tọa độ này.
- Kiểm chứng số `code/scripts/check_zeta_coupling.py`: tại $dE_L=dC=0.05$, $\chi_{q\zeta}$ thay đổi < 1% khi $dE_J$ đi từ 0 đến 0,1; tại $dE_L=dC=0$, $\chi_{q\zeta}=0$ với mọi $dE_J$.

**Hệ quả nếu xác nhận:** cân bằng $E_J$ bằng cổng **không** triệt mất pha do ζ. Lập luận trung tâm của kết quả sơ bộ [20] cần xây lại: hoặc (a) tìm kênh khác mà $dE_J$ thực sự chi phối (ví dụ nhiễu từ thông bậc nhất khi đối xứng phản xạ bị phá kết hợp với $dC_J$), hoặc (b) dùng $V_g$ để bù gián tiếp, hoặc (c) chuyển trọng tâm sang các lợi ích khác của gatemon (điều hòa bậc hai, tần số điều chỉnh được).

**Khung chặt chẽ cho câu hỏi này:** hướng H1 (quy tắc chọn lọc theo biểu diễn nhóm), xem [OQ-8](#oq-8) và [điều chỉnh đề cương](outline-revision.md).

**Việc cần làm:**
- [ ] Đọc L3 Groszkowski 2018 §2–4, Dempster 2014 §III; tự lượng tử hoá mạch 4 nút có rối loạn đầy đủ.
- [ ] Đối chiếu với mô hình trong [20]: ζ được định nghĩa thế nào, có phải mô hình đã ngầm gán $dE_L\equiv dE_J$ (rối loạn tương quan)?
- [ ] Đọc Gyenis 2021 phần phân tích $T_2$: kênh nào được cho là giới hạn 24 µs?
- [ ] Kiểm tra trường hợp có $dC_J$: nhánh mối nối có điện dung riêng; gatemon thay đổi $E_J$ nhưng không thay đổi $C_J$ — điều này phá tương quan $dE_J\leftrightarrow dC_J$ vốn có ở Al/AlOx.

---

## OQ-2 · Cân bằng $E_{J,1}$ có kéo theo cân bằng $E_{J,2}$? — `OPEN`

Với $E^{j}_{J,M}=\sum_i E_{J,M}(\tau^{j}_i)$, điều kiện $E^A_{J,1}=E^B_{J,1}$ không suy ra $E^A_{J,2}=E^B_{J,2}$ vì $r(\tau)$ phi tuyến. Định lượng $dE_{J,2}$ dư theo phân bố kênh (một cổng vs hai cổng mỗi mối nối). Xem [DV2](derivations/dv2-zero-pi-harmonics.md).

## OQ-3 · Cắt cụt điều hòa có nhất quán với độ chính xác $|dE_J|\sim5\times10^{-3}$? — `OPEN`

Tại $\tau=0{,}9$: $E_{J,3}/E_{J,1}\approx0{,}032$, $E_{J,4}/E_{J,1}\approx0{,}010$. Kiểm hội tụ theo $M_{max}$ hoặc dùng thế Beenakker trực tiếp trên lưới. `hpq.zeropi` hỗ trợ cả hai.

## OQ-4 · Ngân sách mất kết hợp của 0-π lai trên đế III-V — `OPEN`

Thiếu: nhiễu cổng 1/f, ngộ độc QP vào ABS (nhảy telegraph cả $E_J$ và $dE_J$), tổn hao điện môi III-V, trạng thái dưới khe. $T_1=1{,}6$ ms là số đo trên Al/sapphire — không chuyển sang được.

## OQ-5 · $T_{2R}$ bão hoà ở 1,08 ms do kênh nào? — `OPEN`

Nếu kênh photon $\propto dE_J^4$ thì $T_{2R}\to2T_1$ khi $dE_J\to0$. Hình 6 đề cương bão hoà sớm → có kênh độc lập $dE_J$ chưa được nêu tên. (Liên quan OQ-1.)

## OQ-6 · Hiệu ứng $\varphi_0$ không bằng nhau giữa hai mối nối — `OPEN`

Rashba + $B_\parallel$ cho dịch pha dị thường điều chỉnh bằng cổng (Mayer 2020). $\varphi_0^A\neq\varphi_0^B$ phá đối xứng $\varphi\to-\varphi$ → mất sweet spot từ thông. Ở $B=0$ có đối xứng nghịch đảo thời gian → $\varphi_0=0$; cần xác định có cần $B$ không.

## OQ-7 · Độ dài kết hợp InAs/Al — `OPEN`

Đề cương ghi $\xi\sim100$–$200$ nm. Ước lượng sạch với $n=10^{12}$ cm⁻², $m^*=0{,}023m_e$: $k_F=\sqrt{2\pi n}\approx2{,}5\times10^8$ m⁻¹, $v_F\approx1{,}3\times10^6$ m/s; với $\Delta^*\approx180$ µeV: $\hbar v_F/\pi\Delta^*\approx1{,}5$ µm — lớn hơn 100–200 nm cả một bậc. Cần phân biệt $\xi_0$, $\ell_e$, $\xi_{dirty}=\sqrt{\xi_0\ell_e}$ và chọn chế độ ballistic/diffusive cho ND1.

---

<a id="oq-8"></a>
## OQ-8 · Quy tắc chọn lọc nhóm cho rối loạn của 0-π lai — `OPEN` · ưu tiên CAO (hướng H1)

Nhóm $G$ của mạch danh định; mỗi $\delta p\in\{dE_J,d_M,dE_L,dC,dC_J,\varphi_0,\dots\}$ thuộc biểu diễn nào; phần tử $\langle0|\partial_{\delta p}H|1\rangle$ và ghép tới ζ/mode mảng bị cấm hay cho phép. DV3 là trường hợp riêng đã kiểm số. Cần: (i) dẫn xuất bằng đại số, (ii) bảng tham số × biểu diễn × kênh nhiễu, (iii) kiểm bằng `scqubits.FullZeroPi`. Điểm khởi đầu: Ferguson 2013 (chưa xác nhận có quy tắc nhóm), Osborne 2024 cho khung đồ thị–đối xứng, Bravyi–DiVincenzo–Loss cho Schrieffer–Wolff chặt chẽ.

## OQ-9 · Hành động instanton của 0-π lai với điều hòa $r<0$ — `CHECKING` · hướng H3

Đã làm cho **một đảo**: $s(r)$ WKB khớp chéo hoá trong 3% với $r\in[-0{,}2,0{,}1]$; $r=-0{,}10$ giảm $S$ 7%, tỉ số $\varepsilon_0$ ×2–3 ở $E_J/E_C=36$–64 (`check_instanton_harmonics.py`). **Chưa làm:** 0-π hai giếng; cận Agmon; ảnh hưởng của $dE_J,d_M$ lên độ chồng lấp hàm sóng tách miền.

## OQ-10 · Có cần mạng tensor cho 0-π có siêu điện cảm là mảng? — `OPEN` · hướng H5

Kiểm: chéo hoá phân cấp (scqubits) cho 0-π + $k$ mode mảng hội tụ theo $k$ không? Nếu đổi $\ge$ ngưỡng sai số đề ra khi $k$ tăng thì mới cân nhắc DMRG/MPO. Tài liệu đã xác minh chỉ cho fluxonium (Di Paolo, arXiv:1912.01018; Viola–Catelani PRB 92, 224511).
