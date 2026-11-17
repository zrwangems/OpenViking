---
type: simulink-block
title: 'Compound Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Brushed Motors'
documentation_page: 'compoundmotor'
documentation_source_path: 'ref/compoundmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Compound Motor

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
- name: C
  summary: 电机外壳机械
  direction: conserving
- name: R
  summary: 电机转子机械
  direction: conserving
- name: Hs
  summary: 串励磁场绕组热端口热
  direction: conserving
- name: Hp
  summary: 并励磁场绕组热端口热
  direction: conserving
- name: Ha
  summary: 电枢热端口热
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与复合电机正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与复合电机负极端子关联的电气守恒端口。

### **C** — 电机外壳机械

与复合电机外壳关联的机械旋转守恒端口。

### **R** — 电机转子机械

与复合电机转子关联的机械旋转守恒端口。

### **Hs** — 串励磁场绕组热端口热

与串励磁场绕组关联的热守恒端口。有关详细信息，请参阅 Model Thermal Effects。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **Hp** — 并励磁场绕组热端口热

与并励磁场绕组关联的热守恒端口。有关详细信息，请参阅 Model Thermal Effects。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **Ha** — 电枢热端口热

与电枢关联的热守恒端口。有关详细信息，请参阅 Model Thermal Effects。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Electrical circuit topology
  summary: 电路拓扑 Long-shunt（默认）| Short-shunt
  group: 配置
- name: Shunt winding polarity
  summary: 并励绕组极性 Cumulative（默认）| Differential
  group: 配置
- name: Steady-state parameterization
  summary: 模块参数化 By equivalent circuit parameters（默认）| By rated, stall, and no-load datasheet parameters
  group: 稳态
- name: Armature resistance, Ra
  summary: 电枢电阻 1.68 Ohm（默认）| 正标量
  group: 稳态
- name: Series field winding resistance, Rs
  summary: 串励磁场绕组电阻 1.68 Ohm（默认）| 正标量
  group: 稳态
- name: Shunt field winding resistance, Rp
  summary: 并励磁场绕组电阻 303 Ohm（默认）| 正标量
  group: 稳态
- name: Series field winding to armature back EMF constant, Lsa
  summary: 串励磁场绕组对电枢反电动势常数 0.69 H（默认）| 正标量
  group: 稳态
- name: Shunt field winding to armature back EMF constant, Lpa
  summary: 并励磁场绕组对电枢反电动势常数 0.64 H（默认）| 正标量
  group: 稳态
- name: Rated voltage
  summary: 额定电压 100 V（默认）| 正标量
  group: 稳态
- name: Rated speed
  summary: 额定转速 1000 rpm（默认）| 正标量
  group: 稳态
- name: Rated electrical power
  summary: 额定电功率 136 W（默认）| 正标量
  group: 稳态
- name: Rated efficiency (percent)
  summary: 额定效率 85（默认）| 正标量
  group: 稳态
- name: Stall current
  summary: 零速电流 30 A（默认）| 正标量
  group: 稳态
- name: No-load speed
  summary: 空载转速 4500 rpm（默认）| 正标量
  group: 稳态
- name: No-load current
  summary: 空载电流 0.33 A（默认）| 正标量
  group: 稳态
- name: Ratio of shunt field winding resistance divided by series field winding resistance
  summary: 并励磁场绕组电阻除以串励磁场绕组电阻的比值 190（默认）| 非负标量
  group: 稳态
- name: Ratio of armature resistance divided by series field winding resistance
  summary: 电枢电阻除以串励磁场绕组电阻的比值 1.0（默认）| 非负标量
  group: 稳态
- name: Rotor inertia
  summary: 转子惯量 1e-4 kg*m^2（默认）| 标量
  group: 机械
- name: Rotor damping
  summary: 转子耗散能量 1e-6 N*m/(rad/s)（默认）| 标量
  group: 机械
- name: Series field winding inductance, Ls
  summary: 串励磁场绕组电感 0.9 H（默认）| 正标量
  group: 电气动态
- name: Shunt field winding inductance, Lp
  summary: 并励磁场绕组电感 0.85 H（默认）| 正标量
  group: 电气动态
- name: Coefficient of mutual inductance between shunt-series windings, k_sp
  summary: 并励-串励绕组之间的互感系数 0.8（默认）| 0 到 1 之间的非负标量
  group: 电气动态
