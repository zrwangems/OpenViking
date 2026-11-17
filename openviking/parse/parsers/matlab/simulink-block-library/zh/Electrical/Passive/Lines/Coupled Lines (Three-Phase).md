---
type: simulink-block
title: 'Coupled Lines (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Lines'
documentation_page: 'coupledlinesthreephase'
documentation_source_path: 'ref/coupledlinesthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Coupled Lines (Three-Phase)

## 端口
```yaml
ports:
- name: ~1
  summary: 线路正极端口 electrical
  direction: conserving
- name: ~2
  summary: 线路负极端口 electrical
  direction: conserving
- name: a1
  summary: 线路 *a* 正极端口 electrical
  direction: conserving
- name: a2
  summary: 线路 *a* 负极端口 electrical
  direction: conserving
- name: b1
  summary: 线路 *b* 正极端口 electrical
  direction: conserving
- name: b2
  summary: 线路 *b* 负极端口 electrical
  direction: conserving
- name: c1
  summary: 线路 *c* 正极端口 electrical
  direction: conserving
- name: c2
  summary: 线路 *c* 负极端口 electrical
  direction: conserving
```

### 守恒端口

### **~1** — 线路正极端口 electrical

可扩展三相
电气守恒端口，与线路 *a*、*b* 和
*c* 的正极
端子关联。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Composite three-phase
ports`

### **~2** — 线路负极端口 electrical

可扩展三相
电气守恒端口，与线路 *a*、*b* 和
*c* 的负极端子
关联。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Composite three-phase
ports`

### **a1** — 线路 *a* 正极端口 electrical

与线路 *a* 正极端子关联的
电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`

### **a2** — 线路 *a* 负极端口 electrical

与线路 *a* 负极端子关联的
电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`

### **b1** — 线路 *b* 正极端口 electrical

与线路 *b* 正极端子关联的
电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`

### **b2** — 线路 *b* 负极端口 electrical

与线路 *b* 负极端子关联的
电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`

### **c1** — 线路 *c* 正极端口 electrical

与线路 *c* 正极端子关联的
电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`

### **c2** — 线路 *c* 负极端口 electrical

与线路 *c* 负极端子关联的
电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical
connection** 设置为 `Expanded three-phase
ports`
## 参数
```yaml
parameters:
- name: Electrical connection
  summary: 建模为复合三相端口还是扩展三相端口 Composite three-phase ports（默认）| Expanded three-phase ports
  group: 主要
- name: Parameterization
  summary: 线路阻抗参数化方式 Balanced impedance（默认）| General impedance
  group: 主要
- name: Line a inductance
  summary: 线路 *a* 自感 1e-3 H（默认）| 正标量
  group: 主要
- name: Line b inductance
  summary: 线路 *b* 自感 1e-3 H（默认）| 正标量
  group: 主要
- name: Line c inductance
  summary: 线路 *c* 自感 1e-3 H（默认）| 正标量
  group: 主要
- name: Line inductance
  summary: 自感 1e-3 H（默认）| 正标量
  group: 主要
- name: Line a-b mutual inductance
  summary: '*a*-*b* 之间的互感 3e-4 H（默认）| 正标量'
  group: 主要
- name: Line b-c mutual inductance
  summary: '*b*-*c* 之间的互感 3e-4 H（默认）| 正标量'
  group: 主要
- name: Line a-c mutual inductance
  summary: '*a*-*c* 之间的互感 3e-4 H（默认）| 正标量'
  group: 主要
- name: Mutual inductance
  summary: 互感 3e-4 H（默认）| 正标量
  group: 主要
- name: Line a resistance
  summary: 线路 *a* 串联电阻 0.001 Ohm（默认）| 非负标量
  group: 电阻
- name: Line b resistance
  summary: 线路 *b* 串联电阻 0.001 Ohm（默认）| 非负标量
  group: 电阻
- name: Line c resistance
  summary: 线路 *c* 串联电阻 0.001 Ohm（默认）| 非负标量
  group: 电阻
- name: Line a-b mutual resistance
  summary: '*a*-*b* 之间的互阻 0 Ohm（默认）| 非负标量'
  group: 电阻
