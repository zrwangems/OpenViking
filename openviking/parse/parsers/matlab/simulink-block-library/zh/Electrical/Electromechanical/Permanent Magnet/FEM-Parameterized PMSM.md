---
type: simulink-block
title: 'FEM-Parameterized PMSM'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'femparameterizedpmsm'
documentation_source_path: 'ref/femparameterizedpmsm.html'
language: zh-CN
chinese_source: worker-translation
---

# FEM-Parameterized PMSM

## 端口
```yaml
ports:
- name: a
  summary: A 相连接 electrical
  direction: conserving
- name: b
  summary: B 相连接 electrical
  direction: conserving
- name: c
  summary: C 相连接 electrical
  direction: conserving
- name: a1
  summary: '*a* 正端连接 electrical'
  direction: conserving
- name: b1
  summary: '*b* 正端连接 electrical'
  direction: conserving
- name: c1
  summary: '*c* 正端连接 electrical'
  direction: conserving
- name: a2
  summary: '*a* 负端连接 electrical'
  direction: conserving
- name: b2
  summary: '*b* 负端连接 electrical'
  direction: conserving
- name: c2
  summary: '*c* 负端连接 electrical'
  direction: conserving
- name: n
  summary: 中性相 electrical
  direction: conserving
- name: C
  summary: 电机外壳 mechanical
  direction: conserving
- name: R
  summary: 电机转子 mechanical
  direction: conserving
- name: HA
  summary: 绕组 A 热端口 thermal
  direction: conserving
- name: HB
  summary: 绕组 B 热端口 thermal
  direction: conserving
- name: HC
  summary: 绕组 C 热端口 thermal
  direction: conserving
- name: HR
  summary: 转子热端口 thermal
  direction: conserving
```

### 守恒端口

### **a** — A 相连接 electrical

与 A 相连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Wye-wound` 或
`Delta-wound`。

### **b** — B 相连接 electrical

与 B 相连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Wye-wound` 或
`Delta-wound`。

### **c** — C 相连接 electrical

