---
type: simulink-block
title: 'Precision Pilot Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Pilot Models'
documentation_page: 'precisionpilotmodel'
documentation_source_path: 'precisionpilotmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Precision Pilot Model

## 端口

### 输入

### **x com** — 信号指令标量

飞行员模型所控制的信号指令，指定为标量。

**数据类型：** `double`

### **x** — 飞行员控制的信号标量

飞行员模型所控制的信号，指定为标量。

**数据类型：** `double`
### 输出

### **u** — 飞机指令标量

飞机指令，以标量形式返回。

**数据类型：** `double`

## 参数

### **Type of control** — 飞机动力学控制 `Proportional`（默认）| `Rate or velocity` | `Acceleration` | `Second order`

飞机动力学控制。均衡器形式根据这些值而变化。有关更多信息，请参阅 [2]。为帮助您做出决定，下表列出了各选项及相关的动力学。

| 选项（受控对象传递函数） | 受控对象传递函数（*Yc*） | 飞行员传递函数（*Yp*） |
| --- | --- | --- |
| Proportional | Kc | 滞后-超前，TI >> TL |
| Rate or velocity | Kcs | 1 |
| Acceleration | Kcs2 | 超前-滞后，TL >> TI |
| Second order | Kcωn2s2+2ζωns+ωn2 | 若 ωm << 2/τ，则为超前-滞后。若 ωm >> 2/τ，则为滞后-超前。 |

下表定义了控制选项列表中使用的变量。

| 变量 | 描述 |
| --- | --- |
| K c | 飞机增益。 |
| T I | 滞后常数。 |
| T L | 超前常数。 |
| ζ | 飞机的阻尼比。 |
| ω n | 飞机的自然频率。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`sw_popup` |
| **类型**：character vector |
| **值**：`'Proportion'` | `'Rate or velocity'` | `'Acceleration'` | `'Second order'` |
| **默认值**：`'Proportion'` |

### **Pilot gain** — 飞行员增益 `1`（默认）| 标量

飞行员增益，指定为双精度标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`Kp` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'1'` |

### **Pilot time delay(s)** — 飞行员时间延迟 `0.1`（默认）| 标量

飞行员总时间延迟，指定为双精度标量，单位为秒。该值通常在 0.1 s 到 0.2 s 之间。

#### 编程使用

|  |
| --- |
| **模块参数**：`time_delay` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'0.1'` |

### **Equalizer lead constant** — 均衡器超前常数 `1`（默认）| 标量

均衡器超前常数，指定为双精度标量。

#### 依赖关系

要启用此参数，请将 **Type of control** 设置为 `Proportional`、`Acceleration` 或 `Second order`。

#### 编程使用

|  |
| --- |
| **模块参数**：`TL` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'1'` |

### **Equalizer lag constant** — 均衡器滞后常数 `5`（默认）| 标量

均衡器滞后常数，指定为双精度标量。

#### 依赖关系

要启用此参数，请将 **Type of control** 设置为 `Proportional`、`Acceleration` 或 `Second order`。

#### 编程使用

|  |
| --- |
| **模块参数**：`TI` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'5'` |

### **Lag constant for neuromuscular system** — 滞后常数 `0.1`（默认）| 标量

神经肌肉系统滞后常数，指定为双精度标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`TN1` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`0.1` |

### **Undamped natural frequency neuromuscular system (rad/s)** — 无阻尼自然频率 `20`（默认）| 标量

神经肌肉系统的无阻尼自然频率，指定为双精度标量，单位为 rad/s。

#### 编程使用

|  |
| --- |
| **模块参数**：`nat_freq` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`20` |

### **Damping neuromuscular system** — 神经肌肉系统阻尼 `0.7`（默认）| 标量

神经肌肉系统阻尼，指定为双精度标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`damp` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`0.7` |

### **Controlled element undamped natural frequency (rad/s)** — 受控对象无阻尼自然频率 `15`（默认）| 标量

受控对象无阻尼自然频率，指定为双精度标量，单位为 rad/s。

#### 依赖关系

要启用此参数，请将 **Type of control** 设置为 `Second order`。

#### 编程使用

|  |
| --- |
| **模块参数**：`omega_m` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`15` |

## 所属库

Aerospace Blockset / Pilot Models

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

表示 Precision Pilot Model

Precision Pilot Model 模块表示 *Mathematical Models of Human Pilot Behavior* [1] 中描述的飞行员模型。该飞行员模型是一个单输入单输出（SISO）模型，表示人类在控制飞机时的某些行为方面。在对人类飞行员模型进行建模时，若需要比 Tustin Pilot Model 和 Crossover Pilot Model 模块更高的精度，请使用此模块。

此模块具有非线性行为。如果您想要对该模块进行线性化（例如，使用 `linearize` (Simulink Control Design) 或某个 `linmod` 函数），您可能需要更改 Pade 近似阶数。Precision Pilot Model 模块的实现包含 Transport Delay 模块，其 **Pade order (for linearization)** 参数默认设置为 `2`。要更改此值，请使用 `set_param` 函数，例如：

```
set_param(gcb,'pade','3')
```

**注意**

`linmod` 函数仅提供基本的线性化功能。要获得完整的线性化功能，请使用 Simulink® Control Design™ 软件。有关更多信息，请参阅 Choose Linearization Tools (Simulink Control Design)。

此模块是 Crossover Pilot Model 模块的扩展。它实现了算法中描述的方程。
