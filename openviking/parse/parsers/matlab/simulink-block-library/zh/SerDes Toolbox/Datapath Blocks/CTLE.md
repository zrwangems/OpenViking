---
type: simulink-block
title: 'CTLE'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'ctle'
documentation_source_path: 'ref/ctle.html'
language: zh-CN
chinese_source: worker-translation
---

# CTLE

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
  summary: CTLE 工作模式 Adapt（默认）| Off | Fixed
  group: ''
- name: Slice select
  summary: 选择使用 3D GPZ 矩阵的哪个角 0（默认）| 非负标量整数
  group: ''
- name: Configuration select
  summary: 选择在固定模式下应用哪个传递函数成员 0（默认）| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
  group: ''
- name: Specification
  summary: CTLE 响应的输入规格 'DC Gain and Peaking Gain'（默认）| 'DC Gain and AC Gain' | 'AC Gain and Peaking Gain' | 'GPZ Matrix'
  group: ''
- name: DC gain (dB)
  summary: 零频率处的增益 [0:-1:-8]（默认）| 标量 | 向量
  group: ''
- name: Peaking gain (dB)
  summary: AC 增益与 DC 增益之差 [0:8]（默认）| 标量 | 向量
  group: ''
- name: AC gain (dB)
  summary: 峰值频率处的增益 0（默认）| 标量 | 向量
  group: ''
- name: Peaking frequency (Hz)
  summary: CTLE 传递函数达到峰值的近似频率 5e9（默认）| 标量 | 向量
  group: ''
- name: Gain pole zero matrix
  summary: 增益极点零点矩阵
  group: ''
- name: Visualize Response
  summary: 绘制 CTLE 响应按钮
  group: ''
- name: Launch CTLE Fitter App
  summary: 启动 CTLE Fitter 应用按钮
  group: ''
- name: Mode
  summary: 在 IBIS-AMI 模型中包含 Mode 参数 on（默认）| off
  group: ''
- name: Slice select
  summary: 在 IBIS-AMI 模型中包含 Slice select 参数 on（默认）| off
  group: ''
- name: Configuration select
  summary: 在 IBIS-AMI 模型中包含 Configuration select 参数 on（默认）| off
  group: ''