与 C 相连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Wye-wound` 或
`Delta-wound`。

### **a1** — *a* 正端连接 electrical

*自 R2024a 起*

与 *a* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **b1** — *b* 正端连接 electrical

*自 R2024a 起*

与 *b* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **c1** — *c* 正端连接 electrical

*自 R2024a 起*

与 *c* 正端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **a2** — *a* 负端连接 electrical

*自 R2024a 起*

与 *a* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **b2** — *b* 负端连接 electrical

*自 R2024a 起*

与 *b* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **c2** — *c* 负端连接 electrical

*自 R2024a 起*

与 *c* 负端连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为
`Open-end`。

### **n** — 中性相 electrical

与中性相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option**
参数设置为以下之一

- `2-D partial derivative data | No thermal
  port`、`2-D partial
  导数数据 | 显示热端口`、
  `3-D partial derivative data | No
  thermal port`、`3-D partial
  导数数据 | 显示热端口`、
  `4-D partial derivative data | No
  thermal port` 或 `4-D
  partial derivative data | Show thermal
  port`，并将 **Winding
  type** 参数设置为
  `Wye-wound`。
- `3-D flux linkage data | No thermal
  port` 或 `3-D flux linkage
  data | Show thermal port`，并将
  **Winding type** 参数设置为
  `Wye-wound`，将
  **Expose neutral port** 参数
  设置为 `Yes`。

### **C** — 电机外壳 mechanical

与电机外壳相关联的机械旋转守恒端口。

### **R** — 电机转子 mechanical

与电机转子相关联的机械旋转守恒端口。

### **HA** — 绕组 A 热端口 thermal

与绕组 A 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HB** — 绕组 B 热端口 thermal

与绕组 B 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HC** — 绕组 C 热端口 thermal

与绕组 C 相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HR** — 转子热端口 thermal

与转子相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 磁链和转矩参数化方法 2-D partial derivative data | No thermal port（默认）| 2-D partial derivative data | Show thermal port |
    3-D partial derivative data | No thermal port | 3-D partial derivative data | Show thermal port | 4-D partial derivative
    data | No thermal port | 4-D partial derivative data | Show thermal port | 3-D flux linkage data | No thermal port | 3-D
    flux linkage data | Show thermal port
  group: ''
- name: Parameterization
  summary: 参数化方法 Assume constant mutual inductance - tabulate 含相电流和转子角（默认）| 假设正弦反电动势 - 用 d 轴和 q-axis currents
  group: 电气（2-D 偏导数数据参数化）
- name: Winding type
  summary: 定子绕组配置 Wye-wound（默认）| Delta-wound | Open-end
  group: 电气（2-D 偏导数数据参数化）
- name: Current vector, i
  summary: 电流向量 [-2, 0, 2] A（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Rotor angle vector, theta
  summary: 转子角度向量 [0, 20, 40, 60] deg（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Flux linkage partial derivative wrt current, dPhi(i,theta)/di
  summary: 磁链对电流的偏导数 0.0002*ones(3,4) Wb/A（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Flux linkage partial derivative wrt angle, dPhi(i,theta)/dtheta
  summary: 磁链对角度的偏导数 [0, -0.16, 0.16, 0; 0, -0.16, 0.16, 0; 0, -0.16, 0.16, 0] Wb/rad（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Direct axis current vector, id
  summary: 直轴电流向量 [-200, 0, 200] A（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Quadrature axis current vector, iq
  summary: 交轴电流向量 [-200, 0, 200] A（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Ld matrix, Ld(id,iq)
  summary: Ld 矩阵 0.0002*ones(3,3) H（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Lq matrix, Lq(id,iq)
  summary: Lq 矩阵 0.0002*ones(3,3) H（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Permanent magnet flux linkage, PM(id,iq)
  summary: 永磁磁链 0.1*ones(3,3) Wb（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Number of pole pairs
  summary: 极对数 6（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Calculate torque matrix?
  summary: 电磁转矩数据指定方式 Yes（默认）| No — specify directly
  group: 电气（2-D 偏导数数据参数化）
- name: Torque matrix, T(i,theta)
  summary: 转矩矩阵 zeros(3, 3, 3, 4) N*m（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Interpolation method
  summary: 插值方法 Linear Smooth（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Stator resistance per phase, Rs
  summary: 每相定子电阻 0.013 Ohm（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Stator mutual inductance, Ms
  summary: 定子互感 0.00002 H（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Stator zero-sequence inductance, L0
  summary: 定子零序电感 0.00016 H（默认）
  group: 电气（2-D 偏导数数据参数化）
- name: Winding type
  summary: 定子绕组配置 Wye-wound（默认）| Delta-wound | Open-end
  group: 电气（3-D 偏导数数据参数化）
- name: Direct-axis current vector, iD
  summary: 直轴电流向量 [-200, 0, 200] A（默认）
  group: 电气（3-D 偏导数数据参数化）
- name: Quadrature-axis current vector, iQ
  summary: 交轴电流向量 [-200, 0, 200] A（默认）
  group: 电气（3-D 偏导数数据参数化）
- name: Rotor angle vector, theta
  summary: 转子角度向量 [0, 20, 40, 60] deg（默认）
  group: 电气（3-D 偏导数数据参数化）
- name: A-phase flux linkage partial derivative wrt iA, dPhiA(id,iq,theta)/diA
  summary: A 相磁链对 iA 的偏导数 zeros(3, 3, 4) Wb/A（默认）
  group: 电气（3-D 偏导数数据参数化）
- name: A-phase flux linkage partial derivative wrt iB, dPhiA(id,iq,theta)/diB
  summary: A 相磁链对 iB 的偏导数 zeros(3, 3, 4) Wb/A（默认）
  group: 电气（3-D 偏导数数据参数化）
- name: A-phase flux linkage partial derivative wrt iC, dPhiA(id,iq,theta)/diC
  summary: A 相磁链对 iC 的偏导数 zeros(3, 3, 4) Wb/A（默认）
  group: 电气（3-D 偏导数数据参数化）
- name: A-phase flux linkage partial derivative wrt angle, dPhiA(id,iq,theta)/dtheta
  summary: A 相磁链对角度的偏导数 zeros(3, 3, 4) Wb/rad（默认）
  group: 电气（3-D 偏导数数据参数化）
- name: Torque matrix, T(id,iq,theta)
  summary: 转矩矩阵 zeros(3, 3, 4) N*m（默认）
  group: 电气（3-D 偏导数数据参数化）
- name: Interpolation method
  summary: 插值方法 Linear（默认）| Smooth
  group: 电气（3-D 偏导数数据参数化）
- name: Stator resistance per phase, Rs
  summary: 每相定子电阻 0.013 Ohm（默认）
  group: 电气（3-D 偏导数数据参数化）
- name: Winding type
  summary: 定子绕组配置 Wye-wound（默认）| Delta-wound | Open-end
  group: Electrical (4-D Partial Derivative Data Parameterization)
- name: A-phase current vector, iA
  summary: A 相电流向量 [-200, 0, 200] A（默认）
  group: Electrical (4-D Partial Derivative Data Parameterization)
- name: B-phase current vector, iB
  summary: B 相电流向量 [-200, 0, 200] A（默认）
  group: Electrical (4-D Partial Derivative Data Parameterization)
- name: C-phase current vector, iC
  summary: C 相电流向量 [-200, 0, 200] A（默认）
  group: Electrical (4-D Partial Derivative Data Parameterization)
- name: Rotor angle vector, theta
  summary: 转子角度向量 [0, 20, 40, 60] deg（默认）
  group: Electrical (4-D Partial Derivative Data Parameterization)
- name: A-phase flux linkage partial derivative wrt iA, dPhiA(iA,iB,iC,theta)/diA
  summary: A 相磁链对 iA 的偏导数 zeros(3, 3, 3, 4) Wb/A（默认）
  group: Electrical (4-D Partial Derivative Data Parameterization)
- name: A-phase flux linkage partial derivative wrt iB, dPhiA(iA,iB,iC,theta)/diB
  summary: A 相磁链对 iB 的偏导数 zeros(3, 3, 3, 4) Wb/A（默认）
  group: Electrical (4-D Partial Derivative Data Parameterization)
- name: A-phase flux linkage partial derivative wrt iC, dPhiA(iA,iB,iC,theta)/diC
  summary: A 相磁链对 iC 的偏导数 zeros(3, 3, 3, 4) Wb/A（默认）
  group: Electrical (4-D Partial Derivative Data Parameterization)
- name: A-phase flux linkage partial derivative wrt angle, dPhiAiA,iB,iC,theta)/dtheta
  summary: A 相磁链对角度的偏导数 zeros(3, 3, 3, 4) Wb/rad（默认）
  group: Electrical (4-D Partial Derivative Data Parameterization)
- name: Torque matrix, T(iA,iB,iC,theta)
  summary: 转矩矩阵 zeros(3, 3, 3, 4) N*m（默认）
  group: Electrical (4-D Partial Derivative Data Parameterization)
- name: Interpolation method
  summary: 插值方法 Linear（默认）| Smooth
  group: Electrical (4-D Partial Derivative Data Parameterization)
- name: Stator resistance per phase, Rs
  summary: 每相定子电阻 0.013 Ohm（默认）
  group: Electrical (4-D Partial Derivative Data Parameterization)
- name: Flux linkage data format
  summary: 磁链数据格式 D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)（默认）|
    D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)
    | A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta) | A-phase flux
    linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Winding type
  summary: 定子绕组配置 Wye-wound（默认）| Delta-wound | Open-end
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Expose neutral port
  summary: 中性点端口可见性 No（默认）| Yes
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Number of pole pairs
  summary: 极对数 4（默认）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Park's convention for tabulated data
  summary: 制表数据的 Park 约定 Q leads D, rotor angle measured from A-phase to D-axis（默认）| Q leads D, rotor angle measured from
    A-phase to Q-axis | D leads Q, rotor angle measured from A-phase to D-axis | D leads Q, rotor angle measured from A-phase
    to Q-axis
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Direct-axis current vector, iD
  summary: 直轴电流向量 [-200, 0, 200] A（默认）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Quadrature-axis current vector, iQ
  summary: 交轴电流向量 [-200, 0, 200] A（默认）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Peak current magnitude vector, I
  summary: 峰值电流幅值向量 [0, 100, 200] A（默认）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Current advance angle, B
  summary: 电流超前角 [-180, -90, 0, 90, 180] deg（默认）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Rotor angle vector, theta
  summary: 转子角度向量 [0, 5, 10, 15, 20, 25, 30] deg（默认值）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: D-axis flux linkage, Fd(iD,iQ,theta)
  summary: D 轴磁链 zeros(3, 3, 7) Wb（默认值）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Q-axis flux linkage, Fq(iD,iQ,theta)
  summary: Q 轴磁链 zeros(3, 3, 7) Wb（默认值）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: D-axis flux linkage, Fd(I,B,theta)
  summary: D 轴磁链 zeros(3, 5, 7) Wb（默认值）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Q-axis flux linkage, Fq(I,B,theta)
  summary: Q 轴磁链 zeros(3, 5, 7) Wb（默认值）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: A-phase flux linkage, F(iD,iQ,theta)
  summary: A 相磁链 zeros(3, 3, 7) Wb（默认值）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: A-phase flux linkage, F(I,B,theta)
  summary: A 相磁链 zeros(3, 5, 7) Wb（默认值）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Torque matrix, T(iD,iQ,theta)
  summary: 转矩矩阵 zeros(3, 3, 7) N*m（默认值）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Torque matrix, T(I,B,theta)
  summary: 转矩矩阵 zeros(3, 5, 7) N*m（默认值）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Interpolation method
  summary: 插值方法 Linear（默认值）| Smooth
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Stator resistance per phase, Rs
  summary: 每相定子电阻 0.013 Ohm（默认值）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Stator zero-sequence inductance, L0
  summary: 定子零序电感 0.00016 H（默认值）
  group: Electrical (3-D Flux Linkage Data Parameterization)
- name: Model
  summary: 铁耗建模选项 None（默认值）| Specify open and short circuit loss data (permanent magnet motors only) | Specify tabulated Steinmetz
    coefficients | Tabulate with current and speed
  group: 铁耗
- name: Open-circuit iron losses, [P_hysteresis P_eddy P_excess]
  summary: 开路铁耗 [0.0, 0.0, 0.0] W（默认值）
  group: 铁耗
- name: Short-circuit iron losses, [P_hysteresis P_eddy P_excess]
  summary: 短路铁耗 [0.0, 0.0, 0.0] W（默认值）
  group: 铁耗
- name: Electrical frequency at which losses determined
  summary: 确定损耗时的电气频率 60 Hz（默认值）
  group: 铁耗
- name: Short-circuit RMS current for short-circuit iron losses
  summary: 短路铁耗对应的短路 RMS 电流 95 A（默认值）
  group: 铁耗
- name: Rotor hysteresis loss coefficient, k_hr(id,iq)
  summary: 转子磁滞损耗系数 zeros(3, 3) W/Hz（默认值）
  group: 铁耗
- name: Rotor eddy current loss coefficient, k_Jr(id,iq)
  summary: 转子涡流损耗系数 zeros(3, 3) W/Hz^2（默认值）
  group: 铁耗
- name: Rotor excess current loss coefficient, k_er(id,iq)
  summary: 转子附加电流损耗系数 zeros(3, 3) W/Hz^1.50000（默认值）
  group: 铁耗
- name: Stator hysteresis loss coefficient, k_hs(id,iq)
  summary: 定子磁滞损耗系数 zeros(3, 3) W/Hz（默认值）
  group: 铁耗
- name: Stator eddy current loss coefficient, k_Js(id,iq)
  summary: 定子涡流损耗系数 zeros(3, 3) W/Hz^2（默认值）
  group: 铁耗
- name: Stator excess current loss coefficient, k_es(id,iq)
  summary: 定子附加电流损耗系数 zeros(3, 3) W/Hz^1.50000（默认值）
  group: 铁耗
- name: Rotor hysteresis loss coefficient, k_hr(I,B)
  summary: 转子磁滞损耗系数 zeros(3, 5) W/Hz（默认值）
  group: 铁耗
- name: Rotor eddy current loss coefficient, k_Jr(I,B)
  summary: 转子涡流损耗系数 zeros(3, 5) W/Hz^2（默认值）
  group: 铁耗
- name: Rotor excess current loss coefficient, k_er(I,B)
  summary: 转子附加电流损耗系数 zeros(3, 5) W/Hz^1.50000（默认值）
  group: 铁耗
- name: Stator hysteresis loss coefficient, k_hs(I,B)
  summary: 定子磁滞损耗系数 zeros(3, 5) W/Hz（默认值）
  group: 铁耗
- name: Stator eddy current loss coefficient, k_Js(I,B)
  summary: 定子涡流损耗系数 zeros(3, 5) W/Hz^2（默认值）
  group: 铁耗
- name: Stator excess current loss coefficient, k_es(I,B)
  summary: 定子过剩电流损耗系数 zeros(3, 5) W/Hz^1.50000（默认值）
  group: 铁耗
- name: Rotor speed vector, w
  summary: 转子速度 [1000, 2000] rpm（默认值）
  group: 铁耗
- name: Rotor iron loss table, Pr(id,iq,w)
  summary: 转子铁损表 zeros(3, 3, 2) W（默认值）
  group: 铁耗
- name: Stator iron loss table, Ps(id,iq,w)
  summary: 定子铁损表 zeros(3, 3, 2) W（默认值）
  group: 铁耗
- name: Rotor iron loss table, Pr(I,B,w)
  summary: 转子铁损表 zeros(3, 5, 2) W（默认值）
  group: 铁耗
- name: Stator iron loss table, Ps(I,B,w)
  summary: 定子铁损表 zeros(3, 5, 2) W（默认值）
  group: 铁耗
- name: Rotor inertia
  summary: 转子惯量 0.01 kg*m^2（默认值）
  group: 机械
- name: Rotor damping
  summary: 转子阻尼 0 N*m/(rad/s)（默认值）
  group: 机械
- name: Measurement temperature
  summary: 测量温度 298.15 K（默认值）
  group: 温度依赖性
- name: Resistance temperature coefficient
  summary: 电阻温度系数 3.93e-3 1/K（默认值）
  group: 温度依赖性
- name: Permanent magnet flux temperature coefficient
  summary: 永磁磁通温度系数 -0.001（默认值）
  group: 温度依赖性
- name: Thermal mass for each stator winding
  summary: 每个定子绕组的熱质量 100 J/K（默认值）
  group: 热端口
- name: Initial stator winding temperatures
  summary: 定子绕组初始温度 [298.15, 298.15, 298.15] K（默认值）
  group: 热端口
- name: Rotor thermal mass
  summary: 转子熱质量 200 J/K（默认值）
  group: 热端口
- name: Rotor initial temperature
  summary: 转子初始温度 298.15 K（默认值）
  group: 热端口
- name: Percentage of main flux path iron losses associated with the rotor
  summary: 与转子相关的主磁通路径铁损百分比 90（默认值）
  group: 热端口
- name: Percentage of cross-tooth flux path iron losses associated with the rotor
  summary: 与转子相关的跨齿磁通路径铁损百分比 30（默认值）
  group: 热端口
```

### **Modeling option** — 磁链和转矩参数化方法 `2-D partial derivative data | No thermal port`（默认）| `2-D partial derivative data | Show thermal port` | `3-D partial derivative data | No thermal port` | `3-D partial derivative data | Show thermal port` | `4-D partial derivative data | No thermal port` | `4-D partial derivative data | Show thermal port` | `3-D flux linkage data | No thermal port` | `3-D flux linkage data | Show thermal port`

磁链和转矩的参数化方法。要对将电功率转换为热量的铜电阻和铁耗效应进行建模，请选择带热端口的选项。

### 电气（2-D 偏导数数据参数化）

**Electrical** 参数的此配置对应于 2-D Partial Derivative Data 模块参数化，带或不带热端口。如果您使用的是该模块的 3-D Partial Derivative Data、4-D Partial Derivative Data 或 3-D Flux Linkage Data 参数化，请分别参阅电气（3-D 偏导数数据参数化）、电气（4-D 偏导数数据参数化）或电气（3-D 磁链数据参数化）。

### **Parameterization** — 参数化方法 `Assume constant mutual inductance - tabulate 含相电流和转子角`（默认）| `假设正弦反电动势 - 用 d 轴和 q-axis currents`

