---
type: simulink-block
title: 'CDR'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'cdr'
documentation_source_path: 'ref/cdr.html'
language: zh-CN
chinese_source: worker-translation
---

# CDR

## 端口

### 输入

### **WaveIn** — 输入基带信号 标量

输入基带信号。CDR 的输入必须一次一个采样地施加，而不是以向量形式。

**数据类型：** `double`

## 参数

### **CDR Mode** — 确定 CDR 阶数 `1st order`（默认）| `2nd order`

确定 CDR 阶数以启用相位和频率跟踪。

- `1st order` — 仅跟踪相位。
- `2nd order` — 同时跟踪相位和频率。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CDRMode` |
| **类型：** 字符向量 |
| **值：** `1st order` | `2nd order` |
| **默认：** `1st order` |

### **Phase Detector** — 时钟相位检测器选项 `BangBang`（默认）| `BaudRateTypeA`

时钟数据恢复中使用的时钟相位检测器选项。您可以选择 bang-bang（Alexander）或波特率 type-A（Mueller-Muller）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PhaseDetector` |
| **类型：** 字符向量 |
| **值：** `BangBang` | `BaudRateTypeA` |
| **默认：** `BangBang` |

### **Phase Offset (symbol time)** — 时钟相位偏移 `0`（默认）| 范围 [-0.5,0.5] 内的实标量

时钟相位偏移，以符号时间的分数形式指定为范围 [-0.5,0.5] 内的实标量。**Phase Offset** 用于手动偏移时钟概率分布函数（PDF），以获得更好的误码率（BER）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PhaseOffset` |
| **类型：** 字符向量 |
| **值：** 范围 [-0.5,0.5] 内的实标量 |
| **默认：** `0` |

**数据类型：** `double`

### **Reference offset (ppm)** — 参考时钟偏移损伤 `0`（默认）| 范围 [0, 300] 内的实标量

参考时钟偏移损伤，以百万分率（ppm）为单位指定为范围 [0, 300] 内的实标量。**Reference offset (ppm)** 是发射器振荡器频率与接收器振荡器频率之间的偏差。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ReferenceOffset` |
| **类型：** 字符向量 |
| **值：** 范围 [0, 300] 内的实标量 |
| **默认：** `0` |

**数据类型：** `double`

### **Early/late count threshold** — 触发相位更新的早/晚 CDR 计数阈值 `16`（默认）| ≥5 的实正整数

触发相位更新的早/晚 CDR 计数阈值，指定为 ≥5 的无量纲实正整数。增大 **Early/late count threshold** 的值可以以收敛速度为代价提供更稳定的输出时钟相位。由于比特判决是在时钟相位输出处进行的，更稳定的时钟相位具有更好的误码率（BER）。

**Early/late count threshold** 还控制 CDR 的带宽。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Count` |
| **类型：** 字符向量 |
| **值：** ≥5 的实正整数 |
| **默认：** `16` |

**数据类型：** `double`

### **Step (symbol time)** — 时钟相位分辨率 `0.0078`（默认）| 实标量

时钟相位分辨率，以符号时间的分数形式指定为实标量。**Step (symbol time)** 是 CDR 中相位调整次数的倒数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Step` |
| **类型：** 字符向量 |
| **值：** 实标量 |
| **默认：** `0.0078` |

**数据类型：** `double`

### **Frequency tracking gain** — 频率跟踪的内部增益 `0.00048828125`（默认）| 非负实标量

频率跟踪环路的内部增益，指定为非负实标量。

#### 依赖关系

要启用此参数，请将 **CDR Mode** 设置为 `2nd order`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrequencyStep` |
| **类型：** 字符向量 |
| **值：** 非负实标量 |
| **默认：** `0.00048828125` |

**数据类型：** `double`

### **Frequency tracking update** — 频率跟踪更新 `16`（默认）| 非负整数标量

每经过 **Frequency tracking update** 个符号，使用频率估计值更新系统相位旋转器时钟。

#### 依赖

要启用此参数，请将 **CDR Mode** 设置为 `2nd order`。

#### 编程使用

|  |
| --- |
| **模块参数：** `FrequencyCount` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认：** `16` |

**数据类型：** `double`

### **Frequency step ramp** — 初始内部频率跟踪增益达到指定值所需的符号时间数 `3000`（默认）| 非负整数标量

为了帮助频率跟踪环路在仿真早期锁定，初始 **Frequency tracking gain** 从一个高值 1/(2\***Frequency tracking update)** 开始。然后 **Frequency tracking gain** 在大约 **Frequency step ramp** 个符号时间内逐渐降低到指定值。

#### 依赖

要启用此参数，请将 **CDR Mode** 设置为 `2nd order`。

#### 编程使用

|  |
| --- |
| **模块参数：** `FrequencyStepRamp` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认：** `3000` |

**数据类型：** `double`

### **Sensitivity (V)** — 采样锁存器亚稳态电压 `0`（默认）| 实数标量

采样锁存器亚稳态电压，指定为以伏特为单位的实数标量。如果数据采样电压位于（±**Sensitivity (V)**）区域内，则误码概率为 50%。

#### 编程使用

|  |
| --- |
| **模块参数：** `Sensitivity` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `0` |

**数据类型：** `double`

#### IBIS-AMI 参数

### **Phase Offset** — 在 IBIS-AMI 模型中包含 Phase Offset 参数 开（默认）| 关

选择以将 **Phase Offset** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Phase Offset**，它将从 AMI 文件中移除，实际上将 **Phase Offset** 硬编码为其当前值。

### **Reference offset** — 在 IBIS-AMI 模型中包含 Reference offset 参数 开（默认）| 关

选择以将 **Reference offset** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Reference offset**，它将从 AMI 文件中移除，实际上将 **Reference offset** 硬编码为其当前值。

## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

对时钟数据恢复电路进行建模

CDR 模块使用一阶相位跟踪以及可选的二阶频率跟踪 CDR 模型，在接收端提供时钟采样时间并估计数据符号。有关详细信息，请参阅 SerDes 系统中的时钟和数据恢复。
