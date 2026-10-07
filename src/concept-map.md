# Bản đồ khái niệm

Mũi tên $X \to Y$: cần nắm $X$ trước khi học $Y$. Nút đậm viền là lõi của luận án.

```mermaid
flowchart TD
  BCS[BCS, khe Δ] --> JJ[Hiệu ứng Josephson]
  BCS --> BdG[Phương trình BdG]
  BdG --> AR[Phản xạ Andreev]
  AR --> ABS[Trạng thái liên kết Andreev]
  SM[Ma trận tán xạ Landauer] --> ABS
  ABS --> CPR[Quan hệ dòng–pha phi sin]
  CPR --> HARM[Điều hòa E_J,M]
  RASHBA[SOC Rashba, Zeeman] --> PHI0[φ0-junction]
  ABS --> PHI0
  LEN[Mối nối dài, L/ξ] --> CPR
  MULTI[Phân bố τ nhiều kênh] --> HARM

  CQ[Lượng tử hoá mạch] --> COMP[Biến tuần hoàn vs mở rộng]
  CQ --> FLUX[Từ thông ngoài, gauge]
  JJ --> CQ
  COMP --> TR[Transmon]
  COMP --> FX[Fluxonium]
  TR --> GM[Gatemon]
  CPR --> GM

  TR --> PROT[Nguyên lý bảo vệ]
  FX --> PROT
  PROT --> ZP[0-π]:::core
  PROT --> C2[cos2φ]:::core
  HARM --> C2
  HARM --> ZPH[0-π lai]:::core
  ZP --> ZPH
  GM --> ZPH
  ZP --> ZETA[Mode ζ, rối loạn]:::core
  PHI0 --> ZPH

  NOISE[Mật độ phổ, quy tắc vàng] --> CH[Kênh nhiễu]
  CQED[cQED, tán sắc] --> SHOT[Nhiễu bắn photon]
  SHOT --> CH
  ZETA --> CH
  CH --> BUD[Ngân sách mất kết hợp]:::core
  ZPH --> BUD

  BUD --> GATE[Cổng chuyển mức bảo vệ]
  GATE --> QEC[Chi phí QEC]
  classDef core stroke-width:3px
```

## Ba câu hỏi xuyên suốt

1. **Đối xứng nào, của biến nào?** — 0-π: phản xạ $\varphi\to-\varphi$, tịnh tiến $\theta\to\theta+2\pi$ (Bloch), hoán vị hai nhánh. cos2φ: chẵn lẻ $e^{i\pi\hat n}$.
2. **Tham số nào phá đối xứng, tham số đó có điều khiển được không?** — $dE_J$ (cổng: có), $dE_L$, $dC$, $dC_J$ (cổng: không), $\varphi_0$ (cổng + $B$: có, nhưng là nguồn phá mới).
3. **Kênh nhiễu nào thấy phần phá vỡ đó?** — xem [D2](d-noise/d2-channels.md), [DV3](derivations/dv3-zeta-coupling.md).