选择参数化方法：

- `Assume constant mutual inductance - tabulate
  含相电流和转子角`
  — 此方法假设链接每个绕组的磁链仅非线性地取决于该同一
  绕组中的电流以及转子角度。
- `Assume sinusoidal back emf - tabulate with d-
  and q-axis currents` — 此方法
  假设链接每个绕组的磁链非线性地取决于所有定子绕组电流。它还假设
  永磁磁链为正弦。此选项通常非常适合内置式磁体 PMSM（或
  IPMSM）。

### **Winding type** — 定子绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

选择定子绕组的配置：

- `Wye-wound` — 定子绕组
  为星形连接。
- `Delta-wound` — 定子
  绕组为三角形连接。*a* 相
  连接在端口 **a** 和
  **b** 之间，*b* 相
  连接在端口 **b** 和
  **c** 之间，
  *c* 相连接在端口
  **c** 和
  **a** 之间。
- `Open-end` — 绕组处于
  开口端配置。该模块将绕组的每一端作为电气连接暴露出来。

### **Current vector, i** — 电流向量 `[-2, 0, 2]` `A`（默认）

与所提供的磁链偏导数对应的电流向量。电流向量必须是双侧的（具有正值和
负值）。

#### 依赖关系

仅当您将
**Parameterization** 参数设置为
`Assume constant mutual inductance - tabulate with
phase current and rotor angle` 时，此参数才可见。

### **Rotor angle vector, theta** — 转子角度向量 `[0, 20, 40, 60]` `deg`（默认）

