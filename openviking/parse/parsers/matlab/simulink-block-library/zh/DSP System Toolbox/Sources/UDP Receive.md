---
type: simulink-block
title: 'UDP Receive'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'udpreceive'
documentation_source_path: 'ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Message** — 接收的数据向量

UDP Receive 模块接收的数据，返回为 **Data type for Message** 中指定的数据类型的一维向量。如果选择 **Message is complex**，模块将接收的消息视为复数数据。

如果数据包在传输过程中被丢弃且接收方未收到该数据包，则接收的数据输出为空。

在您清除 **Output variable-size signal** 参数之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
**复数支持：** Yes

### **Length** — 数据包长度标量

接收到的数据包长度，返回为标量。此值由 **Maximum length for Message** 参数的值确定。

#### 依赖关系

仅当您清除 **Output variable-size signal** 参数时，此端口才会出现。

**数据类型：** `uint16`

## 参数

### **Local IP port** — IP 端口号 25000（默认）| [1, 65535] 范围内的标量

指定用于接收 UDP 数据包的 IP 端口号。此参数在生成的代码中可调，但在仿真期间不可调。

在 Linux® 上，要设置低于 1024 的 IP 端口号，请以 root 权限运行 MATLAB。例如，在 Linux 命令行中，输入 `sudo matlab`。

### **Remote IP address ('0.0.0.0' to accept all)** — 从中接受数据包的 IP 地址 '0.0.0.0'（默认）| IP 地址

指定从中接受 UDP 数据包的 IP 地址。指定特定 IP 地址以阻止来自其他地址的 UDP 数据包。若要接受来自任何 IP 地址的数据包，请指定 `'0.0.0.0'`。

### **Receive buffer size (bytes)** — 接收 UDP 数据包的缓冲区大小 8192（默认）| [1, 67108864] 范围内的标量

指定接收 UDP 数据包的缓冲区大小，以字节为单位。使缓冲区足够大，以避免缓冲区溢出导致的数据丢失。

### **Maximum length for Message** — 输出数据的最大长度 255（默认）| 标量

指定数据输出向量的最大长度，以向量元素为单位。将此参数设置为等于或大于 UDP 数据包数据大小的值。系统会截断超过此长度的数据。

如果禁用 **Output variable-size signal**，则模块输出为此参数指定的长度。

### **Data type for Message** — 消息的数据类型 `uint8`（默认）| `single` | `double` | `int8` | `int16` | `int32` | `uint16` | `uint32` | `boolean`

指定消息输出中向量元素的数据类型。将数据类型与用于创建 UDP 数据包的数据输入匹配。

### **Message is complex** — 消息数据复数性 off（默认）| on

指定模块是否将消息作为复数数据接收。选择此参数以将消息作为复数数据接收。如果接收的消息是实数数据，则清除此参数。

### **Output variable-size signal** — 长度可变的 Message 输出 on（默认）| off

指定您的模型是否支持长度可变的信号。如果您的模型支持长度可变的信号，请选择此参数。在这种情况下：

- 输出向量的长度可变，具体取决于 UDP 数据包中的数据量。
- 模块从单个未标记的输出发出数据向量。

如果您的模型不支持长度可变的信号，请清除此参数。在这种情况下：

- 模块发出固定长度的输出，其长度与 **Maximum length for Message** 指定的长度相同。
- 如果 UDP 数据包包含的数据少于固定长度输出，则差异部分包含无效数据。
- 模块从 **Message** 输出发出数据向量。
- 模块从 **Length** 输出发出有效数据的长度。

如果禁用此参数，则模块发出的输出为 **Maximum length for Message** 指定的长度。

### **Sample time (seconds)** — 调用模块的频率 `1`（默认）| 标量

指定调度器调用 UDP Receive 模块的频率，以秒为单位。输入大于零的值。在实时操作中，将此参数设置为较小的值可降低 UDP 消息丢失的可能性。

## 所属库

DSP System Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 从此模块生成的可执行文件依赖于 MATLAB 附带的预构建动态库文件（`.dll` 文件）。使用 `packNGo` 函数将从此模块生成的代码及所有相关文件打包到一个压缩 ZIP 文件中。使用此 ZIP 文件，您可以在未安装 MATLAB 的另一开发环境中重新定位、解包并重建项目。有关详细信息，请参阅 How To Run a Generated Executable Outside MATLAB。
- **Local IP port** 参数在生成的代码中可调，但在仿真期间不可调。您可以通过多种方式控制生成代码中的参数可调性。其中一种方式是将该参数配置为生成代码中全局结构的可调字段。其他方式包括将内置存储类或自定义存储类应用于 `Simulink.Parameter` 对象，并使用该对象设置模块参数的值。有关详细信息，请参阅 Create Tunable Calibration Parameter in the Generated Code (Simulink Coder)。

## 版本历史

**在 R2010a 中引入**

## 描述

在给定 IP 端口上接收 UDP 数据包

UDP Receive 模块从 IP 网络端口接收 UDP 数据包并将其保存到其缓冲区。由于 UDP 传输协议的性质，接收方无法保证接收到您使用 UDP Send 模块发送的所有数据包。在每个采样中，模块将单个 UDP 数据包的内容作为数据向量输出。

模块接收 UDP 数据包的本地 IP 端口号在生成的代码中可调。此模块生成的代码依赖于预构建的 `.dll` 文件。您可以在 MATLAB® 环境外运行此代码或重新部署它，但必须考虑额外的 `.dll` 文件。`packNGo` 函数创建一个 ZIP 文件，其中包含运行或重建此代码所需的各个部分。有关详细信息，请参阅 How To Run a Generated Executable Outside MATLAB。
