# DV2. Tọa độ 0-π và điều hòa bậc cao

Mức: L3. Mã: `hpq/zeropi.py` (`HybridZeroPi.symmetric(..., dEJ2=...)`).

## 1. Thế Josephson trong tọa độ tập thể

Pha hai mối nối: $\varphi_A=\theta+\varphi'$, $\varphi_B=\theta-\varphi'$, $\varphi'=\varphi-\varphi_{ext}/2$ (chính xác, xem [A1](../a-circuit/a1-circuit-quantization.md) §4).
Mỗi mối nối $U_j=-\sum_ME^{(j)}_{J,M}\cos M\varphi_j$. Đặt $\bar E_M=\tfrac12(E^A_{J,M}+E^B_{J,M})$, $d_M=\frac{E^A_{J,M}-E^B_{J,M}}{E^A_{J,M}+E^B_{J,M}}$. Dùng $\cos(a\pm b)$:
$$
\boxed{U(\theta,\varphi)=\sum_M\Big[-2\bar E_M\cos M\theta\cos M\varphi'+2\bar E_M\,d_M\sin M\theta\sin M\varphi'\Big]}
$$

So sánh với Eq. (17) của đề cương: số hạng phá đối xứng bậc hai là $2\bar E_2\,d_2\sin2\theta\sin2\varphi'$ — **hệ số 2 và $d_2$ thay cho $d_1$**. Hai cách viết trùng nhau chỉ khi $d_2=d_1/2$, không có lý do vật lý nào cho điều đó.

## 2. Phân tích đối xứng (mọi $M$)

| Phép | Tác động | $\cos M\theta\cos M\varphi'$ | $\sin M\theta\sin M\varphi'$ | Hệ quả |
|---|---|---|---|---|
| $P_1:(\theta,\varphi')\to(-\theta,-\varphi')$ | | bất biến | bất biến | luôn là đối xứng (với $n_g\to-n_g$) |
| $P_2:\varphi'\to-\varphi'$ | | bất biến | đổi dấu | đối xứng ⇔ mọi $d_M=0$ |
| $T:\theta\to\theta+2\pi$ | | bất biến | bất biến | Bloch/AC giữ cho mọi $M$ |
| $\theta\to\theta+\pi$ | | $(-1)^M$ | $(-1)^M$ | hoán đổi thung lũng chỉ với $M$ lẻ |

Kết luận cần chứng minh cẩn thận khi viết bài:
- **Sweet spot từ thông** tại $\varphi_{ext}=0$: $E_n(\varphi_{ext})=E_n(-\varphi_{ext})$ được bảo đảm bởi $P_1$ kết hợp với $E_L\varphi^2$ (chẵn) — **với mọi $d_M$**, không cần $P_2$. (Test `test_flux_sweet_spot_any_dEJ_and_r`.) Lưu ý: $P_1$ đảo $n_g^\theta\to-n_g^\theta$; tại $n_g\in\{0,\tfrac12\}$ điều này tương đương (sai khác số nguyên — gauge), ở giá trị khác thì sweet spot từ thông chỉ gần đúng.
- Vai trò thực của $d_M$: trộn $\ket0$ với trạng thái lẻ dưới $P_2$ → thay đổi phần tử ma trận, độ cong, tách mức; **không** phá sweet spot bậc nhất.

## 3. OQ-2: cân bằng một điều hòa không cân bằng điều hòa khác

Mỗi mối nối có tập kênh $\{\tau^{(j)}_n(V_g^{(j)})\}$. Một cổng mỗi mối nối ⇒ một tham số tự do mỗi bên ⇒ chỉ ép được $d_1=0$. Khi đó
$$d_2\big|_{d_1=0}=\frac{\sum_nE_{J,2}(\tau^A_n)-\sum_nE_{J,2}(\tau^B_n)}{\sum_nE_{J,2}(\tau^A_n)+\sum_nE_{J,2}(\tau^B_n)}\neq0$$
nói chung. Ví dụ đồ chơi: A có 1 kênh $\tau=0{,}9$; B có 2 kênh cùng $\tau_B$ chọn sao cho $2E_{J,1}(\tau_B)=E_{J,1}(0{,}9)$. Tính $d_2$ (bài tập — đáp số kiểm bằng `hpq.andreev`).

Chiến lược nghiên cứu: (i) ước lượng $d_2$ dư theo thống kê mesoscopic (ensemble Kwant), (ii) tính độ nhạy $\partial\omega_{01}/\partial d_2$, $\partial T_{1,2}/\partial d_2$ bằng `HybridZeroPi.symmetric(..., dEJ2=...)`, (iii) đánh giá có cần hai cổng/mối nối không.

## 4. Cắt cụt (OQ-3)

Tại $\tau=0{,}9$, $\bar E_3/\bar E_1\approx0{,}032$. Nếu $d_3\sim0{,}1$ thì số hạng $2\bar E_3d_3\sim0{,}006\bar E_1$ — cùng bậc với $2\bar E_1d_1$ ở $d_1=0{,}005$ ($0{,}010\bar E_1$). Quy trình: chạy `HybridZeroPi(EJA=[...M_max], EJB=[...])` với $M_{max}=2,3,4,6$, báo cáo hội tụ của đại lượng mục tiêu.
