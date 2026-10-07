# B2. Ma trận tán xạ và trạng thái liên kết Andreev

## 1. Phát biểu (Beenakker 1991)

Mối nối S–N–S ngắn ($L\ll\xi_0$), vùng N mô tả bằng ma trận tán xạ trạng thái thường $s_N(E)$ ($2N\times2N$), xấp xỉ không phụ thuộc năng lượng trên thang $\Delta$. Trạng thái liên kết thỏa
$$
\det\!\left[\,\mathbb 1-\alpha(E)^2\, r_A^*\, s_N^*(-E)\, r_A\, s_N(E)\right]=0,\qquad \alpha(E)=e^{-i\arccos(E/\Delta)},
$$
$r_A=\mathrm{diag}(e^{i\phi_L}\mathbb 1_N,\,e^{i\phi_R}\mathbb 1_N)$. Dùng phân tích cực của $s_N$ → mỗi kênh riêng với xác suất truyền $\tau_n$ (trị riêng của $t^\dagger t$) cho
$$
\boxed{E_n^{\pm}(\varphi)=\pm\Delta\sqrt{1-\tau_n\sin^2(\varphi/2)}},\qquad \varphi=\phi_L-\phi_R .
$$

## 2. Từ phổ đến năng lượng và dòng

Ở $T=0$, mối nối ngắn: continuum không phụ thuộc $\varphi$ ⇒
$$U(\varphi)=-\Delta\sum_n\sqrt{1-\tau_n\sin^2(\varphi/2)}\quad(\text{mỗi }n\text{ là một kênh suy biến spin}),$$
$$I(\varphi)=\frac{2e}{\hbar}\frac{dU}{d\varphi}=\frac{e\Delta}{2\hbar}\sum_n\frac{\tau_n\sin\varphi}{\sqrt{1-\tau_n\sin^2(\varphi/2)}}\tanh\frac{E_n}{2k_BT}.$$

Giới hạn kiểm tra:
- $\tau\to0$: $U\approx\text{const}-\frac{\Delta}{4}\sum\tau_n\cos\varphi$ ⇒ $E_J=\frac{\Delta}{4}\sum_n\tau_n$; với $G_N=\frac{2e^2}{h}\sum\tau_n$ được Ambegaokar–Baratoff $I_cR_N=\pi\Delta/2e$.
- $\tau=1$: $U=-\Delta|\cos(\varphi/2)|$, CPR $\propto\sin(\varphi/2)\,\mathrm{sgn}\cos(\varphi/2)$ — gãy tại $\varphi=\pi$ (Kulik–Omelyanchuk KO-1 cho tiếp điểm điểm ballistic).

## 3. Phân bố kênh

Mối nối thực có $N\sim W k_F/\pi$ kênh (W ≈ 1 µm, $k_F\approx2{,}5\times10^8$ m⁻¹ → $N\sim80$). Các mô hình phân bố:

| Chế độ | $\rho(\tau)$ | Hệ quả cho điều hòa |
|---|---|---|
| Ballistic lý tưởng | $\delta(\tau-1)$ cho mọi kênh mở | $r=-1/5$ |
| Diffusive (Dorokhov) | $\propto\frac{1}{\tau\sqrt{1-\tau}}$ (lưỡng mốt) | trọng số lớn gần $\tau=1$ → $|r|$ không nhỏ dù $\langle\tau\rangle$ vừa phải |
| Hỗn loạn (chaotic cavity) | $\propto\frac{1}{\sqrt{\tau(1-\tau)}}$ | |
| Gần ngưỡng mở kênh (QPC) | vài kênh với $\tau$ thay đổi theo $V_g$ | điều hòa thay đổi mạnh theo $V_g$ |

**Điểm cần kiểm cho đề cương:** khẳng định "mô hình một kênh cho cận trên của điều hòa bậc hai" không đúng tổng quát — với phân bố Dorokhov, $r_{eff}=\sum E_{J,2}(\tau_i)/\sum E_{J,1}(\tau_i)$ có thể lớn hơn $r(\langle\tau\rangle)$. Hàm `hpq.andreev.effective_ratio` tính cho phân bố bất kỳ.

## 4. Phương pháp đo (đọc dữ liệu)

- Phổ ABS: phổ học tunnel (Bretheau 2013), phổ vi sóng (Janvier 2015; Hays 2018).
- Phân bố $\tau$: dòng dư/MAR (multiple Andreev reflection) fit nhiều kênh; độ bất điều hòa gatemon $\propto\sum\tau^2/\sum\tau$ (Kringhøj 2018).
- Điều hòa trực tiếp: SQUID bất đối xứng; độ tán sắc điện tích gatemon ở $\tau\to1$ (Bargerbos 2020; Kringhøj 2020).

## 5. Bẫy

- $s_N(E)\approx s_N(0)$ chỉ khi thời gian dừng $\tau_{dwell}\ll\hbar/\Delta$; với cấu trúc cộng hưởng (chấm lượng tử trong mối nối) không đúng.
- $\tau_n$ là của **trạng thái thường ở mức Fermi**; với SOC + B không còn suy biến spin, mỗi kênh tách thành hai.

## 6. Tự kiểm tra

1. Dẫn xuất công thức Beenakker cho một kênh từ phương trình định thức (làm trong [DV1](../derivations/dv1-beenakker-fourier.md)).
2. Chứng minh $r\approx-\tau/16$ khi $\tau\ll1$ và $r=-1/5$ khi $\tau=1$. (`test_andreev.py` kiểm cả hai.)
3. Tính $r_{eff}$ cho Dorokhov với $\langle\tau\rangle$ = 0,5 và so với $r(0{,}5)=-0{,}043$.

## 7. Đọc

1. Beenakker 1991 PRL 67, 3836. ★ L3
2. Beenakker & van Houten 1991 PRL 66, 3056 (tiếp điểm điểm lượng tử). L2
3. Nazarov & Blanter, *Quantum Transport* (2009), ch. 1.6, 2.6 (ma trận tán xạ, Andreev). ★ L3
4. Kringhøj et al. 2018 PRB 97, 060508 (bất điều hòa ↔ $\tau$). ★ L3
5. Golubov, Kupriyanov, Il'ichev 2004 RMP 76, 411 "The current-phase relation in Josephson junctions". ★ L2 — tổng quan CPR mọi chế độ.
