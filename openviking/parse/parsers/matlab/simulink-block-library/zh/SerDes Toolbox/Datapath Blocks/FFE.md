---
type: simulink-block
title: 'FFE'
family: 'serdes'
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
```yaml
ports:
- name: WaveIn
  summary: 输入基带信号 标量 | 向量
  direction: input
  data_types: double
- name: WaveOut
  summary: 估计的信道输出 标量 | 向量
  direction: output
  data_types: double
```

### 输入

### **WaveIn** — 输入基带信号 标量 | 向量

输入基带信号。输入信号可以是按样本逐个指定的标量信号，也可以是冲激响应向量信号。

**数据类型：** `double`
### 输出

### **WaveOut** — 估计的信道输出 标量 | 向量

估计的信道输出。如果输入信号是按样本逐个指定的标量信号，则输出也是标量。如果输入信号是冲激响应向量信号，则输出也是向量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Mode
  summary: FFE 工作模式 Fixed（默认）| Off
  group: ''
  block_parameter: Mode
  type: 字符向量
  values: Fixed | Off
- name: Tap Spacing
  summary: 用于子符号均衡控制的分数间隔 T-spaced（默认）| T/2-spaced | T/4-spaced
  group: ''
  block_parameter: TapSpacing
  type: 字符向量
  values: T-spaced | T/2-spaced | T/4-spaced
- name: Tap weights
  summary: FFE 抽头权重 [0,1,0,0,0]（默认）| 行向量
  group: ''
  block_parameter: TapWeights
  type: 字符向量
  values: 行向量
- name: Normalize
  summary: 归一化抽头权重 开（默认）| 关
  group: ''
- name: Visualize Response
  summary: 绘制 FFE FIR 滤波器响应 按钮
  group: ''
- name: Mode
  summary: 在 IBIS-AMI 模型中包含 Mode 参数 开（默认）| 关
  group: ''
- name: Tap weights
  summary: 在 IBIS-AMI 模型中包含 Tap weights 参数 开（默认）| 关
  group: ''
```

### **Mode** — FFE 工作模式 `Fixed`（默认）| `Off`

FFE 工作模式：

- `Off` — 绕过 FFE，输入波形保持不变。
- `Fixed` — FFE 将 **Tap weights** 中指定的 FFE 抽头权重应用于输入波形。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Mode` |
| **类型：** 字符向量 |
| **值：** `Fixed` | `Off` |
| **默认：** `Fixed` |

### **Tap Spacing** — 用于子符号均衡控制的分数间隔 `T-spaced`（默认）| `T/2-spaced` | `T/4-spaced`

用于子符号均衡控制的分数间隔，指定为 `T-spaced`、`T/2-spaced` 或 `T/4-spaced`。*T* 表示符号时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TapSpacing` |
| **类型：** 字符向量 |
| **值：** `T-spaced` | `T/2-spaced` | `T/4-spaced` |
| **默认：** `T-spaced` |

### **Tap weights** — FFE 抽头权重 `[0,1,0,0,0]`（默认）| 行向量

FFE 抽头权重，以伏特为单位指定为行向量。向量的长度指定抽头的数量。向量元素值指定该元素位置上抽头的强度。幅度最大的抽头是主抽头，因此定义了前游标和后游标抽头的数量。

可以使用有效的 MATLAB 表达式来计算 **Initial tap weights (V)** 行向量。

**示例：** `set_param(gcb,'TapWeights',"zeros[(1,4) 1 zeros(1,15)]")` 创建一个具有 20 个抽头的 FFE，其中第五个抽头是主抽头。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TapWeights` |
| **类型：** 字符向量 |
| **值：** 行向量 |
| **默认：** `[0,1,0,0,0]` |

- 使用 `get_param(gcb,'TapWeights')` 查看当前 FFE **Tap weights**。
- 使用 `set_param(gcb,'TapWeights',value)` 将 FFE 设置为特定的 **Tap weights** 向量。

**数据类型：** `double`

### **Normalize** — 归一化抽头权重 开（默认）| 关

选择此项可归一化抽头权重向量，使 **Tap weights** 向量元素绝对值之和为一。

### **Visualize Response** — 绘制 FFE FIR 滤波器响应 按钮

点击以绘制 FFE FIR（有限冲激响应）滤波器的响应。

#### IBIS-AMI 参数

### **Mode** — 在 IBIS-AMI 模型中包含 Mode 参数 开（默认）| 关

选择此项可在 IBIS-AMI 文件中将 **Mode** 作为参数包含。如果取消选择 **Mode**，它将从 AMI 文件中移除，实际上将 **Mode** 硬编码为其当前值。

### **Tap weights** — 在 IBIS-AMI 模型中包含 Tap weights 参数 开（默认）| 关

选择此项可在 IBIS-AMI 文件中将 **Tap weights** 作为参数包含。如果取消选择 **Tap weights**，它将从 AMI 文件中移除，实际上将 **Tap weights** 硬编码为其当前值。
## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

对前馈均衡器进行建模

FFE 模块将前馈均衡器（FFE）作为有限冲激响应（FIR）滤波器应用于按样本逐个输入的信号或冲激响应向量输入信号。此滤波可减少由信道损耗损伤引起的失真。
