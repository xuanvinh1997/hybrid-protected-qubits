# Chương 4. Transmon

## 4.1 Hamiltonian và chế độ làm việc

$$
\hat H=4E_C(\hat n-n_g)^2-E_J\cos\hat\varphi,\qquad E_C=\frac{e^2}{2C_\Sigma},\quad \frac{E_J}{E_C}\sim50\text{–}100,
$$
với $C_\Sigma$ gồm tụ shunt và tụ ký sinh của mối nối. $\varphi$ tuần hoàn (Chương 3).

## 4.2 Khai triển quanh đáy giếng: $\omega_{01}$ và $\alpha$

Khi $E_J/E_C\gg1$, pha dao động nhỏ quanh 0. Khai triển $\cos\varphi=1-\frac{\varphi^2}2+\frac{\varphi^4}{24}-\cdots$:
$$
\hat H\simeq4E_C\hat n^2+\frac{E_J}2\hat\varphi^2-\frac{E_J}{24}\hat\varphi^4 .
$$
Phần bậc hai là dao động tử điều hòa với tần số $\hbar\omega_p=\sqrt{8E_JE_C}$ (khối lượng $1/8E_C$, độ cứng $E_J$). Toán tử thang:
$$
\hat\varphi=\Big(\frac{2E_C}{E_J}\Big)^{1/4}(b+b^\dagger),\qquad
\hat n=\frac i2\Big(\frac{E_J}{2E_C}\Big)^{1/4}(b^\dagger-b).
$$
Kiểm: hệ số của $\hat\varphi$ và $\hat n$ có tích $a\cdot\frac1{2a}=\frac12$, nên $[\hat\varphi,\hat n]=\frac i2\,[b+b^\dagger,\,b^\dagger-b]=\frac i2(1+1)=i$ ✓. Số hạng bậc bốn:
$$
-\frac{E_J}{24}\hat\varphi^4=-\frac{E_J}{24}\cdot\frac{2E_C}{E_J}(b+b^\dagger)^4=-\frac{E_C}{12}(b+b^\dagger)^4 .
$$
Nhiễu loạn bậc nhất theo $\langle m|(b+b^\dagger)^4|m\rangle=6m^2+6m+3$:
$$
E_m\simeq-E_J+\sqrt{8E_JE_C}\Big(m+\tfrac12\Big)-\frac{E_C}{12}(6m^2+6m+3)=-E_J+\sqrt{8E_JE_C}\Big(m+\tfrac12\Big)-\frac{E_C}{2}\Big(m^2+m+\tfrac12\Big).
$$
Từ đó
$$
\hbar\omega_{01}=E_1-E_0\simeq\sqrt{8E_JE_C}-E_C,\qquad
\alpha=\hbar(\omega_{12}-\omega_{01})=E_2-2E_1+E_0\simeq-E_C .
$$
**Kiểm số** (`hpq.transmon`, $E_C=1$): $\omega_{01}=11{,}555,\ 18{,}942,\ 27{,}245$ so với công thức $11{,}649,\ 19{,}000,\ 27{,}284$ ở $E_J/E_C=20,50,100$ (sai 0,8%, 0,3%, 0,14%); $\alpha=-1{,}455,\ -1{,}149,\ -1{,}096$ ($-E_C$ trừ hiệu chỉnh bậc cao cỡ $\sqrt{E_C/E_J}$). Bất điều hòa tương đối:
$$
\frac{|\alpha|}{\hbar\omega_{01}}\simeq\sqrt{\frac{E_C}{8E_J}}\ \ (\approx5\%\ \text{ở }E_J/E_C=50).
$$

## 4.3 Vì sao độ nhạy điện tích triệt tiêu, còn bất điều hòa thì không

- **Độ tán sắc điện tích** $\propto e^{-\sqrt{8E_J/E_C}}$ (Chương 3): giảm hàm mũ khi tăng $E_J/E_C$.
- **Bất điều hòa** $|\alpha|\simeq E_C\propto E_J^{-1}$ ở $\omega_p$ cố định: giảm theo hàm lũy thừa (cụ thể $|\alpha|/\omega_{01}\propto(E_J/E_C)^{-1/2}$).

