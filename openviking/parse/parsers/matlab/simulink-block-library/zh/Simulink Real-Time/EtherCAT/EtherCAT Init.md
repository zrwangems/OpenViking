---
type: simulink-block
title: 'EtherCAT Init'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatinit'
documentation_source_path: 'io_ref/ethercatinit.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Init

## 端口
```yaml
ports:
- name: Status
  summary: 关于 EtherCAT 网络的状态信息向量
  direction: output
  data_types: int32
```

### 输出

### **Status** — 关于 EtherCAT 网络的状态信息向量

`Status` 向量包含以下值：
`ErrVal`、`MdeviceState`、
`DCErrVal`、
`MdeviceToNetworkClkDiff`、
`DCInitState` 和
`NetworkToSubDeviceClkDiff`。

- `ErrVal` — 错误状态：

  - 无
    错误：`0`
  - 错误：小于 `0` 的值。

  由于 `ErrVal` 显示最新的错误
  状态，错误的传播可能会隐藏原始错误。
  要查找原始错误，请添加一个 EtherCAT Get
  Notifications 模块，并使用 `slrealtime.EtherCAT.filterNotifications` 命令
  打印 EtherCAT 协议栈传输的状态码。
- `MdeviceState` — EtherCAT 网络的
  运行状态。

  | 状态 | 值 | 描述 |
  | --- | --- | --- |
  | `INIT` | 1 | 初始化 — 系统查找终端设备并初始化通信控制器。 |
  | `PREOP` | 2 | 预运行 — 系统使用通信控制器交换系统特定的初始化数据。在此状态下，网络无法发送或接收信号数据。 |
  | `SAFEOP` | 4 | 安全运行 — 网络正在运行并准备好进行完整操作。主站向终端设备发送输入数据。终端设备输出保持安全状态。 |
  | `OP` | 8 | 运行 — 网络处于完整运行状态。主站向终端设备发送输入数据。终端设备以输出数据响应。 |
- `DCErrVal` — 主设备移位控制器的
  DC 错误状态：

  - 主设备移位控制器无
    DC 错误：
    `0`
  - 主设备移位控制器 DC 错误：来自 EtherCAT Init 模块 DC Error Values 的值。

  当您选择主设备移位控制器模式时，值
  `0` 表示时钟
  分配成功。当分布式时钟被禁用时，`DCErrVal` 不适用。
- `MdeviceToNetworkClkDiff` — 主设备协议栈时钟与第一个已启用 DC 的
  从属
  设备上的时钟之间的时间
  差，以纳秒为单位。
- `DCInitState` — 分布式时钟的
  运行状态：

  - DC 未启用、未初始化或单个 EtherCAT DC
    从属设备：`0`
  - DC 已启动且 EtherCAT DC 从属设备彼此
    同步：`1`
- `NetworkToSubDeviceClkDiff` — 第一个
  EtherCAT 从属
  设备上的时钟与其余从属设备中锁定最不紧密的时钟之间的时间
  差，以纳秒为单位。

  此值仅适用于已启用 DC 的从属设备。
  如果网络上只有一个
  设备启用了 DC，则此值为
  `0`。

**数据类型：** `int32`
## 参数
```yaml
parameters:
- name: Config file (ENI)
  summary: 来自 EtherCAT 配置器的 ENI 文件 字符向量
  group: ''
  block_parameter: config_file
- name: Network Device Index
  summary: EtherCAT 网络标识符 0-15
  group: ''
  block_parameter: device_id
- name: Ethernet Port Number
  summary: 目标计算机中的端口号 int
  group: ''
  block_parameter: portnum
- name: Initialization End State
  summary: 创建主站后的结束状态 Op（默认）| PreOp | SafeOp
  group: ''
  block_parameter: initstate
- name: DC Tuning
  summary: 分布式时钟初始化参数 Large model（默认）| Medium model | Small model
  group: ''
  block_parameter: dctuning
- name: Enable EtherCAT Log for Debugging
  summary: 访问调试和日志记录模块参数 Off（默认）| Warning | Info | Verbose | All
  group: ''
  block_parameter: enaDebug
```

### **Config file (ENI)** — 来自 EtherCAT 配置器的 ENI 文件 字符向量

指定您从 EtherCAT 配置器导出的 ENI 文件。

您可以指定绝对路径名或相对于
当前文件夹的相对路径名。如果仅指定文件名，软件将在当前文件夹和
MATLAB® 路径中搜索该文件。如果路径上存在多个具有该名称的文件，
MATLAB 将显示一个消息框，指示需要更明确的文件
指定。

点击 **Browse** 插入完整的、可编辑的路径名。

