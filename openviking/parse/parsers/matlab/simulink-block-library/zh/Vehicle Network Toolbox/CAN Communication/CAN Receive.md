---
type: simulink-block
title: 'CAN Receive'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN Communication'
documentation_page: 'canreceive'
documentation_source_path: 'ug/canreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Receive

## 端口

### 输出

### **CAN Msg** — 接收到的 CAN 报文 `CAN_MESSAGE` | bus

`CAN Msg` 输出端口包含在该特定时间步接收到的一条或多条打包 CAN 报文，以信号总线或 `CAN_MESSAGE` 形式输出。输出包含该时间步的一条或所有报文，具体取决于 **Number of messages received at each timestep** 的设置。

**数据类型：** `CAN_MESSAGE` | `bus`

### **f()** — 函数调用事件输出 function-call event

`f()` 输出端口是到 Function-Call 子系统的触发。如果模块接收到新报文，它会从此端口触发 Function-Call。然后您可以连接到 Function-Call Subsystem (Simulink) 来解包并处理报文。

**数据类型：** `function-call event`

## 参数

**提示**

在配置 CAN Receive 模块参数之前，请先配置 CAN Configuration 模块。

### **Device** — CAN 设备和通道列表选项

从列表中选择您要从中接收 CAN 报文的 CAN 设备及设备上的通道。此字段列出系统上安装的所有设备。它显示供应商名称、设备名称和通道 ID。默认值为系统上第一个可用的设备。

#### 编程使用

|  |
| --- |
| **模块参数**：`Device` |
| **类型**：character vector, string |

### **Standard IDs Filter** — 基于标准 ID 限制或允许报文 `Allow all` (default) | `Allow only` | `Block all`

选择标准 ID 的过滤器。选项包括：

- `Allow all`（默认）：允许所有标准 ID 通过过滤器。
- `Allow only`：仅允许文本字段中指定的 ID 或 ID 范围，指定为单个 ID 或 ID 数组。您还可以指定以逗号分隔的不连续 ID 或数组。例如，要允许 ID 400 到 500 以及 600 到 650，请输入 `[[400:500],[600:650]]`。标准 ID 必须是 0 到 2047 的正整数。您还可以使用 `hex2dec` 函数指定十六进制值。
- `Block all`：阻止所有标准 ID 通过过滤器。

#### 编程使用

|  |
| --- |
| **模块参数**：`StdIDsCombo` |
| **类型**：character vector, string |
| **值**：`'Allow all'` | `'Allow only'` | `'Block all'` |
| **默认值**：`'Allow all'` |

如果使用 `'Allow only'`，请使用以下内容设置过滤器值：

|  |
| --- |
| **模块参数**：`StandardIDs` |
| **类型**：character vector, string |
| **值**：integer scalar or row vector |

### **Extended IDs Filter** — 基于扩展 ID 限制或允许报文 `Allow all` (default) | `Allow only` | `Block all`

选择此模块上扩展 ID 的过滤器。选项包括：

- `Allow all`（默认）：允许所有扩展 ID 通过过滤器。
- `Allow only`：仅允许文本字段中指定的那些 ID。仅允许文本字段中指定的 ID 或 ID 范围，指定为单个 ID 或 ID 数组。您还可以指定以逗号分隔的不连续 ID 或数组。例如，要接受 ID 3000 到 3500 以及 3600 到 3620，请输入 `[[3000:3500],[3600:3620]]`。扩展 ID 必须是 0 到 536870911 的正整数。您还可以使用 `hex2dec` 函数指定十六进制值。
- `Block all`：阻止所有扩展 ID 通过过滤器。

#### 编程使用

|  |
| --- |
| **模块参数**：`ExtIDsCombo` |
| **类型**：character vector, string |
| **值**：`'Allow all'` | `'Allow only'` | `'Block all'` |
| **默认值**：`'Allow all'` |

|  |
| --- |
| **模块参数**：`ExtendedIDs` |
| **类型**：character vector, string |
| **值**：integer scalar or row vector |

### **Sample time** — 模块执行速率 `0.01` (default)

