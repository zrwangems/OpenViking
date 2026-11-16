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
chinese_source: official
---

# CAN Receive

## 端口

### 输出

### **CAN Msg** — 接收的 CAN 报文 `CAN_MESSAGE` | 总线

`CAN Msg` 输出端口包含一个或多个在该特定时间步接收的打包的 CAN 报文，以信号总线或 `CAN_MESSAGE` 形式输出。输出包括该时间步的一条或所有报文，具体取决于**每个时间步收到的报文数**的设置。

**数据类型:** `CAN_MESSAGE` | `bus`

### **f()** — 函数调用事件输出 函数调用事件

`f()` 输出端口是 Function-Call 子系统的触发器。如果模块接收到新报文，则会从这个端口触发 Function-Call。然后，您可以连接到 Function-Call Subsystem (Simulink) 以解包并处理报文。

**数据类型:** `function-call event`

## 参数

**提示**

在配置 CAN Receive block 参数之前，请配置 CAN Configuration 模块。

### **设备** — CAN 设备和通道 列表选项

从列表中选择要从其接收 CAN 报文的 CAN 设备和通道。此字段列出系统上安装的所有设备。它显示供应商名称、设备名称和通道 ID。默认值为系统上第一个可用的设备。

#### 编程用法

|  |
| --- |
| **模块参数：**`Device` |
| **类型：**字符向量、字符串 |

### **标准 ID 过滤器** — 基于标准 ID 限制或允许报文 `Allow all` (默认) | `Allow only` | `Block all`

为标准 ID 选择过滤器。选项包括：

- `Allow all`（默认值）：允许所有标准 ID 通过过滤器。
- `Allow only`:仅允许在文本字段中指定的 ID 或 ID 范围，指定为单个 ID 或 ID 数组。您还可以指定不连续的 ID 或以逗号分隔的数组。例如，要允许 ID 400 到 500 以及 600 到 650，请输入 `[[400:500],[600:650]]`。标准 ID 必须是 0 到 2047 之间的正整数。您还可以使用 `hex2dec` 函数指定十六进制值。
- `Block all`:阻止所有标准 ID 通过过滤器。

#### 编程用法

|  |
| --- |
| **模块参数：**`StdIDsCombo` |
| **类型：**字符向量、字符串 |
| **值：**`'Allow all'` | `'Allow only'` | `'Block all'` |
| **默认值：**`'Allow all'` |

如果使用 `'Allow only'`，请使用以下内容设置过滤器值：

|  |
| --- |
| **模块参数：**`StandardIDs` |
| **类型：**字符向量、字符串 |
| **值：**整数标量或行向量 |

### **扩展 ID 过滤器** — 基于扩展 ID 限制或允许报文 `Allow all` (默认) | `Allow only` | `Block all`

选择用于过滤此模块的扩展 ID 的过滤器。选项包括：

- `Allow all`（默认值）：允许所有扩展 ID 通过过滤器。
- `Allow only`:仅允许在文本字段中指定的 ID。仅允许在文本字段中指定的 ID 或 ID 范围，指定为单个 ID 或 ID 数组。您还可以指定不连续的 ID 或以逗号分隔的数组。例如，要接受 3000 到 3500 以及 3600 到 3620 的 ID，请输入 `[[3000:3500],[3600:3620]]`。扩展 ID 必须是从 0 到 536870911 的正整数。您还可以使用 `hex2dec` 函数指定十六进制值。
- `Block all`:阻止所有扩展 ID 通过过滤器。

#### 编程用法

|  |
| --- |
| **模块参数：**`ExtIDsCombo` |
| **类型：**字符向量、字符串 |
| **值：**`'Allow all'` | `'Allow only'` | `'Block all'` |
| **默认值：**`'Allow all'` |

|  |
| --- |
| **模块参数：**`ExtendedIDs` |
| **类型：**字符向量、字符串 |
| **值：**整数标量或行向量 |

### **采样时间** — 模块执行速率 `0.01` (默认)

指定仿真期间模块的采样时间。这是仿真期间模块的执行速率。默认值为 0.01 仿真秒。有关详细信息，请参阅硬件接口模型中的计时。

