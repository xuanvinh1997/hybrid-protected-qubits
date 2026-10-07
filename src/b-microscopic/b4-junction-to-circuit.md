# B4. Từ mối nối vi mô đến Hamiltonian mạch

## 1. Xấp xỉ đoạn nhiệt (Born–Oppenheimer pha)

Hamiltonian toàn phần: $H=H_{circ}(\hat\varphi,\hat n)+H_{junc}(\hat\varphi;\{c\})$. Khi tần số plasma mạch $\omega_p\ll$ khe Andreev tối thiểu $\min_\varphi[E_A^+(\varphi)-E_A^-(\varphi)]/\hbar=2\Delta\sqrt{1-\tau}/\hbar$, các bậc tự do vi mô ở trạng thái cơ bản tức thời:
$$H_{eff}=H_{circ}+E_{GS}(\hat\varphi)+\underbrace{\tfrac{\hbar^2}{2}\ldots}_{\text{hiệu chỉnh Berry / thế hình học}} .$$

**Điều kiện cụ thể:** tại $\tau=0{,}9$, $2\Delta\sqrt{1-\tau}/h\approx2\times44\times0{,}32\approx28$ GHz ≫ vài GHz → tốt. Tại $\tau=0{,}99$: ≈ 9 GHz, bắt đầu vi phạm với plasmon $\theta$ của 0-π. Với $\tau\to1$ khe đóng tại $\varphi=\pi$: chuyển dời Landau–Zener sang trạng thái Andreev kích thích (Zazunov et al. 2003; Bargerbos 2020 dùng đúng hiệu ứng này).

## 2. Khi bậc tự do Andreev không thể loại

Mô hình mở rộng (Zazunov, Shumeiko, Wendin 2003; Kurilovich et al.; Kringhøj 2020): giữ trạng thái chẵn lẻ của mức Andreev như một spin
$$H=4E_C(\hat n-n_g)^2+\Delta\begin{pmatrix}\cos(\hat\varphi/2) & r\sin(\hat\varphi/2)\\ r\sin(\hat\varphi/2) & -\cos(\hat\varphi/2)\end{pmatrix}_{\text{Andreev}},\quad r=\sqrt{1-\tau},$$
lưu ý toán tử $e^{i\hat\varphi/2}$ dịch điện tích nửa cặp → không gian điện tích gồm cả số lẻ electron. Cần cho: ngộ độc QP (trạng thái lẻ), giới hạn $\tau\to1$, qubit Andreev.

## 3. Khai triển Fourier vs thế trực tiếp

Hai cách đưa $E_{GS}$ vào chéo hoá:
- **Fourier** $-\sum_{M\le M_{max}}E_{J,M}\cos M\hat\varphi$: thưa trong cơ sở điện tích ($e^{iM\theta}$ dịch $M$), tiện phân tích đối xứng; cắt cụt có sai số $\sum_{M>M_{max}}|E_{J,M}|$.
- **Trực tiếp** $-\Delta\sum\sqrt{1-\tau\sin^2(\hat\varphi/2)}$: chéo trên lưới pha; chính xác, nhưng trong cơ sở điện tích trở thành ma trận đặc (Toeplitz với hệ số Fourier) — tương đương Fourier với $M_{max}=2n_{cut}$.

Trong 0-π, mối nối nằm trên $\theta\pm\varphi$ với $\theta$ ở cơ sở điện tích, $\varphi$ ở lưới ⇒ Fourier theo $\theta$ là tự nhiên. `hpq.zeropi` nhận danh sách $\{E_{J,M}\}$ tùy ý cho mỗi mối nối.

## 4. Bẫy

- $E_{GS}$ của mối nối 2DEG bao gồm cả hằng số lớn $\propto N\Delta$; chỉ phần phụ thuộc $\varphi$ có nghĩa.
- Đổi dấu: $E_{J,2}<0$ với Beenakker → thế $-E_{J,2}\cos2\varphi=+|E_{J,2}|\cos2\varphi$, **nâng** năng lượng tại $\varphi=0,\pi$ so với $\pm\pi/2$ — làm phẳng đáy giếng (bất điều hòa giảm).
- Spin: dùng $\Delta\sum_n$ với $n$ chạy trên kênh suy biến spin, không nhân 2 thêm.

## 5. Đọc

1. Zazunov, Shumeiko, Bratus', Lantz, Wendin 2003 PRL 90, 087003 "Andreev level quantum dynamics in Josephson junctions". ★ L3
2. Kringhøj et al. 2020 PRL 124, 246803; Bargerbos et al. 2020 PRL 124, 246802. ★ L3
3. Janvier et al. 2015 Science 349, 1199; Hays et al. 2021 Science 373, 430 — khi mức Andreev chính là qubit. L1
