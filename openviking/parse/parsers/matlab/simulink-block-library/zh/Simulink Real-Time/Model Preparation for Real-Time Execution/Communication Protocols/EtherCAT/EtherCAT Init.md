---
type: simulink-block
title: 'EtherCAT Init'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / EtherCAT'
documentation_page: 'ethercatinit'
documentation_source_path: 'io_ref/ethercatinit.html'
language: zh-CN
chinese_source: official
---

# EtherCAT Init

## 端口

### 输出

### **Status** — 关于 EtherCAT 网络的状态信息 向量

`Status` 向量包含以下值：`ErrVal`、`MdeviceState`、`DCErrVal`、`MdeviceToNetworkClkDiff`、`DCInitState` 和 `NetworkToSubDeviceClkDiff`。

- `ErrVal` - 错误状态：

  - 无错误：`0`
  - 错误：值小于 `0`。

  由于 `ErrVal` 显示的是最新错误状态，错误的传播可能掩盖原始错误。要查找原始错误，请添加一个 EtherCAT Get Notifications 模块，并使用 `slrealtime.EtherCAT.filterNotifications` 命令打印 EtherCAT 堆栈传输的状态代码。
- `MdeviceState` - EtherCAT 网络的运行状态。

  | 状态 | 值 | 描述 |
  | --- | --- | --- |
  | `INIT` | 1 | 初始化 - 系统查找终端设备并初始化通信控制器。 |
  | `PREOP` | 2 | 预操作阶段 - 系统通过通信控制器交换系统专用的初始化数据。在此状态下，网络无法传输或接收信号数据。 |
  | `SAFEOP` | 4 | 安全运行 - 网络已启动并准备就绪，可全面投入使用。主管将输入数据发送至终端设备。终端设备输出保持在安全状态。 |
  | `OP` | 8 | 运行状态 - 网络处于全面运行状态。主管将输入数据发送至终端设备。终端设备以输出数据作出响应。 |
- `DCErrVal` - 主设备移位控制器的直流错误状态：

  - 主设备移位控制器无直流电错误：`0`
  - 主设备移位控制器直流误差：EtherCAT Init Block DC Error Values的值。

  当选择主设备时移控制器模式时，值 `0` 表示时钟分配成功。当分布式时钟被禁用时，`DCErrVal` 不适用。
- `MdeviceToNetworkClkDiff` - 主设备堆栈时钟与首个启用直流电的从属设备时钟之间的时差（单位：纳秒）。
- `DCInitState` - 分布式时钟的运行状态：

  - 直流电源未启用、未初始化或单个 EtherCAT 直流电源从属设备：`0`
  - 直流电源已启动，EtherCAT 直流从属设备之间已实现同步：`1`
- `NetworkToSubDeviceClkDiff` - 首个从属设备 EtherCAT 的时钟与其余从属设备中锁定精度最低的时钟之间的时间差，单位为纳秒。

  此值仅适用于已启用直流电的从属设备。如果网络中只有一台设备启用了 DC，则此值为 `0`。

**数据类型:** `int32`

## 参数

### **Config file (ENI)** — 来自 EtherCAT 配置器的 ENI 文件 字符向量

指定从 EtherCAT 配置器导出的 ENI 文件。

您可以指定绝对路径名或相对于当前文件夹的相对路径名。若仅指定文件名，软件将在当前文件夹及 MATLAB® 路径中搜索该文件。如果路径上存在多个同名文件，MATLAB 将显示一个消息框，提示需要更明确的文件指定方式。

点击 **Browse** 可插入完整的可编辑路径名称。

#### 编程用法

|  |
| --- |
| **模块参数：**`config_file` |

### **Network Device Index** — EtherCAT 网络标识符 `0-15`

在 `0–15` 范围内的唯一整数，用于标识 EtherCAT 网络中的以太网卡。

对于每个 EtherCAT 网络，软件都会生成一个唯一的设备索引。该软件将设备索引 **Device index** 插入到代表网络的 EtherCAT Init 模块中。有关 Speedgoat 目标计算机设置的更多信息，请参阅安装用于执行的 EtherCAT 网络。

