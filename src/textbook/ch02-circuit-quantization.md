# Chương 2. Lượng tử hoá mạch

Mục tiêu: từ một sơ đồ mạch viết ra $\hat H$ có kiểm soát, và biết khi nào quy trình hỏng. Từ thông phụ thuộc thời gian: xem [A3](../a-circuit/a3-time-dependent-flux.md).

## 2.1 Biến động lực học

Mạch là đồ thị: **nút** $i=0,1,\dots,N$ (nút 0 là đất), **nhánh** $b$ nối hai nút. Mỗi nhánh có
- điện áp $V_b(t)$ và từ thông nhánh $\Phi_b(t)=\int_{-\infty}^tV_b\,dt'$,
- dòng $I_b(t)$ và điện tích nhánh $Q_b=\int I_b\,dt'$.

Chọn **từ thông nút** $\Phi_i$ ($i=1..N$) làm tọa độ suy rộng, $\Phi_0\equiv0$. Với nhánh nối $i\to j$ không có từ thông ngoài: $\Phi_b=\Phi_i-\Phi_j$. Khi đó định luật Kirchhoff điện áp (KVL) được thoả **tự động** (tổng $\Phi_b$ quanh mọi vòng bằng 0), và định luật Kirchhoff dòng (KCL) tại nút $i$ chính là phương trình Euler–Lagrange của $\Phi_i$.

## 2.2 Lagrangian

Động năng chỉ do tụ; thế năng do điện cảm và mối nối:
$$
\mathcal L=\underbrace{\sum_{b\in\mathrm C}\tfrac12C_b\dot\Phi_b^2}_{T}-\underbrace{\sum_{b\in\mathrm L}\frac{\Phi_b^2}{2L_b}-\sum_{b\in\mathrm{JJ}}\big[-E_{J,b}\cos(2\pi\Phi_b/\Phi_0)\big]}_{U}.
$$
Vì $\Phi_b$ tuyến tính theo $\Phi_i$: $T=\tfrac12\dot{\boldsymbol\Phi}^{\!\top}\mathbf C\,\dot{\boldsymbol\Phi}$, với **ma trận điện dung nút**
$$
C_{ii}=\sum_{b\ni i}C_b,\qquad C_{ij}=-C_{ij}^{(b)}\ (i\ne j).
$$
(Laplacian có trọng số của đồ thị con tụ; hàng/cột của nút đất đã bị bỏ, nên $\mathbf C$ khả nghịch khi mọi nút có đường tụ tới đất.)

Kiểm: chuyển động tại nút $i$ cho $\frac{d}{dt}\partial_{\dot\Phi_i}\mathcal L=\partial_{\Phi_i}\mathcal L$ ⇔ $\sum_b C_b\ddot\Phi_b+\sum_{b\in\mathrm L}\Phi_b/L_b+\sum_{b\in\mathrm{JJ}}I_{c,b}\sin\varphi_b=0$: tổng dòng ra khỏi nút bằng 0. ✓.

## 2.3 Biến đổi Legendre và lượng tử hoá

Xung lượng liên hợp là điện tích nút:
$$
Q_i=\frac{\partial\mathcal L}{\partial\dot\Phi_i}=\sum_jC_{ij}\dot\Phi_j,\qquad
H=\tfrac12\mathbf Q^{\!\top}\mathbf C^{-1}\mathbf Q+U(\boldsymbol\Phi).
$$
Lượng tử hoá chính tắc: $[\hat\Phi_i,\hat Q_j]=i\hbar\delta_{ij}$. Trong biến không thứ nguyên $\varphi_i=2\pi\Phi_i/\Phi_0=2e\Phi_i/\hbar$ và $\hat n_i=\hat Q_i/2e$: $[\hat\varphi_i,\hat n_j]=i\delta_{ij}$, và
$$
H=\tfrac12(2e)^2\,\hat{\mathbf n}^{\!\top}\mathbf C^{-1}\hat{\mathbf n}+U,\qquad 
\text{một nút: }\ \frac{(2e)^2}{2C}\hat n^2=4E_C\hat n^2,\ \ E_C=\frac{e^2}{2C}.
$$

## 2.4 Hai ví dụ chuẩn

**Mạch LC.** $H=\frac{Q^2}{2C}+\frac{\Phi^2}{2L}$. Đặt $Z=\sqrt{L/C}$, $\omega=1/\sqrt{LC}$:
$$
\hat\Phi=\Phi_{zpf}(a+a^\dagger),\ \ \hat Q=-iQ_{zpf}(a-a^\dagger),\ \ \Phi_{zpf}=\sqrt{\tfrac{\hbar Z}{2}},\ \ Q_{zpf}=\sqrt{\tfrac{\hbar}{2Z}},\ \ H=\hbar\omega(a^\dagger a+\tfrac12).
$$
Dao động điểm không của pha: $\varphi_{zpf}=\frac{2e}{\hbar}\Phi_{zpf}=\sqrt{\frac{4\pi Z}{R_K}}$, $R_K=h/e^2\approx25{,}8\,\text{k}\Omega$. Trở kháng $Z\gtrsim R_K/4\pi\approx2\,\text{k}\Omega$ cho $\varphi_{zpf}\sim1$: phần tử là "siêu điện cảm" (pha dao động mạnh); $Z\ll R_K/4\pi$ cho $\varphi_{zpf}\ll1$ (pha định xứ, chế độ transmon).