- name: Resistance temperature coefficient
  summary: 电阻温度系数 3.93e-3 1/K（默认）| 标量
  group: 热
- name: Measurement temperature
  summary: 测量温度 25 degC（默认）| 标量
  group: 热
- name: Thermal masses, [Ms Mp Ma]
  summary: 热质量 [100, 100, 100] J/K（默认）| 向量
  group: 热
- name: Armature winding fault
  summary: 添加电枢绕组故障的选项 Add fault（默认）
  group: 故障
- name: Fraction of revolution during which armature is open-circuit
  summary: 电枢开路期间的旋转比例 1/3（默认）| 标量
  group: 故障
- name: Faulted armature winding open-circuit conductance
  summary: 故障电枢绕组的开路电导 1e-5 S（默认）| 标量
  group: 故障
- name: Trigger type
  summary: 触发类型 Always on（默认）| Timed | Behavioral | Additional triggers | Conditional | Manual
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态前的时间 0 s（默认）| 非负标量
  group: 故障
- name: Maximum permissible armature winding current
  summary: 最大允许电枢绕组电流 inf A（默认）
  group: 故障
- name: Time to fail when exceeding armature winding current
  summary: 超过电枢绕组电流时的故障时间 1 s（默认）| 标量
  group: 故障
- name: Series field winding fault
  summary: 添加串励磁场绕组故障的选项 Add fault（默认）
  group: 故障
- name: Faulted series field winding open-circuit conductance
  summary: 故障磁场绕组的开路电导 1e-5 S（默认）| 标量
  group: 故障
- name: Trigger type
  summary: 触发类型 Always on（默认）| Timed | Behavioral | Additional triggers | Conditional | Manual
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态前的时间 0 s（默认）| 非负标量
  group: 故障
- name: Maximum permissible series field winding current
  summary: 最大允许串励绕组电流 inf A（默认值）
  group: 故障
- name: Time to fail when exceeding series field winding current
  summary: 超过串励绕组电流时的失效时间 1 s（默认值）| 标量
  group: 故障
- name: Trigger configuration
  summary: 启用附加触发类型的选项 Open fault properties
  group: 故障
- name: Shunt field winding fault
  summary: 添加并励绕组故障的选项 Add fault（默认值）
  group: 故障
- name: Faulted shunt field winding open-circuit conductance
  summary: 故障并励绕组的开路电导 1e-5 S（默认值）| 标量
  group: 故障
- name: Trigger type
  summary: 触发类型 Always on（默认值）| Timed | Behavioral | Additional triggers | Conditional | Manual
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态之前的时间 0 s（默认值）| 非负标量
  group: 故障
- name: Maximum permissible shunt field winding current
  summary: 最大允许并励绕组电流 inf A（默认值）
  group: 故障
- name: Time to fail when exceeding shunt field winding current
  summary: 超过并励绕组电流时的失效时间 1 s（默认值）| 标量
  group: 故障
- name: Trigger configuration
  summary: 启用附加触发类型的选项 Open fault properties
  group: 故障
