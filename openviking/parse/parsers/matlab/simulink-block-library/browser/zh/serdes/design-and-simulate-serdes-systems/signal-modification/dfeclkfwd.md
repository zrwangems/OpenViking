---
type: simulink-block
title: 'DFEClkFwd'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Design and Simulate SerDes Systems / Signal Modification'
documentation_page: 'dfeclkfwd'
documentation_source_path: 'ref/dfeclkfwd.html'
language: zh-CN
chinese_source: worker-translation
---

# DFEClkFwd

## 端口

### 输入

### **WaveIn** — 输入基带信号 标量 | 向量

输入基带信号，可以指定为按样本的信号（标量），或指定为冲激响应向量信号。

**数据类型：** `double`

### 输出

### **WaveOut** — 估计的信道输出 标量 | 向量

估计的信道输出。如果输入信号是指定为标量的按样本信号，则输出也是标量。如果输入信号是冲激响应向量信号，则输出也是向量。

**数据类型：** `double`

## 参数

### DFE

### **Mode** — DFE 工作模式 `Fixed`（默认）| `Off` | `Adapt`

DFE 工作模式：

- `Off` — DFE 被旁路，输入波形保持不变。
- `Fixed` — DFE 将 **Initial tap weights (V)** 中指定的输入 DFE 抽头权重应用于输入波形。
- `Adapt` — DFE 模块为统计分析找到最佳眼高开口的最优 DFE 抽头值。在时域仿真期间，模块使用自适应值作为起点，并将其应用于输入波形。有关更多信息，请参阅 Statistical Analysis in SerDes Systems。

#### 编程用法

- 使用 `get_param(gcb,'Mode')` 查看当前 DFEClkFwd **Mode**。
- 使用 `set_param(gcb,'Mode',value)` 将 DFEClkFwd 设置为特定的 **Mode**。

### **Initial tap weights (V)** — 初始 DFE 抽头权重 `[0 0 0 0]`（默认）| 行向量

初始 DFE 抽头权重，以伏特为单位指定为行向量。向量的长度指定 DFE 抽头数量。向量元素值指定该元素位置处抽头的强度。将向量元素值设置为零仅初始化该抽头。

您可以使用有效的 MATLAB 表达式来计算 **Initial tap weights (V)** 行向量。

**示例：** `set_param(gcb,'TapWeights',"zeros(1,100)")` 创建一个具有 100 个抽头的 DFE。

#### 编程用法

- 使用 `get_param(gcb,'TapWeights')` 查看 DFEClkFwd **Initial tap weights (V)** 的当前值。
- 使用 `set_param(gcb,'TapWeights',value)` 将 DFEClkFwd 设置为特定的 **Initial tap weights (V)** 向量值。

**数据类型：** `double`

### **Adaptive gain** — 控制 DFE 抽头权重更新速率 `9.6e-5`（默认）| 正实数标量

控制 DFE 抽头权重更新速率，指定为无单位的正实数标量。增大 **Adaptive gain** 的值会使 DFE 自适应收敛更快，但代价是 DFE 抽头值中的噪声更多。

#### 编程用法

- 使用 `get_param(gcb,'EqualizationGain')` 查看当前 DFEClkFwd **Adaptive gain** 值。
- 使用 `set_param(gcb,'EqualizationGain',value)` 将 DFEClkFwd 设置为特定的 **Adaptive gain** 值。

**数据类型：** `double`

### **Adaptive step size (V)** — DFE 自适应步长分辨率 `1e-06`（默认）| 非负实数标量 | 非负实值行向量

DFE 自适应步长分辨率，以伏特为单位指定为非负实数标量或非负实值行向量。指定为标量以应用于所有 DFE 抽头，或指定为与 **Initial tap weights (V)** 长度相同的向量。

**Adaptive step size (V)** 指定从一个时间步到下一个时间步的最小 DFE 抽头变化，以模拟硬件限制。将 **Adaptive step size (V)** 设置为 `0` 会产生没有任何分辨率限制的 DFE 抽头值。

#### 编程用法

- 使用 `get_param(gcb,'EqualizationStep')` 查看当前 DFEClkFwd **Adaptive step size (V)** 值。
- 使用 `set_param(gcb,'EqualizationStep',value)` 将 DFEClkFwd 设置为特定的 **Adaptive step size (V)** 值。

**数据类型：** `double`

### **Minimum DFE tap value (V)** — 自适应抽头的最小值 `-1`（默认）| 实数标量 | 实值行向量

自适应抽头的最小值，以伏特为单位指定为实数标量或实值行向量。指定为标量以应用于所有 DFE 抽头，或指定为与 **Initial tap weights (V)** 长度相同的向量。

#### 编程用法

- 使用 `get_param(gcb,'MinimumTap')` 查看当前 DFEClkFwd **Minimum DFE tap value (V)** 值。
- 使用 `set_param(gcb,'MinimumTap',value)` 将 DFEClkFwd 设置为特定的 **Minimum DFE tap value (V)** 值。

**数据类型：** `double`

### **Maximum DFE tap value (V)** — 自适应抽头的最大值 `1`（默认）| 非负实数标量 | 非负实值行向量

