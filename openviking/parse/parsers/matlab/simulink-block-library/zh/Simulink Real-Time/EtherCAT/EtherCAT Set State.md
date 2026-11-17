---
type: simulink-block
title: 'EtherCAT Set State'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatsetstate'
documentation_source_path: 'io_ref/ethercatsetstate.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Set State

## 端口

### 输入

### **New State** — 传输到 EtherCAT 网络的状态 `1` | `2` | `4` | `8`

| 状态 | 值 | 描述 |
| --- | --- | --- |
| `INIT` | 1 | 初始化 — 系统查找终端设备并初始化通信控制器。 |
| `PREOP` | 2 | 预运行 — 系统使用通信控制器交换系统特定的初始化数据。在此状态下，网络无法发送或接收信号数据。 |
| `SAFEOP` | 4 | 安全运行 — 网络正在运行并准备好进行完整操作。监控器向终端设备发送输入数据。终端设备输出保持安全状态。 |
| `OP` | 8 | 运行 — 网络处于完整运行状态。监控器向终端设备发送输入数据。终端设备以输出数据响应。 |
### 输出

### **Prev State** — 网络的前一状态 `1` | `2` | `4` | `8`

此端口返回 `New State` 端口上一次设置的值。

### **Error** — 报告 EtherCAT 状态错误 `0` | 整数

如果未发生错误，此端口返回 `0`。否则，返回非零值。

## 参数

### **Network Device Index** — EtherCAT 网络标识符 `0`（默认）| `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **Network Device Index** 值输入到该模块的 **Network Device Index** 中。

#### 编程使用

|  |
| --- |
| **模块参数**：`device_id` |

### **Timeout** — 等待网络改变状态的时间 整数

输入等待 EtherCAT 网络状态转换的秒数。

将超时设置为 `0` 可立即返回。如果指定非零的 **Timeout** 值，请在配置参数 **Solver** 窗格中将 **Fixed-step size** 参数设置为大于 **Timeout** 值的值。

#### 编程使用

|  |
| --- |
| **模块参数**：`timeout` |

### **Sample time** — 模块的采样时间 `-1`（默认）| 数值

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

**在 R2020b 中引入**

## 描述

设置 EtherCAT 网络的状态

EtherCAT Set State 模块将 EtherCAT® 网络的状态设置为通过 `New State` 端口传入的值。
