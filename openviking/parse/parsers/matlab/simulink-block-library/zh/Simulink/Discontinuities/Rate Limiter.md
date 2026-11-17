---
type: simulink-block
title: 'Rate Limiter'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'ratelimiter'
documentation_source_path: 'slref/ratelimiter.html'
language: zh-CN
chinese_source: worker-translation
---

# Rate Limiter

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

速率限幅算法的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

速率限幅算法的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **Rising slew rate** — 输入增大时的导数限值 `1`（默认）| 实数

指定输入信号上升速率的限值。对于定点输入，此参数可调。

#### 程序化使用

|  |
| --- |
| **模块参数**：`RisingSlewLimit` |
| **类型**：字符向量 |
| **值**：实数 |
| **默认值**：`'1'` |

### **Falling slew rate** — 输入减小时的导数限值 `-1`（默认）| 实数

指定输入信号下降速率的下限。对于定点输入，此参数可调。

#### 程序化使用

|  |
| --- |
| **模块参数**：`FallingSlewLimit` |
| **类型**：字符向量 |
| **值**：实数 |
| **默认值**：`'-1'` |

### **Sample time mode** — 采样时间模式 `inherited`（默认）| `continuous`

指定采样时间模式，`continuous` 或从驱动模块 `inherited`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SampleTimeMode` |
| **类型**：字符向量 |
| **值**：`'inherited'` | `'continuous'` |
| **默认值**：`'inherited'` |

### **Initial condition** — 初始输出 `0`（默认）| 标量 | 向量

设置仿真的初始输出。Simulink® 不允许将此模块的初始条件设置为 `inf` 或 `NaN`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型**：字符向量 |
| **值**：`scalar` |
| **默认值**：`'0'` |

### **Treat as gain when linearizing** — 指定增益值 `on`（默认）| `off`

选择此参数可使命令将增益视为 1。Simulink 软件中的线性化命令将此模块视为状态空间中的增益。清除此参数可使命令将增益视为 0。

#### 程序化使用

|  |
| --- |
| **模块参数**：`LinearizeAsGain` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

## 所属库

Simulink / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不能在触发子系统层次结构内使用。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

限制信号的变化率

Rate Limiter 模块限制通过它的信号的一阶导数。输出的变化速度不超过指定的限值。导数使用以下方程计算：

rate=u(i)−y(i−1)t(i)−t(i−1)

其中 *u(i)* 和 *t(i)* 是当前模块输入和时间，*y(i-1)* 和 *t(i-1))* 是上一步的输出和时间。输出通过将 *rate* 与 **Rising slew rate** 和 **Falling slew rate** 参数进行比较来确定：

- 如果 *rate* 大于 **Rising slew rate** 参数（*R*），则输出计算为

  y(i)=Δt⋅R+y(i−1)。
- 如果 *rate* 小于 **Falling slew rate** 参数（*F*），则输出计算为

  y(i)=Δt⋅F+y(i−1)。
- 如果 *rate* 介于 *R* 和 *F* 的边界之间，则输出的变化等于输入的变化：

  y(i)=u(i)

当模块在连续模式下运行（例如，**Sample time mode** 为 `inherited` 且驱动模块的 **Sample time** 为零）时，**Initial condition** 被忽略。`t = 0` 时的模块输出等于初始输入：

y(0)=u(0)

当模块在离散模式下运行（例如，**Sample time mode** 为 `inherited` 且驱动模块的 **Sample time** 为非零）时，**Initial condition** 被保留：

y(−1)=Ic

其中 *Ic* 是初始条件。`t = 0` 时的模块输出按照 *rate* 超出 *R* 和 *F* 边界的情况计算。对于 `t = 0`，*rate* 计算如下：

rate=u(0)−y(−1)sample time
