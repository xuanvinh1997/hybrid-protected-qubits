# A1. Hình thức luận Lagrange–Hamilton cho mạch

## 1. Phát biểu

Cho đồ thị mạch với tập nút $\mathcal N$ (một nút đất) và tập nhánh $\mathcal B$. Biến từ thông nút
$\Phi_j(t)=\int_{-\infty}^t V_j(t')\,dt'$, pha rút gọn $\varphi_j = 2\pi\Phi_j/\Phi_0$, $\Phi_0=h/2e$.

$$
\mathcal L(\boldsymbol\Phi,\dot{\boldsymbol\Phi}) = \tfrac12\dot{\boldsymbol\Phi}^{\!\top}\mathbf C\,\dot{\boldsymbol\Phi}
 - \sum_{b\in\text{L}}\frac{(\Phi_b)^2}{2L_b} - \sum_{b\in\text{JJ}} U_b(\varphi_b),
$$

với $\mathbf C$ là ma trận điện dung nút (Laplacian có trọng số của đồ thị con điện dung), $\Phi_b$ từ thông nhánh.
Với mối nối đường hầm $U_b=-E_J\cos\varphi_b$; với mối nối bán dẫn $U_b$ là năng lượng trạng thái cơ bản của mối nối ([B4](../b-microscopic/b4-junction-to-circuit.md)).

Xung lượng liên hợp: $Q_j=\partial\mathcal L/\partial\dot\Phi_j$ (điện tích nút). Nếu $\mathbf C$ khả nghịch:

$$
H = \tfrac12 \mathbf Q^{\top}\mathbf C^{-1}\mathbf Q + U(\boldsymbol\Phi),\qquad
[\hat\Phi_j,\hat Q_k]=i\hbar\,\delta_{jk}\;\Leftrightarrow\;[\hat\varphi_j,\hat n_k]=i\,\delta_{jk},\; \hat n=\hat Q/2e .
$$

Dạng chuẩn: $4E_C\hat n^2$ với $E_C=e^2/2C$; $\tfrac{E_L}{2}\hat\varphi^2$ với $E_L=(\Phi_0/2\pi)^2/L$.

## 2. Ràng buộc fluxoid

Chọn cây khung $\mathcal T$. Nhánh ngoài cây (chord) $c$ đóng một vòng; từ thông nhánh của chord được cố định bởi
$$\sum_{b\in\text{loop}(c)}\pm\Phi_b = \Phi_{ext,c} \pmod{\Phi_0}.$$
Với $\Phi_{ext}$ tĩnh, việc gán $\Phi_{ext}$ vào nhánh nào chỉ là một phép biến đổi chính tắc. **Khi $\Phi_{ext}(t)$ thay đổi, lựa chọn này có hậu quả vật lý** → [A3](a3-time-dependent-flux.md).

## 3. Ma trận điện dung suy biến và mode thừa

Nếu một nút không có điện dung nào (chỉ nối điện cảm/mối nối), $\mathbf C$ suy biến: biến tương ứng không có động năng, phải khử bằng phương trình ràng buộc $\partial U/\partial\Phi_j=0$. Trong mạch 0-π 4 nút có một mode "thừa" không có thế (tổng tọa độ — chuyển động tịnh tiến toàn cục) bị loại.

## 4. Thực hành: lượng tử hoá 0-π (bài tập L3)

Bốn nút $1..4$; hai mối nối $1$–$3$ (A) và $2$–$4$ (B), hai điện cảm $1$–$2$, $3$–$4$, hai tụ chéo $1$–$4$, $2$–$3$.
Bài tập: tìm phép đổi biến tuyến tính $(\varphi_1..\varphi_4)\to(\theta,\varphi,\zeta,\Sigma)$ làm chéo hoá ma trận điện dung khi mạch đối xứng (tự suy, rồi đối chiếu Dempster 2014 §II và Groszkowski 2018 §2). Kết quả kiểm được: pha hai mối nối là $\theta\pm\varphi$ **đúng tuyệt đối**, độc lập với rối loạn — điều then chốt cho [DV3](../derivations/dv3-zeta-coupling.md).

## 5. Giả thiết & miền hiệu lực

- Mô hình tập trung: kích thước mạch ≪ bước sóng ở tần số liên quan; với siêu điện cảm dạng chuỗi JJ, mode tự cộng hưởng của chuỗi phải nằm xa (Masluk 2012; Viola–Catelani 2015).
- Bỏ qua quasiparticle: $k_BT, \hbar\omega \ll \Delta$.
- Mối nối mô tả bằng một biến pha duy nhất: hợp lệ khi các mức Andreev bám đoạn nhiệt theo pha ([B4](../b-microscopic/b4-junction-to-circuit.md)).

## 6. Bẫy

- Thừa số 2 trong $E_C$: một số tài liệu dùng $E_C=e^2/2C$ với $4E_C n^2$, số khác $E_C=(2e)^2/2C$ với $E_C n^2$.
- $E_L\varphi^2$ trong 0-π (hai điện cảm) vs $\tfrac{E_L}{2}\varphi^2$ (một điện cảm).
- Dấu của $\Phi_{ext}$ theo chiều duyệt vòng.

## 7. Tự kiểm tra

1. Lượng tử hoá dc-SQUID hai mối nối không đối xứng; chứng minh $E_J^{eff}(\Phi)=E_{J\Sigma}\sqrt{\cos^2(\pi\Phi/\Phi_0)+d^2\sin^2(\pi\Phi/\Phi_0)}$.
2. Tìm ma trận $\mathbf C^{-1}$ của 0-π khi có $dC$, $dC_J$; đọc ra các số hạng $\partial_\theta\partial_\zeta$, $\partial_\varphi\partial_\theta$.

## 8. Đọc theo thứ tự

1. Vool & Devoret 2017 (IJCTA) — §2–5. ★ L3
2. Rasmussen et al. 2021, *PRX Quantum* 2, 040204 "Superconducting circuit companion" — §II–IV. ★ L2
3. Devoret 1997 (Les Houches) — lịch sử, kinh điển. L2
4. Burkard, Koch, DiVincenzo 2004 PRB 69, 064503 — lượng tử hoá mạch có tiêu tán. L1