- name: Line a-c mutual resistance
  summary: '*a*-*c* 之间的互阻 0 Ohm（默认）| 非负标量'
  group: 电阻
- name: Line b-c mutual resistance
  summary: '*b*-*c* 之间的互阻 0 Ohm（默认）| 非负标量'
  group: 电阻
- name: Line resistance
  summary: 串联电阻 0.001 Ohm（默认）| 非负标量
  group: 电阻
- name: Mutual resistance
  summary: 互阻 0 Ohm（默认）| 非负标量
  group: 电阻
- name: Line a leakage conductance
  summary: 线路 *a* 并联泄漏电导 1e-9 1/Ohm（默认）| 非负标量
  group: 电阻
- name: Line b leakage conductance
  summary: 线路 *b* 并联泄漏电导 1e-9 1/Ohm（默认）| 非负标量
  group: 电阻
- name: Line c leakage conductance
  summary: 线路 *c* 并联泄漏电导 1e-9 1/Ohm（默认）| 非负标量
  group: 电阻
- name: Line leakage conductance
  summary: 并联泄漏电导 1e-9 1/Ohm（默认）| 非负标量
  group: 电阻
- name: Port 1 connection fault
  summary: 向端口 1 添加故障的选项 Add fault
  group: 故障
- name: Fault type
  summary: 故障类型 Single-phase to ground (a-g)（默认）| Single-phase to ground (b-g) | Single-phase to ground (c-g) | Two-phase
    (a-b) | Two-phase (b-c) | Two-phase (c-a) | Two-phase to ground (a-b-g) | Two-phase to ground (b-c-g) | Two-phase to ground
    (c-a-g) | Three-phase (a-b-c) | Three-phase to ground (a-b-c-g)
  group: 故障
- name: Faulted phase-neutral resistance
  summary: 故障时相连接与中性点之间的电阻 1e-3 Ohm（默认）| 正标量
  group: 故障
- name: Faulted neutral-ground resistance
  summary: 故障时中性点与电气参考之间的电阻 1e-3 Ohm（默认）| 正标量
  group: 故障
- name: Unfaulted phase-neutral conductance
  summary: 未故障时相连接与中性点之间的电导 1e-6 1/Ohm（默认）| 正标量
  group: 故障
- name: Trigger type
  summary: 触发类型 Always on（默认）| Timed | Additional triggers | Conditional | Manual
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态之前的时间 0 s（默认）| 非负标量
  group: 故障
- name: Trigger configuration
  summary: 启用附加触发类型的选项 Open fault properties
  group: 故障
- name: Port 2 connection fault
  summary: 向端口 2 添加故障的选项 Add fault
  group: 故障
- name: Fault type
  summary: 故障类型 Single-phase to ground (a-g)（默认）| Single-phase to ground (b-g) | Single-phase to ground (c-g) | Two-phase
    (a-b) | Two-phase (b-c) | Two-phase (c-a) | Two-phase to ground (a-b-g) | Two-phase to ground (b-c-g) | Two-phase to ground
    (c-a-g) | Three-phase (a-b-c) | Three-phase to ground (a-b-c-g)
  group: 故障
- name: Faulted phase-neutral resistance
  summary: 故障时相连接与中性点之间的电阻 1e-3 Ohm（默认）| 正标量
  group: 故障
- name: Faulted neutral-ground resistance
  summary: 故障时中性点与电气参考之间的电阻 1e-3 Ohm（默认）| 正标量
  group: 故障
- name: 未故障相-中性点电导
  summary: 故障未激活时相连接与中性点之间的未故障电导 1e-6 1/Ohm（默认）| 正标量
  group: 故障
- name: 触发类型
  summary: 触发类型 始终开启（默认）| 定时 | 附加触发 | 条件 | 手动
  group: 故障
- name: 在以下时间触发故障
  summary: 进入故障状态之前的时间 0 s（默认）| 非负标量
  group: 故障
- name: 触发配置
  summary: 启用附加触发类型的选项 打开故障属性
  group: 故障