```

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应进行建模。

### 配置

### **Electrical circuit topology** — 电路拓扑 `Long-shunt`（默认）| `Short-shunt`

电路的拓扑结构。

### **Shunt winding polarity** — 并励绕组极性 `Cumulative`（默认）| `Differential`

并励绕组的磁性方向。

### 稳态

### **Steady-state parameterization** — 模块参数化 `By equivalent circuit parameters`（默认）| `By rated, stall, and no-load datasheet parameters`

选择以下方法之一进行模块参数化：

- `By equivalent circuit parameters` — 为电机的等效电路模型提供电气参数。
- `By rated, stall, and no-load datasheet parameters` — 提供电流和转速参数，模块将其转换为电机的等效电路模型。

### **Armature resistance, Ra** — 电枢电阻 `1.68` `Ohm`（默认）| 正标量

电机导通部分的电阻。

#### 依赖关系

要启用此参数，请将 **Steady-state parameterization** 设置为 `By equivalent circuit parameters`。

### **Series field winding resistance, Rs** — 串励磁场绕组电阻 `1.68` `Ohm`（默认）| 正标量

串励磁场绕组的电阻。

#### 依赖关系

要启用此参数，请将 **Steady-state parameterization** 设置为 `By equivalent circuit parameters`。

### **Shunt field winding resistance, Rp** — 并励磁场绕组电阻 `303` `Ohm`（默认）| 正标量

并励磁场绕组的电阻。

#### 依赖关系

要启用此参数，请将 **Steady-state parameterization** 设置为 `By equivalent circuit parameters`。

### **Series field winding to armature back EMF constant, Lsa** — 串励磁场绕组对电枢反电动势常数 `0.69` `H`（默认）| 正标量

串励磁场绕组对电枢反电动势常数。

#### 依赖关系

要启用此参数，请将 **Steady-state parameterization** 设置为 `By equivalent circuit parameters`。

### **Shunt field winding to armature back EMF constant, Lpa** — 并励磁场绕组对电枢反电动势常数 `0.64` `H`（默认）| 正标量

并励磁场绕组对电枢反电动势常数。

#### 依赖关系

要启用此参数，请将 **Steady-state parameterization** 设置为 `By equivalent circuit parameters`。

### **Rated voltage** — 额定电压 `100` `V`（默认）| 正标量

电机额定工作电压。

#### 依赖关系

要启用此参数，请将 **Steady-state parameterization** 设置为 `By rated, stall, and no-load datasheet parameters`。

### **Rated speed** — 额定转速 `1000` `rpm`（默认）| 正标量

电机额定工作转速。

#### 依赖关系

要启用此参数，请将 **Steady-state parameterization** 设置为 `By rated, stall, and no-load datasheet parameters`。

### **Rated electrical power** — 额定电功率 `136` `W`（默认）| 正标量

电机额定工作功率。

#### 依赖关系

要启用此参数，请将 **Steady-state parameterization** 设置为 `By rated, stall, and no-load datasheet parameters`。

### **Rated efficiency (percent)** — 额定效率 `85`（默认）| 正标量

电机额定工作效率，以百分比表示。

#### 依赖关系

要启用此参数，请将 **Steady-state parameterization** 设置为 `By rated, stall, and no-load datasheet parameters`。

### **Stall current** — 零速电流 `30` `A`（默认）| 正标量

转速约为零时电机产生的电流量。此参数必须大于 **No-load current** 参数的值。

#### 依赖关系

要启用此参数，请将 **Steady-state parameterization** 设置为 `By rated, stall, and no-load datasheet parameters`。

### **No-load speed** — 空载转速 `4500` `rpm`（默认）| 正标量

未施加负载时电机的转速。此参数必须大于 **Rated speed** 参数的值。

#### 依赖关系

要启用此参数，请将 **Steady-state parameterization** 设置为 `By rated, stall, and no-load datasheet parameters`。

### **No-load current** — 空载电流 `0.33` `A`（默认）| 正标量

未施加负载时电机的电流。

#### 依赖关系

要启用此参数，请将 **Steady-state parameterization** 设置为 `By rated, stall, and no-load datasheet parameters`。

### **Ratio of shunt field winding resistance divided by series field winding resistance** — 并励磁场绕组电阻除以串励磁场绕组电阻的比值 `190`（默认）| 非负标量

并励磁场绕组电阻除以串励磁场绕组电阻的比值。

#### 依赖关系

要启用此参数，请在 **Configuration** 选项卡中将 **Electrical circuit topology** 设置为 `Short-shunt`，并在 **Steady-state** 选项卡中将 **Steady-state parameterization** 设置为 `By rated, stall, and no-load datasheet parameters`。

### **Ratio of armature resistance divided by series field winding resistance** — 电枢电阻除以串励磁场绕组电阻的比值 `1.0`（默认）| 非负标量

电枢电阻除以串励磁场绕组电阻的比值。

#### 依赖关系

要启用此参数，请在 **Configuration** 选项卡中将 **Electrical circuit topology** 设置为 `Long-shunt`，并在 **Steady-state** 选项卡中将 **Steady-state parameterization** 设置为 `By rated, stall, and no-load datasheet parameters`。

### 机械

### **Rotor inertia** — 转子惯量 `1e-4` `kg*m^2`（默认）| 标量

转子对电机运动变化的阻力。该值可以为零。

### **Rotor damping** — 转子耗散能量 `1e-6` `N*m/(rad/s)`（默认）| 标量

转子耗散的能量。该值可以为零。

#### 依赖关系

要启用此参数，请在 **Steady-State** 选项卡中将 **Steady-state parameterization** 设置为 `By equivalent circuit parameters`。

### 电气动态

### **Series field winding inductance, Ls** — 串励磁场绕组电感 `0.9` `H`（默认）| 正标量

串励磁场绕组的电感。

### **Shunt field winding inductance, Lp** — 并励磁场绕组电感 `0.85` `H`（默认）| 正标量

并励磁场绕组的电感。

### **Coefficient of mutual inductance between shunt-series windings, k\_sp** — 并励-串励绕组之间的互感系数 `0.8`（默认）| `0` 到 `1` 之间的非负标量

并励-串励绕组之间的互感系数。

### 热

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）| 标量

电阻与温度关系方程中的系数 α。默认值为铜的值。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）| 标量

电机参数对应的温度。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **Thermal masses, [Ms Mp Ma]** — 热质量 `[100, 100, 100]` `J/K`（默认）| 向量

1×3 行向量，定义串励和并励磁场绕组以及电枢绕组的热质量。热质量是将温度升高一度所需的能量。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### 故障

### **Armature winding fault** — 添加电枢绕组故障的选项 `Add fault`（默认）

向 Compound Motor 模块的电枢绕组添加故障的选项。

要添加故障，请单击 **Add fault** 超链接。

### **Fraction of revolution during which armature is open-circuit** — 电枢开路期间的旋转比例 `1/3`（默认）| 标量

复合电机旋转过程中电枢绕组发生故障且电压源观察到开路的比例。有关详细信息，请参阅 Faults 部分。

#### 依赖关系

要启用此参数，请单击 **Armature winding fault** 参数的 **Add fault** 超链接。

### **Faulted armature winding open-circuit conductance** — 故障电枢绕组的开路电导 `1e-5` `S`（默认）| 标量

电枢绕组发生故障时的开路电导。

#### 依赖关系

要启用此参数，请单击 **Armature winding fault** 参数的 **Add fault** 超链接。

### **Trigger type** — 触发类型 `Always on`（默认）| `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 故障在仿真时间达到 **Trigger fault at time** 参数指定的值时注入。
- `Behavioral` — 故障在仿真期间根据故障参数值注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障由模块对话框中不可用的附加触发器注入。选择此选项并单击 **Open fault properties** 超链接，在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障由反映信号相关行为的条件注入。条件在每个时间步评估 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。当触发条件首次变为真时，模块进入故障状态，并在仿真的剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为真时模块进入故障状态，当触发条件为假时进入非故障状态。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请单击 **Armature winding fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数，请单击 **Armature winding fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Timed`。

### **Maximum permissible armature winding current** — 最大允许电枢绕组电流 `inf` `A`（默认）

电枢绕组开路故障的负载电流上限阈值。

#### 依赖关系

要启用此参数，请单击 **Armature winding fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding armature winding current** — 超过电枢绕组电流时的故障时间 `1` `s`（默认）| 标量

在触发行为故障之前，绕组电流必须持续超过最大允许电枢绕组电流的时间量。

#### 依赖关系

要启用此参数，请单击 **Armature winding fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Series field winding fault** — 添加串励磁场绕组故障的选项 `Add fault`（默认）

向 Compound Motor 模块的串励磁场绕组添加故障的选项。

要添加故障，请单击 **Add fault** 超链接。

### **Faulted series field winding open-circuit conductance** — 故障磁场绕组的开路电导 `1e-5` `S`（默认）| 标量

串励磁场绕组发生故障时的开路电导。

#### 依赖关系

要启用此参数，请单击 **Series field winding fault** 参数的 **Add fault** 超链接。

### **Trigger type** — 触发类型 `Always on`（默认）| `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 故障在仿真时间达到 **Trigger fault at time** 参数指定的值时注入。
- `Behavioral` — 故障在仿真期间根据故障参数值注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障由模块对话框中不可用的附加触发器注入。选择此选项并单击 **Open fault properties** 超链接，在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障由反映信号相关行为的条件注入。条件在每个时间步评估 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。当触发条件首次变为真时，模块进入故障状态，并在仿真的剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为真时模块进入故障状态，当触发条件为假时进入非故障状态。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请单击 **Series field winding fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数，请为 **Series field winding fault** 参数点击 **Add fault** 超链接，并将 **Trigger type** 设置为 `Timed`。

