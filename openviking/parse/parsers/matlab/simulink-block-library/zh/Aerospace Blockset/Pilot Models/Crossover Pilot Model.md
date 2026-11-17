---
type: simulink-block
title: 'Crossover Pilot Model'
family: 'pilot-models'
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

### 输入

### **x com** — 信号指令标量

由飞行员模型控制的信号指令，指定为标量。

**数据类型：** `double`

### **x** — 信号标量

由飞行员模型控制的信号，指定为标量。

**数据类型：** `double`
### 输出

### **u** — 飞机指令标量

飞机指令，以标量形式返回。

**数据类型：** `double`

## 参数

### **Type of control** — 动力学控制 `Proportional`（默认）| `Rate or velocity` | `Spiral divergence` | `Second order - Short period` | `Acceleration(*)` | `Roll attitude(*)` | `Unstable short period(*)` | `Second order - Phugoid(*)`

希望飞行员对飞机拥有的动力学控制。下表列出了选项及相关动力学。

| 选项（受控元件传递函数） | 受控元件传递函数 (  *Y c*) | 飞行员传递函数 (  *Y p* ) | *Y c*  *Y p* | 注释 |
| --- | --- | --- | --- | --- |
| `Proportion al` | Kc | Kpe−τss | KcKpe−τss |  |
| `Rate or velocity` | Kcs | Kpe−τs | KcKpe−τss |  |
| `Spiral divergence` | KcTIs−1 | Kpe−τs | KcKpe−τs(TIs−1) |  |
| `Second order - Short period` | Kcωn2s2+2ζωns+ωn2 | Kpe−τsTIs+1 | Kcωn2s2+2ζωns+ωn2×Kpe−τsTIs+1 | Short   period,   with ωn>1/τ |
| `Acceleration (*)` | Kcs2 | Kpse−τs | KcKpe−τss |  |
| `Roll attitude (*)` | Kcs(TIs+1) | Kp(TLs+1)e−τs | KcKpe−τss | With   T L ≈ T I |
| `Unstable short period(*)` | Kc(TI1s+1)(TI2s−1) | Kp(TLs+1)e−τs | KcKpe−τs(TI2s−1) | With   T L ≈ T I1 |
| `Second order - Phugoid(*)` | Kcωn2s2+2ζωns+ωn2 | Kp(TLs+1)e−τs | KcKpωn2e−τss | Phugoid,   with ωn≪1/τ,1/TL≈ζωn |

\* 表示飞行员模型包含一个 Derivative 模块，该模块产生数值导数。因此，不要向 Crossover Pilot Model 模块发送不连续（例如阶跃）或含噪输入。此类输入可能导致大输出，从而使系统不稳定。

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

#### 程序化使用

|  |
| --- |
| **模块参数**: `sw_popup` |
| **类型**: character vector |
| **值**: `'Proportion'` | `'Rate or velocity'` |`'Spiral divergence'` | `'Second order - Short period'` | `'Acceleration(*)'` | `'Roll attitude(*)'` | `'Unstable short period(*)'` | `'Second order - Phugoid(*)'` |
| **默认值**: `'Proportion'` |

### **Calculated value** — 交叉频率或飞行员增益 `Crossover frequency`（默认）| `Pilot gain`

希望模块计算的交叉频率或飞行员增益值：

- `Crossover frequency` — 模块计算交叉频率值。参数值被禁用。
- `Pilot gain` — 模块计算飞行员增益值。参数值被禁用。

#### 程序化使用

|  |
| --- |
| **模块参数**: `freq_gain_popup` |
| **类型**: character vector |
| **值**: `'Crossover frequency'` | `'Pilot gain'` |
| **默认值**: `'Crossover frequency'` |

### **Controlled element gain** — 受控元件增益 `1`（默认）| 标量

受控元件增益，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Kc` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'1'` |

### **Pilot gain** — 飞行员增益 `3`（默认）| 标量

飞行员增益，指定为 double 标量。

#### 依赖关系

要启用此参数，将 **Calculated value** 设置为 `Pilot gain`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Kp` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'3'` |

### **Crossover frequency (rad/s)** — 交叉频率 `3`（默认）| 1 到 10 范围内的标量

交叉频率值，指定为 double 标量，单位为 rad/s。该值必须在 1 到 10 范围内。

#### 依赖关系

要启用此参数，将 **Calculated value** 设置为 `Crossover frequency`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `omega_c` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'3'` |

### **Pilot time delay(s)** — 飞行员时间延迟 `0.1`（默认）| 标量

总飞行员时间延迟，指定为 double 标量，单位为秒。该值通常在 0.1 s 到 0.2 s 范围内。

#### 程序化使用

|  |
| --- |
| **模块参数**: `time_delay` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'0.1'` |

### **Pilot lead constant** — 飞行员超前常数 `1`（默认）| 标量

飞行员超前常数，指定为 double 标量。

#### 依赖关系

要启用此参数，将 **Type of control** 设置为以下选项之一：

- `Roll attitude (*)`
- `Unstable short period (*)`
- `Second order - Phygoid(*)`

#### 程序化使用

|  |
| --- |
| **模块参数**: `T` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'1'` |

### **Pilot lag constant** — 飞行员滞后常数 `5`（默认）| 标量

飞行员滞后常数，指定为 double 标量。

#### 依赖关系

要启用此参数，将 **Type of control** 设置为 `Second order - Short period`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Ti` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'5'` |

## 所属库

Aerospace Blockset / Pilot Models

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

表示交叉飞行员模型

Crossover Pilot Model 模块表示 *Mathematical Models of Human Pilot Behavior* [1]) 中描述的飞行员模型。该飞行员模型是单输入单输出 (SISO) 模型，表示人类在控制飞机时的某些行为方面。

Crossover Pilot Model 考虑了人类飞行员和飞机的组合动力学，使用 Algorithms 中围绕交叉频率描述的形式。

此模块具有非线性行为。如果要线性化该模块（例如，使用 `linearize` (Simulink Control Design) 或某个 `linmod` 函数），可能需要更改 Pade 近似阶数。Crossover Pilot Model 模块实现包含 Transport Delay 模块，其 **Pade order (for linearization)** 参数默认设置为 `2`。要更改此值，请使用 `set_param` 函数，例如：

`set_param(gcb,'pade','3')`

**注意**

`linmod` 函数仅提供基本的线性化功能。要获得完整的线性化功能，请使用 Simulink® Control Design™ 软件。有关详细信息，请参阅 Choose Linearization Tools (Simulink Control Design)。

在对人类飞行员模型建模时，使用此模块可获得比 Tustin Pilot Model 模块更高的精度。此模块的精度也不如 Precision Pilot Model 模块。
