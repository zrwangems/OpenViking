---
type: simulink-block
title: 'DFECDR'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'dfecdr'
documentation_source_path: 'ref/dfecdr.html'
language: zh-CN
chinese_source: worker-translation
---

# DFECDR

## 端口

### 输入

### **WaveIn** — 输入基带信号 标量 | 向量

输入基带信号。输入信号可以是逐样本指定的标量信号，也可以是冲激响应向量信号。

**数据类型：** `double`
### 输出

### **WaveOut** — 估计的信道输出 标量 | 向量

估计的信道输出。如果输入信号是逐样本指定的标量信号，则输出也是标量。如果输入信号是冲激响应向量信号，则输出也是向量。

**数据类型：** `double`

## 参数

### DFE

### **Mode** — DFE 工作模式 `Adapt`（默认）| `Off` | `Fixed`

DFE 工作模式：

- `Off` — DFECDR 被旁路，输入波形保持不变。
- `Fixed` — DFECDR 将 **Initial tap weights (V)** 中指定的输入 DFE 抽头权重应用于输入波形。
- `Adapt` — Init 子系统调用 DFECDR System object™。DFECDR System object 为统计分析寻找最佳眼高张开度的最优 DFE 抽头值。在时域仿真期间，DFECDR 使用自适应值作为起点并将其应用于输入波形。有关 Init 子系统的更多信息，请参阅 SerDes 系统中的统计分析。

#### 编程使用

- 使用 `get_param(gcb,'Mode')` 查看当前 DFECDR 的 **Mode**。
- 使用 `set_param(gcb,'Mode',value)` 将 DFECDR 设置为特定的 **Mode**。

### **Initial tap weights (V)** — 初始 DFE 抽头权重 `[0 0 0 0]`（默认）| 行向量

初始 DFE 抽头权重，以伏特为单位的行向量指定。向量的长度指定 DFE 抽头的数量。向量元素值指定该元素位置处抽头的强度。将向量元素值设置为零仅初始化该抽头。

您可以使用有效的 MATLAB 表达式来求值 **Initial tap weights (V)** 行向量。

**示例：** `set_param(gcb,'TapWeights',"zeros(1,100)")` 创建一个具有 100 个抽头的 DFE。

#### 编程使用

- 使用 `get_param(gcb,'TapWeights')` 查看 DFECDR **Initial tap weights (V)** 的当前值。
- 使用 `set_param(gcb,'TapWeights',value)` 将 DFECDR 设置为特定的 **Initial tap weights (V)** 向量值。

**数据类型：** `double`

### **Adaptive gain** — 控制 DFE 抽头权重更新速率 `9.6e-5`（默认）| 正实数标量

控制 DFE 抽头权重更新速率，以无量纲正实数标量指定。增大 **Adaptive gain** 的值会导致 DFE 自适应更快收敛，但代价是 DFE 抽头值中噪声更多。

#### 编程使用

- 使用 `get_param(gcb,'EqualizationGain')` 查看当前 DFECDR **Adaptive gain** 值。
- 使用 `set_param(gcb,'EqualizationGain',value)` 将 DFECDR 设置为特定的 **Adaptive gain** 值。

**数据类型：** `double`

### **Adaptive step size (V)** — DFE 自适应步长分辨率 `1e-06`（默认）| 非负实数标量 | 非负实值行向量

DFE 自适应步长分辨率，以伏特为单位的非负实数标量或非负实值行向量指定。指定为标量以应用于所有 DFE 抽头，或指定为与 **Initial tap weights (V)** 长度相同的向量。

**Adaptive step size (V)** 指定从一个时间步到下一个时间步的最小 DFE 抽头变化，以模拟硬件限制。将 **Adaptive step size (V)** 设置为 `0` 会产生没有任何分辨率限制的 DFE 抽头值。

#### 编程使用

- 使用 `get_param(gcb,'EqualizationStep')` 查看当前 DFECDR **Adaptive step size (V)** 值。
- 使用 `set_param(gcb,'EqualizationStep',value)` 将 DFECDR 设置为特定的 **Adaptive step size (V)** 值。

**数据类型：** `double`

### **Minimum DFE tap value (V)** — 自适应抽头的最小值 `-1`（默认）| 实数标量 | 实值行向量

