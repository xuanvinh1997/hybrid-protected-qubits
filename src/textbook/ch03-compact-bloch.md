# Chương 3. Biến tuần hoàn, định lý Bloch và điện tích lệch

Câu hỏi của chương: khi nào $\hat n$ có phổ nguyên, $n_g$ đi vào Hamiltonian như thế nào, và vì sao độ nhạy với $n_g$ tương ứng với một biên độ xuyên hầm.

## 3.1 "Tuần hoàn" là tính chất của không gian Hilbert, không chỉ của $H$

Hamiltonian $H=4E_C\hat n^2+U(\hat\varphi)$ với $U(\varphi+2\pi)=U(\varphi)$ bất biến dưới $\varphi\to\varphi+2\pi$ trong cả hai trường hợp sau, nhưng chúng khác nhau về vật lý:

| | Không gian Hilbert | Phổ $\hat n$ | Tên |
|---|---|---|---|
| (a) | $L^2(S^1)$: $\psi(\varphi+2\pi)=\psi(\varphi)$ | $\mathbb Z$ | biến **tuần hoàn** (compact) |
| (b) | $L^2(\mathbb R)$ | $\mathbb R$ | biến **mở rộng** (extended) |

Phân loại vật lý: $\hat n$ đếm số cặp Cooper dư trên một đảo. Nếu đảo chỉ nối ra ngoài qua tụ và mối nối đường hầm, điện tích đảo là bội của $2e$ (cộng điện tích lệch liên tục) ⇒ trường hợp (a). Nếu đảo nối với đất qua một **điện cảm tuyến tính**, dòng siêu dẫn qua điện cảm có thể mang điện tích liên tục ra/vào ⇒ trường hợp (b). Phần tử cos trong thế không quyết định điều này; **kết nối** quyết định.

Với biến (a), toán tử $e^{i\hat\varphi}$ là toán tử dịch số cặp, $e^{i\hat\varphi}|n\rangle=|n+1\rangle$, và chỉ các hàm của $e^{i\hat\varphi}$ (như $\cos\hat\varphi$) là toán tử hợp lệ; bản thân $\hat\varphi$ không được xác định như một toán tử. Với biến (b), $\hat\varphi$ là toán tử hợp lệ, và có thể xuất hiện số hạng $\hat\varphi^2$.

## 3.2 Điện tích lệch là một điều kiện biên

Điện tích lệch $n_g$ (do điện áp cổng và điện tích tạp) đi vào như $H=4E_C(\hat n-n_g)^2+U(\hat\varphi)$. Trong biểu diễn pha, $\hat n=-i\partial_\varphi$ và phép biến đổi
$$
\psi(\varphi)=e^{in_g\varphi}\chi(\varphi)
$$
đưa $H$ về $4E_C\hat n^2+U$ cho $\chi$, nhưng điều kiện biên đổi:
$$
\psi(\varphi+2\pi)=\psi(\varphi)\ \Longleftrightarrow\ \chi(\varphi+2\pi)=e^{-2\pi in_g}\chi(\varphi).
$$
Vậy $n_g$ là một **góc xoắn** của điều kiện biên. Hệ quả tức thì:
1. phổ tuần hoàn theo $n_g$ với chu kỳ 1: $n_g\to n_g+1$ chỉ là gán lại nhãn $n\to n+1$;
2. với biến mở rộng không có điều kiện biên nên phép biến đổi trên là phép biến đổi unita thật: **phổ không phụ thuộc $n_g$** (tính chính xác, với điện cảm tuyến tính).

## 3.3 Định lý Bloch

Xét $H_0=4E_Cp^2+U(\varphi)$ trên $\mathbb R$ với $p=-i\partial_\varphi$, $U$ có chu kỳ $2\pi$. Toán tử dịch $T:\varphi\to\varphi+2\pi$ giao hoán với $H_0$, nên có thể chọn hàm riêng đồng thời, $T\chi=e^{2\pi iq}\chi$, với **giả điện tích** (quasicharge) $q\in[0,1)$:
$$
\chi_{m,q}(\varphi)=e^{iq\varphi}u_{m,q}(\varphi),\quad u_{m,q}(\varphi+2\pi)=u_{m,q}(\varphi),\quad H_0\chi_{m,q}=E_m(q)\chi_{m,q}.
$$
So với §3.2: $q\equiv-n_g\ (\mathrm{mod}\ 1)$ (dấu phụ thuộc quy ước; $E_m$ chẵn theo $n_g$ khi $U$ chẵn). Phổ của hệ tuần hoàn với điện tích lệch $n_g$ là các vùng Bloch $E_m(q)$ tính tại $q=n_g$. **Độ tán sắc điện tích** là độ rộng vùng:
$$
\epsilon_m=E_m(n_g=\tfrac12)-E_m(n_g=0).
$$

## 3.4 Độ rộng vùng từ biên độ xuyên hầm

Khi $E_J\gg E_C$ mỗi cực tiểu $\varphi_k=2\pi k$ giữ các trạng thái định xứ $|m,k\rangle$ (mức $m$ của dao động tử điều hòa trong giếng $k$). Xấp xỉ liên kết chặt với chỉ nhảy sang giếng lân cận (biên độ $-t_m$):
$$
E_m(n_g)=\bar E_m-2t_m\cos(2\pi n_g)\ \Longrightarrow\ \epsilon_m=E_m(\tfrac12)-E_m(0)=4t_m .
$$
(Dấu của $t_m$ thay đổi theo $m$ vì hàm sóng giếng thứ $m$ có $m$ nút; đây là nguồn của $(-1)^m$ trong công thức dưới.)