### **Maximum permissible series field winding current** — 最大允许串励绕组电流 `inf` `A`（默认值）

串励绕组开路故障的负载电流上限阈值。

#### 依赖关系

要启用此参数，请为 **Series field winding fault** 参数点击 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding series field winding current** — 超过串励绕组电流时的失效时间 `1` `s`（默认值）| 标量

在触发行为故障之前，绕组电流必须持续超过最大允许串励绕组电流的时间量。

#### 依赖关系

要启用此参数，请为 **Series field winding fault** 参数点击 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Trigger configuration** — 启用附加触发类型的选项 `Open fault properties`

用于启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数，请为 **Series field winding fault** 参数点击 **Add fault** 超链接，并将 **Trigger type** 设置为 `Additional triggers`。

### **Shunt field winding fault** — 添加并励绕组故障的选项 `Add fault`（默认值）

用于向 Compound Motor 模块的并励绕组添加故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Faulted shunt field winding open-circuit conductance** — 故障并励绕组的开路电导 `1e-5` `S`（默认值）| 标量

并励绕组发生故障时的开路电导。

#### 依赖关系

要启用此参数，请为 **Shunt field winding fault** 参数点击 **Add fault** 超链接。

### **Trigger type** — 触发类型 `Always on`（默认值）| `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 当仿真时间达到 **Trigger fault at time** 参数指定的值时，故障注入。
- `Behavioral` — 故障根据仿真期间的故障参数值注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障根据模块对话框中不可用的附加触发器注入。选择此选项并点击 **Open fault properties** 超链接，以在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障根据反映信号相关行为的条件注入。条件在每个时间步评估 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。当触发条件首次变为 true 时，模块进入故障状态，并在仿真的剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入无故障状态。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请为 **Shunt field winding fault** 参数点击 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认值）| 非负标量

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数，请为 **Shunt field winding fault** 参数点击 **Add fault** 超链接，并将 **Trigger type** 设置为 `Timed`。