#### 编程使用

|  |
| --- |
| **模块参数**：`config_file` |

### **Network Device Index** — EtherCAT 网络标识符 `0-15`

一个范围在 `0–15` 之间的唯一整数，用于标识 EtherCAT 网络的以太网卡。

对于每个 EtherCAT 网络，软件生成一个唯一的
设备索引。软件将该设备索引作为
**Device index**
插入到代表该网络的 EtherCAT Init 模块中。有关 Speedgoat Target Machine 设置的更多
信息，请参阅 Install EtherCAT Network for Execution。

#### 编程使用

|  |
| --- |
| **模块参数**：`device_id` |

### **Ethernet Port Number** — 目标计算机中的端口号 `int`

由 `speedgoat.configureEthernet` 函数为 EtherCAT 保留的第一个端口在此处为端口 1。有关详细信息，请参阅 Speedgoat 文档中 `speedgoat.configureEthernet` 函数的描述。有关 Speedgoat 目标机设置的详细信息，请参阅 Install EtherCAT Network for Execution。

#### 编程使用

|  |
| --- |
| **模块参数**：`portnum` |

### **Initialization End State** — 创建主站后的结束状态 `Op`（默认）| `PreOp` | `SafeOp`

从以下值之一输入初始化结束状态参数：

- `Op`（默认）— 选择 OP 状态
- `PreOp` — 选择 PREOP 状态
- `SafeOp` — 选择 SAFEOP 状态

此参数在创建主站之后立即将 EtherCAT 主站栈设置为请求的状态。当需要在 SAFEOP 等状态下完成工作时，此方法很有用。完成该工作后，使用 EtherCAT Set State 将模块设置为 INIT。

#### 编程使用

|  |
| --- |
| **模块参数**：`initstate` |

### **DC Tuning** — 分布式时钟初始化参数 `Large model`（默认）| `Medium model` | `Small model`

从以下值之一输入分布式时钟初始化参数：

- `Large model`（默认）— 发送 `16,000` 个时间初始化数据包，并允许 `1` 秒的稳定时间。在启用了 DC 的多个从站设备之间提供最佳的初始同步。
- `Medium model` — 发送 `8,000` 个时间初始化数据包，并允许 `0.3` 秒的稳定时间。与使用 `Large model` 设置相比，模型大约提前一秒达到运行状态。
- `Small model` — 发送 `2,000` 个时间初始化数据包，并允许 `0.2` 秒的稳定时间。与其他设置相比，模型更早达到运行状态。

在模型进入运行状态时观察设备同步情况。如果 ENI 文件启用了 DC，请确保设备同步程度足够紧密，以满足您的应用需求。

#### 编程使用

|  |
| --- |
| **模块参数**：`dctuning` |

### **Enable EtherCAT Log for Debugging** — 访问调试和日志记录模块参数 `Off`（默认）| `Warning` | `Info` | `Verbose` | `All`

这些选项选择：

- `Off` — 日志中跳过除致命错误以外的所有内容。
- `Warning` — 日志中包含警告和致命错误。
- `Info` — 日志中包含信息显示、警告和致命错误。
- `Verbose` — 日志中包含来自 EtherCAT 栈的时序信息、信息显示、警告和致命错误。
- `All` — 日志中包含底层调试信息和所有其他类别。

`Verbose` 和 `All` 日志记录级别可能产生大量数据，从而在快速任务速率下导致过载。

目标日志文件名为 `E_Mdevice%d`，其中 `%d` 是设备 ID 值。

#### 编程使用

|  |
| --- |
| **模块参数**：`enaDebug` |
## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

使用 EtherCAT 网络信息（ENI）文件中的数据初始化 EtherCAT 主设备节点

EtherCAT Init 模块初始化 EtherCAT® 主设备协议栈。该模块指定网络中的以太网接口卡。

在使用此模块之前，请创建并保存 EtherCAT 网络信息（ENI）文件。您可以从 Beckhoff® TwinCAT® 或 acontis EC-Engineer 导出 ENI 文件。请参阅使用 TwinCAT 3 配置 EtherCAT 网络。

要查找 ENI 文件，请点击 **Browse**。要读取 ENI 文件并将数据存储到 EtherCAT Init 模块中，请点击 **Refresh Data**。

Simulink® Real-Time™ 软件支持多个 EtherCAT 网络。要使用多个网络：

- 为每个 EtherCAT 网络使用不同的以太网卡接口。
- 在模型中，为每个网络使用一个 EtherCAT Init 模块。

当模型启用了 PTP 时，要包含 EtherCAT 分布式时钟，请使用 EtherCAT 总线偏移模式。
