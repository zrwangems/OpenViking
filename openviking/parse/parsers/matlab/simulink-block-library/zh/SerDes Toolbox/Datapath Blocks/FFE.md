---
type: simulink-block
title: 'FFE'
family: 'datapath-blocks'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'ffe'
documentation_source_path: 'ref/ffe.html'
language: zh-CN
chinese_source: worker-translation
---

# FFE

## 端口

### 输入

### **WaveIn** — 输入基带信号 标量 | 向量

输入基带信号。输入信号可以是指定为标量的逐样本信号，也可以是脉冲响应向量信号。

**数据类型：** `double`
### 输出

### **WaveOut** — 估计的信道输出 标量 | 向量

估计的信道输出。如果输入信号是指定为标量的逐样本信号，则输出也是标量。如果输入信号是脉冲响应向量信号，则输出也是向量。

**数据类型：** `double`

## 参数

### **Mode** — FFE 工作模式 `Fixed`（默认）| `Off`

FFE 工作模式：

- `Off` — FFE 被旁路，输入波形保持不变。
- `Fixed` — FFE 将 **Tap weights** 中指定的 FFE 抽头权重应用于输入波形。

#### 编程使用

|  |
| --- |
| **模块参数：** `Mode` |
| **类型：** character vector |
| **取值：** `Fixed` | `Off` |
| **默认值：** `Fixed` |

### **Tap Spacing** — 用于子符号均衡控制的分数抽头 `T-spaced`（默认）| `T/2-spaced` | `T/4-spaced`

用于子符号均衡控制的分数抽头，指定为
`T-spaced`、`T/2-spaced` 或
`T/4-spaced`。*T* 表示符号时间。

#### 编程使用

|  |
| --- |
| **模块参数：** `TapSpacing` |
| **类型：** character vector |
| **取值：** `T-spaced` | `T/2-spaced` | `T/4-spaced` |
| **默认值：** `T-spaced` |

### **Tap weights** — FFE 抽头权重 `[0,1,0,0,0]`（默认）| 行向量

FFE 抽头权重，指定为以 volts 为单位的行向量。向量长度指定抽头数量。向量元素值指定该元素位置处抽头的强度。幅值最大的抽头是主抽头，因此定义了前游标和后游标抽头的数量。

您可以使用有效的 MATLAB 表达式来计算 **Initial tap weights
(V)** 行向量。

**示例：** `set_param(gcb,'TapWeights',"zeros[(1,4) 1 zeros(1,15)]")`
创建一个具有 20 个抽头的 FFE，其中第五个抽头是主抽头。

#### 编程使用

|  |
| --- |
| **模块参数：** `TapWeights` |
| **类型：** character vector |
| **取值：** 行向量 |
| **默认值：** `[0,1,0,0,0]` |

- 使用 `get_param(gcb,'TapWeights')` 查看当前 FFE
  **Tap weights**。
- 使用 `set_param(gcb,'TapWeights',value)` 将 FFE 设置为特定的
  **Tap weights** 向量。

**数据类型：** `double`

### **Normalize** — 归一化抽头权重 on（默认）| fff

选择此项可归一化抽头权重向量，使 **Tap weights** 向量元素的绝对值之和为 1。

### **Visualize Response** — 绘制 FFE FIR 滤波器响应的按钮

单击可绘制 FFE FIR（有限脉冲响应）滤波器的响应。

#### IBIS-AMI 参数

### **Mode** — 在 IBIS-AMI 模型中包含 Mode 参数 on（默认）| off

选择此项可将 **Mode** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Mode**，则会将其从 AMI 文件中移除，实际上将 **Mode** 硬编码为其当前值。

### **Tap weights** — 在 IBIS-AMI 模型中包含 Tap weights 参数 on（默认）| off

选择此项可将 **Tap weights** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Tap weights**，则会将其从 AMI 文件中移除，实际上将 **Tap weights** 硬编码为其当前值。

## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

为前馈均衡器建模

FFE 模块将前馈均衡器 (FFE) 作为有限脉冲响应 (FIR) 滤波器应用于逐样本输入信号或脉冲响应向量输入信号。此滤波可减少由信道损耗损伤引起的失真。
