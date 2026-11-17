---
type: simulink-block
title: 'Crossover Pilot Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Pilot Models'
documentation_page: 'crossoverpilotmodel'
documentation_source_path: 'crossoverpilotmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Crossover Pilot Model

## 端口
```yaml
ports:
- name: x com
  summary: 信号指令 标量
  direction: input
  data_types: double
- name: x
  summary: 信号 标量
  direction: input
  data_types: double
- name: u
  summary: 飞机指令 标量
  direction: output
  data_types: double
```

### 输入

### **x com** — 信号指令 标量

飞行员模型所控制的信号指令，指定为标量。

**数据类型：** `double`

### **x** — 信号 标量

飞行员模型所控制的信号，指定为标量。

**数据类型：** `double`
### 输出

### **u** — 飞机指令 标量

飞机指令，以标量形式返回。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Type of control
  summary: 动力学控制 Proportional（默认）| Rate or velocity | Spiral divergence | Second order - Short period | Acceleration(*) |
    Roll attitude(*) | Unstable short period(*) | Second order - Phugoid(*)
  group: ''
  block_parameter: sw_popup
  type: 字符向量
  values: '''Proportion'' | ''Rate or velocity'' |''Spiral divergence'' | ''Second order - Short period'' | ''Acceleration(*)''
    | ''Roll attitude(*)'' | ''Unstable short period(*)'' | ''Second order - Phugoid(*)'''
  default: '''Proportion'''
- name: Calculated value
  summary: 穿越频率或飞行员增益 Crossover frequency（默认）| Pilot gain
  group: ''
  block_parameter: freq_gain_popup
  type: 字符向量
  values: '''Crossover frequency'' | ''Pilot gain'''
  default: '''Crossover frequency'''
- name: Controlled element gain
  summary: 被控对象增益 1（默认）| 标量
  group: ''
  block_parameter: Kc
  type: 字符向量
  values: 双精度标量
  default: '''1'''
- name: Pilot gain
  summary: 飞行员增益 3（默认）| 标量
  group: ''
  block_parameter: Kp
  type: 字符向量
  values: 双精度标量
  default: '''3'''
- name: Crossover frequency (rad/s)
  summary: 穿越频率 3（默认）| 1 到 10 范围内的标量
  group: ''
  block_parameter: omega_c
  type: 字符向量
  values: 双精度标量
  default: '''3'''
- name: Pilot time delay(s)
  summary: 飞行员时间延迟 0.1（默认）| 标量
  group: ''
  block_parameter: time_delay
  type: 字符向量
  values: 双精度标量
  default: '''0.1'''
- name: Pilot lead constant
  summary: 飞行员超前常数 1（默认）| 标量
  group: ''
  block_parameter: T
  type: 字符向量
  values: 双精度标量
  default: '''1'''
- name: Pilot lag constant
  summary: 飞行员滞后常数 5（默认）| 标量
  group: ''
  block_parameter: Ti
  type: 字符向量
  values: 双精度标量
  default: '''5'''
```

### **Type of control** — 动力学控制 `Proportional`（默认）| `Rate or velocity` | `Spiral divergence` | `Second order - Short period` | `Acceleration(*)` | `Roll attitude(*)` | `Unstable short period(*)` | `Second order - Phugoid(*)`

您希望飞行员对飞机施加的动力学控制。下表列出了各选项及关联的动力学。

| 选项（被控对象传递函数） | 被控对象传递函数（  *Y c*） | 飞行员传递函数（  *Y p* ） | *Y c*  *Y p* | 备注 |
| --- | --- | --- | --- | --- |
| `Proportion al` | Kc | Kpe−τss | KcKpe−τss |  |
| `Rate or velocity` | Kcs | Kpe−τs | KcKpe−τss |  |
| `Spiral divergence` | KcTIs−1 | Kpe−τs | KcKpe−τs(TIs−1) |  |
| `Second order - Short period` | Kcωn2s2+2ζωns+ωn2 | Kpe−τsTIs+1 | Kcωn2s2+2ζωns+ωn2×Kpe−τsTIs+1 | 短周期，  其中 ωn>1/τ |
| `Acceleration (*)` | Kcs2 | Kpse−τs | KcKpe−τss |  |
| `Roll attitude (*)` | Kcs(TIs+1) | Kp(TLs+1)e−τs | KcKpe−τss | 其中   T L ≈ T I |
| `Unstable short period(*)` | Kc(TI1s+1)(TI2s−1) | Kp(TLs+1)e−τs | KcKpe−τs(TI2s−1) | 其中   T L ≈ T I1 |
| `Second order - Phugoid(*)` | Kcωn2s2+2ζωns+ωn2 | Kp(TLs+1)e−τs | KcKpωn2e−τss | 长周期，  其中 ωn≪1/τ,1/TL≈ζωn |

\* 表示飞行员模型包含 Derivative 模块，该模块会产生数值导数。因此，请勿向 Crossover Pilot Model 模块发送不连续（例如阶跃）或含噪声的输入。此类输入可能导致输出过大，从而使系统不稳定。

下表定义了控制选项列表中使用的变量。

| 变量 | 描述 |
| --- | --- |
| K c | 飞机增益。 |
| K p | 飞行员增益。 |
| τ | 飞行员时间延迟。 |
| T I | 滞后常数。 |
| T L | 超前常数。 |
| ζ | 飞机的阻尼比。 |
| ω n | 飞机的自然频率。 |

#### 依赖关系

Crossover Pilot Model 参数根据 **Type of control** 选项启用和禁用。**Calculated value**、**Controlled element gain**、**Pilot gain**、**Crossover frequency (rad/s)** 和 **Pilot time delay(s)** 参数始终启用。

#### 编程用法

|  |
| --- |
| **模块参数**：`sw_popup` |
| **类型**：字符向量 |
| **值**：`'Proportion'` | `'Rate or velocity'` |`'Spiral divergence'` | `'Second order - Short period'` | `'Acceleration(*)'` | `'Roll attitude(*)'` | `'Unstable short period(*)'` | `'Second order - Phugoid(*)'` |
| **默认值**：`'Proportion'` |

### **Calculated value** — 穿越频率或飞行员增益 `Crossover frequency`（默认）| `Pilot gain`

您希望模块计算的穿越频率或飞行员增益值：

- `Crossover frequency` — 模块计算穿越频率值。该参数值被禁用。
- `Pilot gain` — 模块计算飞行员增益值。该参数值被禁用。

#### 编程用法

|  |
| --- |
| **模块参数**：`freq_gain_popup` |
| **类型**：字符向量 |
| **值**：`'Crossover frequency'` | `'Pilot gain'` |
| **默认值**：`'Crossover frequency'` |

### **Controlled element gain** — 被控对象增益 `1`（默认）| 标量

被控对象增益，指定为双精度标量。

#### 编程用法

|  |
| --- |
| **模块参数**：`Kc` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'1'` |