```

### **Mode** — CTLE 工作模式 `Adapt`（默认）| `Off` | `Fixed`

CTLE 工作模式：

- `Off` — CTLE 被旁路，输入波形保持不变。
- `Fixed` — CTLE 将 **Configuration select** 指定的 CTLE 传递函数应用于输入波形。
- `Adapt` — 如果输入信号是冲激响应向量或波形向量，则 Init 子系统调用 CTLE System object™。CTLE System object 确定 CTLE 传递函数以最大化 SNR，并将该传递函数应用于输入波形以进行时域仿真。该优化后的传递函数由 CTLE 用于整个时域仿真。有关 Init 子系统的更多信息，请参阅 SerDes 系统中的统计分析

  如果输入信号是按样本逐个指定的标量，则 CTLE 以 `Fixed` 模式运行。

#### 编程使用

- 使用 `get_param(gcb,'Mode')` 查看当前 CTLE 的 **Mode**。
- 使用 `set_param(gcb,'Mode',value)` 将 CTLE 设置为特定的 **Mode**。

### **Slice select** — 选择使用 3D GPZ 矩阵的哪个角 `0`（默认）| 非负标量整数

选择在 CTLE 配置期间使用 3-D GPZ 矩阵的哪个切片、族或角。

必须将 **Specification** 参数设置为 `'GPZ Matrix'` 才能有效使用 **Slice Select** 参数。根据 GPZ 矩阵中可用的切片数量，您可以从下拉菜单中提供的从零开始的索引中选择您感兴趣的切片。

不能对某个切片使用 GPZ，而对另一个切片使用峰值增益、DC 增益或 AC 增益。

#### 编程使用

- 使用 `get_param(gcb,'SliceSelect')` 查看 **Slice select** 的当前值。
- 使用 `set_param(gcb,'SliceSelect',value)` 将 **Slice select** 设置为特定值。

**数据类型：** `double`

### **Configuration select** — 选择在固定模式下应用哪个传递函数成员 `0`（默认）| `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8`

选择在 CTLE 固定模式下应用哪个传递函数配置，指定为实数整数标量。根据 **Specification**，**Configuration select** 指定将哪个增益系数应用于滤波器传递函数。

例如，将 **Configuration select** 设置为 *n*，将 **Specification** 设置为 `'DC Gain and Peaking Gain'`，则选择 **DC gain (dB)** 和 **Peaking gain (dB)** 向量中的第 (*n*+1) 个元素应用于滤波器传递函数。

如果 CTLE **Mode** 设置为 `Adapt` 且输入是冲激响应向量或波形向量，则自动计算 **Configuration select** 以确定最佳眼高张开度。要查看 **Configuration select** 参数的值，请在 SerDes Designer 应用中选择 **Add Plots** > **Report**。

#### 编程使用

- 使用 `get_param(gcb,'ConfigSelect')` 查看 **Configuration select** 的当前值。
- 使用 `set_param(gcb,'ConfigSelect',value)` 将 **Configuration select** 设置为特定值。

**数据类型：** `double`

### **Specification** — CTLE 响应的输入规格 `'DC Gain and Peaking Gain'`（默认）| `'DC Gain and AC Gain'` | `'AC Gain and Peaking Gain'` | `'GPZ Matrix'`

定义将用于 CTLE 传递函数族的输入。有五个输入可用于定义 CTLE 传递函数族：**DC gain (dB)**、**Peaking gain (dB)**、**AC gain (dB)**、**Peaking frequency (Hz)** 和 **Gain pole zero matrix**。

您可以从三个增益和峰值频率中的任意两个来定义 CTLE 响应，也可以为 CTLE 定义 GPZ 矩阵。

- 选择 `'DC Gain and Peaking Gain'` 以根据 **DC gain (dB)**、**Peaking gain (dB)** 和 **Peaking frequency (Hz)** 指定 CTLE 响应。
- 选择 `'DC Gain and AC Gain'` 以根据 **DC gain (dB)**、**AC gain (dB)** 和 **Peaking frequency (Hz)** 指定 CTLE 响应。
- 选择 `'AC Gain and Peaking Gain'` 以根据 **AC gain (dB)**、**Peaking gain (dB)** 和 **Peaking frequency (Hz)** 指定 CTLE 响应。
- 选择 `'GPZ Matrix'` 以根据 **Gain pole zero matrix** 指定 CTLE 响应。

#### 编程使用

- 使用 `get_param(gcb,'Specification')` 查看当前 CTLE **Specification**。
- 使用 `set_param(gcb,'Specification',value)` 将 CTLE 设置为特定的 **Specification**。

**Data Types:** `char`

### **DC gain (dB)** — 零频率处的增益 `[0:-1:-8]`（默认）| 标量 | 向量

CTLE 传递函数在零频率处的增益，指定为以 dB 为单位的标量或向量。如果指定为标量，则通过标量扩展将其转换为与 **Peaking gain (dB)**、**AC gain (dB)** 和 **Peaking frequency (Hz)** 的长度匹配。如果指定为向量，则向量长度必须与 **Peaking gain (dB)**、**AC gain (dB)** 和 **Peaking frequency (Hz)** 中的向量相同。

#### 依赖关系

此参数仅在 **Specification** 设置为 `'DC Gain and Peaking Gain'` 或 `'DC Gain and AC Gain'` 时可用。

#### 编程使用

- 使用 `get_param(gcb,'DCGain')` 查看 **DC gain (dB)** 的当前值。
- 使用 `set_param(gcb,'DCGain',value)` 将 **DC gain (dB)** 设置为特定值。

**Data Types:** `double`

### **Peaking gain (dB)** — AC 增益与 DC 增益之差 `[0:8]`（默认）| 标量 | 向量

峰值增益，指定为以 dB 为单位的标量或向量。**Peaking gain (dB)** 是 CTLE 传递函数的 **AC gain (dB)** 与 **DC gain (dB)** 之差。如果指定为标量，则通过标量扩展将其转换为与 **DC gain (dB)**、**AC gain (dB)** 和 **Peaking frequency (Hz)** 的长度匹配。如果指定为向量，则向量长度必须与 **DC gain (dB)**、**AC gain (dB)** 和 **Peaking frequency (Hz)** 中的向量相同。

#### 依赖关系

此参数仅在 **Specification** 设置为 `'DC Gain and Peaking Gain'` 或 `'AC Gain and Peaking Gain'` 时可用。

#### 编程使用

- 使用 `get_param(gcb,'PeakingGain')` 查看 **Peaking gain (dB)** 的当前值。
- 使用 `set_param(gcb,'PeakingGain',value)` 将 **Peaking gain (dB)** 设置为特定值。

**Data Types:** `double`

### **AC gain (dB)** — 峰值频率处的增益 `0`（默认）| 标量 | 向量

CTLE 传递函数在峰值频率处的增益，指定为以 dB 为单位的标量或向量。如果指定为标量，则通过标量扩展将其转换为与 **DC gain (dB)**、**Peaking gain (dB)** 和 **Peaking frequency (Hz)** 的长度匹配。如果指定为向量，则向量长度必须与 **DC gain (dB)**、**Peaking gain (dB)** 和 **Peaking frequency (Hz)** 中的向量相同。

#### 依赖关系

此参数仅在 **Specification** 设置为 `'DC Gain and AC Gain'` 或 `'AC Gain and Peaking Gain'` 时可用。

#### 编程使用

- 使用 `get_param(gcb,'ACGain')` 查看 **AC gain (dB)** 的当前值。
- 使用 `set_param(gcb,'ACGain',value)` 将 **AC gain (dB)** 设置为特定值。

**Data Types:** `double`

### **Peaking frequency (Hz)** — CTLE 传递函数达到峰值的近似频率 `5e9`（默认）| 标量 | 向量

CTLE 传递函数在幅度上达到峰值的近似频率，指定为以 GHz 为单位的标量或向量。如果指定为标量，则通过标量扩展将其转换为与 **DC gain (dB)**、**AC gain (dB)** 和 **Peaking gain (dB)** 长度匹配。如果指定为向量，则向量长度必须与 **DC gain (dB)**、**AC gain (dB)** 和 **Peaking gain (dB)** 中的向量相同。

#### 依赖关系

当 **Specification** 设置为 `'GPZ Matrix'` 时，此参数不可用。

#### 编程使用

- 使用 `get_param(gcb,'PeakingFrequency')` 查看 **Peaking frequency (Hz)** 的当前值。
- 使用 `set_param(gcb,'PeakingFrequency',value)` 将 **Peaking frequency (Hz)** 设置为特定值。

**Data Types:** `double`

### **Gain pole zero matrix** — 增益极点零点矩阵

增益极点零点，指定为矩阵。**Gain pole zero matrix** 通过在第一列指定 **DC gain (dB)**（dB），然后在交替列中指定极点和零点，来显式定义 CTLE 传递函数族。极点和零点以 Hz 为单位指定。使用参数 **Configuration Select** 选择由 GPZ 矩阵的行定义的滤波器

该模块仅在使用级联滤波器时允许重复极点或零点。要更改该模块使用的滤波方法，请查看掩码下并双击 CTLE System object。这将启动模块参数对话框，您可以在 **Advanced** 选项卡中找到 **Filter method** 参数。

复极点或复零点必须具有共轭。为保证系统稳定性，极点数必须大于零点数。该模块忽略 0 Hz 的极点和零点，您可以使用它们对矩阵进行零填充。

您可以通过使用 3-D GPZ 矩阵来定义 CTLE 响应的多个切片。您可以拼接并零填充两个 GPZ 矩阵以扩展到第三维。

**Example:** 要创建具有三个极点和两个零点的增益极点零点矩阵，请按如下方式输入矩阵：[G, P1, Z1, P2, Z2, P3]。

#### 依赖关系

此参数仅在 **Specification** 设置为 `'GPZ Matrix'` 时可用。

#### 编程使用

- 使用 `get_param(gcb,'GPZ')` 查看 **Gain pole zero matrix** 的当前值。
- 使用 `set_param(gcb,'GPZ',value)` 将 **Gain pole zero matrix** 设置为特定值。

**Data Types:** `double`
**Complex Number Support:** Yes

### **Visualize Response** — 绘制 CTLE 响应按钮

点击以绘制 CTLE 响应。生成的绘图显示不同 CTLE 配置的 CTLE 传递函数族曲线。

### **Launch CTLE Fitter App** — 启动 CTLE Fitter 应用按钮

点击以启动 CTLE fitter 应用。有关详细信息，请参阅 CTLE Fitter。

#### IBIS-AMI 参数

### **Mode** — 在 IBIS-AMI 模型中包含 Mode 参数 on（默认）| off

选择以在 IBIS-AMI 文件中将 **Mode** 包含为参数。如果取消选择 **Mode**，则会将其从 AMI 文件中移除，从而有效地将 **Mode** 硬编码为其当前值。

### **Slice select** — 在 IBIS-AMI 模型中包含 Slice select 参数 on（默认）| off

选择以在 IBIS-AMI 文件中将 **Slice select** 包含为参数。如果取消选择 **Slice select**，则会将其从 AMI 文件中移除，从而有效地将 **Slice select** 硬编码为其当前值。

### **Configuration select** — 在 IBIS-AMI 模型中包含 Configuration select 参数 on（默认）| off

选择以在 IBIS-AMI 文件中将 **Configuration select** 包含为参数。如果取消选择 **Configuration select**，则会将其从 AMI 文件中移除，从而有效地将 **Configuration select** 硬编码为其当前值。
## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

### R2023b: 切片选择

现在，在配置 CTLE 时，您可以选择使用 3-D GPZ 矩阵的哪个切片、族或角。

## 描述

对连续时间线性均衡器 (CTLE) 进行建模

CTLE 模块应用线性峰值滤波器来均衡逐样本输入信号的频率响应。该均衡过程可减少由有损信道引起的失真。除非您定义增益-极点-零点 (GPZ) 矩阵，否则该滤波器为实一零点两极点 (1z/2p) 滤波器。时域滤波器系数可由一个大的部分分式或许多级联节计算得出。
