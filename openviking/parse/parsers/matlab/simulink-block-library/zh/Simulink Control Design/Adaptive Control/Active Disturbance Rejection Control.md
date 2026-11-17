---
type: simulink-block
title: 'Active Disturbance Rejection Control'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Adaptive Control'
documentation_page: 'activedisturbancerejectioncontrol'
documentation_source_path: 'ug/activedisturbancerejectioncontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# Active Disturbance Rejection Control

## 端口
```yaml
ports:
- name: r
  summary: 参考信号标量
  direction: input
- name: y
  summary: 被控对象输出标量
  direction: input
- name: u
  summary: 控制输入标量
  direction: output
- name: xhat
  summary: 估计的扩张状态向量
  direction: output
```

### 输入

### **r** — 参考信号标量

为受控系统提供要跟随的参考信号。

### **y** — 被控对象输出标量

提供被控对象的输出信号。

### 输出

### **u** — 控制输入标量

将控制输入信号连接到被控对象输入。

### **xhat** — 估计的扩张状态向量

来自扩张状态观测器的被控对象模型估计扩张状态。

如果 **Model type** 为 **first-order**，则 **xhat** 是长度为二的向量，包含估计状态 y^ 和 f^(t)。

如果 **Model type** 为 **second-order**，则 **xhat** 是长度为三的向量，包含估计状态 y^、y˙^ 和 f^(t)。

#### 依赖

要启用此输出端口，请选择 **Estimated extended states** 参数。
## 参数
```yaml
parameters:
- name: Time domain
  summary: 控制器时域 discrete-time（默认）| continuous-time
  group: 参数选项卡
  block_parameter: '''time_domain'''
  type: 字符向量
  values: '''discrete-time'' | ''continuous-time'''
- name: Sample time
  summary: 控制器采样时间 0.01（默认）| 有限正标量
  group: 参数选项卡
  block_parameter: '''Ts'''
  type: 字符向量
  values: 有限正标量
- name: Model type
  summary: 被控对象阶次类型 first-order（默认）| second-order
  group: 参数选项卡
  block_parameter: '''model_type'''
  type: 字符向量
  values: '''first-order'' | ''second-order'''
- name: Critical gain
  summary: 临界增益 1（默认）| 有限非零标量
  group: 参数选项卡
  block_parameter: '''b0'''
  type: 字符向量
  values: 有限非零标量
- name: Controller bandwidth (rad/sec)
  summary: 控制器带宽 1（默认）| 有限正标量
  group: 参数选项卡
  block_parameter: '''wc'''
  type: 字符向量
  values: 有限正标量
- name: Observer bandwidth (rad/sec)
  summary: 观测器带宽 10（默认）| 有限正标量
  group: 参数选项卡
  block_parameter: '''wo'''
  type: 字符向量
  values: 有限正标量
- name: Initial conditions
  summary: 扩张状态观测器的初始状态值 0（默认）| 标量 | 向量
  group: 模块选项卡
  block_parameter: '''x0'''
  type: 字符向量
  values: 有限标量 | 向量
- name: Limit output (u)
  summary: 将模块输出限制在指定的饱和限值 off（默认）| on
  group: 模块选项卡
  block_parameter: '''ulim_checkbox'''
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Upper limit
  summary: 模块输出的饱和上限 inf（默认）| 标量
  group: 模块选项卡
  block_parameter: '''umax'''
  type: character vector
  values: scalar
  default: '''inf'''
- name: Lower limit
  summary: 模块输出的饱和下限 –inf（默认）| 标量
  group: 模块选项卡
  block_parameter: '''umin'''
  type: character vector
  values: scalar
  default: '''–inf'''
- name: Estimated extended states (xhat)
  summary: 从观测器输出估计状态 off（默认）| on
  group: 模块选项卡
  block_parameter: '''xhat_checkbox'''
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
```

### 参数选项卡

### **Time domain** — 控制器时域 **discrete-time**（默认）| **continuous-time**

指定控制器时域。

当您选择 **discrete-time** 时，使用 **Sample time** 参数指定采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `'time_domain'` |
| **类型：** 字符向量 |
| **值：** `'discrete-time'` | `'continuous-time'` |
| **默认：** `'discrete-time'` |

### **Sample time** — 控制器采样时间 `0.01`（默认）| 有限正标量

指定离散时间控制器的采样时间值。

#### 依赖

要启用此参数，请将 **Time domain** 参数设置为 **discrete-time**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `'Ts'` |
| **类型：** 字符向量 |
| **值：** 有限正标量 |
| **默认：** `'0.01'` |

### **Model type** — 被控对象阶次类型 **first-order**（默认）| **second-order**

将您的被控对象模型类型指定为以下之一。

- **first-order** — 如果您的被控对象表现出一阶动态系统行为，请选择此选项。
- **second-order** — 如果您的被控对象表现出二阶动态系统行为，请选择此选项。