与所提供的磁链偏导数对应的转子角度向量。该向量必须从零开始。此值
对应于 A 相磁通与转子永磁峰值磁通方向（直轴，或
*`d`* 轴）对齐的角度。最后一个值
*Θ*max 必须是磁链模式再次达到峰值的转子
角度。因此，如果 *Θ*max 以度表示，则极对数为 360/*Θ*max。默认值对应于 6 极对
电机。

#### 依赖关系

仅当您将
**Parameterization** 参数设置为
`Assume constant mutual inductance - tabulate with
phase current and rotor angle` 时，此参数才可见。

### **Flux linkage partial derivative wrt current, dPhi(i,theta)/di** — 磁链对电流的偏导数 `0.0002*ones(3,4)` `Wb/A`（默认）

磁链对电流的偏导数矩阵，定义为电流向量和转子角度向量的函数。
磁链是磁通乘以绕组匝数。默认值对应于定子电感
不依赖于定子电流或转子角度的特殊情况。

#### 依赖关系

仅当您将
**Parameterization** 参数设置为
`Assume constant mutual inductance - tabulate with
phase current and rotor angle` 时，此参数才可见。

### **Flux linkage partial derivative wrt angle, dPhi(i,theta)/dtheta** — 磁链对角度的偏导数 `[0, -0.16, 0.16, 0; 0, -0.16, 0.16, 0; 0, -0.16, 0.16, 0]` `Wb/rad`（默认）

磁链对转子角度的偏导数矩阵，定义为电流向量和转子角度
向量的函数。磁链是磁通乘以绕组匝数。默认值为 `[0, -0.16, 0.16, 0; 0, -0.16, 0.16,
0; 0, -0.16, 0.16, 0]` Wb/rad，它对应于定子电感不依赖于定子
电流的特殊情况。

#### 依赖关系

仅当您将
**Parameterization** 参数设置为
`Assume constant mutual inductance - tabulate with
phase current and rotor angle` 时，此参数才可见。

### **Direct axis current vector, id** — 直轴电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的电感对应的 *`d`* 轴电流
向量。电流向量必须是双侧的（具有正值和负值）。

#### 依赖关系

仅当您将
**Parameterization** 参数设置为
`假设正弦反电动势 - 用 d 轴和
q-axis currents` 时，此参数才可见。

### **Quadrature axis current vector, iq** — 交轴电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的电感对应的 *`q`* 轴电流
向量。电流向量必须是双侧的（具有正值和负值）。

#### 依赖关系

仅当您将
**Parameterization** 参数设置为
`假设正弦反电动势 - 用 d 轴和
q-axis currents` 时，此参数才可见。

### **Ld matrix, Ld(id,iq)** — Ld 矩阵 `0.0002*ones(3,3)` `H`（默认）

*`d`* 轴电感关于电流的矩阵，
定义为 *`d`* 轴和
*`q`* 轴电流向量的函数。

#### 依赖关系

仅当您将
**Parameterization** 参数设置为
`假设正弦反电动势 - 用 d 轴和
q-axis currents` 时，此参数才可见。

### **Lq matrix, Lq(id,iq)** — Lq 矩阵 `0.0002*ones(3,3)` `H`（默认）

*`q`* 轴电感关于电流的矩阵，
定义为 *`d`* 轴和
*`q`* 轴电流向量的函数。

#### 依赖关系

仅当您将
**Parameterization** 参数设置为
`假设正弦反电动势 - 用 d 轴和
q-axis currents` 时，此参数才可见。

### **Permanent magnet flux linkage, PM(id,iq)** — 永磁磁链 `0.1*ones(3,3)` `Wb`（默认）

永磁磁链关于电流的矩阵，定义为 *`d`* 轴和
*`q`* 轴电流向量的函数。磁链是
磁通乘以绕组匝数。

#### 依赖关系

仅当您将
**Parameterization** 参数设置为
`假设正弦反电动势 - 用 d 轴和
q-axis currents` 时，此参数才可见。

### **Number of pole pairs** — 极对数 `6`（默认）

永磁电机的极对数。

#### 依赖关系

仅当您将
**Parameterization** 参数设置为
`假设正弦反电动势 - 用 d 轴和
q-axis currents` 时，此参数才可见。

### **Calculate torque matrix?** — 电磁转矩数据指定方式 `Yes`（默认）| `No — specify directly`

指定提供电磁转矩数据的方式：

- Yes — 该模块根据磁链信息计算转矩，作为电流和转子
  角度的函数。
- `No — specify directly`
  — 通过使用 **Torque matrix, T(i,theta)**
  参数直接输入电磁转矩数据。

#### 依赖关系

仅当您将
**Parameterization** 参数设置为
`Assume constant mutual inductance - tabulate with
phase current and rotor angle` 时，此参数才可见。如果您将
**Parameterization** 参数设置为
`假设正弦反电动势 - 用 d 轴和
q-axis currents`，则转矩方程
以所提供的矩阵显式表示。

### **Torque matrix, T(i,theta)** — 转矩矩阵 `zeros(3, 3, 3, 4)` `N*m`（默认）

指定施加到转子的电磁转矩矩阵，作为电流和转子角度的函数。仅当
**Calculate torque matrix?** 设置为
`No — specify directly` 时，此参数才可见。

#### 依赖关系

仅当您将
**Calculate torque matrix?** 参数设置为
`No — specify directly` 时，此参数才可见。

### **Interpolation method** — 插值方法 `Linear` `Smooth`（默认）

当输入值位于两个连续网格点之间时，选择以下插值方法之一来近似
输出值：

- `Linear` — 使用多维插值的线性算法扩展。选择
  此选项以获得最佳性能。
- `Smooth` — 使用改进的
  Akima 插值算法。选择此选项以生成具有连续一阶
  导数的连续曲面。

有关插值方法的详细信息，请参阅 PS Lookup Table (2D)
模块参考页。

### **Stator resistance per phase, Rs** — 每相定子电阻 `0.013` `Ohm`（默认）

每个定子绕组的电阻。

### **Stator mutual inductance, Ms** — 定子互感 `0.00002` `H`（默认）

定子-定子互感，假设其既不依赖于电流也不依赖于转子角度。

#### 依赖关系

仅当您将
**Parameterization** 参数设置为
`Assume constant mutual inductance - tabulate with
phase current and rotor angle` 时，此参数才可见。

### **Stator zero-sequence inductance, L0** — 定子零序电感 `0.00016` `H`（默认）

零序电感。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Assume
正弦反电动势 - 用 d 轴和 q 轴
currents`。

### 电气（3-D 偏导数数据参数化）

**Electrical** 参数的此配置对应于 3-D Partial Derivative Data 模块变体，带或不带热端口。如果您
使用的是该模块的 2-D Partial Derivative Data、4-D Partial Derivative Data 或 3-D
Flux Linkage Data 参数化，请分别参阅电气（2-D 偏导数数据参数化）、电气（4-D 偏导数数据参数化）或电气（3-D 磁链数据参数化）。

### **Winding type** — 定子绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

选择定子绕组的配置：

- `Wye-wound` — 定子绕组
  为星形连接。
- `Delta-wound` — 定子
  绕组为三角形连接。*a* 相
  连接在端口 **a** 和
  **b** 之间，*b* 相
  连接在端口 **b** 和
  **c** 之间，
  *c* 相连接在端口
  **c** 和
  **a** 之间。
- `Open-end` — 绕组处于
  开口端配置。该模块将绕组的每一端作为电气连接暴露出来。

### **Direct-axis current vector, iD** — 直轴电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的磁链偏导数对应的直轴电流向量。电流向量必须是双侧的（具有
正值和负值）。

### **Quadrature-axis current vector, iQ** — 交轴电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的磁链偏导数对应的交轴电流向量。电流向量必须是双侧的（具有
正值和负值）。

### **Rotor angle vector, theta** — 转子角度向量 `[0, 20, 40, 60]` `deg`（默认）

与所提供的磁链偏导数对应的转子角度向量。该向量必须从零开始。此值对应于 A 相磁通与转子永磁峰值磁通方向（直轴，即 *`d`* 轴）对齐时的角度。最后一个值 *Θ*max 必须是磁链模式再次达到峰值时的转子角度。因此，如果 *Θ*max 以度为单位表示，则极对数为 360/*Θ*max。默认值对应于 6 极对电机。

### **A-phase flux linkage partial derivative wrt iA, dPhiA(id,iq,theta)/diA** — A 相磁链对 iA 的偏导数 `zeros(3, 3, 4)` `Wb/A`（默认）

A 相磁链对绕组 A 电流的偏导数矩阵，定义为两个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **A-phase flux linkage partial derivative wrt iB, dPhiA(id,iq,theta)/diB** — A 相磁链对 iB 的偏导数 `zeros(3, 3, 4)` `Wb/A`（默认）

A 相磁链对绕组 B 电流的偏导数矩阵，定义为两个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **A-phase flux linkage partial derivative wrt iC, dPhiA(id,iq,theta)/diC** — A 相磁链对 iC 的偏导数 `zeros(3, 3, 4)` `Wb/A`（默认）

A 相磁链对绕组 C 电流的偏导数矩阵，定义为两个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **A-phase flux linkage partial derivative wrt angle, dPhiA(id,iq,theta)/dtheta** — A 相磁链对角度的偏导数 `zeros(3, 3, 4)` `Wb/rad`（默认）

A 相磁链对转子角度的偏导数矩阵，定义为两个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **Torque matrix, T(id,iq,theta)** — 转矩矩阵 `zeros(3, 3, 4)` `N*m`（默认）

指定施加到转子上的电磁转矩矩阵，作为两个电流和转子角度的函数。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

当输入值位于两个相邻网格点之间时，选择以下插值方法之一来近似输出值：

- `Linear` — 使用多维插值的线性算法扩展。选择此选项以获得最佳性能。
- `Smooth` — 使用改进的 Akima 插值算法。选择此选项以生成具有连续一阶导数的连续曲面。

有关插值方法的更多信息，请参阅 PS Lookup Table (3D) 模块参考页。

### **Stator resistance per phase, Rs** — 每相定子电阻 `0.013` `Ohm`（默认）

每个定子绕组的电阻。

### Electrical (4-D Partial Derivative Data Parameterization)

**Electrical** 参数的此配置对应于 4-D Partial Derivative Data 模块变体，带或不带热端口。如果您使用的是该模块的 2-D Partial Derivative Data、3-D Partial Derivative Data 或 3-D Flux Linkage Data 参数化，请分别参阅 Electrical (2-D Partial Derivative Data Parameterization)、Electrical (3-D Partial Derivative Data Parameterization) 或 Electrical (3-D Flux Linkage Data Parameterization)。

### **Winding type** — 定子绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

选择定子绕组的配置：

- `Wye-wound` — 定子绕组为星形连接。
- `Delta-wound` — 定子绕组为三角形连接。*a* 相连接在端口 **a** 和 **b** 之间，*b* 相连接在端口 **b** 和 **c** 之间，*c* 相连接在端口 **c** 和 **a** 之间。
- `Open-end` — 绕组为开口端配置。该模块将绕组的每一端作为电气连接暴露出来。

### **A-phase current vector, iA** — A 相电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的磁链偏导数对应的 A 相电流向量。电流向量必须是双侧的（具有正值和负值）。

### **B-phase current vector, iB** — B 相电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的磁链偏导数对应的 B 相电流向量。电流向量必须是双侧的（具有正值和负值）。

### **C-phase current vector, iC** — C 相电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的磁链偏导数对应的 C 相电流向量。电流向量必须是双侧的（具有正值和负值）。

### **Rotor angle vector, theta** — 转子角度向量 `[0, 20, 40, 60]` `deg`（默认）

与所提供的磁链偏导数对应的转子角度向量。该向量必须从零开始。此值对应于 A 相磁通与转子永磁峰值磁通方向（直轴，即 *`d`* 轴）对齐时的角度。最后一个值 *Θ*max 必须是磁链模式再次达到峰值时的转子角度。因此，如果 *Θ*max 以度为单位表示，则极对数为 360/*Θ*max。默认值对应于 6 极对电机。

### **A-phase flux linkage partial derivative wrt iA, dPhiA(iA,iB,iC,theta)/diA** — A 相磁链对 iA 的偏导数 `zeros(3, 3, 3, 4)` `Wb/A`（默认）

A 相磁链对绕组 A 电流的偏导数矩阵，定义为三个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **A-phase flux linkage partial derivative wrt iB, dPhiA(iA,iB,iC,theta)/diB** — A 相磁链对 iB 的偏导数 `zeros(3, 3, 3, 4)` `Wb/A`（默认）

A 相磁链对绕组 B 电流的偏导数矩阵，定义为三个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **A-phase flux linkage partial derivative wrt iC, dPhiA(iA,iB,iC,theta)/diC** — A 相磁链对 iC 的偏导数 `zeros(3, 3, 3, 4)` `Wb/A`（默认）

A 相磁链对绕组 C 电流的偏导数矩阵，定义为三个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **A-phase flux linkage partial derivative wrt angle, dPhiAiA,iB,iC,theta)/dtheta** — A 相磁链对角度的偏导数 `zeros(3, 3, 3, 4)` `Wb/rad`（默认）

A 相磁链对转子角度的偏导数矩阵，定义为三个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **Torque matrix, T(iA,iB,iC,theta)** — 转矩矩阵 `zeros(3, 3, 3, 4)` `N*m`（默认）

指定施加到转子上的电磁转矩矩阵，作为三个电流和转子角度的函数。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

当输入值位于两个相邻网格点之间时，选择以下插值方法之一来近似输出值：

- `Linear` — 使用多维插值的线性算法扩展。选择此选项以获得最佳性能。
- `Smooth` — 使用改进的 Akima 插值算法。选择此选项以生成具有连续一阶导数的连续曲面。

有关插值方法的更多信息，请参阅 PS Lookup Table (3D) 模块参考页。

### **Stator resistance per phase, Rs** — 每相定子电阻 `0.013` `Ohm`（默认）

每个定子绕组的电阻。

### Electrical (3-D Flux Linkage Data Parameterization)

**Electrical** 参数的此配置对应于 3-D Flux Linkage Data 模块变体，带或不带热端口。如果您使用的是该模块的 2-D Partial Derivative Data、3-D Partial Derivative Data 或 4-D Partial Derivative Data 参数化，请分别参阅 Electrical (2-D Partial Derivative Data Parameterization)、Electrical (3-D Partial Derivative Data Parameterization) 或 Electrical (4-D Partial Derivative Data Parameterization)。

### **Flux linkage data format** — 磁链数据格式 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`（默认）| `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` | `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` | `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`

选择您的 FE 工具所使用的磁链数据格式：

- `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`
- `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`
- `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`
- `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`

### **Winding type** — 定子绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

选择定子绕组的配置：

- `Wye-wound` — 定子绕组为星形连接。
- `Delta-wound` — 定子绕组为三角形连接。*a* 相连接在端口 **a** 和 **b** 之间，*b* 相连接在端口 **b** 和 **c** 之间，*c* 相连接在端口 **c** 和 **a** 之间。
- `Open-end` — 绕组为开口端配置。该模块将绕组的每一端作为电气连接暴露出来。

### **Expose neutral port** — 中性点端口可见性 `No`（默认）| `Yes`

是否暴露该模块的中性点端口。

如果暴露中性点端口，该模块还会对零序电流进行建模。零序由 **Stator zero-sequence inductance, L0** 参数进行参数化。当您以 *iD* 和 *iQ* 为变量制表，或以电流幅值和相位超前角为变量制表时，没有关于对零序电流非线性依赖的信息，该模块会引入一定程度的近似。为了获得更准确的结果，特别是对于大零序电流，请使用 **4-D partial derivative data** 参数化选项。

#### 依赖关系

要启用此参数，请将 **Winding type** 参数设置为 `Wye-wound`。

### **Number of pole pairs** — 极对数 `4`（默认）

永磁电机的极对数。默认值为 `4`。

### **Park's convention for tabulated data** — 制表数据的 Park 约定 `Q leads D, rotor angle measured from A-phase to D-axis`（默认）| `Q leads D, rotor angle measured from A-phase to Q-axis` | `D leads Q, rotor angle measured from A-phase to D-axis` | `D leads Q, rotor angle measured from A-phase to Q-axis`

选择将给定 *dq* 数据映射到三个绕组的 Park 变换的顺序和参考角度。

- `Q leads D, rotor angle measured from A-phase to D-axis` — 交-直变换，角度相对于 *d* 轴测量。
- `Q leads D, rotor angle measured from A-phase to Q-axis` — 交-直变换，角度相对于 *q* 轴测量。
- `D leads Q, rotor angle measured from A-phase to D-axis` — 直-交变换，角度相对于 *d* 轴测量。
- `D leads Q, rotor angle measured from A-phase to Q-axis` — 直-交变换，角度相对于 *q* 轴测量。

### **Direct-axis current vector, iD** — 直轴电流向量 `[-200, 0, 200]` `A`（默认）

磁链制表所用的直轴电流向量。电流向量必须是双侧的（具有正值和负值）。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **Quadrature-axis current vector, iQ** — 交轴电流向量 `[-200, 0, 200]` `A`（默认）

磁链制表所用的交轴电流向量。电流向量必须是双侧的（具有正值和负值）。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **Peak current magnitude vector, I** — 峰值电流幅值向量 `[0, 100, 200]` `A`（默认）

磁链制表所用的电流幅值行向量。第一个元素必须为零。相邻电流值应相对于磁饱和开始发生时的电流值较小。这是因为推导出的磁链偏导数在零电流处定义不明确，因此改为在此第一个非零电流处计算。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 时，此参数才可见。

### **Current advance angle, B** — 电流超前角 `[-180, -90, 0, 90, 180]` `deg`（默认）

磁链制表所用的电流超前角值行向量。电流超前角定义为电流超前交轴（Q 轴）的角度。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 时，此参数才可见。

### **Rotor angle vector, theta** — 转子角度向量 `[0, 5, 10, 15, 20, 25, 30]` `deg`（默认值）

用于制表磁链的转子角度向量。该向量必须从零开始。默认值对应于一个 4 极对电机。

如果 **Flux linkage data format** 为 `D and
Q axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` 或
`D and Q axes flux linkages as a function of peak
current magnitude (I), current advance angle (B), and rotor angle
(theta)`（即，如果您对 D 轴和 Q 轴磁链数据进行制表），则转子角度向量必须具有四个或更多点，并且范围从 0 到 120/*N* 度，其中 *N* 为极对数。如果 **Flux
linkage data format** 为 `A-phase flux linkage
as a function of D-axis current (iD), Q-axis current (iQ), and rotor
angle (theta)` 或 `A-phase flux linkage as
a function of peak current magnitude (I), current advance angle (B),
and rotor angle (theta)`（即，如果您对 A 相磁链数据进行制表），则转子角度向量必须具有 3*n*+1 个点，其中 *n*>=2，并且范围必须从 0 到 360/*N* 度。

### **D-axis flux linkage, Fd(iD,iQ,theta)** — D 轴磁链 `zeros(3, 3, 7)` `Wb`（默认值）

*D* 轴磁链矩阵，定义为 *dq* 电流和转子角度向量的函数。磁链是磁通量乘以绕组匝数。

如果您的磁通数据以不同的顺序给出，您可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中相关的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux
linkage data format** 参数设置为 `D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **Q-axis flux linkage, Fq(iD,iQ,theta)** — Q 轴磁链 `zeros(3, 3, 7)` `Wb`（默认值）

*Q* 轴磁链矩阵，定义为 *dq* 电流和转子角度向量的函数。磁链是磁通量乘以绕组匝数。

如果您的磁通数据以不同的顺序给出，您可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中相关的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux
linkage data format** 参数设置为 `D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **D-axis flux linkage, Fd(I,B,theta)** — D 轴磁链 `zeros(3, 5, 7)` `Wb`（默认值）

*D* 轴磁链值的 3-D 矩阵，作为 **Peak current magnitude vector, I**、**Current advance angle, B** 和 **Rotor
angle vector, theta** 的函数。

如果您的磁通数据以不同的顺序给出，您可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中相关的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux
linkage data format** 参数设置为 `D and Q
axes flux linkages as a function of peak current magnitude (I),
current advance angle (B), and rotor angle
(theta)` 时，此参数才可见。

### **Q-axis flux linkage, Fq(I,B,theta)** — Q 轴磁链 `zeros(3, 5, 7)` `Wb`（默认值）

*Q* 轴磁链值的 3-D 矩阵，作为 **Peak current magnitude vector, I**、**Current advance angle, B** 和 **Rotor
angle vector, theta** 的函数。

如果您的磁通数据以不同的顺序给出，您可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中相关的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux
linkage data format** 参数设置为 `D and Q
axes flux linkages as a function of peak current magnitude (I),
current advance angle (B), and rotor angle
(theta)` 时，此参数才可见。

### **A-phase flux linkage, F(iD,iQ,theta)** — A 相磁链 `zeros(3, 3, 7)` `Wb`（默认值）

A 相磁链值的 3-D 矩阵，作为 *dq* 电流和转子角度的函数。

如果您的磁通数据以不同的顺序给出，您可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中相关的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux
linkage data format** 参数设置为 `A-phase
flux linkage as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **A-phase flux linkage, F(I,B,theta)** — A 相磁链 `zeros(3, 5, 7)` `Wb`（默认值）

A 相磁链值的 3-D 矩阵，作为 **Peak current magnitude vector, I**、**Current advance angle, B** 和 **Rotor
angle vector, theta** 的函数。

如果您的磁通数据以不同的顺序给出，您可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中相关的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux
linkage data format** 参数设置为 `A-phase
flux linkage as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **Torque matrix, T(iD,iQ,theta)** — 转矩矩阵 `zeros(3, 3, 7)` `N*m`（默认值）

施加到转子上的电磁转矩的 3-D 矩阵，作为 *dq* 电流和转子角度的函数。

如果您的磁通数据以不同的顺序给出，您可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中相关的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux
linkage data format** 参数设置为 `D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` 或
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)` 时，此参数才可见。

### **Torque matrix, T(I,B,theta)** — 转矩矩阵 `zeros(3, 5, 7)` `N*m`（默认值）

施加到转子上的电磁转矩的 3-D 矩阵，作为 **Peak current magnitude vector, I**、**Current advance angle, B** 和 **Rotor
angle vector, theta** 的函数。

如果您的磁通数据以不同的顺序给出，您可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中相关的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux
linkage data format** 参数设置为 `D and Q
axes flux linkages as a function of peak current magnitude (I),
current advance angle (B), and rotor angle (theta)`
或 `A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)` 时，此参数才可见。

### **Interpolation method** — 插值方法 `Linear`（默认值）| `Smooth`

当输入值位于两个连续网格点之间时，选择以下插值方法之一来近似输出值：

- `Linear` — 使用线性算法的扩展进行多维插值。选择此选项以获得最佳性能。
- `Smooth` — 使用改进的 Akima 插值算法。选择此选项以生成具有连续一阶导数的连续曲面。

有关插值方法的更多信息，请参阅 PS Lookup Table (4D) 模块参考页。

### **Stator resistance per phase, Rs** — 每相定子电阻 `0.013` `Ohm`（默认值）

每个定子绕组的电阻。

### **Stator zero-sequence inductance, L0** — 定子零序电感 `0.00016` `H`（默认值）

零序电感。

#### 依赖关系

要启用此参数，请将 **Winding type** 设置为 `Delta-Wound` 或将 **Expose
neutral port** 设置为 `Yes`。

### 铁耗

有关计算铁耗的更多信息，请参阅 Calculating Iron Losses。

### **Model** — 铁耗建模选项 `None`（默认值）| `Specify open and short circuit loss data (permanent magnet motors only)` | `Specify tabulated Steinmetz coefficients` | `Tabulate with current and speed`

是否启用铁耗建模。`Specify
tabulated Steinmetz coefficients` 和
`Tabulate with current and speed` 选项仅在您选择 **3-D flux linkage data
| No thermal port** 或 **3-D flux linkage
data | Show thermal port** 变体时可用。

### **Open-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — 开路铁耗 `[0.0, 0.0, 0.0]` `W`（默认值）

长度为 3 的行向量，分别表示在 **Electrical frequency at which losses
determined** 指定的频率下，由磁滞、涡流和附加损耗引起的开路铁耗。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify open and short circuit loss data (permanent
magnet motors only)`

### **Short-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — 短路铁耗 `[0.0, 0.0, 0.0]` `W`（默认值）

长度为 3 的行向量，分别表示在 **Electrical frequency at which losses
determined** 指定的频率下，由磁滞、涡流和附加损耗引起的短路铁耗。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify open and short circuit loss data (permanent
magnet motors only)`

### **Electrical frequency at which losses determined** — 确定损耗时的电气频率 `60` `Hz`（默认值）

测量开路和短路铁耗时的电气频率。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify open and short circuit loss data (permanent
magnet motors only)`。

### **Short-circuit RMS current for short-circuit iron losses** — 短路铁耗对应的短路 RMS 电流 `95` `A`（默认值）

测量短路损耗时得到的短路 RMS 相电流。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify open and short circuit loss data (permanent
magnet motors only)`

### **Rotor hysteresis loss coefficient, k\_hr(id,iq)** — 转子磁滞损耗系数 `zeros(3, 3)` `W/Hz`（默认值）

转子的磁滞损耗系数，取决于 *d* 轴和 *q* 轴电流。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz
coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage
data format** 设置为 `D and Q axes flux
linkages as a function of D-axis current (iD), Q-axis current
(iQ), and rotor angle (theta)` 或
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`。

### **Rotor eddy current loss coefficient, k\_Jr(id,iq)** — 转子涡流损耗系数 `zeros(3, 3)` `W/Hz^2`（默认值）

转子的涡流损耗系数，取决于 *d* 轴和 *q* 轴电流。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz
coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage
data format** 设置为 `D and Q axes flux
linkages as a function of D-axis current (iD), Q-axis current
(iQ), and rotor angle (theta)` 或
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`。

### **Rotor excess current loss coefficient, k\_er(id,iq)** — 转子附加电流损耗系数 `zeros(3, 3)` `W/Hz^1.50000`（默认值）

转子的附加电流损耗系数，取决于 *d* 轴和 *q* 轴电流。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz
coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage
data format** 设置为 `D and Q axes flux
linkages as a function of D-axis current (iD), Q-axis current
(iQ), and rotor angle (theta)` 或
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`。

### **Stator hysteresis loss coefficient, k\_hs(id,iq)** — 定子磁滞损耗系数 `zeros(3, 3)` `W/Hz`（默认值）

定子的磁滞损耗系数，取决于 *d* 轴和 *q* 轴电流。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz
coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage
data format** 设置为 `D and Q axes flux
linkages as a function of D-axis current (iD), Q-axis current
(iQ), and rotor angle (theta)` 或
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`。

### **Stator eddy current loss coefficient, k\_Js(id,iq)** — 定子涡流损耗系数 `zeros(3, 3)` `W/Hz^2`（默认值）

定子的涡流损耗系数，取决于 *d* 轴和 *q* 轴电流。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz
coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage
data format** 设置为 `D and Q axes flux
linkages as a function of D-axis current (iD), Q-axis current
(iQ), and rotor angle (theta)` 或
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`。

### **Stator excess current loss coefficient, k\_es(id,iq)** — 定子附加电流损耗系数 `zeros(3, 3)` `W/Hz^1.50000`（默认值）

定子的附加电流损耗系数，取决于 *d* 轴和 *q* 轴电流。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz
coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage
data format** 设置为 `D and Q axes flux
linkages as a function of D-axis current (iD), Q-axis current
(iQ), and rotor angle (theta)` 或
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`。

### **Rotor hysteresis loss coefficient, k\_hr(I,B)** — 转子磁滞损耗系数 `zeros(3, 5)` `W/Hz`（默认值）

转子的磁滞损耗系数，取决于电流幅值和电流相位超前角。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz
coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage
data format** 设置为 `D and Q axes flux
linkages as a function of peak current magnitude (I), current
advance angle (B), and rotor angle (theta)` 或
`A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`。

### **Rotor eddy current loss coefficient, k\_Jr(I,B)** — 转子涡流损耗系数 `zeros(3, 5)` `W/Hz^2`（默认值）

转子的涡流损耗系数，取决于电流幅值和电流相位超前角。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz
coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage
data format** 设置为 `D and Q axes flux
linkages as a function of peak current magnitude (I), current
advance angle (B), and rotor angle (theta)` 或
`A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`。

### **Rotor excess current loss coefficient, k\_er(I,B)** — 转子附加电流损耗系数 `zeros(3, 5)` `W/Hz^1.50000`（默认值）

转子的附加电流损耗系数，取决于电流幅值和电流相位超前角。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为
`Specify tabulated Steinmetz
coefficients`，并在
**Electrical** 选项卡中，将 **Flux linkage
data format** 设置为
`D and Q axes flux
linkages as a function of peak current magnitude (I), current
advance angle (B), and rotor angle (theta)` 或
`A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`。

### **Stator hysteresis loss coefficient, k\_hs(I,B)** — 定子磁滞损耗系数 `zeros(3, 5)` `W/Hz`（默认值）

定子的磁滞损耗系数，取决于电流幅值和电流超前角。它用于 Steinmetz
方程。

#### 依赖关系

要启用此参数，请将 **Model** 设置为
`Specify tabulated Steinmetz
coefficients`，并在
**Electrical** 选项卡中，将 **Flux linkage
data format** 设置为
`D and Q axes flux
linkages as a function of peak current magnitude (I), current
advance angle (B), and rotor angle (theta)` 或
`A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`。

### **Stator eddy current loss coefficient, k\_Js(I,B)** — 定子涡流损耗系数 `zeros(3, 5)` `W/Hz^2`（默认值）

定子的涡流损耗系数，取决于电流幅值和电流超前角。它用于 Steinmetz
方程。

#### 依赖关系

要启用此参数，请将 **Model** 设置为
`Specify tabulated Steinmetz
coefficients`，并在
**Electrical** 选项卡中，将 **Flux linkage
data format** 设置为
`D and Q axes flux
linkages as a function of peak current magnitude (I), current
advance angle (B), and rotor angle (theta)` 或
`A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`。

### **Stator excess current loss coefficient, k\_es(I,B)** — 定子过剩电流损耗系数 `zeros(3, 5)` `W/Hz^1.50000`（默认值）

定子的过剩电流损耗系数，取决于电流幅值和电流超前角。它用于 Steinmetz
方程。

#### 依赖关系

要启用此参数，请将 **Model** 设置为
`Specify tabulated Steinmetz
coefficients`，并在
**Electrical** 选项卡中，将 **Flux linkage
data format** 设置为
`D and Q axes flux
linkages as a function of peak current magnitude (I), current
advance angle (B), and rotor angle (theta)` 或
`A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`。

### **Rotor speed vector, w** — 转子速度 `[1000, 2000]` `rpm`（默认值）

铁损制表所依据的转子速度向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为
`Tabulate with current and speed`，并在
**Electrical** 设置中，将 **Flux
linkage data format** 设置为
`D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` 或
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`。

### **Rotor iron loss table, Pr(id,iq,w)** — 转子铁损表 `zeros(3, 3, 2)` `W`（默认值）

转子的铁损，基于 *d* 轴和 *q* 轴电流以及转子速度制表。

#### 依赖关系

要启用此参数，请将 **Model** 设置为
`Tabulate with current and speed`，并在
**Electrical** 设置中，将 **Flux
linkage data format** 设置为
`D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` 或
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`。

### **Stator iron loss table, Ps(id,iq,w)** — 定子铁损表 `zeros(3, 3, 2)` `W`（默认值）

定子的铁损，基于 *d* 轴和 *q* 轴电流以及转子速度制表。

#### 依赖关系

要启用此参数，请将 **Model** 设置为
`Tabulate with current and speed`，并在
**Electrical** 设置中，将 **Flux
linkage data format** 设置为
`D and Q
axes flux linkages as a function of D-axis current (iD), Q-axis
current (iQ), and rotor angle (theta)` 或
`A-phase flux linkage as a function of D-axis
current (iD), Q-axis current (iQ), and rotor angle
(theta)`。

### **Rotor iron loss table, Pr(I,B,w)** — 转子铁损表 `zeros(3, 5, 2)` `W`（默认值）

转子的铁损，基于电流幅值、电流超前角和转子速度制表。

#### 依赖关系

要启用此参数，请将 **Model** 设置为
`Tabulate with current and speed`，并在
**Electrical** 设置中，将 **Flux
linkage data format** 设置为
`D and Q
axes flux linkages as a function of peak current magnitude (I),
current advance angle (B), and rotor angle (theta)`
或 `A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`。

### **Stator iron loss table, Ps(I,B,w)** — 定子铁损表 `zeros(3, 5, 2)` `W`（默认值）

定子的铁损，基于电流幅值、电流超前角和转子速度制表。

#### 依赖关系

要启用此参数，请将 **Model** 设置为
`Tabulate with current and speed`，并在
**Electrical** 设置中，将 **Flux
linkage data format** 设置为
`D and Q
axes flux linkages as a function of peak current magnitude (I),
current advance angle (B), and rotor angle (theta)`
或 `A-phase flux linkage as a function of peak current
magnitude (I), current advance angle (B), and rotor angle
(theta)`。

### 机械

### **Rotor inertia** — 转子惯量 `0.01` `kg*m^2`（默认值）

连接到机械平移端口 **R** 的转子惯量。该值可以为零。

### **Rotor damping** — 转子阻尼 `0` `N*m/(rad/s)`（默认值）

旋转阻尼。

### 温度依赖性

要启用这些参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Measurement temperature** — 测量温度 `298.15` `K`（默认值）

电机参数的标称温度。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认值）

电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值为铜的值。

### **Permanent magnet flux temperature coefficient** — 永磁磁通温度系数 `-0.001`（默认值）

永磁磁通密度随温度变化的分数变化率。它用于在温度升高时线性降低转矩和感应反电动势。

### 热端口

要启用这些参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Thermal mass for each stator winding** — 每个定子绕组的熱质量 `100` `J/K`（默认值）

A、B 和 C 相绕组的熱质量值。熱质量是将温度升高一度所需的能量。

### **Initial stator winding temperatures** — 定子绕组初始温度 `[298.15, 298.15, 298.15]` `K`（默认值）

一个 1×3 行向量，定义仿真开始时 A、B 和 C 热端口的温度。

### **Rotor thermal mass** — 转子熱质量 `200` `J/K`（默认值）

转子的熱质量，即将转子温度升高一度所需的能量。

### **Rotor initial temperature** — 转子初始温度 `298.15` `K`（默认值）

仿真开始时转子的温度。

### **Percentage of main flux path iron losses associated with the rotor** — 与转子相关的主磁通路径铁损百分比 `90`（默认值）

与通过转子的磁路相关的主磁通路径铁损百分比。它决定了有多少铁损热量归属于转子热端口 **HR**，以及有多少归属于三个绕组热端口 **HA**、**HB** 和 **HC**。

### **Percentage of cross-tooth flux path iron losses associated with the rotor** — 与转子相关的跨齿磁通路径铁损百分比 `30`（默认值）

与通过转子的磁路相关的跨齿磁通路径铁损百分比。它决定了有多少铁损热量归属于转子热端口 **HR**，以及有多少归属于三个绕组热端口 **HA**、**HB** 和 **HC**。
## 所属库

Simscape / Electrical / Electromechanical / Permanent Magnet

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

### R2024a：定子绕组的开放式配置

要以开放式配置对电机的定子绕组进行建模，请将 **Winding type** 参数设置为
`Open-end`。FEM-Parameterized PMSM 模块随后通过启用相应的电气守恒端口来暴露绕组的每一端。

## 描述

以磁链定义的永磁同步电机

FEM-Parameterized PMSM 模块对以磁链定义的永磁同步电机（PMSM）进行建模。使用此模块对任何具有永磁转子的三相电机进行建模，例如：

- 轴向磁通（盘式）电机
- 无刷伺服电机
- 具有内置磁钢转子的电机，例如内置式永磁（IPM）电机或内置式永磁同步电机（IPMSM）
- 具有表贴式磁钢转子的电机：

  - 表贴式永磁（SPM）电机或表贴式永磁同步电机（SPMSM）
  - 无刷直流（BLDC）电机

您通过使用电机磁通作为电流和转子角函数的制表数据来参数化该模块。这是有限元法（FEM）软件包通常导出磁通信息的方式。由于该模块使用制表数据，磁通可以随转子角和电流非线性变化。对转子角的非线性依赖性使该模块能够支持 BLDC 电机表现出的梯形磁通曲线，并且还能捕获仅具有近似正弦磁通曲线的电机的高次谐波。

此图显示了星形连接 PMSM 的等效电路。

此图显示了转子上具有单对极的电机结构。当永磁磁通与 *A* 相磁轴对齐时，转子角为零。

在实践中，链接三个绕组中每一个的磁通取决于所有三个电流和转子角。将磁通表示为四个自变量的函数可能导致仿真效率低下和显著的内存需求。因此，该模块允许您使用 **Modeling option** 参数来指定如何对磁通和转矩进行建模：

- 2-D 偏导数数据 — 二维查表，可选择以电流和转子角制表，或以 *`d`* 轴和 *`q`* 轴电流制表。第一个选项假设互感恒定，并支持非正弦反电动势（EMF）曲线。第二个选项假设正弦反电动势，并捕获 IPMSM 的饱和效应。
- 3-D 偏导数数据 — 三维查表，基于直轴电流、交轴电流和转子角。您提供 *a* 相的磁通查表数据。该模块使用 Park 变换将三个定子绕组电流映射为直轴和交轴电流。与四维查表相比，此方法降低了数据复杂度，并改善了仿真性能。
- 4-D 偏导数数据 — 四维查表，基于三个定子绕组电流和转子角。您提供 *a* 相的磁通查表数据。此模型比二维和三维偏导数数据模型具有更高的保真度，但其仿真性能最低效，内存需求最高。
- 3-D 磁链数据 — 三维查表，基于磁链数据。您可以以多种格式提供磁链数据。该模块使用 Park 变换将三个定子绕组电流映射为直轴和交轴电流。与四维查表相比，此方法降低了数据复杂度，并改善了仿真性能。

某些 **Modeling option** 参数设置还会启用热端口。有关详细信息，请参阅 Model Thermal Effects。

默认情况下，对于所有这些参数化方法，该模块为定子绕组实现星形连接配置。但是，您可以使用 **Winding type** 参数切换到三角形连接或开放式配置。在三角形连接配置中，*a* 相连接端口 **a** 和 **b**，*b* 相连接端口 **b** 和 **c**，*c* 相连接端口 **c** 和 **a**。

**注意**

Simscape™ Electrical™ 包含多个可以对同一类型电机或执行器进行建模的模块。选择一个具有足够建模细节的模块来回答您需要解决的工程设计问题。不要使用建模细节超过您需要的模块，因为更高保真度的模型会减慢仿真速度，并且参数化更复杂。

像 FEM-Parameterized PMSM 模块这样的模块以磁链定义电机行为。这些模型具有高水平的保真度。仅在需要高水平建模细节时使用此模块，例如，预测牵引应用的效率或捕获转矩和电流谐波。有关选择正确的模块以适当的保真度对电机进行建模的更多信息，请参阅 Choose Blocks to Model Motors or Actuators。

### 恒定互感 2-D 数据模型

在此二维磁通数据模型中，假设每个绕组交链的磁通仅非线性地依赖于该同一绕组中的电流以及转子角度。在实践中，这对于许多永磁同步电机是一个合理的假设；然而，对于开关磁阻电机则不太准确。基于此假设，三个绕组中的磁通为：

[ϕaϕbϕc]=[0−Ms−Ms−Ms0−Ms−Ms−Ms0][iaibic]+[ϕ(ia,θr)ϕ(ib,θr−2π/(3N))ϕ(ic,θr−4π/(3N))]

其中 ϕ(θr,ia) 是 A 相绕组的磁链，作为转子角度和 A 相电流的函数。*Θ*r = 0 对应于转子 *`d`* 轴与 A 相正磁通方向对齐。*M*s 是定子-定子互感。

为了提高数值性能，模块中实现的方程实际上使用的是磁链对电流的偏导数 ∂ϕ(i,θr)/∂i 以及对转子角度的偏导数 ∂ϕ(i,θr)/∂θr，而不是直接使用磁通。如果您的 FEM 软件包不导出这些偏导数，您可以使用 MATLAB® 脚本确定它们。有关如何执行此操作的示例，请参见 Solenoid Parameterized with FEM Data 示例模型及其配套的 MATLAB 脚本。

该模块的电气方程，以磁通偏导数形式定义，为：

va=∂ϕ∂iadiadt+∂ϕ∂θrdθrdt−Ms(dibdt+dicdt)+Rsiavb=∂ϕ∂ibdibdt+∂ϕ∂θrdθrdt−Ms(diadt+dicdt)+Rsibvc=∂ϕ∂icdicdt+∂ϕ∂θrdθrdt−Ms(diadt+dibdt)+Rsic

其中

- *v*a、*v*b、*v*c 是施加到 A、B、C 定子绕组的电压。
- *i*a、*i*b、*i*c 是三个绕组中每个绕组的定子电流。
- *R*s 是每个定子绕组的电阻。
- *M*s 是定子-定子互感。
- ∂ϕ/∂ia、∂ϕ/∂ib、∂ϕ/∂ic 是磁链对三个绕组中每个绕组定子电流的偏导数。
- ∂ϕ/∂θr 是磁链对转子角度的偏导数。

该模块可以根据您提供的磁通信息自动计算转矩矩阵。或者，您可以将 **Calculate torque matrix?** 参数设置为 `No`，并直接指定转矩作为电流和转子角度的函数。有关更多信息，请参见 FEM-Parameterized Rotary Actuator 模块参考页。

### 正弦反电动势 2-D 数据模型

在此二维磁通数据模型中，假设每个绕组交链的磁通非线性地依赖于所有定子绕组电流，并且假设永磁磁链是正弦的。内置式磁钢 PMSM（或 IPMSM）通常很好地符合此假设。方程为：

[ϕdϕq]=[Ld(id,iq)Lq(id,iq)][idiq]+[ϕm(id,iq)]

T=32N(iq(idLd(id,iq)+ϕm(id,iq))−idiqLq(id,iq))

其中

- *i*d 和 *i*q 分别是 *`d`* 轴和 *`q`* 轴电流。
- *ϕ*d 和 *ϕ*q 分别是 *`d`* 轴和 *`q`* 轴磁链。
- *ϕ*m 是永磁磁链。
- *L*d 和 *L*q 分别是 *`d`* 轴和 *`q`* 轴电感。假设它们依赖于 *`d`* 轴和 *`q`* 轴电流。
- *N* 是极对数。
- *T* 是电磁转矩。

### 使用 Park 变换的 3-D 偏导数数据模型

处理四维数据既有仿真性能成本，也有内存成本。为了将表格维度降至三维，三维数据模型使用 Park 变换将三个电流映射为直轴和交轴电流：

[idiq]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)][iaibic]

在一般情况下，Park 变换映射为直轴、交轴和零序电流。然而，在正常工作条件下，零序电流通常很小。因此，该模型忽略了磁链项对零序电流的依赖性，仅根据直轴和交轴电流以及转子角度来确定磁链。三维数据模型的磁通方程为：

[ϕaϕbϕc]=[ϕ(id,iq,θr)ϕ(id,iq,θr−2π/(3N))ϕ(id,iq,θr−4π/(3N))]

该模块的电气方程也以磁通偏导数形式定义，类似于四维数据模型。您可以使用 `ee_calculateFluxPartialDerivatives` 从四维磁链数据计算三维磁链偏导数数据。

### 4-D 偏导数数据模型

每个绕组交链的磁通是该绕组中的电流、其他两个绕组中的电流以及转子角度的函数。为了获得完全精度，四维磁通数据模型假设磁链是三个电流和转子角度的函数，因此执行四维表格查找。磁通方程为：

[ϕaϕbϕc]=[ϕ(ia,ib,ic,θr)ϕ(ib,ic,ia,θr−2π/(3N))ϕ(ic,ia,ib,θr−4π/(3N))]

其中

- *ϕ*a、*ϕ*b、*ϕ*c 是 A、B、C 定子绕组的磁链。
- *i*a、*i*b、*i*c 是三个绕组中每个绕组的定子电流。
- *Θ*r 是转子角度。*Θ*r = 0 对应于永磁磁通与 A 相定子绕组磁通对齐的情况。
- *N* 是极对数。

假设磁链数据关于 *Θ*r 是周期性的。例如，如果电机有六个极对，则数据范围为 0 ≤ *Θ*r ≤ 60°。您必须提供 0 度和 60 度处的数据，并且由于数据是周期性的，磁链偏导数在这两个端点处必须相同。

转矩方程为：

τ=T(ia,ib,ic,θr)

四维数据模型没有让模块根据磁链确定转矩的选项。由于四维情况下数值开销增加，最好预先计算一次转矩，而不是每次运行仿真时都计算它。

为了提高数值性能，模块中实现的方程实际上使用的是磁链对三个电流和转子角度的偏导数，而不是直接使用磁通。如果您的 FEM 软件包不导出这些偏导数，您可以使用 `ee_calculateFluxPartialDerivatives` 确定它们。

该模块的电气方程，以磁通偏导数形式定义，为：

va=∂ϕa∂iadiadt+∂ϕa∂ibdibdt+∂ϕa∂icdicdt+∂ϕa∂θrdθrdt+Rsiavb=∂ϕb∂iadiadt+∂ϕb∂ibdibdt+∂ϕb∂icdicdt+∂ϕb∂θrdθrdt+Rsibvc=∂ϕc∂iadiadt+∂ϕc∂ibdibdt+∂ϕc∂icdicdt+∂ϕc∂θrdθrdt+Rsic

其中

- *v*a、*v*b、*v*c 是施加到 A、B、C 定子绕组的电压。
- *i*a、*i*b、*i*c 是三个绕组中每个绕组的定子电流。
- *R*s 是每个定子绕组的电阻。

### 3-D Flux Linkage Data Models

三维磁链数据选项允许您使用从有限元（FE）电机设计工具导出的原始磁链数据。这与三维偏导数数据选项形成对比，后者需要您确定偏导数。您可以提供多种格式的磁链数据，以支持不同的 FE 工具约定：

- 将 DQ 轴磁链数据或 A 相磁链数据制成表格 — 一些工具支持使用分解为直轴（D）和交轴（Q）的磁链。这种方法的一个优点是只需要转子角度在 0 到 360/*N*/3 度范围内的数据（其中 *N* 是极对数）。其他工具直接使用 A、B、C 相磁链，为此您可以仅导入 A 相磁链，其转子角度范围必须在 0 到 360/*N* 度范围内。仅导入 A 相数据的隐含假设是 B 相和 C 相数据相同，只是相位偏移。
- 使用笛卡尔或极坐标电流坐标制成表格 — 笛卡尔制表意味着磁链根据 D 轴电流和 Q 轴电流（加上转子角度）制成表格。或者，极坐标制表涉及根据电流幅值、相对于 Q 轴的电流超前角以及转子角度来制表磁链。极坐标的优点是它更自然地反映了允许的工作电流，从而避免了未使用的表格数据点。

这些约定产生了四种 **Flux linkage data format** 参数化选项：

- `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`
- `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`
- `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`
- `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`

FEM-Parameterized PMSM 模块需要三维磁链数据。要将二维磁链数据 `F(id,iq)` 转换为三维表格 `F(id,iq,x)`，请使用 `repmat` 函数。

除了选择您的 FE 工具使用的磁链数据格式外，您还必须选择该工具使用的 Park 变换版本。下面描述了四种约定，它们对应于 **Park’s convention for tabulated data** 下拉菜单的四个选项。

**注意**

在查看 D 轴和 Q 轴电流的记录值时，请记住，对于这些选项中的每一个，格式都会根据需要进行转换，以便 FEM-Parameterized PMSM 模块在内部一致地使用选项 1。

**注意**

为了保留由永磁体反电动势引起的高阶谐波，请提供 A 相磁通数据而不是 D 轴和 Q 轴磁通数据。相反，如果您提供 D 轴和 Q 轴磁通，Park 变换会消除高阶谐波。对于许多应用来说，使用 D 和 Q 磁通就足够了，特别是如果您将 **Winding type** 参数设置为 `Wye-wound` 并且没有连接到该模块的中性端口的连接。对于这种特定情况，中性端口电流和为零的约束会消除所有三次谐波。

**选项 1. Q 超前 D，转子角度从 A 相测量到 D 轴**

这是 Simscape Electrical 电机和机械模块内部使用的 Park 约定。所有其他选项都转换为此格式。

- *N*：极对数
- *θ*r：转子角度
- *i*d、*i*q：D 轴和 Q 轴电流
- *i*p：电流幅值 = id2+iq2
- *β*：电流超前角 = tan−1(−id/iq)

相应的 Park 变换为

[idiqi0]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)121212][iaibic]

其中 *i*a、*i*b 和 *i*c 分别是 A 相、B 相和 C 相电流。

**选项 2. Q 超前 D，转子角度从 A 相测量到 Q 轴**

- *N*：极对数
- *θ*r：转子角度
- *i*d、*i*q：D 轴和 Q 轴电流
- *i*p：电流幅值 = id2+iq2
- *β*：电流超前角 = tan−1(−id/iq)

相应的 Park 变换为

[idiqi0]=23[sin(Nθr)sin(Nθr−2π3)sin(Nθr+2π3)cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)121212][iaibic]

其中 *i*a、*i*b 和 *i*c 分别是 A 相、B 相和 C 相电流。

**选项 3. D 超前 Q，转子角度从 A 相测量到 D 轴**

- *N*：极对数
- *θ*r：转子角度
- *i*d、*i*q：D 轴和 Q 轴电流
- *i*p：电流幅值 = id2+iq2
- *β*：电流超前角 = tan−1(−id/iq)

相应的 Park 变换为

[idiqi0]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)sin(Nθr)sin(Nθr−2π3)sin(Nθr+2π3)121212][iaibic]

其中 *i*a、*i*b 和 *i*c 分别是 A 相、B 相和 C 相电流。

**选项 4. D 超前 Q，转子角度从 A 相测量到 Q 轴**

- *N*：极对数
- *θ*r：转子角度
- *i*d、*i*q：D 轴和 Q 轴电流
- *i*p：电流幅值 = id2+iq2
- *β*：电流超前角 = tan−1(−id/iq)

相应的 Park 变换为

[idiqi0]=23[−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)121212][iaibic]

其中 *i*a、*i*b 和 *i*c 分别是 A 相、B 相和 C 相电流。

### Calculating Iron Losses

FEM-Parameterized PMSM 模块根据您为磁链和转矩选择的参数化方法来建模铁耗。

这些铁耗会产生热量。该模块将转子铁耗产生的热量注入表示转子热质量的 **HR** 热端口。该模块将定子铁耗分成三个相等的部分，并将每个部分分别注入定子绕组热端口 **HA**、**HB** 和 **HC**。

**指定开路和短路损耗数据（仅限永磁电机）**

对于 **2-D partial derivative data**、**3-D partial derivative data** 和 **4-D partial derivative data** 选项（无论是否带热端口），铁耗模型基于 Mellor [1] 的工作。铁耗分为两项，一项表示主磁化路径，另一项表示在弱磁运行期间变得活跃的跨齿尖路径。

表示主磁化路径的项取决于感应的 RMS 定子电压 Vmrms：

POC(Vmrms)=ahkVmrms+ajk2Vmrms2+aexk1.5Vmrms1.5.

这是空载运行期间的主导项。*k* 是反电动势常数，表示每 Hz 的 RMS 伏特数。其定义为 k=Vmrms/f，其中 *f* 是电频率。右侧第一项是磁滞损耗，第二项是涡流损耗，第三项是 excess loss。分子中出现的三个系数由您为开路磁滞、涡流和 excess loss 提供的值导出。

表示跨齿尖路径的项在建立去磁场时变得重要，可以通过有限元分析短路测试来确定。它取决于与跨齿尖磁链相关的 RMS EMF，Vdrms\*：

PSC(Vdrms\*)=bhkVdrms\*+bjk2Vdrms\*2+bexk1.5Vdrms\*1.5.

这三个分子项由您为短路磁滞、涡流和 excess loss 提供的值导出。

**Steinmetz 参数化方法**

对于 **3-D flux linkage data**（无论是否带热端口），您还可以基于 Steinmetz 方程来建模铁耗。Steinmetz 方法针对不同的电机转速或电频率进行缩放，因此铁耗数据仅需要作为电机电流的函数。

如果在 **Iron Losses** 设置中，您将 **Model** 参数设置为 `Specify open and short circuit loss data (permanent magnet motors only)`，则该模块使用 Steinmetz 方法，但假设系数恒定且不依赖于峰值电流和电流超前角。如果您有测功机测量数据，或者执行 FE 分析以仅从开路和短路仿真获得铁耗，请选择此选项。

相反，如果您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`，则该模块使用 **Peak current magnitude vector, I** 和 **Current advance angle vector, B** 参数来制表系数，因此铁耗由下式给出：

Protor(f)=khr(Ip,β)f+kJr(Ip,β)f2+ker(Ip,β)f1.5Pstator(f)=khs(Ip,β)f+kJs(Ip,β)f2+kes(Ip,β)f1.5

其中：

- *f* 是电瞬时频率，单位为 `Hz`，等于转子机械转速乘以极对数。该频率是随时间变化的变量。
- *khr(Ip,β)* 是 **Rotor hysteresis loss coefficient, k\_hr(I,B)**。
- *kJr(Ip,β)* 是 **Rotor eddy current loss coefficient, k\_Jr(I,B)**。
- *ker(Ip,β)* 是 **Rotor excess current loss coefficient, k\_er(I,B)**。
- *khs(Ip,β)* 是 **Stator hysteresis loss coefficient, k\_hs(I,B)**。
- *kJs(Ip,β)* 是 **Stator eddy current loss coefficient, k\_Js(I,B)**。
- *kes(Ip,β)* 是 **Stator excess current loss coefficient, k\_es(I,B)**。

类似地，如果您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`，则铁耗由下式给出：

Ploss,rotor(f)=khr(id,iq)f+kJr(id,iq)f2+ker(id,iq)f1.5Ploss,stator(f)=khs(id,iq)f+kJs(id,iq)f2+kes(id,iq)f1.5

其中：

- *khr(id,iq)* 是 **Rotor hysteresis loss coefficient, k\_hr(id,iq)**。
- *kJr(id,iq)* 是 **Rotor eddy current loss coefficient, k\_Jr(id,iq)**。
- *ker(id,idq)* 是 **Rotor excess current loss coefficient, k\_er(id,iq)**。
- *khs(id,iq)* 是 **Stator hysteresis loss coefficient, k\_hs(id,iq)**。
- *kJs(id,iq)* 是 **Stator eddy current loss coefficient, k\_Js(id,iq)**。
- *kes(id,iq)* 是 **Stator excess current loss coefficient, k\_es(id,iq)**。

仅在配合能够计算这些系数的电机设计工具时选择此选项。您可以使用 Motor-CAD 或 ANSYS® Maxwell® 等 FEM 工具，以笛卡尔坐标 (*id*,*iq*) 或极坐标 (*Ip*,*β*) 导出 Steinmetz 系数查找表。这些系数在一定电流和频率范围内有效。为了根据电机的当前状态获得正确的值，该模块在运行时对 Steinmetz 系数值进行插值。

有关从 FEM 工具导入 Steinmetz 系数的更多信息，请参阅 Import IPMSM Flux Linkage Data from Motor-CAD 示例。

**按电流和转速制表**

对于 **3-D flux linkage data**（无论是否带热端口），您还可以通过分别对转子和定子进行制表来建模铁耗。

如果您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`，则该模块使用 **Peak current magnitude vector, I** 和 **Current advance angle vector, B** 参数来制表铁耗，因此铁耗由下式给出：

Ploss(Ip,β,w)=tablelookup(Ptable,Ip,β,w)

其中 *w* 是 **Rotor speed vector, w** 参数。

类似地，如果您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`，则铁耗由下式给出：

Ploss(id,iq,w)=tablelookup(Ptable,id,iq,w).

### Model Thermal Effects

您可以暴露热端口来建模将功率转换为热量的损耗效应。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `2-D partial derivative data | No thermal port` — 2-D 查表参数化，可选择按电流和转子角度制表，但不带热端口。
- `2-D partial derivative data | Show thermal port` — 2-D 查表参数化，可选择按电流和转子角度制表，并带热端口。
- `3-D partial derivative data | No thermal port` — 3-D 查表参数化，基于直轴电流、交轴电流和转子角度，但不带热端口。
- `3-D partial derivative data | Show thermal port` — 3-D 查表参数化，基于直轴电流、交轴电流和转子角度，并带热端口。
- `4-D partial derivative data | No thermal port` — 4-D 查表参数化，基于三个定子绕组电流和转子角度，但不带热端口。
- `4-D partial derivative data | Show thermal port` — 4-D 查表参数化，基于三个定子绕组电流和转子角度，并带热端口。
- `3-D flux linkage data | No thermal port` — 3-D 查表参数化，基于磁链数据，不带热端口。
- `3-D flux linkage data | Show thermal port` — 3-D 查表参数化，基于磁链数据，带热端口。

有关在执行器模块中使用热端口的更多信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

**永磁磁链的温度依赖性**

为了计算永磁体的温度依赖性，该模块使用 **Permanent magnet flux temperature coefficient** 参数 *αflux*。该参数决定了电机磁链每升高一度温度时减少多少。该模块使用以下方程计算磁链减少因子：

FluxReductionForTemp=1+αflux⋅(TR−Tmeas),

其中 *TR* 是 **HR** 端口处的温度，*Tmeas* 是 **Measurement temperature** 参数的值。在该模块中，磁链随温度线性减小。这种减小导致反电动势和转矩也随温度以相同的量线性减小，

EMF=FluxReductionForTemp⋅EMF0τ=FluxReductionForTemp⋅τ0

其中：

- *τ0* 是当转子温度等于 **Measurement temperature** 参数值时的转矩。
- *EMF0* 是当转子温度等于 **Measurement temperature** 参数值时的 EMF。

在根据温度调整转矩后，该模块基于铁耗进一步减小转矩 *τ*。

**定子电阻的温度依赖性**

永磁体中温度的升高会改变定子电阻。**Resistance temperature coefficient** 参数 *α* 驱动这种电阻变化：

Ra=Rs⋅[1+α(TA−Tmeas)]Rb=Rs⋅[1+α(TB−Tmeas)]Rc=Rs⋅[1+α(TC−Tmeas)]

其中 *Ra*、*Rb* 和 *Rc* 是各相的温度调整后电阻，*TA*、*TB* 和 *TC* 是 **HA**、**HB** 和 **HC** 端口处的温度。
