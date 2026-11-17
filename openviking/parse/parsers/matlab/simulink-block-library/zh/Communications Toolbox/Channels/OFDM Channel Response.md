---
type: simulink-block
title: 'OFDM Channel Response'
family: 'channels'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Channels'
documentation_page: 'ofdmchannelresponseblock'
documentation_source_path: 'ref/ofdmchannelresponseblock.html'
language: zh-CN
chinese_source: worker-translation
---

# OFDM Channel Response

## 端口

### 输入

### **Path gains** — 信道路径增益数组

信道路径增益，指定为 *N*S-by-*N*P-by-T-by-*N*R 的值数组。

- *N*S 是样本数。
- *N*P 是路径数。
- *N*T 是发射天线数。
- *N*R 是接收天线数。

信道路径增益遵循由衰落信道 System object 计算并输出的信道路径增益定义。例如，请参阅 MIMO Fading Channel 或 SISO Fading Channel。此模块假设路径增益采样率与 OFDM 采样率匹配。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **Path filters** — 信道路径滤波器系数矩阵

信道路径滤波器系数，指定为 *N*P-by-*N*H 的值矩阵。

- *N*P 是路径数。
- *N*H 是冲激响应样本数。

信道路径滤波器系数矩阵用于针对每个样本以及每对发射和接收天线，将路径增益转换为信道滤波器抽头增益。信道路径滤波器系数遵循由衰落信道 System object 的 `info` 对象函数计算的信道路径滤波器系数定义。

信道路径增益遵循由衰落信道 System object 计算并输出的信道路径增益定义。例如，请参阅 MIMO Fading Channel 或 SISO Fading Channel。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **Offset** — 定时偏移标量

以样本为单位的定时偏移，指定为非负整数标量。

#### 依赖关系

- 要启用此输入端口，请选择 **启用定时偏移输入端口** 参数。

**数据类型：** `double` | `single`

### 输出

### **hEst** — 频率响应数组

频率响应，返回为 *N*SC-by-*N*Symbols-by-*N*T-by-*N*R 数组。

- *N*SC 是 OFDM 子载波数，等于 **活动子载波索引** 的长度。
- *N*Symbols 是 **Path gains** 中包含的完整 OFDM 符号数。具体而言，floor(*N*S/(*N*FFT + *L*CP))。

  - *N*S 是 **Path gains** 中的样本数
  - *N*FFT 是 **FFT 长度** 的值
  - *L*CP 是 **循环前缀长度** 的值。
- *N*T 是发射天线数。
- *N*R 是接收天线数。

- 返回的频率响应对应于接收端使用定时偏移进行的 OFDM 符号定时对齐：

  - 当选择 **启用定时偏移输入端口** 时，由 **Offset** 端口提供
  - 当未选择 **启用定时偏移输入端口** 时，由 `channelDelay` 函数使用 **Path gains** 和 **Path filters** 作为输入计算得出的 OFDM 发射机与 OFDM 接收机之间的定时偏移

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **FFT 长度** — FFT 长度 `512`（默认）| 正整数

FFT 长度，指定为正整数标量。FFT 长度必须与 OFDM 调制信号的 FFT 长度一致。

### **循环前缀长度** — 一个 OFDM 符号的循环前缀长度 `16`（默认）| 非负整数

一个 OFDM 符号的循环前缀长度，指定为值小于 **FFT 长度** 的非负整数标量。

### **活动子载波索引** — 活动子载波数量 `1:512`（默认）| 正整数 | 列向量

活动子载波数量，指定为范围 [`1`, **FFT 长度**] 中的正整数标量或列向量。

### **启用定时偏移输入端口** — 用于添加定时偏移输入端口的选项 `off`（默认）| `on`

选择此参数可添加输入端口以输入定时偏移。

- `on` — 添加 **Offset** 输入端口，以指定用于信道响应估计的定时偏移。
- `off` — 模块使用 **Path gains** 和 **Path filters** 输入来估计用于 OFDM 信道响应估计的定时偏移。

### **仿真使用** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项需要较少的启动时间，但后续仿真的速度比 `Code generation` 选项慢。在此模式下，可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 为模块生成 C 代码。除非模型更改，否则模型将在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比 `Interpreted execution` 选项快。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / Channels

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

计算 OFDM 信道响应

OFDM Channel Response 模块通过使用来自信道的完美信息，在频域中计算 OFDM 信道响应。有关详细信息，请参阅 OFDM Channel Response。

此图标显示启用了所有端口的模块。

显示所有输入端口（path gains、path filters 和 offset）以及输出端口（hEst）的 OFDM Channel Response 模块。
