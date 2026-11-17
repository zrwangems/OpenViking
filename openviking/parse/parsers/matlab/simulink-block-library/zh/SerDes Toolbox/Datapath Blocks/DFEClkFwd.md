---
type: simulink-block
title: 'DFEClkFwd'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'dfeclkfwd'
documentation_source_path: 'ref/dfeclkfwd.html'
language: zh-CN
chinese_source: worker-translation
---

# DFEClkFwd

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

输入基带信号，可以是指定为标量的逐样本信号，也可以是冲激响应向量信号。

**数据类型：** `double`
### 输出

### **WaveOut** — 估计的信道输出 标量 | 向量

估计的信道输出。如果输入信号是指定为标量的逐样本信号，则输出也是标量。如果输入信号是冲激响应向量信号，则输出也是向量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Mode
  summary: DFE 工作模式 Fixed（默认）| Off | Adapt
  group: DFE
- name: Initial tap weights (V)
  summary: 初始 DFE 抽头权重 [0 0 0 0]（默认）| 行向量
  group: DFE
- name: Adaptive gain
  summary: 控制 DFE 抽头权重更新速率 9.6e-5（默认）| 正实数标量
  group: DFE
- name: Adaptive step size (V)
  summary: DFE 自适应步长分辨率 1e-06（默认）| 非负实数标量 | 非负实值行向量
  group: DFE
- name: Minimum DFE tap value (V)
  summary: 自适应抽头的最小值 -1（默认）| 实数标量 | 实值行向量
  group: DFE
- name: Maximum DFE tap value (V)
  summary: 自适应抽头最大值 1（默认）| 非负实数标量 | 非负实值行向量
  group: DFE
- name: 2x tap weights
  summary: 将 DFE 抽头权重乘以二 on（默认）| off
  group: DFE
- name: Phase offset (symbol time)
  summary: 手动时钟相位偏移 0（默认）| 范围 [−0.5, 0.5] 内的实数标量
  group: CDR
- name: Reference offset (ppm)
  summary: 参考时钟偏移损伤 0（默认）| 范围 [−300, 300] 内的实数标量
  group: CDR
- name: Early/late count threshold
  summary: 触发相位更新的早/晚 CDR 计数阈值 5（默认）| 正整数 ≥5
  group: CDR
- name: Step (symbol time)
  summary: 时钟相位分辨率 0.005（默认）| 实数标量
  group: CDR
- name: Sensitivity (V)
  summary: 采样锁存器亚稳态电压 0（默认）| 实数标量
  group: CDR