```

### 主要

### **Electrical connection** — 建模为复合三相端口还是扩展三相端口 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

建模为复合三相端口还是扩展三相端口。

复合三相端口用单个模块端口表示三个独立的电气
守恒端口。您可以使用复合
三相端口来构建与三相电气系统单线
图对应的模型。

扩展三相端口使用三个独立的电气守恒
端口来表示三相系统的各个相。

### **Parameterization** — 线路阻抗参数化方式 `Balanced impedance`（默认）| `General impedance`

指定如何参数化三条线路的阻抗：

- `Balanced impedance` — 为所有线路指定
  相同的串联电阻、串联电感和并联
  泄漏电导。
- `General impedance` — 分别为每条线路指定
  串联电阻、串联电感和并联泄漏
  电导。

### **Line a inductance** — 线路 *a* 自感 `1e-3` `H`（默认）| 正标量

线路 *a* 的自感。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line b inductance** — 线路 *b* 自感 `1e-3` `H`（默认）| 正标量

线路 *b* 的自感。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line c inductance** — 线路 *c* 自感 `1e-3` `H`（默认）| 正标量

线路 *c* 的自感。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line inductance** — 自感 `1e-3` `H`（默认）| 正标量

线路 *a*、*b* 和 *c* 的
自感。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Balanced
impedance`。

### **Line a-b mutual inductance** — *a*-*b* 之间的互感 `3e-4` `H`（默认）| 正标量

线路 *a* 和 *b* 之间的
互感。如果已知耦合系数，请将此
值设置为 kLaLb。要使互感在物理上可实现，
此值必须满足：

−LaLb<Lm,ab<LaLb。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line b-c mutual inductance** — *b*-*c* 之间的互感 `3e-4` `H`（默认）| 正标量

线路 *b* 和 *c* 之间的
互感。如果已知耦合系数，请将此
值设置为 kLbLc。要使互感在物理上可实现，
此值必须满足：

−LbLc<Lm,bc<LbLc。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line a-c mutual inductance** — *a*-*c* 之间的互感 `3e-4` `H`（默认）| 正标量

线路 *a* 和 *c* 之间的
互感。如果已知耦合系数，请将此
值设置为 kLaLc。要使互感在物理上可实现，
此值必须满足：

−LaLc<Lm,ac<LaLc。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Mutual inductance** — 互感 `3e-4` `H`（默认）| 正标量

每对线路之间的互感。如果已知耦合
系数，请将此值设置为 *kL*，其中
*L* 是每条线路的串联电感。
要使互感在物理上可实现，此值必须满足：

−L<Lm<L。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Balanced
impedance`。

### 电阻

### **Line a resistance** — 线路 *a* 串联电阻 `0.001` `Ohm`（默认）| 非负标量

线路 *a* 的串联电阻。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line b resistance** — 线路 *b* 串联电阻 `0.001` `Ohm`（默认）| 非负标量

线路 *b* 的串联电阻。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line c resistance** — 线路 *c* 串联电阻 `0.001` `Ohm`（默认）| 非负标量

线路 *c* 的串联电阻。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line a-b mutual resistance** — *a*-*b* 之间的互阻 `0` `Ohm`（默认）| 非负标量

*自 R2025a 起*

线路 *a* 和 *b* 之间的
互阻。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line a-c mutual resistance** — *a*-*c* 之间的互阻 `0` `Ohm`（默认）| 非负标量

*自 R2025a 起*

线路 *a* 和 *c* 之间的
互阻。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line b-c mutual resistance** — *b*-*c* 之间的互阻 `0` `Ohm`（默认）| 非负标量

*自 R2025a 起*

线路 *b* 和 *c* 之间的
互阻。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line resistance** — 串联电阻 `0.001` `Ohm`（默认）| 非负标量

线路 *a*、*b* 和 *c* 的
串联电阻。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Balanced
impedance`。

### **Mutual resistance** — 互阻 `0` `Ohm`（默认）| 非负标量

