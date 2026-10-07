# B1. BdG, phản xạ Andreev, hiệu ứng lân cận

## 1. Phát biểu

Hamiltonian trường trung bình với cặp s-wave, trong cơ sở Nambu $\Psi=(\psi_\uparrow,\psi_\downarrow,\psi_\downarrow^\dagger,-\psi_\uparrow^\dagger)^\top$:
$$
H_{BdG}=\begin{pmatrix} h(\mathbf r) & \Delta(\mathbf r)\\ \Delta^*(\mathbf r) & -\sigma_y h^*(\mathbf r)\sigma_y\end{pmatrix},\qquad
h=\frac{\mathbf p^2}{2m^*}-\mu+V(\mathbf r)+\alpha_R(\sigma_xp_y-\sigma_yp_x)+\tfrac12 g\mu_B\mathbf B\cdot\boldsymbol\sigma .
$$
Đối xứng hạt–lỗ $\mathcal P=\tau_y\sigma_y\mathcal K$: $\{\mathcal P,H\}=0$ → phổ đối xứng $E\leftrightarrow-E$. Mọi nghiệm đến theo cặp; năng lượng trạng thái cơ bản là $E_{GS}=-\tfrac12\sum_{E_n>0}E_n+\text{const}$ (ở $T=0$).

Với cơ sở Nambu 4 thành phần như trên, khi không có SOC và $\mathbf B$, khối spin tách và có thể làm việc với BdG 2×2 (bỏ thừa số suy biến spin 2).

## 2. Phản xạ Andreev

Tại mặt N|S lý tưởng (cùng $\mu$, không rào), electron năng lượng $0<E<\Delta$ phản xạ thành lỗ với biên độ
$$r_{he}=e^{-i\arccos(E/\Delta)}\,e^{-i\phi_S},\qquad r_{eh}=e^{-i\arccos(E/\Delta)}\,e^{+i\phi_S}.$$
Hai pha cần nhớ: $-\arccos(E/\Delta)$ (độ trễ thâm nhập, $=-\pi/2$ tại $E=0$) và $\mp\phi_S$ (pha vĩ mô). Mô hình BTK thêm rào $Z$ → cạnh tranh phản xạ thường/Andreev.

## 3. Hiệu ứng lân cận và khe cảm ứng

- Ghép yếu (tunnel) Sm–S với tốc độ $\gamma$: tự năng lượng của S tích phân ra $\Sigma(\omega)=-\gamma\frac{\omega+\Delta\tau_x}{\sqrt{\Delta^2-\omega^2}}$ → khe cảm ứng $\Delta^*\approx\gamma\Delta/(\gamma+\Delta)$.
- Ghép mạnh (Al epitaxy trên InAs nông): **metallization** — $g^*$, $\alpha_R$, $m^*$ hiệu dụng bị tái chuẩn hoá bởi trọng số sóng trong Al; $\mu$ của Sm bị kéo bởi chênh lệch công thoát (band bending). Điều này ảnh hưởng trực tiếp tới $\tau_i(V_g)$ của ND1.
- **Khe cứng** (hard gap): DOS dưới khe $\lesssim10^{-2}$ so với trạng thái thường; đo bằng phổ tunnel. Khe mềm → kênh tiêu tán + ngộ độc QP.

## 4. Giả thiết & miền hiệu lực

- Trường trung bình, $\Delta$ không tự hợp (self-consistency bỏ qua trong Sm) — tốt cho Sm vì không có tương tác hút nội tại.
- Mô hình Al dày như bể với $\Delta$ cố định: kém khi Al mỏng (≈ 5–10 nm), cần mô tả Al tường minh trong tight-binding hoặc mô hình hai lớp.

## 5. Bẫy

- Hai quy ước Nambu (có/không $-\psi_\uparrow^\dagger$) đổi dấu của $\Delta$ trong khối ngoài đường chéo và dạng của $\mathcal P$.
- Đếm đôi trạng thái: tổng trên mọi trị riêng BdG dương đã bao gồm spin khi dùng 4×4; khi dùng 2×2 phải nhân 2.

## 6. Tự kiểm tra

1. Giải BdG 1D N|S cho biên độ $r_{he}(E)$; kiểm $|r_{he}|=1$ với $E<\Delta$, $Z=0$.
2. Dẫn xuất khe cảm ứng từ tự năng lượng; tìm giới hạn $\gamma\gg\Delta$.

## 7. Đọc

1. de Gennes, *Superconductivity of Metals and Alloys*, ch. 5. ★ L2
2. Beenakker 1997 RMP 69, 731 "Random-matrix theory of quantum transport" §VI (Andreev). L2
3. Blonder, Tinkham, Klapwijk 1982 PRB 25, 4515. L2
4. Stanescu & Das Sarma 2017; Reeg, Loss, Klinovaja 2018 PRB 97, 165425 (metallization). ★ L2
5. Antipov et al. 2018 PRX 8, 031041 "Effects of gate-induced electric fields on semiconductor Majorana nanowires" (band bending + SOC từ tính toán Schrödinger–Poisson). L2
6. Kjaergaard et al. 2016 Nat. Commun. 7, 12841 (khe cứng 2DEG). L1
