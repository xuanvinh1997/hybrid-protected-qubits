# Chương 1. Hiệu ứng Josephson

Phạm vi: chỉ những gì cần để dùng mối nối Josephson như một phần tử mạch. Mối nối bán dẫn (nhiều kênh, $\tau\to1$) là Chương 6–7; ở đây xét mối nối đường hầm $\tau\ll1$.

## 1.1 Pha và số cặp là một cặp biến liên hợp

Trạng thái ngưng tụ BCS của một điện cực siêu dẫn có tham số trật tự $\Delta e^{i\varphi}$. Hàm sóng BCS với pha $\varphi$:
$$
|\varphi\rangle=\prod_{\mathbf k}\big(u_{\mathbf k}+v_{\mathbf k}\,e^{i\varphi}\,c^\dagger_{\mathbf k\uparrow}c^\dagger_{-\mathbf k\downarrow}\big)|0\rangle .
$$
Khai triển theo số cặp $N$ (số hạt chẵn $2N$): $|\varphi\rangle=\sum_N a_N e^{iN\varphi}|N\rangle$ với $|N\rangle$ là trạng thái có đúng $N$ cặp. Do đó $|\varphi\rangle$ là hàm riêng của dịch pha theo biến liên hợp $\hat N$:
$$
e^{-i\alpha\hat N}|\varphi\rangle=|\varphi-\alpha\rangle,\qquad \hat N=-i\,\partial_\varphi \ \text{trong biểu diễn pha},\qquad [\hat\varphi,\hat N]=i .
$$
Đây là hệ thức bất định cơ bản của siêu dẫn: pha xác định ⇒ số cặp hoàn toàn bất định, và ngược lại. Với hai điện cực, biến vật lý là **hiệu pha** $\varphi=\varphi_R-\varphi_L$ và **số cặp đã chuyển** $\hat n$ từ trái sang phải, $[\hat\varphi,\hat n]=i$.

Lưu ý quan trọng cho Chương 3: $\hat n$ có phổ nguyên chỉ khi trạng thái của đảo là trạng thái số cặp. Điều này không tự động đúng; nó là một giả thiết về không gian Hilbert.

## 1.2 Năng lượng Josephson từ lý thuyết nhiễu loạn bậc hai