自适应抽头的最小值，以伏特为单位指定为实数标量或实值行向量。指定为标量以应用于所有 DFE 抽头，或指定为与 **Initial tap weights (V)** 长度相同的向量。

#### 程序化使用

- 使用 `get_param(gcb,'MinimumTap')` 查看当前 DFECDR 的 **Minimum DFE tap value (V)** 值。
- 使用 `set_param(gcb,'MinimumTap',value)` 将 DFECDR 设置为 **Minimum DFE tap value (V)** 的特定值。

**数据类型：** `double`

### **Maximum DFE tap value (V)** — 自适应抽头的最大值 `1`（默认）| 非负实数标量 | 非负实值行向量

自适应抽头的最大值，以伏特为单位指定为非负实数标量或非负实值行向量。指定为标量以应用于所有 DFE 抽头，或指定为与 **Initial tap weights (V)** 长度相同的向量。

#### 程序化使用

- 使用 `get_param(gcb,'MaximumTap')` 查看当前 DFECDR 的 **Maximum DFE tap value (V)** 值。
- 使用 `set_param(gcb,'MaximumTap',value)` 将 DFECDR 设置为 **Maximum DFE tap value (V)** 的特定值。

**数据类型：** `double`

### **2x tap weights** — 将 DFE 抽头权重乘以二 关（默认）| 开

选择以将 DFE 抽头权重乘以二。

SerDes Toolbox™ 中 DFECDR 模块的限幅器输出为 [-0.5 0.5]。但某些行业应用要求限幅器输出为 [-1 1]。**2x tap weights** 允许您快速将 DFE 抽头权重加倍以更改限幅器参考。

### CDR

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

时钟数据恢复中使用的时钟相位检测器选项。您可以在 bang-bang（Alexander）或波特率 type-A（Mueller-Muller）之间选择。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PhaseDetector` |
| **类型：** 字符向量 |
| **值：** `BangBang` | `BaudRateTypeA` |
| **默认：** `BangBang` |

### **Phase Offset (symbol time)** — 时钟相位偏移 `0`（默认）| 范围 [-0.5,0.5] 内的实数标量

时钟相位偏移，以符号时间的分数形式指定为范围 [-0.5,0.5] 内的实数标量。**Phase Offset** 用于手动偏移时钟概率分布函数（PDF）以获得更好的误码率（BER）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PhaseOffset` |
| **类型：** 字符向量 |
| **值：** 范围 [-0.5,0.5] 内的实数标量 |
| **默认：** `0` |

**数据类型：** `double`

### **Reference offset (ppm)** — 参考时钟偏移损伤 `0`（默认）| 范围 [0, 300] 内的实数标量

