---
type: simulink-block
title: 'TCP/IP Send'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'tcpipsend'
documentation_source_path: 'tcpipsend.html'
language: zh-CN
chinese_source: worker-translation
---

# TCP/IP Send

## 端口

### 输入

### **Data** — 要发送的数据值 向量 | 矩阵 | 数组

从模块发送到远程主机的数据值，指定为向量、矩阵或数组。此数据的数组大小在仿真期间不得更改。在发送数据之前设置此模块的参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

## 参数

### **Remote address** — 远程主机名或地址 远程主机名或 IP 地址

要向其发送数据的 TCP/IP 服务器的 IP 地址或名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`Host` |
| **类型**：character vector, string |

### **Port** — 远程主机端口 `80`（默认）| 远程主机端口

要连接的 TCP/IP 服务器上的远程端口，指定为 1 到 65535 之间的数字。

#### 编程使用

|  |
| --- |
| **模块参数**：`Port` |
| **类型**：character vector, string |
| **值**：1 to 65,535 |
| **默认值**：`'80'` |

### **Verify address and port connectivity** — 远程机器连接验证按钮

点击此按钮以检查到指定远程地址和端口的连接是否有效。

### **Byte order** — 字节的顺序 `big-endian`（默认）| `little-endian`

字节排列为更大数值的顺序。如果字节顺序为 `little-endian`，则远程机器将第一个字节存储在第一内存地址中。如果字节顺序为 `big-endian`，则远程机器将最后一个字节存储在第一内存地址中。

在发送数据之前，将字节顺序配置为与远程机器相应的值匹配。有关其存储字节顺序的信息，请参阅您的仪器文档。

#### 编程使用

|  |
| --- |
| **模块参数**：`ByteOrder` |
| **类型**：character vector, string |
| **值**：`'little-endian'` | `'big-endian'` |
| **默认值**：`'big-endian'` |

### **Enable blocking mode** — 仿真在发送数据时等待 `on`（默认）| `off`

此参数使仿真在模块发送数据时等待。如果您不希望写入操作导致仿真等待，请清除该复选框。

如果启用阻塞模式，仿真将等待数据发送完成。如果未启用阻塞模式，仿真将持续运行。

有关详细信息，请参阅 Enable Blocking Mode in Receive and Send Blocks。

#### 编程使用

|  |
| --- |
| **模块参数**：`EnableBlockingMode` |
| **类型**：character vector, string |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Timeout** — 完成操作所允许的时间 10（默认）| 正标量

模型在每个仿真时间步期间等待数据发送的时间量，以秒为单位。此值相对于真实世界或“挂钟”时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`Timeout` |
| **类型**：character vector, string |
| **值**：positive scalar |
| **默认值**：`'10'` |

#### 依赖关系

要启用此参数，请将 **Enable blocking mode** 设置为 `on`。

### **Transfer Delay** — 启用延迟确认 `on`（默认）| `off`

如果启用此参数，模块将收集未完成数据的小段，并在从服务器收到确认（ACK）时将它们作为单个数据包发送。如果您希望立即将数据发送到网络，请清除此复选框。

如果网络较慢，您可以通过启用传输延迟来提高其性能。但是，在快速网络上，确认会很快到达，启用或禁用传输延迟之间的差异可以忽略不计。

#### 编程使用

|  |
| --- |
| **模块参数**：`TransferDelay` |
| **类型**：character vector, string |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

## 所属库

Instrument Control Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块仅为主机平台（Windows®、macOS、Linux®）生成平台特定的代码。在**模型设置** > **硬件实现**中设置 **Device vendor** 和 **Device type**。您还必须在 **Device details** 下选择 **Support long long**。

## 版本历史

**在 R2007b 中引入**

## 描述

通过 TCP/IP 网络将数据发送到指定的远程机器

TCP/IP Send 模块使用 TCP/IP 协议配置并打开到指定远程地址的接口。配置和初始化在模型执行开始时仅发生一次。该模块在模型运行期间以阻塞模式或非阻塞模式发送数据。使用 TCP/IP Send 模块通过 TCP/IP 网络写入流数据。此模块仅作为 TCP/IP 客户端工作，不能用作 TCP/IP 服务器。

TCP/IP Send 模块有一个输入端口，可接受一维向量和矩阵数据。此数据的数组大小在仿真期间不得更改。此模块没有输出端口。该模块从输入端口的信号继承数据类型。有效数据类型为 `single`、`double`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64` 和 `uint64`。

### 其他支持的功能

- TCP/IP Send 模块支持使用 Simulink® Accelerator 模式和 Rapid Accelerator。此功能可加速 Simulink 模型的执行。
- TCP/IP Send 模块支持使用模型引用。此功能允许您的模型将其他 Simulink 模型作为模块化组件包含在内。
- TCP/IP Send 模块支持 C/C++ 代码生成。此功能允许您使用 Simulink Coder™ 生成 C 和 C++ 代码。

有关这些功能的更多信息，请参阅 Simulink 文档。