Hamiltonian xuyên hầm giữa hai điện cực (đảo L và R, cùng $\Delta$, hiệu pha $\varphi$):
$$
H_T=\sum_{\mathbf k\mathbf q\sigma}\big(t_{\mathbf k\mathbf q}\,c^\dagger_{\mathbf k\sigma}d_{\mathbf q\sigma}+\text{h.c.}\big),\qquad t_{\mathbf k\mathbf q}\to t\ \text{(không phụ thuộc }\mathbf k,\mathbf q).
$$
Ở bậc nhất $\langle H_T\rangle=0$ (nó đổi số hạt mỗi bên lẻ). Ở bậc hai, trạng thái trung gian là hai quasiparticle $\gamma^\dagger_{\mathbf k}\gamma^\dagger_{\mathbf q}|\text{BCS}\rangle$ với năng lượng kích thích $E_{\mathbf k}+E_{\mathbf q}$, $E_{\mathbf k}=\sqrt{\xi_{\mathbf k}^2+\Delta^2}$. Biên độ chuyển lên trạng thái đó có hai đóng góp (chuyển electron, hoặc chuyển "lỗ"):
$$
A\propto t\,\big(u_{\mathbf k}v_{\mathbf q}\,e^{i\varphi_R}-v_{\mathbf k}u_{\mathbf q}\,e^{i\varphi_L}\big)\ \Rightarrow\ |A|^2\propto |t|^2\big[u_k^2v_q^2+v_k^2u_q^2-2u_kv_ku_qv_q\cos\varphi\big].
$$
Chỉ số hạng giao thoa phụ thuộc $\varphi$. Với $u_kv_k=\Delta/2E_k$, cộng spin, và chuyển tổng thành tích phân với mật độ trạng thái $\rho_L,\rho_R$ ở mức Fermi:
$$
E(\varphi)=\text{const}-E_J\cos\varphi,\qquad
E_J=|t|^2\rho_L\rho_R\int_{-\infty}^{\infty}\!\!d\xi\int_{-\infty}^{\infty}\!\!d\xi'\;\frac{\Delta^2}{E\,E'\,(E+E')} .
$$
Đặt $\xi=\Delta\sinh x$ thì $d\xi/E=dx$ và tích phân trở thành
$$
\Delta\iint\frac{dx\,dx'}{\cosh x+\cosh x'}=\Delta\int_{-\infty}^{\infty}\frac{2x'}{\sinh x'}dx'=\pi^2\Delta
\quad\Big(\textstyle\int_{-\infty}^{\infty}\frac{x}{\sinh x}dx=\frac{\pi^2}{2}\Big).
$$
(Kiểm số: `dblquad` cho $9{,}8696044=\pi^2$ đến 9 chữ số.) Vậy
$$
\boxed{E_J=\pi^2\Delta\,\rho_L\rho_R|t|^2 .}
$$

**Đối chiếu với điện dẫn thường.** Điện dẫn trạng thái thường của cùng mối nối (có spin) là $G_N=\frac{4\pi e^2}{\hbar}\rho_L\rho_R|t|^2$. Suy ra $\rho_L\rho_R|t|^2=\hbar G_N/4\pi e^2$ và
$$
E_J=\frac{\pi\hbar\Delta}{4e^2R_N}=\frac{\Delta}{8}\frac{R_K}{R_N},\qquad R_K=\frac{h}{e^2},
$$
tức hệ thức **Ambegaokar–Baratoff** $I_cR_N=\pi\Delta/2e$ (dùng $E_J=\hbar I_c/2e$, §1.3). Phép đếm spin ở trên được kiểm bởi sự khớp này; nếu thiếu thừa số 2 từ spin, kết quả lệch $2\times$.

Hệ quả thực hành: $E_J$ của mối nối đường hầm chỉ do $R_N$ quyết định (điện trở đo được ở nhiệt độ phòng), vì vậy cố định sau khi chế tạo. Với Al, $\Delta\approx180\,\mu$eV, $R_N=10\,\text{k}\Omega$: $E_J\approx\frac{180}{8}\cdot\frac{25{,}8}{10}\ \mu\text{eV}=58\ \mu\text{eV}\approx14{,}0$ GHz.

## 1.3 Hai hệ thức Josephson

**Dòng.** Trong biểu diễn pha $\hat n=-i\partial_\varphi$, nên với $H_J=-E_J\cos\varphi$: $[\hat n,f(\varphi)]=-if'(\varphi)$. Tốc độ thay đổi số cặp trên đảo:
$$
\dot{\hat n}=\frac1{i\hbar}[\hat n,H]=-\frac1\hbar\frac{\partial H}{\partial\varphi},
\qquad
I=-2e\,\dot n\ \Rightarrow\ I=\frac{2e}{\hbar}\frac{\partial H_J}{\partial\varphi}=I_c\sin\varphi,\quad I_c=\frac{2e}{\hbar}E_J .
$$
(Dấu theo quy ước dòng từ trái sang phải.) Ở trạng thái riêng, $\langle I\rangle=\frac{2e}{\hbar}\frac{dE}{d\varphi}$ theo định lý Hellmann–Feynman; đây là dạng tổng quát cho mọi quan hệ dòng–pha (Chương 7).

**Điện áp.** Thêm năng lượng tích điện của hai bản tụ: $H_C=\frac{(2e)^2\hat n^2}{2C}$. Phương trình Heisenberg cho pha:
$$
\dot\varphi=\frac1{i\hbar}[\hat\varphi,H]=\frac1\hbar\frac{\partial H}{\partial n}=\frac{(2e)^2n}{\hbar C}=\frac{2eV}{\hbar},
\qquad V=\frac{2en}{C}.
$$
Hai hệ thức độc lập về mặt lý thuyết: một cái là hệ quả của $E(\varphi)$, cái kia là hệ quả của việc $\varphi$ liên hợp với điện tích.

## 1.4 Điện cảm phi tuyến

Từ $V=\frac\hbar{2e}\dot\varphi$ và $\dot I=I_c\cos\varphi\,\dot\varphi$:
$$
V=L_J\dot I,\qquad L_J(\varphi)=\frac{\hbar}{2eI_c\cos\varphi}=\frac{\Phi_0}{2\pi I_c\cos\varphi}=\frac{(\Phi_0/2\pi)^2}{E_J\cos\varphi}.
$$
Gần $\varphi=0$: $E_J\cos\varphi\approx E_J-\tfrac12E_J\varphi^2+\tfrac1{24}E_J\varphi^4$. Số hạng bậc hai là điện cảm tuyến tính $L_J(0)$ (cho mạch LC đều bậc), số hạng bậc bốn là **độ phi tuyến duy nhất cần có** để phổ không cách đều. Một mạch LC thuần tuý có mọi mức cách đều $\hbar\omega$ nên không thể chọn riêng hai mức; mọi thiết kế qubit chỉ là cách tổ chức phần phi tuyến này.

## 1.5 Phạm vi hiệu lực

| Giả thiết | Điều kiện | Khi vi phạm |
|---|---|---|
| Bậc hai theo $H_T$ | $\tau\ll1$ (mọi kênh) | $E(\varphi)$ có điều hòa bậc cao, Chương 7 |
| Quasiparticle không ảnh hưởng | $k_BT,\hbar\omega\ll\Delta$ | tiêu tán, ngộ độc |
| Hai điện cực là khối | kích thước ≫ $\xi$ | hiệu ứng kích thước |
| $E(\varphi)$ ở trạng thái cơ bản | $\hbar\omega_p\ll$ khe Andreev | mức Andreev kích thích (Chương 7) |

## Bài tập

1. Chứng minh $\int_{-\infty}^{\infty}\frac{dx}{\cosh x+\cosh x'}=\frac{2x'}{\sinh x'}$ (gợi ý: $\cosh x+\cosh x'=2\cosh\frac{x+x'}2\cosh\frac{x-x'}2$ và đổi biến).
2. Tính $E_J/h$ (GHz) và $I_c$ (nA) của mối nối Al/AlOx có $R_N=5\,\text{k}\Omega$.
3. Với $H=\frac{(2e)^2}{2C}\hat n^2-E_J\cos\hat\varphi$, viết phương trình chuyển động cổ điển cho $\varphi(t)$ và nhận dạng con lắc; tìm tần số plasma $\omega_p=\sqrt{8E_JE_C}/\hbar$.