#### 编程用法

|  |
| --- |
| **模块参数：**`SampleTime` |
| **类型：**字符向量、字符串 |
| **值：**双精度值 |
| **默认值：**`'0.01'` |

### **每个时间步收到的报文数** — 接收一条或所有报文 `all` (默认) | `1`

选择模块在每个指定的时间步接收的报文数。有效选项是：

- `all`（默认值）：CAN Receive 模块在特定时间步期间将 FIFO 缓冲区中的所有可用报文传递给模型。该模块为每个传递的报文生成一个函数调用。输出端口一次包含一条 CAN 报文。
- `1`:CAN Receive 模块在每个时间步将一条报文从 FIFO 缓冲区传递给模型。

如果模块在下一个时间步之前没有收到任何报文，它将输出最后收到的报文。

#### 编程用法

|  |
| --- |
| **模块参数：**`MsgsPerTimestep` |
| **类型：**字符向量、字符串 |
| **值：**`'all'` | `'1'` |
| **默认值：**`'all'` |

### **作为总线输出** — 输出 Simulink 总线信号 `off` (默认) | `on`

输出原生 Simulink 总线信号。有关 Simulink 总线对象的详细信息，请参阅合成接口 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：**`BusOutput` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

## 所属库

Vehicle Network Toolbox / CAN Communication

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

此模块生成的代码可移植性有限，只能在主机上运行。请参阅代码生成。

## 版本历史

**在 R2009a 中推出**

## 描述

从指定的 CAN 设备接收 CAN 报文

CAN Receive 模块从 CAN 网络接收报文并将其传递给 Simulink® 模型。它根据模块参数在每个时间步输出一条报文或所有报文。

**注意**

您需要 Vehicle Network Toolbox™ 和 Simulink 软件的许可证才能使用此模块。

CAN Receive 模块将 CAN 报文存储在一个先进先出 (FIFO) 缓冲区中。该 FIFO 缓冲区在每个时间步按照排队顺序将报文传递给模型。

**注意**

在一个模型中，一个 PEAK-System 设备通道只能连接一个 CAN Receive 模块。

### 其他支持的功能

CAN Receive 模块支持使用 Simulink 加速模式。使用此功能，可以加快 Simulink 模型的执行速度。有关此功能的详细信息，请参阅加速 (Simulink)。

CAN Receive 模块支持使用代码生成和 packNGo 函数将所需的源代码和依赖共享库打包。

### 代码生成

Vehicle Network Toolbox 提供的 Simulink 模块支持您生成代码，使包含这些模块的模型可在加速、快速加速、外部和已部署模式下运行。

**使用 Simulink Coder 进行代码生成**

您可以将 Vehicle Network Toolbox、Simulink Coder™ 和 Embedded Coder® 软件结合使用，以在您用来实现模型的主机端生成代码。有关代码生成的详细信息，请参阅生成代码编译 (Simulink Coder)。

**共享库依赖关系**

这些模块生成的代码可移植性有限。它使用预编译的共享库（如 DLL）来支持特定类型设备的 I/O。使用此模块，您可以使用 Simulink Coder 支持的 `packNGo` 函数来设置和管理模型的编译信息。`packNGo` (Simulink Coder) 函数允许您将模型代码和依赖共享库打包到一个 zip 文件中进行部署。您不需要在目标系统上安装 MATLAB®，但需要 MATLAB 支持目标系统。

要设置 `packNGo`，请执行以下代码：

```
set_param(gcs,'PostCodeGenCommand','packNGo(buildInfo)');
```

在此示例中，`gcs` 是您要编译的当前模型。编译模型会创建一个与模型同名的 zip 文件。您可以将此 zip 文件移至另一台机器，并在该机器中编译 zip 文件中的源代码以创建可独立于 MATLAB 和 Simulink 运行的可执行文件。生成的代码使用 C 和 C++ 编译器进行编译。有关详细信息，请参阅代码编译自定义 (Simulink Coder)。

**注意**

在 Linux® 平台上，您需要将用于解压缩库的文件夹添加到环境变量 `LD_LIBRARY_PATH`。