参考时钟偏移损伤，以百万分率（ppm）为单位指定为范围 [0, 300] 内的实数标量。**Reference offset (ppm)** 是发射器振荡器频率与接收器振荡器频率之间的偏差。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ReferenceOffset` |
| **类型：** 字符向量 |
| **值：** 范围 [0, 300] 内的实数标量 |
| **默认：** `0` |

**数据类型：** `double`

### **Early/late count threshold** — 触发相位更新的早/晚 CDR 计数阈值 `16`（默认）| 实数正整数 ≥5

触发相位更新的早/晚 CDR 计数阈值，指定为无单位的实数正整数 ≥5。增大 **Early/late count threshold** 的值可提供更稳定的输出时钟相位，但会牺牲收敛速度。由于位判决是在时钟相位输出处进行的，更稳定的时钟相位具有更好的误码率（BER）。

**Early/late count threshold** 还控制 CDR 的带宽。

#### 编程使用

|  |
| --- |
| **模块参数：** `Count` |
| **类型**：character vector |
| **值**：real positive integer ≥5 |
| **默认值**：`16` |

**Data Types:** `double`

### **Step (symbol time)** — 时钟相位分辨率 `0.0078`（默认）| 实数标量

时钟相位分辨率，指定为以符号时间分数表示的实数标量。**Step (symbol time)** 是 CDR 中相位调整次数的倒数。

#### 编程使用

|  |
| --- |
| **模块参数：** `Step` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`0.0078` |

**Data Types:** `double`

### **Frequency tracking gain** — 频率跟踪的内部增益 `0.00048828125`（默认）| 非负实数标量

频率跟踪环路的内部增益，指定为非负实数标量。

#### 依赖关系

要启用此参数，请将 **CDR Mode** 设置为 `2nd order`。

#### 编程使用

|  |
| --- |
| **模块参数：** `FrequencyStep` |
| **类型**：character vector |
| **值**：nonnegative real scalar |
| **默认值**：`0.00048828125` |

**Data Types:** `double`

### **Frequency tracking update** — 频率跟踪更新 `16`（默认）| 非负整数标量

每经过 **Frequency tracking update** 个符号，使用频率估计值更新系统相位旋转器时钟。

#### 依赖关系

要启用此参数，请将 **CDR Mode** 设置为 `2nd order`。

#### 编程使用

|  |
| --- |
| **模块参数：** `FrequencyCount` |
| **类型**：character vector |
| **值**：nonnegative real scalar |
| **默认值**：`16` |

**Data Types:** `double`

### **Frequency step ramp** — 初始内部频率跟踪增益达到指定值所需的符号时间数 `3000`（默认）| 非负整数标量

为帮助频率跟踪环路在仿真中尽早锁定，初始 **Frequency tracking gain** 从高值 1/(2\***Frequency tracking update**) 开始。然后 **Frequency tracking gain** 在大约 **Frequency step ramp** 个符号时间内逐渐减小到指定值。

#### 依赖关系

要启用此参数，请将 **CDR Mode** 设置为 `2nd order`。

#### 编程使用

|  |
| --- |
| **模块参数：** `FrequencyStepRamp` |
| **类型**：character vector |
| **值**：nonnegative real scalar |
| **默认值**：`3000` |

**Data Types:** `double`

### **Sensitivity (V)** — 采样锁存器亚稳态电压 `0`（默认）| 实数标量

采样锁存器亚稳态电压，指定为以伏特为单位的实数标量。如果数据采样电压位于（±**Sensitivity (V)**）区域内，则位错误的概率为 50%。

#### 编程使用

|  |
| --- |
| **模块参数：** `Sensitivity` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`0` |

**Data Types:** `double`

#### IBIS-AMI 参数

### **Mode** — 在 IBIS-AMI 模型中包含 Mode 参数 on（默认）| off

选择以将 **Mode** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Mode**，它将从 AMI 文件中移除，实际上将 **Mode** 硬编码为其当前值。

### **Tap weights** — 在 IBIS-AMI 模型中包含 Tap weights 参数 on（默认）| off

选择以将 **Tap weights** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Tap weights**，它将从 AMI 文件中移除，实际上将 **Tap weights** 硬编码为其当前值。

### **Phase Offset** — 在 IBIS-AMI 模型中包含 Phase Offset 参数 on（默认）| off

选择以在 IBIS-AMI 文件中将 **Phase Offset** 作为参数包含。如果取消选择 **Phase Offset**，则会将其从 AMI 文件中移除，实际上会将 **Phase Offset** 硬编码为其当前值。

### **Reference offset** — 在 IBIS-AMI 模型中包含 Reference offset 参数 on（默认）| off

选择以在 IBIS-AMI 文件中将 **Reference offset** 作为参数包含。如果取消选择 **Reference offset**，则会将其从 AMI 文件中移除，实际上会将 **Reference offset** 硬编码为其当前值。

## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

带时钟和数据恢复（CDR）的判决反馈均衡器（DFE）

DFECDR 模块对逐样本输入信号进行自适应处理，或对脉冲响应向量输入信号进行解析处理，以消除后游标抽头处的失真。

DFE 修改基带信号，以最小化时钟采样时刻的符号间干扰（ISI）。DFE 在每个时钟采样时刻对数据采样，并通过校正电压调整波形幅度。

对于脉冲响应处理，使用呼啦圈算法来寻找时钟采样位置。然后使用迫零算法确定 *N* 个校正因子，以在后续 *N* 个采样位置处无 ISI，其中 *N* 是 DFE 抽头数。

对于逐样本处理，时钟恢复通过一阶相位跟踪以及可选的二阶频率跟踪模型实现。bang-bang 相位检测器利用未均衡的边沿采样和已均衡的数据采样来确定最佳采样位置。第 *N* 个抽头的 DFE 校正电压通过寻找一个电压来自适应地确定，该电压补偿相隔 *N* 个符号时间的两个数据采样之间的任何相关性。这要求数据模式与信道 ISI 不相关，以实现正确的自适应行为。