### **Pilot gain** — 飞行员增益 `3`（默认）| 标量

飞行员增益，指定为双精度标量。

#### 依赖关系

要启用此参数，请将 **Calculated value** 设置为 `Pilot gain`。

#### 编程用法

|  |
| --- |
| **模块参数**：`Kp` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'3'` |

### **Crossover frequency (rad/s)** — 穿越频率 `3`（默认）| 1 到 10 范围内的标量

穿越频率值，指定为双精度标量，单位为 rad/s。该值必须在 1 到 10 之间。

#### 依赖关系

要启用此参数，请将 **Calculated value** 设置为 `Crossover frequency`。

#### 编程用法

|  |
| --- |
| **模块参数**：`omega_c` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'3'` |

### **Pilot time delay(s)** — 飞行员时间延迟 `0.1`（默认）| 标量

飞行员总时间延迟，指定为双精度标量，单位为秒。该值通常在 0.1 s 到 0.2 s 之间。

#### 编程用法

|  |
| --- |
| **模块参数**：`time_delay` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'0.1'` |

### **Pilot lead constant** — 飞行员超前常数 `1`（默认）| 标量

飞行员超前常数，指定为双精度标量。

#### 依赖关系

要启用此参数，请将 **Type of control** 设置为以下选项之一：

- `Roll attitude (*)`
- `Unstable short period (*)`
- `Second order - Phygoid(*)`

#### 编程用法

|  |
| --- |
| **模块参数**：`T` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'1'` |

### **Pilot lag constant** — 飞行员滞后常数 `5`（默认）| 标量

飞行员滞后常数，指定为双精度标量。

#### 依赖关系

要启用此参数，请将 **Type of control** 设置为 `Second order - Short period`。

#### 编程用法

|  |
| --- |
| **模块参数**：`Ti` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'5'` |
## 所属库

Aerospace Blockset / Pilot Models

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

表示穿越飞行员模型

Crossover Pilot Model 模块表示 *Mathematical Models of Human Pilot Behavior* [1] 中描述的飞行员模型。该飞行员模型是单输入单输出（SISO）模型，表示人类在控制飞机时的某些行为方面。

Crossover Pilot Model 考虑人类飞行员和飞机的组合动力学，使用算法中围绕穿越频率描述的形式。

该模块具有非线性行为。如果您想对该模块进行线性化（例如，使用 `linearize` (Simulink Control Design) 或某个 `linmod` 函数），可能需要更改 Pade 近似阶数。Crossover Pilot Model 模块实现包含 Transport Delay 模块，其 **Pade order (for linearization)** 参数默认设置为 `2`。要更改此值，请使用 `set_param` 函数，例如：

```
set_param(gcb,'pade','3')
```

**注意**

`linmod` 函数仅提供基本线性化功能。要获得完整的线性化功能，请使用 Simulink® Control Design™ 软件。有关详细信息，请参阅 Choose Linearization Tools (Simulink Control Design)。

在对人类飞行员模型进行建模时，使用此模块可获得比 Tustin Pilot Model 模块更高的精度。此模块的精度也低于 Precision Pilot Model 模块。