指定仿真期间模块的采样时间。这是仿真期间模块执行的速率。默认值为 0.01 仿真秒。有关详细信息，请参阅 Timing in Hardware Interface Models。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector, string |
| **值**：double |
| **默认值**：`'0.01'` |

### **Number of messages received at each timestep** — 接收一条或所有报文 `all` (default) | `1`

选择模块在每个指定时间步接收多少条报文。有效选项包括：

- `all`（默认）：CAN Receive 模块在特定时间步将所有 FIFO 缓冲区中可用的报文传递给模型。模块为每条传递的报文生成一次函数调用。输出端口始终一次包含一条 CAN 报文。
- `1`：CAN Receive 模块每个时间步从 FIFO 缓冲区向模型传递一条报文。

如果模块在下一个时间步之前未接收到任何报文，则输出最后接收到的报文。

#### 编程使用

|  |
| --- |
| **模块参数**：`MsgsPerTimestep` |
| **类型**：character vector, string |
| **值**：`'all'` | `'1'` |
| **默认值**：`'all'` |

### **Output as bus** — 输出 Simulink 总线信号 `off` (default) | `on`

输出原生 Simulink 总线信号。有关 Simulink 总线对象的详细信息，请参阅 Composite Interfaces (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`BusOutput` |
| **类型**：character vector, string |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

## 所属库

Vehicle Network Toolbox / CAN Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块生成的代码可移植性有限，仅在主机上运行。请参阅 Code Generation。

## 版本历史

**在 R2009a 中引入**

## 描述

从指定的 CAN 设备接收 CAN 报文

CAN Receive 模块从 CAN 网络接收报文并将其传递给 Simulink® 模型。它根据模块参数在每个时间步输出一条报文或所有报文。

**注意**

使用此模块需要同时拥有 Vehicle Network Toolbox™ 和 Simulink 软件的许可证。

CAN Receive 模块将 CAN 报文存储在先入先出（FIFO）缓冲区中。FIFO 缓冲区在每个时间步按排队顺序将报文传递给您的模型。

**注意**

在同一个模型中使用同一 PEAK-System 设备通道时，不能有多个 CAN Receive 模块。

### 其他支持的功能

CAN Receive 模块支持使用 Simulink 加速模式。使用此功能，您可以加速 Simulink 模型的执行。有关此功能的详细信息，请参阅 Acceleration (Simulink)。

CAN Receive 模块支持结合 `packNGo` 函数使用代码生成，以将所需的源代码和依赖的共享库分组。

### 代码生成

Vehicle Network Toolbox Simulink 模块允许您生成代码，使包含这些模块的模型能够在加速、快速加速、外部和部署模式下运行。

**使用 Simulink Coder 进行代码生成**

您可以结合使用 Vehicle Network Toolbox、Simulink Coder™ 和 Embedded Coder® 软件在主机端生成代码，用于实现您的模型。有关代码生成的详细信息，请参阅 Generated Code Compilation (Simulink Coder)。

**共享库依赖项**

此模块生成的代码可移植性有限。此模块使用预编译的共享库（如 DLL）来支持特定类型设备的 I/O。使用此模块，您可以利用 Simulink Coder 支持的 `packNGo` 函数来设置和管理模型的构建信息。`packNGo` (Simulink Coder) 函数允许您将模型代码和依赖的共享库打包到 zip 文件中进行部署。目标系统上不需要安装 MATLAB®，但目标系统需要受 MATLAB 支持。

要设置 `packNGo`：

```
set_param(gcs,'PostCodeGenCommand','packNGo(buildInfo)');
```

在此示例中，`gcs` 是您要构建的当前模型。构建模型会创建一个与模型名称相同的 zip 文件。您可以将此 zip 文件移动到另一台机器上，并在那里构建 zip 文件中的源代码以创建可独立于 MATLAB 和 Simulink 运行的可执行文件。生成的代码可使用 C 和 C++ 编译器编译。有关详细信息，请参阅 Code Compilation Customization (Simulink Coder)。

**注意**

在 Linux® 平台上，您需要将解压库的文件夹添加到环境变量 `LD_LIBRARY_PATH` 中。
