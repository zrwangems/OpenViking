---
type: simulink-block
title: 'UDP Send'
family: 'instrument-control-toolbox'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: 'Instrument Control Toolbox'
documentation_page: 'udpsend'
documentation_source_path: 'udpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Send

## 端口

### 输入

### **Data** — 要发送的数据值 向量 | 矩阵 | 数组

要从模块发送到远程主机的数据值，指定为向量、矩阵或数组。发送数据之前，请设置此模块的参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

## 参数

### **远程地址** — 远程主机名或地址 远程主机名或 IP 地址

要向其发送数据的远程机器或服务器的 IP 地址或名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `Host` |
| **类型：** character vector, string |

### **远程端口** — 远程主机端口 `9090`（默认） | 远程主机端口

要连接到的远程机器或服务器上的远程端口，指定为 1 到 65,535 的数字。

您也可以将此参数的值指定为现有工作区变量。

#### 编程用法

|  |
| --- |
| **模块参数：** `Port` |
| **类型：** character vector, string |
| **值：** 1 到 65,535 |
| **默认值：** `'80'` |

### **本地地址** — 本地主机名或 IP 地址 0.0.0.0（默认） | 本地主机名或 IP 地址

本地主机的主机名、点分十进制 IP 地址或 Web 服务器。此模块支持 IPV4 和 IPV6 地址格式。

#### 编程用法

|  |
| --- |
| **模块参数：** `LocalAddress` |
| **类型：** character vector, string |

### **本地端口** — 用于绑定的本地主机端口 -1（默认） | 本地主机端口

用于 UDP 绑定的本地主机端口，指定为 1 到 65,535 的数字。如果未指定值，则会自动分配一个值。

您也可以将此参数的值指定为现有工作区变量。

#### 编程用法

|  |
| --- |
| **模块参数：** `LocalPort` |
| **类型：** character vector, string |

### **启用本地端口共享** — 允许其他 UDP 套接字绑定到同一本地端口 `off`（默认） | `on`

启用本地端口共享的参数。如果您希望允许其他 UDP 套接字绑定到同一本地端口，请选择此参数。

UDP 端口可由其他应用程序共享，以允许多个应用程序侦听该端口上的 UDP 数据报。您可以将此模块绑定到特定的 **本地端口**，并在另一个应用程序中将 UDP 套接字绑定到同一本地端口号，以便两者都能接收 UDP 广播数据。

#### 编程用法

|  |
| --- |
| **模块参数：** `EnablePortSharing` |
| **类型：** character vector, string |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

### **验证地址和端口连接** — 远程机器连接验证按钮

单击此按钮可检查到指定远程地址和端口的连接是否有效。

### **UDP 数据包大小** — 数据报数据包中写入的最大字节数 512（默认） | numeric

数据报数据包中要写入的最大数据字节数。如有必要，您可以增大或减小数据包大小。

您也可以将此参数的值指定为现有工作区变量。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputDatagramPacketSize` |
| **类型：** character vector, string |
| **值：** 1 到 65,535 |
| **默认值：** `'512'` |

### **字节顺序** — 字节的排列顺序 `big-endian`（默认） | `little-endian`

将字节排列为更大数值的顺序。如果字节顺序为 `little-endian`，远程机器将第一个字节存储到第一个内存地址中。如果字节顺序为 `big-endian`，远程机器将最后一个字节存储到第一个内存地址中。

在发送数据之前，配置字节顺序以匹配远程机器的相应值。有关仪器存储字节顺序的信息，请参阅您的仪器文档。

#### 编程用法

|  |
| --- |
| **模块参数：** `ByteOrder` |
| **类型：** character vector, string |
| **值：** `'little-endian'` | `'big-endian'` |
| **默认值：** `'big-endian'` |

### **启用阻塞模式** — 仿真在发送数据时等待 `on`（默认） | `off`

此参数使仿真在模块发送数据时等待。如果您不希望写操作导致仿真等待，请取消选择此参数。

如果启用阻塞模式，仿真会等待数据发送完成。如果未启用阻塞模式，仿真会连续运行。

有关详细信息，请参阅接收和发送模块中的启用阻塞模式。

#### 编程用法

|  |
| --- |
| **模块参数：** `EnableBlockingMode` |
| **类型：** character vector, string |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

## 所属库

Instrument Control Toolbox

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2007b 中引入**

## 描述

通过 UDP 网络将数据发送到指定的远程机器

UDP Send 模块使用 UDP 协议配置并打开到指定远程机器的接口。配置和初始化在模型执行开始时进行一次。该模块在模型运行期间以阻塞模式或非阻塞模式发送数据。您可以同时使用多个 UDP Send 模块将数据发送到特定端口。

UDP Send 模块有一个输入端口，可接受一维向量和矩阵数据。此模块没有输出端口。该模块从输入端口处的信号继承数据类型。有效的数据类型为 `single`、`double`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64` 和 `uint64`。

**注意**

您必须同时拥有 Instrument Control Toolbox™ 和 Simulink® 许可证才能使用此模块。

### 其他支持的功能

- UDP Send 模块支持使用 Simulink 加速模式和快速加速模式。您可以使用这些模式加快 Simulink 模型的执行速度。有关这些仿真模式的详细信息，请参阅加速 (Simulink)。
- UDP Send 模块支持使用模型引用。此功能允许您的模型将其他 Simulink 模型作为模块化组件包含在内。

有关这些功能的详细信息，请参阅 Simulink 文档。