Do đó tồn tại khoảng $E_J/E_C\sim50$–100 mà độ tán sắc điện tích dưới kHz trong khi $|\alpha|$ vẫn đủ lớn (cỡ 5%) để điều khiển chọn lọc chuyển dời 0–1 bằng xung vi sóng ngắn cỡ 10 ns, không rò sang mức 2. Đây là toàn bộ nội dung của "bảo vệ điện tích" của transmon: bảo vệ **mất pha** (tần số phẳng theo $n_g$), không phải bảo vệ hồi phục.

## 4.4 Phần tử ma trận và $T_1$

Từ biểu thức của $\hat n$:
$$
\langle m+1|\hat n|m\rangle=-\frac i2\Big(\frac{E_J}{2E_C}\Big)^{1/4}\sqrt{m+1},\qquad
|\langle1|\hat n|0\rangle|=\frac12\Big(\frac{E_J}{2E_C}\Big)^{1/4}.
$$
Ở $E_J/E_C=50$: $|\langle1|\hat n|0\rangle|\approx1{,}12$, bậc đơn vị. Quy tắc vàng cho hồi phục (Chương 11) cho $\Gamma_1\propto|\langle1|\hat n|0\rangle|^2S_V(\omega_{01})$ không có hệ số triệt tiêu, nên $T_1$ của transmon bị giới hạn trực tiếp bởi tổn hao điện môi của tụ. Điều kiện (R) của Chương 8 **không** thoả: đây chính là động cơ của các thiết kế bảo vệ.

Quy tắc chọn lọc: $\hat n$ là toán tử lẻ theo $b$, nên chỉ nối $m\leftrightarrow m\pm1$ ở bậc thấp nhất; chuyển dời $m\to m\pm2$ chỉ qua số hạng phi tuyến, cỡ $(E_C/E_J)^{1/2}$ nhỏ hơn.

## 4.5 Transmon điều chỉnh bằng từ thông

Thay mối nối bằng dc-SQUID (§2.5): $E_J\to E_J^{\mathrm{eff}}(\Phi)=E_{J\Sigma}\sqrt{\cos^2\frac\delta2+d^2\sin^2\frac\delta2}$, nên
$$
\hbar\omega_{01}(\Phi)\simeq\sqrt{8E_{J\Sigma}E_C}\,\big[\cos^2\tfrac\delta2+d^2\sin^2\tfrac\delta2\big]^{1/4}-E_C .
$$
Độ nhạy với từ thông bằng 0 tại $\Phi=0$ và $\Phi_0/2$ (điểm tối ưu); độ cong tại đó tỉ lệ $E_J^{\mathrm{eff}}{}''$. Nhiễu từ thông $1/f$ ($A_\Phi\sim1\,\mu\Phi_0$) gây mất pha bậc hai tại điểm tối ưu (Chương 11).

## 4.6 Giới hạn của mô hình

| Giả thiết | Điều kiện | Ghi chú |
|---|---|---|
| $\cos\varphi$ thuần | $\tau\ll1$ | mối nối bán dẫn: $E_J\to U(\varphi)$ tổng quát (gatemon, Chương 7) |
| Nhiễu loạn bậc nhất | $E_C\ll\sqrt{8E_JE_C}$ | bậc hai cho sai số $O(E_C\sqrt{E_C/E_J})$ |
| Một mode | tụ shunt không có mode riêng thấp | kiểm bằng mô phỏng điện từ / EPR |

## Bài tập

1. Tính nhiễu loạn bậc hai cho $E_m$ (số hạng $\sim\sqrt{E_C^3/E_J}$) và kiểm với bảng số ở §4.2.
2. Với $E_J/h=15$ GHz, $E_C/h=0{,}3$ GHz tìm $\omega_{01}/2\pi$, $\alpha/2\pi$ và $|\langle1|\hat n|0\rangle|$.
3. Chứng minh $|\langle m+2|\hat n|m\rangle|=0$ ở bậc thấp nhất và tìm số hạng đầu tiên khác 0.
