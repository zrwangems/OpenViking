---
type: simulink-block
title: 'Configuration'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'configuration'
documentation_source_path: 'ref/configuration.html'
language: zh-CN
chinese_source: worker-translation
---

# Configuration

## 端口

R2025b 中未记录。

## 参数

### **Symbol time (s)** — 单个符号持续时间的时长 `100e-12`（默认）| 实正标量

单个符号持续时间的时长，指定为以 s 为单位的实正标量。

#### 编程用法

- 使用 `get_param(gcb,'SymbolTime')` 查看 **Symbol time (s)** 的当前值。
- 使用 `set_param(gcb,'SymbolTime',value)` 将 **Symbol time (s)** 设置为特定值。

**数据类型：** `double`

### **Samples per symbol** — 每个符号的数据点数 `16`（默认）| `8` | `32` | `64` | `128`

每个符号的数据点数。

#### 编程用法

- 使用 `get_param(gcb,'SamplesPerSymbol')` 查看 **Samples per symbol** 的当前值。
- 使用 `set_param(gcb,'SamplesPerSymbol',value)` 将 **Samples per symbol** 设置为特定值。

**数据类型：** `double`

### **Sample interval (s)** — 波形的均匀时间步长 `6.25e-12`（默认）| 实正标量

波形的均匀时间步长，指定为以 s 为单位的实正标量。此参数为只读，并由 **Symbol time (s)** 和 **Samples per symbol** 派生。

#### 编程用法

- 使用 `get_param(gcb,'SampleIntervalText')` 查看 **Sample interval (s)** 的当前值。

**数据类型：** `double`

### **Target BER** — 目标误码率 `1e-6`（默认）| 实正标量

用于生成眼图轮廓的目标误码率，指定为无单位的实正标量。

#### 编程用法

- 使用 `get_param(gcb,'TargetBER')` 查看 **Target BER** 的当前值。
- 使用 `set_param(gcb,'TargetBER',value)` 将 **Target BER** 设置为特定值。

**数据类型：** `double`

### **Modulation** — 调制方案 `NRZ`（默认）| `PAM3` | `PAM4` | `PAM5` | `PAM6` | `PAM7` | `PAM8` | `PAM9` | `PAM10` | `PAM11` | `PAM12` | `PAM13` | `PAM14` | `PAM15` | `PAM16`

调制方案中的逻辑电平数，指定为介于 `NRZ`（2 电平）和 `PAM16`（16 电平）之间。

#### 编程用法

- 使用 `get_param(gcb,'Modulation')` 查看 **Modulation** 的当前值。
- 使用 `set_param(gcb,'Modulation',value)` 将 **Modulation** 设置为特定值。

**数据类型：** `char`

### **Signaling** — 信号如何通过导线传输 `'Differential'`（默认）| `'Single-ended'`

传入信号如何通过导线传输：

- `'Differential'` — 使用差分信号对传输传入信号。接收器响应两个信号之间的差值。
- `'Single-ended'` — 使用变化的电压传输传入信号。接收器响应传入信号与参考或地之间的差值。

**Signaling** 仅影响生成的 IBIS 文件。更改信令类型时，Simulink 中的电压电平不会改变。当 **Channel model** 为 `Loss model` 时，**Signaling** 还会影响 Analog Channel 的 **Impedance**。

#### 编程用法

- 使用 `get_param(gcb,'Signaling')` 查看 **Signaling** 的当前值。
- 使用 `set_param(gcb,'Signaling',value)` 将 **Signaling** 设置为特定值。

**数据类型：** `char`

### **Plot statistical analysis after simulation** — 仿真后绘制统计分析 on（默认）| off

选择以在仿真运行后绘制统计分析 (Init) 结果。默认情况下，此选项处于选中状态。从均衡脉冲响应推导出的结果包括脉冲响应、波形、统计眼图以及统计眼图指标（眼高、眼宽、眼面积、通道工作裕量以及垂直眼闭合）。

### **Plot time domain analysis after simulation** — 仿真后绘制时域分析 on（默认）| off

选择以在仿真运行后绘制时域分析结果。默认情况下，此选项处于选中状态。结果包括带时钟节拍直方图的时域眼图以及时域眼图指标（眼高、眼宽、眼面积、通道工作裕量、垂直眼闭合以及最小 BER）。

时域眼图由接收器模块的输出以及由 DFECDR、CDR block 或 IBIS-AMI clock\_times block 生成的时钟节拍推导得出。为生成有意义的时域眼图，将使用 SerDes IBIS-AMI Manager 对话框 **Export** 选项卡中 Tx 和 Rx 的 **Bits to ignore** 参数的最大值。

### **Eye Diagram Clock** — 用于在后仿真结果中形成眼图的触发 `Clocked`（默认）| `Ideal`

用于在后仿真结果中形成眼图的触发：

- `Clocked` — 数据眼图显示为如同受恢复时钟控制。
- `Ideal` — 数据眼图和时钟 PDF 相对于理想外部参考时钟独立确定。

有关详细信息，请参阅 Clock Modes (Signal Integrity Toolbox)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **Open SerDes IBIS-AMI Manager** — Open SerDes IBIS-AMI Manager 按钮

单击以打开 SerDes IBIS-AMI Manager 对话框。使用此对话框，可以设置 IBIS 和 AMI 文件内容并导出 IBIS-AMI 模型。

在 SerDes IBIS-AMI Manager 对话框的 **Export** 选项卡中，为发送器和接收器设置模型配置（Tx 和 Rx、I/O、redriver、retimer）、IBIS 设置（模型名称、corner 百分比）和 AMI 模型设置（模型类型、要忽略的位数），并指定文件创建选项。

SerDes IBIS-AMI Manager 对话框的 **IBIS** 选项卡包含 IBS 文件内容。

可以使用 **AMI-Tx** 和 **AMI-Rx** 选项卡添加自定义 AMI 参数、附加抽头结构以及抖动和噪声曲线。有关详细信息，请参阅 Manage Contents of IBIS and AMI files。

### **Open Signal Integrity Link** — Open Signal Integrity Link to Signal Integrity Toolbox™ 按钮

单击以打开 Signal Integrity Link 对话框。Signal Integrity Link 对话框用于在 Signal Integrity Toolbox 的 Serial Link Designer 或 Parallel Link Designer 应用中测试 IBIS-AMI SerDes 模型。可以将复现 Serial Link Designer 或 Parallel Link Designer 测试用例所需的数据传回 Simulink，以进行调试和改进。

使用 Signal Integrity Link，可以：

- 创建 Serial Link Designer 项目。
- 创建 Parallel Link Designer 项目。
- 将 Serial Link Designer 或 Parallel Link Designer 仿真数据导入 Simulink 工作区。
- 使用来自 Simulink 工作区的新数据更新 Serial Link Designer 或 Parallel Link Designer。

如果链接的 Serial Link Designer 或 Parallel Link Designer 项目与 SerDes Simulink 模型文件位于不同目录中，则需要保存完整路径以便定位它。有关详细信息，请参阅 Signal Integrity Link。

## 所属库

SerDes Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

配置 SerDes 系统模型中的系统级设置

Configuration 模块设置 SerDes 系统的系统级设置，例如符号时间、每个符号的采样数、目标误码率 (BER)、调制方案和信令类型。它还配置 IBIS 和 AMI 模型的生成并自定义 AMI 参数。