**rf-SQUID.** Mối nối $E_J$ song song với điện cảm $L$ và tụ $C$; vòng có từ thông ngoài $\Phi_{ext}$. Gọi $\varphi$ là pha qua mối nối (và tụ). KVL quanh vòng: $\Phi_L=\Phi_{J}-\Phi_{ext}$, nên thế năng điện cảm là $\frac{E_L}{2}(\varphi-\varphi_{ext})^2$, $E_L=(\Phi_0/2\pi)^2/L$:
$$
H=4E_C\hat n^2-E_J\cos\hat\varphi+\frac{E_L}{2}(\hat\varphi-\varphi_{ext})^2 .
$$
Đây là dạng của fluxonium (Chương 5) và là điểm xuất phát của 0-π.

## 2.5 dc-SQUID: $E_J$ hiệu dụng

Hai mối nối song song, từ thông $\Phi$ qua vòng (điện cảm vòng bỏ qua), $\delta=2\pi\Phi/\Phi_0$:
$$
U=-E_1\cos\varphi-E_2\cos(\varphi-\delta)=-\mathrm{Re}\big[(E_1+E_2e^{-i\delta})e^{i\varphi}\big]
=-E_J^{\mathrm{eff}}\cos(\varphi-\varphi_0),
$$
$$
E_J^{\mathrm{eff}}=\big|E_1+E_2e^{-i\delta}\big|=(E_1+E_2)\sqrt{\cos^2\tfrac\delta2+d^2\sin^2\tfrac\delta2},\quad d=\frac{E_2-E_1}{E_1+E_2},
$$
dịch pha $\varphi_0=\arg(E_1+E_2e^{-i\delta})$. (Kiểm: $(E_1+E_2)^2\cos^2\frac\delta2+(E_2-E_1)^2\sin^2\frac\delta2=E_1^2+E_2^2+2E_1E_2\cos\delta$ ✓.) Với $d\ne0$, $E_J^{\mathrm{eff}}$ không bao giờ bằng 0: điều này quyết định độ sâu điều chỉnh của transmon điều chỉnh bằng từ thông, và là gốc của số hạng phá đối xứng $d_1$ trong Chương 10.

## 2.6 Khi $\mathbf C$ suy biến

Nếu nút $i$ không có tụ nào (chỉ nối bằng điện cảm hoặc mối nối), hàng $i$ của $\mathbf C$ bằng 0. Biến $\Phi_i$ không có động năng; phương trình Euler–Lagrange của nó là ràng buộc $\partial U/\partial\Phi_i=0$ (KCL không có số hạng tụ). Xử lý:
1. giải ràng buộc theo các biến còn lại, hoặc
2. thêm tụ ký sinh $C_p$ rồi lấy $C_p\to0$: nút trở thành mode tần số rất cao, bị đóng băng ở đáy (xấp xỉ đoạn nhiệt).

Hai mối nối nối tiếp không tụ ở nút giữa là ví dụ: nút giữa chỉ nhận một giá trị làm cực tiểu $E_1\cos\varphi_1+E_2\cos\varphi_2$ với $\varphi_1+\varphi_2=\varphi$ cố định.

## 2.7 Điều kiện hiệu lực

- **Mô hình tập trung:** kích thước mạch ≪ bước sóng ở tần số liên quan. Siêu điện cảm chế tạo bằng chuỗi mối nối có mode riêng (cộng hưởng chuỗi) có thể rơi vào dải tần của qubit.
- **Không có tiêu tán:** bể nhiệt thêm vào ở Chương 11.
- **Mối nối chỉ là $-E_J\cos\varphi$:** nếu không, thay bằng $U_J(\varphi)$ tổng quát, quy trình giữ nguyên (đây là cách đưa mối nối bán dẫn vào).

## Bài tập

1. Lượng tử hoá mạch gồm hai tụ $C_1,C_2$ nối tiếp, nút giữa nối với mối nối $E_J$ xuống đất. Viết $\mathbf C$, $\mathbf C^{-1}$ và $H$.
2. Chứng minh tần số plasma của mối nối có tụ $C$ là $\omega_p=\sqrt{8E_JE_C}/\hbar$ và so sánh với $\omega=1/\sqrt{L_J(0)C}$.
3. Với dc-SQUID $d=0{,}1$, tìm tỉ số $E_J^{\mathrm{eff}}(\Phi_0/2)/E_J^{\mathrm{eff}}(0)$.