#### 程序化使用

|  |
| --- |
| **模块参数：** `'model_type'` |
| **类型：** 字符向量 |
| **值：** `'first-order'` | `'second-order'` |
| **默认：** `'first-order'` |

### **Critical gain** — 临界增益 `1`（默认）| 有限非零标量

指定描述模型行为的临界增益 *b*0。

#### 程序化使用

|  |
| --- |
| **模块参数：** `'b0'` |
| **类型：** 字符向量 |
| **值：** 有限非零标量 |
| **默认：** `'1'` |

### **Controller bandwidth (rad/sec)** — 控制器带宽 `1`（默认）| 有限正标量

指定控制器带宽。此参数决定控制器响应的速度。通常，更快的响应需要更大的控制器带宽。

#### 程序化使用

|  |
| --- |
| **模块参数：** `'wc'` |
| **类型：** 字符向量 |
| **值：** 有限正标量 |
| **默认：** `'1'` |

### **Observer bandwidth (rad/sec)** — 观测器带宽 `10`（默认）| 有限正标量

指定观测器带宽。通常，将其设置为控制器带宽的 5 到 10 倍，以便观测器比控制器更快收敛。

#### 程序化使用

|  |
| --- |
| **模块参数：** `'wo'` |
| **类型：** 字符向量 |
| **值：** 有限正标量 |
| **默认：** `'10'` |

### 模块选项卡

### **Initial conditions** — 扩张状态观测器的初始状态值 `0`（默认）| 标量 | 向量

将扩张状态观测器的初始状态值指定为标量或长度为 *n* 的向量。

如果 **Model type** 为 **first-order**，则 *n* = 2。否则，*n* = 3。

#### 程序化使用

|  |
| --- |
| **模块参数：** `'x0'` |
| **类型：** 字符向量 |
| **值：** 有限标量 | 向量 |
| **默认：** `'0'` |

### **Limit output (u)** — 将模块输出限制在指定的饱和限值 `off`（默认）| `on`

用于将模块输出限制在指定饱和限值的选项。使用 **Upper limit** 和 **Lower limit** 参数指定输出饱和限值。

#### 编程使用

|  |
| --- |
| **模块参数**：`'ulim_checkbox'` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Upper limit** — 模块输出的饱和上限 `inf`（默认）| 标量

指定模块输出的上限。当模块输出本应超过此值时，输出将保持在此值。

#### 依赖关系

要启用此参数，请选中 **Limit output** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`'umax'` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'inf'` |

### **Lower limit** — 模块输出的饱和下限 `–inf`（默认）| 标量

指定模块输出的下限。当模块输出本应低于此值时，输出将保持在此值。

#### 依赖关系

要启用此参数，请选中 **Limit output** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`'umin'` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'–inf'` |

### **Estimated extended states (xhat)** — 从观测器输出估计状态 `off`（默认）| `on`

用于从扩张状态观测器输出状态的选项。

如果 **Model type** 为 **first-order**，模块输出 y^ 和 f^(t)。

如果 **Model type** 为 **second-order**，模块输出 y^、y˙^ 和 f^(t)。

#### 编程使用

|  |
| --- |
| **模块参数**：`'xhat_checkbox'` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |
## 所属库

Simulink Control Design / Adaptive Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2023b：库位置变更

Active Disturbance Rejection Control 模块现在位于 **Simulink Control Design/Adaptive Control** 子库中。

在 R2023b 中，当您打开在先前版本中保存的模型时，Active Disturbance Rejection Control 模块的库链接会自动更新。

## 描述

为具有未知动态和扰动的被控对象设计控制器

Active Disturbance Rejection Control 模块允许您为具有未知动态以及内部和外部扰动的被控对象设计自抗扰控制（ADRC）。ADRC 是一种无模型控制技术，仅需要被控对象动态的近似即可设计出提供鲁棒扰动抑制的控制器。

该模块使用已知系统动态的一阶或二阶模型近似，并将未知动态和扰动建模为被控对象的扩张状态。通常，您根据被控对象在工作范围内的开环阶跃响应来确定此阶数。

- 一阶近似 — y˙(t)=b0u(t)+f(t)
- 二阶近似 — y¨(t)=b0u(t)+f(t)

其中：

- *y*(*t*) 是被控对象输出。
- *u*(*t*) 是输入信号。
- *b*0 是临界增益，即描述被控对象对输入 *u*(*t*) 响应的估计增益。
- *f*(*t*) 是总扰动，包括未知动态和其他扰动。

该模块使用扩张状态观测器（ESO）来估计 *f*(*t*)，并通过减小估计扰动对模型近似中已知部分的影响来实现扰动抑制控制。要调节 ADRC，请设置适当的时域、模型类型和临界增益、控制器和观测器带宽以及初始条件。

有关详细信息，请参阅 Active Disturbance Rejection Control。
