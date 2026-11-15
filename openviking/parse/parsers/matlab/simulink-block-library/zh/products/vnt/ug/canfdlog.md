---
type: simulink-block
title: 'CAN FD Log'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN and CAN FD Communication / Communication in Simulink / CAN FD'
documentation_page: 'canfdlog'
documentation_source_path: 'ug/canfdlog.html'
language: zh-CN
chinese_source: official
---

# CAN FD Log

## 端口

### 输入

### **CAN Msg** — 要记录的 CAN FD 报文 `CAN_FD_MESSAGE_BUS`

当**记录来自以下位置的报文**参数设置为 `Input port` 时，**CAN Msg** 输入端口可用。从另一个模块以类型为 `CAN_FD_MESSAGE_BUS` 的 Simulink 信号总线形式提供输入。

**数据类型:** `CAN_FD_MESSAGE_BUS`

## 参数

**提示**

如果记录来自网络的报文，则需要使用 CAN FD Configuration 模块配置 CAN 通道。

### **文件名** — 日志文件位置和名称 `untitled.mat` (默认) | 文件名

输入要将 CAN 报文记录到的 MAT 文件的路径和名称，或点击**浏览**以浏览到文件位置。

模型会在日志文件名后追加 `YYYY-MMM-DD_hhmmss` 格式的当前日期和时间。指定唯一名称以将重复记录的文件区分开来。

### **变量名称** — 日志文件中 CAN FD 报文的变量名称 `ans` (默认) | 变量名称

指定 MAT 文件中保存 CAN 报文信息的变量的名称。

### **要记录的最大报文数** — 限制报文数量 `10000` (默认) | 数值

指定此模块可以从所选设备或端口记录的最大报文数。指定的值必须是正整数。默认值为 `10000` 个报文。日志文件将滚动保存最新的报文，条数不超过指定的最大数量。

### **记录来自以下位置的报文** — 报文来源 `CAN FD Bus` (默认) | `Input port`

选择模块记录的报文的来源。要记录来自 CAN FD 总线网络的报文，请选择 `CAN FD Bus`，然后指定一个**设备**。要记录来自模型中另一个模块的报文，请选择 `Input port`（为模块添加输入端口）。

### **设备** — CAN 设备和通道 列表选项

在要从中记录报文的 CAN FD 网络上选择设备。仅当您为**记录来自以下位置的报文**参数选择了 `CAN FD Bus` 时，此字段才可用。

### **采样时间** — 仿真中的模块采样时间 `0.01` (默认) | 数值

指定仿真期间模块的采样时间。该值定义在仿真期间 CAN FD Log 模块运行的频率。如果模块位于触发子系统内或要继承采样时间，则可以将 `–1` 指定为采样时间。您还可以为采样时间指定一个 MATLAB 变量。默认值为 `0.01` 仿真秒。有关详细信息，请参阅硬件接口模型中的计时。

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

记录收到的 CAN FD 报文

CAN FD Log 模块将来自 CAN 网络的 CAN FD 报文或发送到模块输入端口的报文记录到 `.mat` 文件。您可以将保存的报文加载到 MATLAB® 中以进行进一步分析，或者加载到另一个 Simulink® 模型中。

配置 CAN FD Log 模块以从 Simulink 输入端口进行记录。有关详细信息，请参阅记录和回放 CAN 报文。

CAN FD Log 模块会在指定的文件名后追加当前日期和时间，从而为重复创建唯一的日志文件。

如果要在 MATLAB 命令行窗口中使用通过 Simulink 模块记录的报文，请使用 `canFDMessage` 将报文转换为正确的格式。

**注意**

您需要 Vehicle Network Toolbox™ 和 Simulink 软件的许可证才能使用此模块。

**注意**

在一个模型中，一个 PEAK-System 设备通道只能连接一个 CAN FD Log 模块。

### 其他支持的功能

- CAN FD Log 模块支持使用 Simulink 加速模式。使用此功能，可以加快 Simulink 模型的执行速度。有关此功能的详细信息，请参阅加速 (Simulink)。
- CAN FD Log 模块支持使用代码生成和 packNGo 函数将所需的源代码和依赖共享库打包。

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