#### 编程用法

|  |
| --- |
| **模块参数：**`device_id` |

### **Ethernet Port Number** — 目标计算机的端口号 `int`

由 `speedgoat.configureEthernet` 函数为 EtherCAT 保留的首个端口在此处为端口 1。有关更多信息，请参阅 Speedgoat 文档中对 `speedgoat.configureEthernet` 函数的描述。有关 Speedgoat 目标计算机设置的更多信息，请参阅安装用于执行的 EtherCAT 网络。

#### 编程用法

|  |
| --- |
| **模块参数：**`portnum` |

### **Initialization End State** — 创建主分支后的最终状态 **Op** (默认) | **PreOp** | **SafeOp**

请从以下值中输入初始化结束状态参数：

- **Op**（默认）- 选择操作状态
- **PreOp** - 选择术前状态
- **SafeOp** - 选择 SAFEOP 状态

此参数在创建主站后，将 EtherCAT 主站堆栈设置为请求的状态。当需要在 SAFEOP 等状态下执行操作时，此方法便显得尤为实用。完成该操作后，使用 EtherCAT Set State 将该模块设置为初始化状态。

#### 编程用法

|  |
| --- |
| **模块参数：**`initstate` |

### **DC Tuning** — 分布式时钟初始化参数 **Large model** (默认) | **Medium model** | **Small model**

请从以下值中选择一个作为分布式时钟初始化参数：

- **Large model**（默认）- 发送 `16,000` 定时初始化数据包，并允许 `1` 秒的稳定时间。为启用了直流电的多个从属设备提供最佳初始同步。
- **Medium model** - 发送 `8,000` 时序初始化数据包，并允许 `0.3` 秒的稳定时间。该模型达到运行状态的时间比采用 **Large model** 设置时提前约一秒。
- **Small model** - 发送 `2,000` 时序初始化数据包，并允许 `0.2` 秒的稳定时间。该模型比其他设置更早达到运行状态。

在模型进入运行状态的瞬间，观察设备同步情况。如果 ENI 文件启用了直流模式，请确保设备之间的同步精度足以满足您的应用需求。

#### 编程用法

|  |
| --- |
| **模块参数：**`dctuning` |

### **Enable EtherCAT Log for Debugging** — 调试和日志记录模块参数的访问权限 **Off** (默认) | **Warning** | **Info** | **Verbose** | `All`

选项选择：

- `Off` - 日志中仅记录致命错误，其余全部跳过。
- `Warning` - 在日志中包含警告和致命错误。
- `Info` - 将信息显示、警告和致命错误包含在日志中。
- `Verbose` - 在日志中包含来自 EtherCAT 协议栈的序列化信息、信息显示、警告和致命错误。
- `All` - 在日志中包含低级调试信息及所有其他类别。

`Verbose` 和 `All` 日志级别可能产生海量数据，在快速任务速率下可能导致系统过载。

目标日志文件名为 `E_Mdevice%d`，其中 `%d` 是设备 ID 值。

#### 编程用法

|  |
| --- |
| **模块参数：**`enaDebug` |

## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

## 描述

使用 EtherCAT 网络信息 (ENI) 文件中的数据初始化 EtherCAT 主设备节点

EtherCAT Init 模块初始化 EtherCAT® 主设备堆栈。该模块指定了网络中的以太网接口卡。

在使用此模块之前，请创建并保存一个 EtherCAT 网络信息 (ENI) 文件。您可从 Beckhoff® TwinCAT® 或 acontis EC-Engineer 中导出 ENI 文件。请参阅使用 TwinCAT 3 配置 EtherCAT 网络。

要查找 ENI 文件，请点击 **Browse**。要读取 ENI 文件并将数据存储在 EtherCAT Init 模块中，请点击 **Refresh Data**。

Simulink® Real-Time™ 软件支持多个 EtherCAT 网络。要使用多个网络：

- 为每个 EtherCAT 网络使用不同的以太网卡接口。
- 在模型中，每个网络使用一个 EtherCAT Init 模块。

当模型启用 PTP 时，需采用 EtherCAT 总线移位模式才能包含 EtherCAT 分布式时钟。