### **Maximum permissible shunt field winding current** — 最大允许并励绕组电流 `inf` `A`（默认值）

并励绕组开路故障的负载电流上限阈值。

#### 依赖关系

要启用此参数，请为 **Shunt field winding fault** 参数点击 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding shunt field winding current** — 超过并励绕组电流时的失效时间 `1` `s`（默认值）| 标量

在触发行为故障之前，绕组电流必须持续超过最大允许并励绕组电流的时间量。

#### 依赖关系

要启用此参数，请为 **Shunt field winding fault** 参数点击 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Trigger configuration** — 启用附加触发类型的选项 `Open fault properties`

用于启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数，请为 **Shunt field winding fault** 参数点击 **Add fault** 超链接，并将 **Trigger type** 设置为 `Additional triggers`。
## 所属库

Simscape / Electrical / Electromechanical / Brushed Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2025a：对可逆条件故障建模

您现在可以通过清除 **Trigger stays on once activated** 参数，在 Compound Motor 模块中对可逆条件故障建模。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入无故障状态。

在 R2025a 之前，当触发条件首次变为 true 时，模块进入故障状态，并在仿真的剩余时间内保持故障状态。

如果您在 R2025a 之前创建了模型，并在 Compound Motor 模块中启用了条件故障，则为了向后兼容，该模块现在默认选择 **Trigger stays on once activated** 参数。

## 描述

具有电气和转矩特性以及故障建模的复励电机模型

Compound Motor 模块表示复励电机的电气和转矩特性。此图显示了短并复励电机的等效电路：

短并复励电机模型

此图显示了长并复励电机的等效电路：

长并复励电机模型

其中：

- *i* 是总电流。
- *is* 是串励绕组电流。
- *ip* 是并励绕组电流。
- *ia* 是电枢电流。
- *V* 是总电压。
- *Vs* 是串励绕组电压。
- *Vp* 是并励绕组电压。
- *Va* 是电枢电压。
- *ω* 是角速度。
- *te* 是转矩。

如果将 **Steady-state parameterization** 参数设置为 `By equivalent circuit parameters`，则可以为该模型指定等效电路参数：

- *Ra* — **Armature resistance, Ra**
- *Rs* — **Series field winding resistance, Rs**
- *Rp* — **Shunt field winding resistance, Rp**
- *Lsa* — **Series field winding to armature back EMF constant, Lsa**
- *Lpa* — **Shunt field winding to armature back EMF constant, Lpa**

