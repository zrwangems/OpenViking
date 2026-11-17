---
type: simulink-block
title: 'CAN FD Log'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN FD Communication'
documentation_page: 'canfdlog'
documentation_source_path: 'ug/canfdlog.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN FD Log

## 端口

### 输入

### **CAN Msg** — 要记录的 CAN FD 消息 `CAN_FD_MESSAGE_BUS`

当 **Log messages from** 参数设置为 `Input port` 时，**CAN Msg** 输入端口可用。从另一个模块提供输入，作为类型为 `CAN_FD_MESSAGE_BUS` 的 Simulink 信号总线。

**数据类型：** `CAN_FD_MESSAGE_BUS`

## 参数

**提示**

如果要从网络记录，需要使用 CAN FD Configuration 模块配置 CAN 通道。

### **File name** — 日志文件位置和名称 `untitled.mat`（默认）| 文件名

输入要将 CAN 消息记录到的 MAT 文件的路径和名称，或点击 **Browse** 浏览到文件位置。

该模块会在日志文件名后附加当前日期和时间，格式为 `YYYY-MMM-DD_hhmmss`。请指定唯一的名称，以区分重复记录的文件。

### **Variable name** — 日志文件中 CAN FD 消息的变量名 `ans`（默认）| 变量名

指定保存在 MAT 文件中用于存储 CAN 消息信息的变量名称。

### **Maximum number of messages to log** — 限制消息数量 `10000`（默认）| 数值

指定此模块可从所选设备或端口记录的最大消息数。指定的值必须为正整数。默认值为 `10000` 条消息。日志文件保存最近的、最多达到指定最大数量的消息。

### **Log messages from** — 消息来源 `CAN FD Bus`（默认）| `Input port`

选择模块记录的消息来源。要从 CAN FD 总线网络记录消息，请选择 `CAN FD Bus`，然后指定 **Device**。要从模型中的另一个模块记录消息，请选择 `Input port`，这会在模块上添加一个输入端口。

### **Device** — CAN 设备和通道列表选项

选择要从中记录消息的 CAN FD 网络上的设备。仅当 **Log messages from** 参数选择 `CAN FD Bus` 时，此字段才可用。

### **Sample time** — 仿真中的模块采样时间 `0.01`（默认）| 数值

指定仿真期间模块的采样时间。此值定义了 CAN FD Log 模块在仿真期间运行的频率。如果模块位于触发子系统内或要继承采样时间，可以将采样时间指定为 `–1`。也可以为采样时间指定 MATLAB 变量。默认值为 `0.01` 仿真秒。有关详细信息，请参阅 Timing in Hardware Interface Models。

## 所属库

Vehicle Network Toolbox / CAN FD Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块生成的代码可移植性有限，仅在主机上运行。请参阅 Code Generation。

## 版本历史

**在 R2018b 中引入**

## 描述

记录接收到的 CAN FD 消息

CAN FD Log 模块将来自 CAN 网络的 CAN FD 消息，或发送到模块输入端口的消息，记录到 `.mat` 文件中。您可以将保存的消息加载到 MATLAB® 中进行进一步分析，或加载到另一个 Simulink® 模型中。

将 CAN FD Log 模块配置为从 Simulink 输入端口记录。有关详细信息，请参阅 Log and Replay CAN Messages。

CAN FD Log 模块会在指定的文件名后附加当前日期和时间，为重复记录创建唯一的日志文件。

如果要在 MATLAB 命令窗口中使用通过 Simulink 模块记录的消息，请使用 `canFDMessage` 将消息转换为正确的格式。

**注意**

使用此模块需要同时拥有 Vehicle Network Toolbox™ 和 Simulink 软件的许可证。

**注意**

在同一个模型中使用相同 PEAK-System 设备通道时，不能有多个 CAN FD Log 模块。

### 其他支持的功能

- CAN FD Log 模块支持使用 Simulink 加速器模式。使用此功能，您可以加速 Simulink 模型的执行。有关此功能的详细信息，请参阅 Acceleration (Simulink)。
- CAN FD Log 模块支持结合使用代码生成和 `packNGo` 函数，以将所需的源代码和依赖的共享库打包在一起。

### 代码生成

Vehicle Network Toolbox
Simulink 模块允许您生成代码，使包含这些模块的模型能够在加速器、快速加速器、外部和部署模式下运行。

**使用 Simulink
Coder 进行代码生成**

您可以结合使用 Vehicle Network Toolbox、Simulink
Coder™ 和 Embedded Coder® 软件，在主机端生成可用于实现模型的代码。有关代码生成的详细信息，请参阅 Generated Code Compilation (Simulink Coder)。

**共享库依赖项**

该模块生成的代码可移植性有限。该模块使用预编译的共享库（如 DLL）来支持特定类型设备的 I/O。使用此模块，您可以使用 Simulink
Coder 支持的 `packNGo` 函数来设置和管理模型的构建信息。`packNGo` (Simulink Coder) 函数允许您将模型代码和依赖的共享库打包到一个 zip 文件中以便部署。目标系统上不需要安装 MATLAB，但目标系统需要受 MATLAB 支持。

要设置 `packNGo`：

```
set_param(gcs,'PostCodeGenCommand','packNGo(buildInfo)');
```

在此示例中，`gcs` 是您要构建的当前模型。构建模型会创建一个与模型名称相同的 zip 文件。您可以将此 zip 文件移动到另一台机器，并在那里构建 zip 文件中的源代码，以创建一个可独立于 MATLAB 和 Simulink 运行的可执行文件。生成的代码可使用 C 和 C++ 编译器进行编译。有关详细信息，请参阅 Code Compilation Customization (Simulink Coder)。

**注意**

在 Linux® 平台上，您需要将解压库所在的文件夹添加到环境变量 `LD_LIBRARY_PATH` 中。