自适应抽头的最大值，以伏特为单位指定为非负实数标量或非负实值行向量。指定为标量以应用于所有 DFE 抽头，或指定为与 **Initial tap weights (V)** 长度相同的向量。

#### 编程用法

- 使用 `get_param(gcb,'MaximumTap')` 查看当前 DFEClkFwd **Maximum DFE tap value (V)** 值。
- 使用 `set_param(gcb,'MaximumTap',value)` 将 DFEClkFwd 设置为特定的 **Maximum DFE tap value (V)** 值。

**数据类型：** `double`

### **2x tap weights** — 将 DFE 抽头权重乘以二 on（默认）| off

选择以将 DFE 抽头权重乘以二。

来自 SerDes Toolbox™ 的 DFEClkFwd 模块中判决器的输出为 `[-0.5 0.5]`。但某些行业应用要求判决器输出为 `[-1 1]`。**2x tap weights** 允许您快速将 DFE 抽头权重加倍，以更改判决器参考。

### CDR

### **Phase offset (symbol time)** — 手动时钟相位偏移 `0`（默认）| 范围 [−0.5, 0.5] 内的实数标量

手动时钟相位偏移，用于移动恢复的时钟相位，以符号时间的分数指定为范围 [-0.5, 0.5] 内的实数标量。**Phase offset (symbol time)** 用于手动移动时钟概率分布函数 (PDF)，以获得更好的误码率 (BER)。

#### 编程用法

- 使用 `get_param(gcb,'PhaseOffset')` 查看当前 DFEClkFwd **Phase offset (symbol time)** 值。
- 使用 `set_param(gcb,'PhaseOffset',value)` 将 DFEClkFwd 设置为特定的 **Phase offset (symbol time)** 值。

**数据类型：** `double`

### **Reference offset (ppm)** — 参考时钟偏移损伤 `0`（默认）| 范围 [−300, 300] 内的实数标量

参考时钟偏移损伤，以百万分率 (ppm) 为单位指定为范围 [−300, 300] 内的实数标量。**Reference offset (ppm)** 是发射器振荡器频率与接收器振荡器频率之间的偏差。

#### 编程用法

- 使用 `get_param(gcb,'ReferenceOffset')` 查看当前 DFEClkFwd **Reference offset (ppm)** 值。
- 使用 `set_param(gcb,'ReferenceOffset',value)` 将 DFEClkFwd 设置为特定的 **Reference offset (ppm)** 值。

**数据类型：** `double`

### **Early/late count threshold** — 触发相位更新的早或晚 CDR 计数阈值 `5`（默认）| 正实数整数 ≥5

触发相位更新的早或晚 CDR 计数阈值，指定为无单位的正实数整数 ≥5。增大 **Early/late count threshold** 的值会提供更稳定的输出时钟相位，但代价是收敛速度。由于位判决是在时钟相位输出处做出的，更稳定的时钟相位具有更好的误码率 (BER)。

**Early/late count threshold** 还控制 CDR 的带宽。

#### 编程用法

- 使用 `get_param(gcb,'Count')` 查看当前 DFEClkFwd **Early/late count threshold** 值。
- 使用 `set_param(gcb,'Count',value)` 将 DFEClkFwd 设置为特定的 **Early/late count threshold** 值。

**数据类型：** `double`

### **Step (symbol time)** — 时钟相位分辨率 `0.005`（默认）| 实数标量

恢复时钟的时钟相位分辨率，以符号时间的分数指定为实数标量。**Step (symbol time)** 是 CDR 中相位调整次数的倒数。如果 CDR 具有 128 个相位调整步长，则 **Step (symbol time)** 值为 1/128。

#### 编程用法

- 使用 `get_param(gcb,'ClockStep')` 查看当前 DFEClkFwd **Step (symbol time)** 值。
- 使用 `set_param(gcb,'ClockStep',value)` 将 DFEClkFwd 设置为特定的 **Step (symbol time)** 值。

**数据类型：** `double`

### **Sensitivity (V)** — 采样锁存器亚稳态电压 `0`（默认）| 实数标量

采样锁存器亚稳态电压，以伏特为单位指定为实数标量。如果数据采样电压位于 (±**Sensitivity (V)**) 区域内，则有 50% 的误码概率。

#### 编程用法

- 使用 `get_param(gcb,'Sensitivity')` 查看当前 DFEClkFwd **Sensitivity (V)** 值。
- 使用 `set_param(gcb,'Sensitivity',value)` 将 DFEClkFwd 设置为特定的 **Sensitivity (V)** 值。

**数据类型：** `double`

## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

接收器 AMI 模型中的带时钟转发的 DFE

在并行链路通道中，单独的时钟（或选通）信号随数据信号一起发送，用于锁存每个单独的数据位。这称为时钟转发。IBIS-AMI Specification 描述了一种机制，通过该机制可以将时钟波形或恢复的时钟时刻传递给数据 AMI 接收器模型，以允许模型制作者访问时钟。这使接收器模型能够包含时钟相位噪声、时钟树延迟、相位插值器等。

您可以使用 DFEClkFwd 模块根据 IBIS-AMI Specification 仿真并生成时钟转发 DLL。
