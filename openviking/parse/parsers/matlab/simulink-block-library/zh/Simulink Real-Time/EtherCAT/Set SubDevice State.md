---
type: simulink-block
title: 'EtherCAT Set Device State'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatsetdevicestate'
documentation_source_path: 'io_ref/ethercatsetdevicestate.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Set Device State

## 端口
```yaml
ports:
- name: New State
  summary: 发送到 EtherCAT 网络的状态 1 | 2 | 4 | 8
  direction: input
- name: Enable
  summary: 使能模块发送状态请求 0 | 1
  direction: input
- name: Prev State
  summary: 所选设备的先前状态 1 | 2 | 4 | 8
  direction: output
- name: Error
  summary: 报告 EtherCAT 状态错误 0 | 整数
  direction: output
```

### 输入

### **New State** — 发送到 EtherCAT 网络的状态 `1` | `2` | `4` | `8`

| 状态 | 值 | 描述 |
| --- | --- | --- |
| `INIT` | 1 | 初始化 — 系统查找终端设备并初始化通信控制器。 |
| `PREOP` | 2 | 预运行 — 系统使用通信控制器交换系统特定的初始化数据。在此状态下，网络无法发送或接收信号数据。 |
| `SAFEOP` | 4 | 安全运行 — 网络正在运行并准备好进行完整操作。主站向终端设备发送输入数据。终端设备输出保持安全状态。 |
| `OP` | 8 | 运行 — 网络处于完整运行状态。主站向终端设备发送输入数据。终端设备以输出数据响应。 |

### **Enable** — 使能模块发送状态请求 `0` | `1`

该端口接受布尔值。当为 true (1) 时，模块发送新的状态请求。当为 false (0) 时，模块不执行任何操作。
### 输出

### **Prev State** — 所选设备的先前状态 `1` | `2` | `4` | `8`

该端口返回设备先前状态的值。该值可能与此模块的先前状态不同。

### **Error** — 报告 EtherCAT 状态错误 `0` | 整数

如果未发生错误，该端口返回 `0`。否则，返回非零值。有关详细信息，请参阅 EtherCAT Error Codes。
## 参数
```yaml
parameters:
- name: Network Device Index
  summary: EtherCAT 网络标识符 0 (默认) | 0-11
  group: ''
  block_parameter: device_id
- name: SubDevice Name
  summary: EtherCAT 从站设备名称 字符向量
  group: ''
  block_parameter: device_name
- name: Sample time
  summary: 模块的采样时间 -1 (默认) | 数值
  group: ''
  block_parameter: sample_time
```

### **Network Device Index** — EtherCAT 网络标识符 `0` (默认) | `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **Network Device Index** 值输入到该模块的 **Network Device Index** 中。

#### 编程使用

|  |
| --- |
| **模块参数**：`device_id` |

### **SubDevice Name** — EtherCAT 从站设备名称 字符向量

从 ENI 配置文件提供的可用从站设备列表中选择一个 EtherCAT 从站设备。该配置文件由 EtherCAT Init 模块选择。

#### 编程使用

|  |
| --- |
| **模块参数**：`device_name` |

### **Sample time** — 模块的采样时间 `-1` (默认) | 数值

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 编程使用

|  |
| --- |
| **模块参数**：`sample_time` |
## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

设置 EtherCAT 网络的状态

EtherCAT Set Device State 模块将 EtherCAT® 网络上设备的状态设置为通过 `New State` 端口传递的值。
