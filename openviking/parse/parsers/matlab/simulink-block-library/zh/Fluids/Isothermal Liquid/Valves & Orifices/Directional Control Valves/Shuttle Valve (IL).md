---
type: simulink-block
title: 'Shuttle Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: 'shuttlevalveil'
documentation_source_path: 'ref/shuttlevalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Shuttle Valve (IL)

## 端口
```yaml
ports:
- name: A
  summary: 液体端口（等温液体）
  direction: conserving
- name: A1
  summary: 液体端口（等温液体）
  direction: conserving
- name: B
  summary: 液体端口（等温液体）
  direction: conserving
```

### 守恒端口

### **A** — 液体端口（等温液体）

阀的入口端口。

### **A1** — 液体端口（等温液体）

阀的入口端口。

### **B** — 液体端口（等温液体）

阀的出口端口。
## 参数
```yaml
parameters:
- name: Pressure at which A-B is fully closed and A1-B is fully open
  summary: 入口 A1 完全打开时的阈值压力 -0.01 MPa（默认）| 标量
  group: ''
- name: Pressure at which A-B is fully open and A1-B is fully closed
  summary: 入口 A 完全打开时的阈值压力 0.01 MPa（默认）| 标量
  group: ''
- name: Maximum opening area
  summary: 最大阀面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Leakage area
  summary: 完全关闭位置时的间隙面积 1e-10 m^2（默认）| 正标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 守恒端口处的面积 inf m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: ''
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| [0,1] 范围内的正标量
  group: ''
- name: Pressure recovery
  summary: 是否考虑面积扩大时的压力增加 Off（默认）| On
  group: ''
- name: Opening dynamics
  summary: 是否引入阀打开导致的流量滞后 Off（默认）| On
  group: ''
- name: Opening time constant
  summary: 阀打开时间常数 0.1 s（默认）| 正标量
  group: ''
```

### **Pressure at which A-B is fully closed and A1-B is fully open** — 入口 A1 完全打开时的阈值压力 `-0.01 MPa`（默认）| 标量

端口 **A** 和 **A1** 之间的压力阈值，低于该值时，端口 **A1** 和 **B** 之间的流路完全打开，端口 **A** 和 **B** 之间的流路完全关闭。

### **Pressure at which A-B is fully open and A1-B is fully closed** — 入口 A 完全打开时的阈值压力 `0.01 MPa`（默认）| 标量

端口 **A** 和 **A1** 之间的压力阈值，高于该值时，端口 **A** 和 **B** 之间的流路完全打开，端口 **A1** 和 **B** 之间的流路完全关闭。

### **Maximum opening area** — 最大阀面积 `1e-4 m^2`（默认）| 正标量

阀的最大打开面积。该值用于确定运行期间的归一化阀压力和阀打开面积。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。任何小于该值的面积都会被饱和到指定的泄漏面积。这通过保持流动的连续性来帮助数值稳定性。

### **Cross-sectional area at ports A and B** — 守恒端口处的面积 `inf m^2`（默认）| 正标量

入口和出口端口 **A**、**A1** 和 **B** 处的面积，用于确定通过阀的质量流量的压力-流量方程中。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过孔口的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值可提高这些工况下仿真的稳定性。

### **Pressure recovery** — 是否考虑面积扩大时的压力增加 `Off`（默认）| `On`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

### **Opening dynamics** — 是否引入阀打开导致的流量滞后 `Off`（默认）| `On`

是否考虑打开阀对流体系统造成的瞬态效应。将 **Opening dynamics** 设置为 `On` 通过在流量响应中引入一阶滞后来近似打开条件。**Opening time constant** 也会影响建模的打开动态。

### **Opening time constant** — 阀打开时间常数 `0.1 s`（默认）| 正标量

捕获将阀从一个位置打开或关闭到另一个位置时流体达到稳态条件所需时间的常数。该参数影响建模的打开动态。

#### 依赖关系

要启用此参数，请将 **Opening dynamics** 设置为 `On`。
## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中的单向切换阀

Shuttle Valve (IL) 模块在等温液体网络中建模一个单向压力控制阀或切换组件。通过阀的流动从端口 **A** 或端口 **A1** 流向端口 **B**。当 **A** 和 **A1** 之间的压差 *p*AA1 高于指定的阈值压力时，端口 **A** 和 **B** 之间的流路打开，**A1** 处的端口关闭。当压力达到 **Pressure at which A-B is fully open and A1-B is fully closed** 时，流路已完全切换。当 *p*AA1 低于阈值压力时，流入口切换到端口 **A1**。

### 质量流量方程

通过阀的质量守恒：

m˙A+m˙A1+m˙B=0。

端口 **A** 和 **A1** 之间没有流动。

通过阀的质量流量计算如下：

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4，

其中：

- *C*d 是 **Discharge coefficient**。
- *A*valve 是阀打开面积，位于端口 **A** 和 **B** 之间或端口 **A1** 和 **B** 之间。
- *A*port 是 **Cross-sectional area at ports A and B**。
- ρ¯ 是平均流体密度。
- *Δp* 是阀压差。根据通过阀的流路，这可以是 *p*A – *p*B、*p*A1 – *p*B，或在两个入口端口之间切换时的归一化压力 p^，定义如下。

临界压差 *Δp*crit 是与 **Critical Reynolds number** *Re*crit 相关的压差，也取决于通过阀的流路：

Δpcrit=πρ¯8Avalve(νRecritCd)2。

临界雷诺数是层流和湍流之间的流态转变点。

*Pressure loss* 描述了由于面积减小而导致的阀中压力降低，并且如果不同的阀流路具有不同的面积，则可能会变化。*PR*loss 计算如下：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport。

*Pressure recovery* 描述了由于面积增加而导致的阀中正压力变化。如果您不想捕获这种压力增加，请将 **Pressure recovery** 设置为 `Off`。在这种情况下，*PR*loss 为 1。

打开面积 *A*valve 也受阀打开动态的影响。

### 打开参数化

阀面积的线性参数化取决于通过阀的流路。动态面积基于端口 **A** 和 **B** 之间的常开路径：

Avalve,AB=p^(Amax−Aleak)+Aleak。

归一化压力 p^ 为

p^=pAA1−popen,A1Bpopen,AB−popen,A1B，

当 *p*AA1 位于参数 **Pressure at which A-B is fully closed and A1-B is fully open** 和 **Pressure at which A-B is fully open and A1-B is fully closed** 之间时。如果 *p*AA1 低于 **Pressure at which A-B is fully closed and A1-B is fully open**，则 p^ 为 0。如果 *p*AA1 高于 **Pressure at which A-B is fully open and A1-B is fully closed**，则 p^ 为 1。

当阀入口从端口 **A** 切换到端口 **A1** 时，阀打开面积为：

Avalve,A1B=Amax+Aleak−Avalve,AB。

当阀在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会在 `0` 和 `1` 之间平滑地饱和归一化控制压力。有关更多信息，请参阅 Numerical Smoothing。

### 打开动态

如果对打开动态进行建模，则会在建模的控制压力中为流量响应引入滞后。*p*control 变为动态控制压力 *p*dyn；否则，*p*control 为稳态压力。动态控制压力的瞬时变化基于 **Opening time constant** *τ* 计算：

p˙dyn,AB=pcontrol−pdyn,ABτ。

默认情况下，**Opening dynamics** 设置为 `Off`。
