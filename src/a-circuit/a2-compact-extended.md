# A2. Biến tuần hoàn, biến mở rộng, điện tích lệch

## 1. Phát biểu

Một biến pha $\varphi_k$ là **tuần hoàn (compact)** nếu Hamiltonian bất biến dưới $\varphi_k\to\varphi_k+2\pi$ **và** không gian Hilbert được chọn là hàm trên đường tròn: khi đó $\hat n_k$ có phổ nguyên. Ngược lại là **mở rộng (extended)**: $\hat n_k$ liên tục.

- Đảo siêu dẫn chỉ nối qua tụ và mối nối → tuần hoàn (điện tích đảo lượng tử hoá theo $2e$).
- Có nhánh điện cảm tuyến tính nối nút → thế $\propto\varphi^2$ phá tịnh tiến → mở rộng.

## 2. Định lý Bloch và điện tích lệch

Với thế $2\pi$-tuần hoàn, nghiệm $\psi_{m,q}(\varphi+2\pi)=e^{2\pi i q}\psi_{m,q}(\varphi)$. Điện tích lệch $n_g$ đóng vai trò giả xung lượng $q$:
$$
H=4E_C(\hat n-n_g)^2+U(\hat\varphi)\;\xrightarrow{\;e^{in_g\varphi}\;}\;4E_C\hat n^2+U(\hat\varphi),\quad\psi(\varphi+2\pi)=e^{-2\pi i n_g}\psi(\varphi).
$$
Độ tán sắc điện tích $\epsilon_m=E_m(n_g=1/2)-E_m(0)$ chính là độ rộng vùng Bloch → tỉ lệ với biên độ xuyên hầm $2\pi$ (phase slip).

**Với biến mở rộng**, $n_g$ bị loại bằng biến đổi gauge (không có điều kiện biên tuần hoàn) → miễn nhiễm điện tích hoàn toàn (fluxonium). Lưu ý: điều này phụ thuộc vào việc điện cảm thực sự là tuyến tính; siêu điện cảm bằng chuỗi JJ có phase slip trong chuỗi → độ nhạy điện tích dư (Koch et al. 2009, *PRL* 103, 217004).

## 3. Giao thoa Aharonov–Casher trong 0-π

$\theta$ tuần hoàn. Hai thung lũng ($\theta=0$ và $\theta=\pi$) nối bởi hai đường xuyên hầm $\theta:0\to\pi$ và $\theta:0\to-\pi$. Pha Berry do $n_g^\theta$: $\pm\pi n_g^\theta$. Biên độ hiệu dụng
$$t_{eff}=t_+e^{i\pi n_g}+t_-e^{-i\pi n_g}\xrightarrow{t_+=t_-}2t\cos(\pi n_g^\theta).$$
Hệ quả: tại $n_g^\theta=1/2$ hai đường triệt tiêu → điểm tối ưu điện tích; với $t_+\neq t_-$ (bất đối xứng) không triệt tiêu hết.

**Câu hỏi luận án:** $dE_J\neq0$ có làm $t_+\neq t_-$ không? Dưới $(\theta,\varphi)\to(-\theta,-\varphi)$, số hạng $\sin\theta\sin\varphi$ bất biến; hai đường $0\to\pm\pi$ liên hệ qua phép này → $|t_+|=|t_-|$ vẫn giữ khi $\varphi_{ext}=0$. Kiểm bằng số.

## 4. Phương pháp số

- Biến tuần hoàn: cơ sở điện tích $\{|n\rangle\}_{|n|\le n_{cut}}$, $e^{iM\hat\theta}|n\rangle=|n+M\rangle$. Thế trơn → hội tụ hàm mũ theo $n_{cut}$.
- Biến mở rộng: lưới $\varphi_k=-\varphi_{max}+kh$, $-\partial^2\to$ sai phân 3 điểm (sai số $O(h^2)$) hoặc DVR sinc (hội tụ hàm mũ).

## 5. Bẫy

- Áp lưới tuần hoàn cho biến mở rộng (hay ngược lại) → phổ sai mà vẫn "trông hợp lý".
- Trong cơ sở điện tích với $\cos(M\theta)$, $M\ge2$: không gian tách thành $M$ lớp $n\bmod M$ — đúng là cơ chế bảo vệ chẵn lẻ của cos2φ, nhưng cũng là nguồn suy biến số làm eigsh hội tụ chậm.

## 6. Tự kiểm tra

1. Tái lập Koch 2007 Fig. 2 (vùng Bloch transmon) bằng cơ sở điện tích và so với nghiệm Mathieu (`scipy.special.mathieu_a`).
2. Chứng minh độ tán sắc của cos2φ: $\epsilon\propto e^{-\sqrt{8E_2/E_C}\cdot(\ldots)}$ và xác định số mũ.

## 7. Đọc

1. Koch et al. 2007 PRA 76, 042319 — §II–III, App. A. ★ L4
2. Koch, Manucharyan, Devoret, Glazman 2009 PRL 103, 217004. L2
3. Groszkowski 2018 (AC trong 0-π). ★ L3
4. Pop et al. 2014 *Nature* 508, 369 "Coherent suppression of electromagnetic dissipation due to superconducting quantum phase slips" — quan sát AC trong mạch. L1