每对线路之间的互阻。使用此值来
考虑公共返回路径中的损耗。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Balanced
impedance`。

### **Line a leakage conductance** — 线路 *a* 并联泄漏电导 `1e-9` `1/Ohm`（默认）| 非负标量

线路 *a* 的并联泄漏电导。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line b leakage conductance** — 线路 *b* 并联泄漏电导 `1e-9` `1/Ohm`（默认）| 非负标量

线路 *b* 的并联泄漏电导。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line c leakage conductance** — 线路 *c* 并联泄漏电导 `1e-9` `1/Ohm`（默认）| 非负标量

线路 *a* 的并联泄漏电导。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `General
impedance`。

### **Line leakage conductance** — 并联泄漏电导 `1e-9` `1/Ohm`（默认）| 非负标量

线路 *a*、*b* 和 *c* 的
并联泄漏电导。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Balanced
impedance`。

### 故障

### **Port 1 connection fault** — 向端口 1 添加故障的选项 `Add fault`

*自 R2025a 起*

向模块的三相连接端口
**~1** 添加故障的选项。

要添加故障，请单击 **Add fault**
超链接。

### **Fault type** — 故障类型 `Single-phase to ground (a-g)`（默认）| `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

*自 R2025a 起*

要建模的故障类型。相关参数的可见性
取决于故障模型。

#### 依赖关系

要启用此参数，请单击 **Port 1 connection fault** 参数的
**Add fault** 超链接。

### **Faulted phase-neutral resistance** — 故障时相连接与中性点之间的电阻 `1e-3` `Ohm`（默认）| 正标量

*自 R2025a 起*

故障激活时相连接与中性点之间的
电阻。

#### 依赖关系

要启用此参数，请单击 **Port 1 connection fault** 参数的
**Add fault** 超链接，并将
**Fault type** 设置为以下选项之一：

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground
  (a-b-c-g)`

### **Faulted neutral-ground resistance** — 故障时中性点与电气参考之间的电阻 `1e-3` `Ohm`（默认）| 正标量

*自 R2025a 起*

故障激活时中性点与电气参考之间的
电阻。

#### 依赖关系

要启用此参数，请单击 **Port 1 connection fault** 参数的
**Add fault** 超链接，并将
**Fault type** 设置为以下选项之一：

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase to ground
  (a-b-c-g)`

### **Unfaulted phase-neutral conductance** — 未故障时相连接与中性点之间的电导 `1e-6` `1/Ohm`（默认）| 正标量

*自 R2025a 起*

故障未激活时相连接与中性点之间的
电导。

#### 依赖关系

要启用此参数，请单击 **Port 1 connection fault** 参数的
**Add fault** 超链接，并将
**Fault type** 设置为以下选项之一：

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground
  (a-b-c-g)`

### **Trigger type** — 触发类型 `Always on`（默认）| `Timed` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时
  注入。
- `Timed` — 当仿真时间达到您为 **Trigger fault at time**
  参数指定的值时，故障
  注入。
- `Additional triggers` — 故障因模块对话框中不可用的附加触发器
  而注入。选择此选项
  并单击 **Open fault properties** 超链接，以在属性检查器中将
  **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障因反映与信号相关行为的条件
    而注入。
    条件在每个时间步评估
    **Condition** 参数中的布尔表达式。要了解
    更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，
    故障注入或清除。
    要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请单击 **Port 1 connection fault**
参数的 **Add fault**
超链接。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请单击 **Port 1 connection fault** 参数的 **Add fault** 超链接，并将
**Trigger type** 设置为
`Timed`。

### **Trigger configuration** — 启用附加触发类型的选项 `Open fault properties`

启用模块对话框中不可用的附加触发类型的选项。要将
**Trigger type** 参数设置为 `Conditional` 或
`Manual`，请单击 **Open fault properties**
超链接，并在属性检查器中设置 **Trigger type**。

要启用此参数，请单击 **Port 1 connection fault** 参数的 **Add fault** 超链接，并将
**Trigger type** 设置为
`Additional triggers`。

### **Port 2 connection fault** — 向端口 2 添加故障的选项 `Add fault`

*自 R2025a 起*

向模块的三相连接端口
**~2** 添加故障的选项。

要添加故障，请单击 **Add fault**
超链接。

### **Fault type** — 故障类型 `Single-phase to ground (a-g)`（默认）| `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

*自 R2025a 起*

要建模的故障类型。相关参数的可见性
取决于故障模型。