### 短并复励方程

当 **Electrical circuit topology** 设置为 `Short-shunt` 时，电气动态方程为：

Vs=Rsis+Lsdisdt+LspdipdtVp=Rpip+Lpdipdt+LspdisdtVemf=kvω=(Lsais+Lpaip)ωV=Vs+VpVp=kvω+Raiai=isia=is−ip

以下是短并复励电机的机械动态方程：

Jω˙+Dω=te+tloadte=kvia=(Lsais+Lpaip)ia

根据这些动态方程，模块通过令导数为零来获得稳态方程：

Vemf=Lsaisω+Lpaipωtelec=kv(is−ip)=Vemfis−ipωV=Rsis+RpipRpip=Vemf+Ra(is−ip)

然后，它按如下方式计算稳态电流和转矩：

telec(ω,V)=−V2(Lpaω+Lsaω−Rp)(RaLpa+RaLsa+RpLsa)(RaRp+RaRs+RpRs+LsaRpω−LpaRsω)2i=is(ω,V)=V(Ra+Rp−Lpaω)RaRp+RaRs+RpRs+LsaRpω−LpaRsω

### 长并复励方程

当 **Electrical circuit topology** 设置为 `Long-shunt` 时，电气动态方程为：

Vs=Rsis+Lsdisdt+LspdipdtVp=Rpip+Lpdipdt+LspdisdtVemf=kvω=(Lsais+Lpaip)ωV=VpVp=kvω+Raia+Vsi=is+ipia=is

以下是长并复励电机的机械动态方程：

Jω˙+Dω=te+tloadte=kvia=(Lsais+Lpaip)ia

根据这些动态方程，模块通过令导数为零来获得稳态方程：

Vemf=Lsaisω+Lpaipωtelec=kvis=VemfisωV=RpipRpip=Vemf+(Ra+Rs)is

然后，它按如下方式计算稳态电流和转矩：

telec(ω,V)=V2(Ra−Lpaω)(RaLpa+RsLpa+RpLsa)Rp2(Ra+Rs+Lsaω)2i(ω,V)=is+ip=VRp+RpV−LpaVωRp(Ra+Rs+Lsaω)

### 故障

要对 Compound Motor 模块中的故障建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

Compound Motor 模块允许您对三种类型的故障建模：

- 电枢绕组故障 — 电枢绕组失效并变为开路。
- 串励绕组故障 — 串励绕组失效并变为开路。
- 并励绕组故障 — 并励绕组失效并变为开路。

当电枢失效时，连接到此模块的电压源会在电机总转数的一小部分时间内观察到开路，该部分由 **Fraction of revolution during which armature is open-circuit** 参数指定。此图说明了在一个旋转周期内的电路状态行为和开路状态（`rev_faulted`）：

**故障触发器**

您可以使用 **Trigger type** 参数指定故障发生的方式和时间。

如果将 **Trigger type** 设置为 `Behavioral`，则当绕组电流持续超过阈值的时间长于特定时间间隔时，Compound Motor 模块会触发故障：

- 当绕组电流持续超过 **Maximum permissible armature winding current** 参数的值，且持续时间长于 **Time to fail when exceeding armature winding current** 参数的值时，会发生电枢绕组故障。
- 当绕组电流超过 **Maximum permissible series field winding current** 参数的值，且持续时间长于 **Time to fail when exceeding series field winding current** 参数的值时，会发生串励绕组故障。
- 当绕组电流超过 **Maximum permissible shunt field winding current** 参数的值，且持续时间长于 **Time to fail when exceeding shunt field winding current** 参数的值时，会发生并励绕组故障。

如果将 **Trigger type** 设置为 `Conditional`，您可以选择 Compound Motor 模块中的故障是否为可逆故障*（自 R2025a 起）*。要对不可逆故障建模，请点击 **Open fault properties** 以打开 Property Inspector，并选择 **Trigger stays on once activated** 参数。当触发条件首次变为 true 时，模块进入故障状态，并在仿真的剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入无故障状态。

有关向模块添加故障和指定故障触发器的详细信息，请参阅 Introduction to Simscape Faults。

### 对热效应建模

您可以暴露热端口，以对将功率转换为热量的损耗效应建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含串励绕组、并励绕组和电枢的守恒热端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。