```

### DFE

### **Mode** — DFE 工作模式 `Fixed`（默认）| `Off` | `Adapt`

DFE 工作模式：

- `Off` — 旁路 DFE，输入波形保持不变。
- `Fixed` — DFE 将 **Initial tap weights (V)** 中指定的输入 DFE 抽头权重应用于输入波形。
- `Adapt` — DFE 模块为统计分析寻找最佳眼高张开度的最优 DFE 抽头值。在时域仿真期间，该模块使用自适应值作为起点并将其应用于输入波形。有关详细信息，请参阅 SerDes 系统中的统计分析。

#### 编程使用

- 使用 `get_param(gcb,'Mode')` 查看当前 DFEClkFwd 的 **Mode**。
- 使用 `set_param(gcb,'Mode',value)` 将 DFEClkFwd 设置为特定的 **Mode**。

### **Initial tap weights (V)** — 初始 DFE 抽头权重 `[0 0 0 0]`（默认）| 行向量

初始 DFE 抽头权重，以伏特为单位指定为行向量。向量的长度指定 DFE 抽头的数量。向量元素值指定该元素位置处抽头的强度。将向量元素值设置为零仅初始化该抽头。

您可以使用有效的 MATLAB 表达式来求值 **Initial tap weights (V)** 行向量。

**示例：** `set_param(gcb,'TapWeights',"zeros(1,100)")` 创建一个具有 100 个抽头的 DFE。

#### 编程使用

- 使用 `get_param(gcb,'TapWeights')` 查看 DFEClkFwd **Initial tap weights (V)** 的当前值。
- 使用 `set_param(gcb,'TapWeights',value)` 将 DFEClkFwd 设置为特定的 **Initial tap weights (V)** 向量值。

**数据类型：** `double`

### **Adaptive gain** — 控制 DFE 抽头权重更新速率 `9.6e-5`（默认）| 正实数标量

控制 DFE 抽头权重更新速率，指定为无单位的正实数标量。增大 **Adaptive gain** 的值会导致 DFE 自适应更快收敛，但代价是 DFE 抽头值中会有更多噪声。

#### 编程使用

- 使用 `get_param(gcb,'EqualizationGain')` 查看当前 DFEClkFwd **Adaptive gain** 值。
- 使用 `set_param(gcb,'EqualizationGain',value)` 将 DFEClkFwd 设置为特定的 **Adaptive gain** 值。

**数据类型：** `double`

### **Adaptive step size (V)** — DFE 自适应步长分辨率 `1e-06`（默认）| 非负实数标量 | 非负实值行向量

DFE 自适应步长分辨率，以伏特为单位指定为非负实数标量或非负实值行向量。指定为标量时应用于所有 DFE 抽头，或指定为与 **Initial tap weights (V)** 长度相同的向量。

**Adaptive step size (V)** 指定从一个时间步到下一个时间步的最小 DFE 抽头变化，以模拟硬件限制。将 **Adaptive step size (V)** 设置为 `0` 会产生没有任何分辨率限制的 DFE 抽头值。

#### 编程使用

- 使用 `get_param(gcb,'EqualizationStep')` 查看当前 DFEClkFwd **Adaptive step size (V)** 值。
- 使用 `set_param(gcb,'EqualizationStep',value)` 将 DFEClkFwd 设置为特定的 **Adaptive step size (V)** 值。

**数据类型：** `double`

### **Minimum DFE tap value (V)** — 自适应抽头的最小值 `-1`（默认）| 实数标量 | 实值行向量

自适应抽头的最小值，以伏特为单位指定为实数标量或实值行向量。指定为标量时应用于所有 DFE 抽头，或指定为与 **Initial tap weights (V)** 长度相同的向量。

#### 程序化使用

- 使用 `get_param(gcb,'MinimumTap')` 查看当前 DFEClkFwd 的 **Minimum DFE tap value (V)** 值。
- 使用 `set_param(gcb,'MinimumTap',value)` 将 DFEClkFwd 设置为 **Minimum DFE tap value (V)** 的特定值。

**数据类型：** `double`

### **Maximum DFE tap value (V)** — 自适应抽头最大值 `1`（默认）| 非负实数标量 | 非负实值行向量

自适应抽头的最大值，指定为非负实数标量或非负实值行向量，单位为伏特。指定为标量时应用于所有 DFE 抽头，或指定为与 **Initial tap weights (V)** 长度相同的向量。

#### 程序化使用

- 使用 `get_param(gcb,'MaximumTap')` 查看当前 DFEClkFwd 的 **Maximum DFE tap value (V)** 值。
- 使用 `set_param(gcb,'MaximumTap',value)` 将 DFEClkFwd 设置为 **Maximum DFE tap value (V)** 的特定值。

**数据类型：** `double`

### **2x tap weights** — 将 DFE 抽头权重乘以二 on（默认）| off

选择以将 DFE 抽头权重乘以二。

SerDes Toolbox™ 中 DFEClkFwd 模块的判决器输出为 `[-0.5 0.5]`。但某些行业应用要求判决器输出为 `[-1 1]`。**2x tap weights** 允许您快速将 DFE 抽头权重加倍以更改判决器参考。

### CDR

### **Phase offset (symbol time)** — 手动时钟相位偏移 `0`（默认）| 范围 [−0.5, 0.5] 内的实数标量

用于移动恢复时钟相位的手动时钟相位偏移，指定为范围 [-0.5, 0.5] 内的实数标量，以符号时间的分数表示。**Phase offset (symbol time)** 用于手动偏移时钟概率分布函数 (PDF)，以获得更好的误码率 (BER)。

#### 程序化使用

- 使用 `get_param(gcb,'PhaseOffset')` 查看当前 DFEClkFwd 的 **Phase offset (symbol time)** 值。
- 使用 `set_param(gcb,'PhaseOffset',value)` 将 DFEClkFwd 设置为 **Phase offset (symbol time)** 的特定值。

**数据类型：** `double`

### **Reference offset (ppm)** — 参考时钟偏移损伤 `0`（默认）| 范围 [−300, 300] 内的实数标量

参考时钟偏移损伤，指定为范围 [−300, 300] 内的实数标量，单位为百万分率 (ppm)。**Reference offset (ppm)** 是发射器振荡器频率与接收器振荡器频率之间的偏差。

#### 程序化使用

- 使用 `get_param(gcb,'ReferenceOffset')` 查看当前 DFEClkFwd 的 **Reference offset (ppm)** 值。
- 使用 `set_param(gcb,'ReferenceOffset',value)` 将 DFEClkFwd 设置为 **Reference offset (ppm)** 的特定值。

**数据类型：** `double`

### **Early/late count threshold** — 触发相位更新的早/晚 CDR 计数阈值 `5`（默认）| 正整数 ≥5

触发相位更新的早或晚 CDR 计数阈值，指定为无单位正整数 ≥5。增大 **Early/late count threshold** 的值可提供更稳定的输出时钟相位，但会牺牲收敛速度。由于位判决在时钟相位输出处进行，更稳定的时钟相位具有更好的误码率 (BER)。

**Early/late count threshold** 还控制 CDR 的带宽。

#### 程序化使用

- 使用 `get_param(gcb,'Count')` 查看当前 DFEClkFwd 的 **Early/late count threshold** 值。
- 使用 `set_param(gcb,'Count',value)` 将 DFEClkFwd 设置为 **Early/late count threshold** 的特定值。

**数据类型：** `double`

### **Step (symbol time)** — 时钟相位分辨率 `0.005`（默认）| 实数标量

恢复时钟的时钟相位分辨率，指定为以符号时间分数表示的实数标量。**Step (symbol time)** 是 CDR 中相位调整次数的倒数。如果 CDR 有 128 个相位调整步进，则 **Step (symbol time)** 值为 1/128。

#### 程序化使用

- 使用 `get_param(gcb,'ClockStep')` 查看当前 DFEClkFwd **Step (symbol time)** 值。
- 使用 `set_param(gcb,'ClockStep',value)` 将 DFEClkFwd 设置为 **Step (symbol time)** 的特定值。

**数据类型：** `double`

### **Sensitivity (V)** — 采样锁存器亚稳态电压 `0`（默认）| 实数标量

采样锁存器亚稳态电压，指定为以伏特为单位的实数标量。如果数据采样电压位于 (±**Sensitivity (V)**) 区域内，则误码概率为 50%。

#### 程序化使用

- 使用 `get_param(gcb,'Sensitivity')` 查看当前 DFEClkFwd **Sensitivity (V)** 值。
- 使用 `set_param(gcb,'Sensitivity',value)` 将 DFEClkFwd 设置为 **Sensitivity (V)** 的特定值。

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

接收器 AMI 模型中带时钟前向的 DFE

在并行链路通道中，一个单独的时钟（或选通）信号与数据信号一起发送，用于锁存每个单独的数据位。这被称为时钟前向。IBIS-AMI 规范描述了一种机制，通过该机制可以将时钟波形或恢复的时钟时间传递给数据 AMI 接收器模型，以使模型制作者能够访问时钟。这使接收器模型能够包含时钟相位噪声、时钟树延迟、相位插值器等。

您可以使用 DFEClkFwd 模块根据 IBIS-AMI 规范来仿真和生成时钟前向 DLL。
