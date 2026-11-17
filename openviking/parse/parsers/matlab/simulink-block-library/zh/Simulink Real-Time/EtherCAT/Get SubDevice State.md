---
type: simulink-block
title: 'EtherCAT Get Device State'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatgetdevicestate'
documentation_source_path: 'io_ref/ethercatgetdevicestate.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Get Device State

## 端口
```yaml
ports:
- name: State
  summary: 从所选设备接收的状态 1 | 2 | 4 | 8
  direction: output
```

### 输出

### **State** — 从所选设备接收的状态 `1` | `2` | `4` | `8`

| 状态 | 值 | 描述 |
| --- | --- | --- |
| `INIT` | 1 | 初始化 — 系统查找终端设备并初始化通信控制器。 |
| `PREOP` | 2 | 预运行 — 系统使用通信控制器交换系统特定的初始化数据。在此状态下，网络无法发送或接收信号数据。 |
| `SAFEOP` | 4 | 安全运行 — 网络正在运行并准备好进行完整操作。主站向终端设备发送输入数据。终端设备输出保持在安全状态。 |
| `OP` | 8 | 运行 — 网络处于完整运行状态。主站向终端设备发送输入数据。终端设备以输出数据响应。 |
## 参数
```yaml
parameters:
- name: Network Device Index
  summary: EtherCAT 网络标识符 0（默认）| 0-11
  group: ''
  block_parameter: device_id
- name: SubDevice Name
  summary: EtherCAT 从站设备名称 字符向量
  group: ''
  block_parameter: device_name
- name: Sample time
  summary: 模块采样时间 -1（默认）| 数值
  group: ''
  block_parameter: sample_time
```

### **Network Device Index** — EtherCAT 网络标识符 `0`（默认）| `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **Network Device Index** 值输入到该模块的 **Network Device Index** 中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `device_id` |

### **SubDevice Name** — EtherCAT 从站设备名称 字符向量

从 ENI 配置文件提供的可用从站设备列表中选择一个 EtherCAT 从站设备。配置文件由 EtherCAT Init 模块选择。

#### 程序化使用

|  |
| --- |
| **模块参数：** `device_name` |

### **Sample time** — 模块采样时间 `-1`（默认）| 数值

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sample_time` |
## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

获取 EtherCAT 网络的状态

EtherCAT Get Device State 模块返回 EtherCAT® 网络上设备的状态。
