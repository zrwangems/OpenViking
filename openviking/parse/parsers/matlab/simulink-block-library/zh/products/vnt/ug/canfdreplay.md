---
type: simulink-block
title: 'CAN FD Replay'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN and CAN FD Communication / Communication in Simulink / CAN FD'
documentation_page: 'canfdreplay'
documentation_source_path: 'ug/canfdreplay.html'
language: zh-CN
chinese_source: official
---

# CAN FD Replay

## 端口

### 输出

### **CAN Msg** — 回放的 CAN FD 报文 `CAN_FD_MESSAGE_BUS`

此输出端口包含在该特定时间步记录的打包的 CAN FD 报文，以 `CAN_FD_MESSAGE_BUS` 类型的信号总线形式输出。

**数据类型:** `CAN_FD_MESSAGE_BUS`

### **f()** — 函数调用事件输出 函数调用事件

当模块接收到新报文时，此端口向函数调用子系统提供触发。您可以将其连接到 Function-Call Subsystem (Simulink) 以解包和处理报文。

**数据类型:** `function-call event`

## 参数

**提示**

在配置 CAN FD Receive 模块参数之前，请先配置模型中的 CAN FD Configuration 模块。

### **文件名** — 具有报文的 MAT 文件的路径和名称 `untitled.mat` (默认) | 文件名

指定包含您可以回放的已记录 CAN FD 报文的 MAT 文件的路径和名称。您可以点击**浏览**以浏览到文件位置并选择文件。

### **变量名称** — MAT 文件中存储报文的变量 `ans` (默认) | 变量

指定 MAT 文件中存储 CAN FD 报文的变量。

### **回放报文的次数** — 重复值 `Inf` (默认) | 整数

指定要在模型中回放报文的次数。您可以指定任何正整数，包括 `Inf`。指定 `Inf` 会不断回放报文，直到仿真停止。

### **将报文回放给** — 指定输出位置 CAN FD 总线 (默认) | `Output port`

指定模型是将报文回放到 CAN FD 网络还是输出端口。对于网络，您还必须指定一个**设备**。

### **设备** — CAN FD 设备和通道 设备列表选项

选择 CAN FD 网络上作为报文回放目标的设备。如果为**将报文回放给**参数选择了 `Output port`，则此字段不可用。

### **采样时间** — 模块执行速率 `0.01` (默认) | 数值

指定仿真期间模块的采样时间。该值定义在仿真期间 CAN FD Replay 模块运行的频率。如果模块位于触发子系统内或要继承采样时间，则可以将 `–1` 指定为采样时间。您还可以为采样时间指定一个 MATLAB 变量。默认值为 `0.01` 仿真秒。有关详细信息，请参阅硬件接口模型中的计时。

## 所属库

Vehicle Network Toolbox / CAN FD Communication

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

此模块生成的代码可移植性有限，只能在主机上运行。请参阅代码生成。

## 版本历史

**在 R2018b 中推出**

## 描述

回放记录的 CAN FD 报文

CAN FD Replay 模块将在 `.mat` 文件中记录的报文回放到 CAN 网络，或作为总线信号回放到 Simulink®。有关 Simulink 总线对象的详细信息，请参阅合成接口 (Simulink)。您需要 CAN FD Configuration 模块才能回放到网络。

要在 Simulink 模型中回放在 MATLAB® 命令行窗口中记录的报文，请使用 `canMessageReplayBlockStruct` 将其转换为兼容格式并将结果保存到单独的文件。有关详细信息，请参阅记录和回放 CAN 报文。

**注意**

您需要 Vehicle Network Toolbox™ 和 Simulink 软件的许可证才能使用此模块。

### 回放时间

该模块使用报文的原始时间戳回放报文，以与仿真时间（对于常规仿真）或挂钟时间（对于回放到物理网络）同步。具体来说，当 Simulink 求解器前进一个时间步时，该模块会发送其时间戳属于该时间步的报文。因此，时间戳与仿真的时间范围保持一致非常重要。建议将仿真开始时间设置为 `0`，并更改报文时间戳，使初始时间戳为 `0`。

有关详细信息，请参阅**开始时间 (Simulink)**和示例记录并回放 CAN FD 报文。

### 其他支持的功能

- CAN FD Replay 模块支持使用 Simulink 加速模式。使用此功能，可以加快 Simulink 模型的执行速度。有关此功能的详细信息，请参阅加速 (Simulink)。
- CAN FD Replay 模块支持使用代码生成和 packNGo 函数将所需的源代码和依赖共享库打包。

### 代码生成

Vehicle Network Toolbox 提供的 Simulink 模块支持您生成代码，使包含这些模块的模型可在加速、快速加速、外部和已部署模式下运行。

**使用 Simulink Coder 进行代码生成**

您可以将 Vehicle Network Toolbox、Simulink Coder™ 和 Embedded Coder® 软件结合使用，以在您用来实现模型的主机端生成代码。有关代码生成的详细信息，请参阅生成代码编译 (Simulink Coder)。

**共享库依赖关系**

这些模块生成的代码可移植性有限。它使用预编译的共享库（如 DLL）来支持特定类型设备的 I/O。使用此模块，您可以使用 Simulink Coder 支持的 `packNGo` 函数来设置和管理模型的编译信息。`packNGo` (Simulink Coder) 函数允许您将模型代码和依赖共享库打包到一个 zip 文件中进行部署。您不需要在目标系统上安装 MATLAB，但需要 MATLAB 支持目标系统。

要设置 `packNGo`，请执行以下代码：

```
set_param(gcs,'PostCodeGenCommand','packNGo(buildInfo)');
```

在此示例中，`gcs` 是您要编译的当前模型。编译模型会创建一个与模型同名的 zip 文件。您可以将此 zip 文件移至另一台机器，并在该机器中编译 zip 文件中的源代码以创建可独立于 MATLAB 和 Simulink 运行的可执行文件。生成的代码使用 C 和 C++ 编译器进行编译。有关详细信息，请参阅代码编译自定义 (Simulink Coder)。

**注意**

在 Linux® 平台上，您需要将用于解压缩库的文件夹添加到环境变量 `LD_LIBRARY_PATH`。
