---
type: simulink-block
title: 'CAN Replay'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN Communication'
documentation_page: 'canreplay'
documentation_source_path: 'ug/canreplay.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Replay

## 端口

### 输出

### **CAN Msg** — 重放的 CAN 报文 `CAN_MESSAGE` | `CAN_MESSAGE_BUS`

此输出端口包含在该特定时间步记录的打包 CAN 报文，
以 `CAN_MESSAGE` 或类型为
`CAN_MESSAGE_BUS` 的信号总线形式输出。

**数据类型：** `CAN_MESSAGE` | `CAN_MESSAGE_BUS`

### **f()** — 函数调用事件输出 函数调用事件

当模块接收到新报文时，此端口向函数调用子系统提供触发信号。您可以将其连接到函数调用子系统 (Simulink)，以解包并处理该报文。

**数据类型：** `function-call event`

## 参数

**提示**

在配置 CAN Receive 模块参数之前，请先配置您的 CAN Configuration 模块。

### **File name** — 包含报文的 MAT 文件的路径和名称 `untitled.mat`（默认）| 文件名

指定包含可重放的已记录 CAN 报文的文件的名称和路径。您可以点击 **Browse** 浏览到文件位置并选择该文件。

### **Variable name** — MAT 文件中保存报文的变量 `ans`（默认）| 变量

指定保存在 MAT 文件中包含 CAN 报文信息的变量。

### **Number of times to replay messages** — 重复次数 `Inf`（默认）| 整数

指定您希望在模型中重放报文的次数。您可以指定任意正整数，包括 `Inf`。指定 `Inf` 将连续重放报文，直到仿真停止。

### **Replay messages to** — 指定输出位置 CAN Bus（默认）| `Output port`

指定模型是将报文重放到 CAN 网络还是输出端口。当重放到 CAN 网络时，您还必须选择一个 **Device**。

### **Device** — CAN 设备和通道 设备列表选项

选择 CAN 网络上要重放报文的目标设备。如果您为 **Replay message to** 参数选择了 `Output port`，则此字段不可用。

### **Sample time** — 模块执行速率 `0.01`（默认）| 数值

指定仿真期间模块的采样时间。此值定义了 CAN Replay 模块在仿真期间运行的频率。如果模块位于触发子系统内或要继承采样时间，可以将采样时间指定为 `–1`。您还可以为采样时间指定 MATLAB 变量。默认值为 `0.01` 仿真秒。有关详细信息，请参阅 Timing in Hardware Interface Models。

### **Output as bus** — 启用信号总线输出 off（默认）| on

选择此选项可使模块将 CAN 报文作为 Simulink 总线信号输出。有关 Simulink 总线对象的详细信息，请参阅 Composite Interfaces (Simulink)。

## 所属库

Vehicle Network Toolbox / CAN Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块生成的代码可移植性有限，仅在主机上运行。请参阅 Code Generation。

## 版本历史

**在 R2011b 中引入**

## 描述

重放已记录的 CAN 报文

CAN Replay 模块将 `.mat` 文件中已记录的报文重放到 CAN 网络或 Simulink®。您需要一个 CAN Configuration 模块才能重放到网络。

要将 MATLAB® 命令窗口中记录的报文在 Simulink 模型中重放，请使用 `canMessageReplayBlockStruct` 将其转换为兼容格式，并将结果保存到单独的文件中。有关详细信息，请参阅 Log and Replay CAN Messages。

**注意**

使用此模块需要同时拥有 Vehicle Network Toolbox™ 和 Simulink 软件的许可证。

### Replay Timing

该模块使用消息的原始时间戳重放消息，以与仿真时间（用于常规仿真）或挂钟时间（用于重放到物理网络）同步。具体而言，当 Simulink 求解器推进一个时间步时，该模块会发送时间戳属于该时间步的消息。因此，时间戳与仿真的时间范围保持一致非常重要。建议将仿真开始时间设置为 `0`，并平移消息时间戳，使初始时间戳为 `0`。

有关详细信息，请参阅 **Start time (Simulink)** 以及示例 Log and Replay CAN Messages。

### Other Supported Features

CAN Replay 模块支持使用 Simulink 加速模式和快速加速模式。使用此功能，您可以加快 Simulink 模型的执行速度。有关此功能的详细信息，请参阅 Acceleration (Simulink)。

CAN Replay 模块支持结合使用代码生成和 packNGo 函数，以将所需源代码和依赖共享库打包。有关详细信息，请参阅 Code Generation。

### 代码生成

Vehicle Network Toolbox
Simulink 模块允许您生成代码，使包含这些模块的模型能够在加速、快速加速、外部和部署模式下运行。

**Code Generation with Simulink
Coder**

您可以结合使用 Vehicle Network Toolbox、Simulink
Coder™ 和 Embedded Coder® 软件在主机端生成代码，然后使用这些代码来实现您的模型。有关代码生成的详细信息，请参阅 Generated Code Compilation (Simulink Coder)。

**Shared Library Dependencies**

该模块生成的代码可移植性有限。该模块使用预编译共享库（例如 DLL）来支持特定类型设备的 I/O。使用此模块，您可以使用 Simulink
Coder 支持的 `packNGo` 函数来设置和管理模型的构建信息。`packNGo` (Simulink Coder) 函数允许您将模型代码和依赖共享库打包到一个 zip 文件中以便部署。目标系统上不需要安装 MATLAB，但目标系统需要受 MATLAB 支持。

要设置 `packNGo`：

```
set_param(gcs,'PostCodeGenCommand','packNGo(buildInfo)');
```

在此示例中，`gcs` 是您要构建的当前模型。构建模型会创建一个与模型名称同名的 zip 文件。您可以将此 zip 文件移动到另一台机器，并在那里构建 zip 文件中的源代码，以创建可独立于 MATLAB 和 Simulink 运行的可执行文件。生成的代码可使用 C 和 C++ 编译器进行编译。有关详细信息，请参阅 Code Compilation Customization (Simulink Coder)。

**Note**

在 Linux® 平台上，您需要将解压库所在的文件夹添加到环境变量
`LD_LIBRARY_PATH` 中。