#### 依赖关系

要启用此参数，请单击 **Port 2 connection fault**
参数的 **Add fault**
超链接。

### **Faulted phase-neutral resistance** — 故障时相连接与中性点之间的电阻 `1e-3` `Ohm`（默认）| 正标量

*自 R2025a 起*

故障激活时相连接与中性点之间的
电阻。

#### 依赖关系

要启用此参数，请单击 **Port 2 connection fault**
参数的 **Add fault**
超链接，并将 **Fault type** 设置为以下选项之一：

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground
  (a-b-c-g)`

### **Faulted neutral-ground resistance** — 故障时中性点与电气参考之间的电阻 `1e-3` `Ohm`（默认）| 正标量

*自 R2025a 起*

故障激活时中性点与电气参考之间的
电阻。

#### 依赖项

要启用此参数，请为 **端口 2 连接故障** 参数点击 **添加故障** 超链接，并将 **故障类型** 设置为以下选项之一：

- `单相接地 (a-g)`
- `单相接地 (b-g)`
- `单相接地 (c-g)`
- `两相接地 (a-b-g)`
- `两相接地 (b-c-g)`
- `两相接地 (c-a-g)`
- `三相接地 (a-b-c-g)`

### **未故障相-中性点电导** — 故障未激活时相连接与中性点之间的未故障电导 `1e-6` `1/Ohm`（默认）| 正标量

*自 R2025a 起*

故障未激活时，相连接与中性点之间的电导。

#### 依赖项

要启用此参数，请为 **端口 2 连接故障** 参数点击 **添加故障** 超链接，并将 **故障类型** 设置为以下选项之一：

- `单相接地 (a-g)`
- `单相接地 (b-g)`
- `单相接地 (c-g)`
- `两相 (a-b)`
- `两相 (b-c)`
- `两相 (c-a)`
- `两相接地 (a-b-g)`
- `两相接地 (b-c-g)`
- `两相接地 (c-a-g)`
- `三相 (a-b-c)`
- `三相接地 (a-b-c-g)`

### **触发类型** — 触发类型 `始终开启`（默认）| `定时` | `附加触发` | `条件` | `手动`

触发类型，指定为以下选项之一：

- `始终开启` — 故障在仿真开始时注入。
- `定时` — 故障在仿真时间达到 **在以下时间触发故障** 参数指定的值时注入。
- `附加触发` — 故障由模块对话框中不可用的附加触发引起。选择此选项并点击 **打开故障属性** 超链接，在属性检查器中将 **触发类型** 设置为以下值之一：

  - `条件` — 故障由反映信号相关行为的条件引起。条件在每个时间步评估 **条件** 参数中的布尔表达式。要了解更多信息，请参阅创建和管理条件。
  - `手动` — 故障在 **故障仪表板** 窗格中切换状态时注入或清除。要了解更多信息，请参阅在模型中手动触发故障。

#### 依赖项

要启用此参数，请为 **端口 2 连接故障** 参数点击 **添加故障** 超链接。

### **在以下时间触发故障** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态时的仿真时间。

#### 依赖项

要启用此参数，请为 **端口 2 连接故障** 参数点击 **添加故障** 超链接，并将 **触发类型** 设置为 `定时`。

### **触发配置** — 启用附加触发类型的选项 `打开故障属性`

用于启用模块对话框中不可用的附加触发类型的选项。要将 **触发类型** 参数设置为 `条件` 或 `手动`，请点击 **打开故障属性** 超链接，并在属性检查器中设置 **触发类型**。

要启用此参数，请为 **端口 2 连接故障** 参数点击 **添加故障** 超链接，并将 **触发类型** 设置为 `附加触发`。
## 所属库

Simscape / Electrical / Passive / Lines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2025a：在三个相连接端口处对故障建模

现在，您可以在模块的两个三相连接端口中的每一个处对相接地故障或相间故障进行建模。要指定故障电阻和未故障电导的值，请使用 **故障相-中性点电阻**、**故障中性点-接地电阻** 和 **未故障相-中性点电导** 参数。

### R2025a：**建模选项** 参数已更改

**建模选项** 参数已被模块对话框或属性检查器中 **主要** 部分内的 **电气连接** 参数替换。

如果您在早期版本中创建的模型包含此模块，软件会自动将 **电气连接** 参数的值设置为您为 **建模选项** 参数指定的值。

## 描述

磁耦合三相线路

Coupled Lines (Three-Phase) 模块对三条磁耦合线路进行建模。每条线路具有自感、串联电阻和并联电导。此外，每对线路之间存在互感 and 互阻。

当三相网络中的磁耦合不可忽略时，请使用此模块。这些效应在以下情况下最为显著：

- 线路平行且彼此靠近。
- 线路的自感较高。
- 网络的交流频率较高。

要对单对线路的磁耦合进行建模，请使用 Coupled Lines (Pair) 模块。要对线路之间的电容耦合进行建模，请使用 Transmission Line 模块。

### 等效电路

等效电路显示了两个任意相 *i* 和 *j* 之间的耦合。该模块使用此类等效电路在三个相 *a*、*b* 和 *c* 的每一对之间对磁耦合进行建模。

在此图中：

- *Ri* 和 *Rj* 分别是线路 *i* 和 *j* 的串联电阻。
- *Li* 和 *Lj* 分别是线路 *i* 和 *j* 的自感。
- *Rm,ij* 分别是线路 *i* 和 *j* 之间的互阻。
- *Lm,ij* 分别是线路 *i* 和 *j* 之间的互感。
- *Gi* 和 *Gj* 分别是线路 *i* 和 *j* 的泄漏电导。
- *Vi* 和 *Vj* 分别是线路 *i* 和 *j* 上的电压降。
- *Ii* 和 *Ij* 分别是流过电阻 *Ri-Rm,ij* 和 *Rj-Rm,ij* 的电流。

### 方程

此模块的定义方程为：

V=[RaRm,abRm,acRm,abRbRm,bcRm,acRm,bcRc]I+[LaLm,abLm,acLm,abLbLm,bcLm,acLm,bcLc]dIdt,

其中：

V=[VaVbVc],

I=[IaIbIc].

*Ia*、*Ib* 和 *Ic* 通常不等于线路 *a*、*b* 和 *c* 中的电流。这些端子电流构成向量：

Itotal=I+[Ga000Gb000Gc]V.

### 电感耦合

要量化两条线路之间耦合的强度，可以使用耦合因子或耦合系数 *k*。耦合因子将互感与线路自感关联起来：

Lm,ij=kLiLj.

此耦合因子必须落在 −1<k<1 范围内，其中负耦合因子表示其中一个线圈的取向反转。*k* 的大小表示：

- |k|=0 — 两条线路之间没有磁耦合。
- 0<|k|<0.5 — 两条线路为松耦合，互感磁效应较小。
- 0.5≤|k|<1 — 两条线路为强耦合，互感磁效应较大。

### 互阻

如果三条线路共享公共返回路径，您可以使用 **互阻** 参数 *Rm* 对该返回路径的电阻进行建模。此工作流程等效于将 **互阻** 设置为零并显式建模返回路径电阻 *Rm*，如此图所示。

如果三条线路不共享公共返回路径，请将互阻参数设置为零并显式建模每个返回电阻。

### 故障

*自 R2025a 起*

要对 Coupled Lines (Three-Phase) 模块中的故障进行建模，请在 **故障** 部分中，点击要建模的故障旁边的 **添加故障**。有关故障建模的详细信息，请参阅故障行为建模和故障触发。

Coupled Lines (Three-Phase) 模块允许您对以下类型的故障进行建模：

- 单相接地故障（a-g、b-g 或 c-g）
- 两相故障（a-b、b-c 或 c-a）
- 两相接地故障（a-b-g、b-c-g 或 c-a-g）
- 三相故障（a-b-c）
- 三相接地故障（a-b-c-g）

您可以在两个三相连接端口之一处或同时在两个端口处对故障进行建模。

此图显示了该模块如何对两个三相端口处的故障进行建模：

有关向模块添加故障和指定故障触发的详细信息，请参阅 Simscape 故障简介。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅按标称值进行系统缩放。