**Biên độ $t_m$ do xuyên hầm instanton.** Dưới rào, thế $U(\varphi)-U_{\min}=E_J(1-\cos\varphi)=2E_J\sin^2(\varphi/2)$. Hamiltonian $4E_C p^2+U$ có "khối lượng" $M$ sao cho $p^2/2M=4E_Cp^2$, tức $M=1/(8E_C)$ (ħ = 1, đơn vị năng lượng). Tác dụng WKB của một lần đi từ giếng 0 sang giếng $2\pi$ ở năng lượng đáy:
$$
S_0=\int_0^{2\pi}\!\sqrt{2M\,[U(\varphi)-U_{\min}]}\,d\varphi=\sqrt{\frac{E_J}{2E_C}}\int_0^{2\pi}\!\sin\frac\varphi2\,d\varphi=4\sqrt{\frac{E_J}{2E_C}}=\sqrt{\frac{8E_J}{E_C}} .
$$
Vậy $t_m\propto e^{-S_0}=e^{-\sqrt{8E_J/E_C}}$: độ tán sắc điện tích suy giảm **hàm mũ** theo $\sqrt{E_J/E_C}$. Tính chính xác các tiền thừa (xấp xỉ bán cổ điển cải tiến, Koch et al. 2007):
$$
\epsilon_m\simeq(-1)^mE_C\frac{2^{4m+5}}{m!}\sqrt{\frac2\pi}\Big(\frac{E_J}{2E_C}\Big)^{\frac m2+\frac34}e^{-\sqrt{8E_J/E_C}} .
$$

**Kiểm số** (chéo hoá trong cơ sở điện tích, `hpq.transmon`, đơn vị $E_C=1$):

| $E_J/E_C$ | $\epsilon_0$ (số) | $\epsilon_0$ (công thức) | $\epsilon_1$ (số) | $\epsilon_1$ (công thức) | $\epsilon_2$ (số) | $\epsilon_2$ (công thức) |
|---|---|---|---|---|---|---|
| 20 | $4{,}27\!\times\!10^{-4}$ | $4{,}61\!\times\!10^{-4}$ | $-1{,}70\!\times\!10^{-2}$ | $-2{,}33\!\times\!10^{-2}$ | $0{,}269$ | $0{,}590$ |
| 50 | $5{,}62\!\times\!10^{-7}$ | $5{,}88\!\times\!10^{-7}$ | $-3{,}91\!\times\!10^{-5}$ | $-4{,}71\!\times\!10^{-5}$ | $1{,}22\!\times\!10^{-3}$ | $1{,}88\!\times\!10^{-3}$ |
| 100 | $2{,}41\!\times\!10^{-10}$ | $2{,}50\!\times\!10^{-10}$ | $-2{,}49\!\times\!10^{-8}$ | $-2{,}83\!\times\!10^{-8}$ | $1{,}20\!\times\!10^{-6}$ | $1{,}60\!\times\!10^{-6}$ |

Đọc bảng: với $m=0$ công thức đúng trong 4% (từ $E_J/E_C=50$). Với $m\ge1$ khai triển chỉ là hướng dẫn về bậc độ lớn (sai 15–120% ở các giá trị này), vì sai số tương đối của khai triển tăng theo $m$; dấu $(-1)^m$ luôn đúng.

## 3.5 Phương trình Mathieu (nghiệm chính xác)

Với $U=-E_J\cos\varphi$, đặt $\varphi=2x$: $-4E_C\partial_\varphi^2=-E_C\partial_x^2$, nên
$$
\chi''(x)+\Big(\frac{E}{E_C}+\frac{E_J}{E_C}\cos2x\Big)\chi=0,
$$
dạng chuẩn Mathieu $y''+(a-2q\cos2x)y=0$ với $a=E/E_C$, $q=-E_J/2E_C$. Điều kiện biên $\chi(x+\pi)=e^{-2\pi in_g}\chi(x)$ chọn các số đặc trưng $a_{\nu}$ với chỉ số không nguyên $\nu$ phụ thuộc $n_g$. Việc gán $m\leftrightarrow\nu$ có cấu trúc phức tạp (phụ thuộc cách vùng nối nhau), nên trong thực hành **chéo hoá ma trận tridiagonal** trong cơ sở điện tích (như `hpq.transmon.levels`) tin cậy hơn dùng hàm Mathieu; phép kiểm hai chiều trên với công thức tiệm cận là đủ.

## 3.6 Hai lưu ý

- **Siêu điện cảm không lý tưởng.** Siêu điện cảm bằng chuỗi mối nối có phase slip trong chuỗi nên điều kiện biên "mở rộng" chỉ đúng gần đúng, để lại độ nhạy $n_g$ nhỏ nhưng khác 0.
- **$E_J\cos(M\varphi)$ với $M\ge2$.** Phần tử này chỉ nối các trạng thái $|n\rangle\to|n\pm M\rangle$, nên không gian tách thành $M$ lớp đồng dư $n\bmod M$. Với $M=2$ đây là chẵn lẻ số cặp (Chương 12).

## Bài tập

1. Chứng minh trực tiếp từ $\psi(\varphi+2\pi)=\psi(\varphi)$ rằng $\hat n$ chỉ nhận giá trị nguyên và $\hat\varphi$ không phải toán tử hợp lệ trên $L^2(S^1)$.
2. Tính $S_0$ cho thế $-E_J\cos2\varphi$ (chu kỳ $\pi$) và so với $\cos\varphi$; kết luận về độ nhạy $n_g$ của phần tử cos2φ.
3. Dùng `hpq.transmon.charge_dispersion` kiểm $\epsilon_0(E_J/E_C)$ có đường thẳng trong đồ thị $\ln\epsilon_0$ theo $\sqrt{E_J/E_C}$ với độ dốc $-\sqrt8$.
