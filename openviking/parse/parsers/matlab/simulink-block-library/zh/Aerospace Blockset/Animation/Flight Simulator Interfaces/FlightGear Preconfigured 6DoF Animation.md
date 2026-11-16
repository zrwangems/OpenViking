---
type: simulink-block
title: 'FlightGear Preconfigured 6DoF Animation'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Flight Simulator Interfaces'
documentation_page: 'flightgearpreconfigured6dofanimation'
documentation_source_path: 'flightgearpreconfigured6dofanimation.html'
language: zh-CN
chinese_source: worker-translation
---

# FlightGear Preconfigured 6DoF Animation

## 端口

### 输入

### **l,μ,h,ϕ,θ,ψ** — 经度、纬度、高度、滚转、俯仰和偏航向量

经度、纬度、高度、滚转、俯仰和偏航，以双精度指定为向量。单位：经度和纬度为度（经度用西经，纬度用北纬），高度为平均海平面以上米数，姿态值为弧度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **目标 IP 地址** — 目标 IP 地址 `127.0.0.1`（默认） | 标量

运行 FlightGear 软件的机器的目标 IP 地址，指定为标量。

#### 编程用法

|  |
| --- |
| **模块参数**：`DestinationIpAddress` |
| **类型**：character vector |
| **值**：标量 |
| **默认值**：`'127.0.0.1'` |

### **目标端口** — 目标端口 标量

运行 FlightGear 软件的机器的目标端口，指定为标量。

#### 编程用法

|  |
| --- |
| **模块参数**：`DestinationPort` |
| **类型**：character vector |
| **值**：标量 |
| **默认值**：`'5502'` |

### **采样时间** — 采样时间 1/30（默认） | 标量

采样时间，指定为标量（–1 表示继承）。

#### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **值**：标量 |
| **默认值**：`'1/30'` |

## 所属库

Aerospace Blockset / Animation / Flight Simulator Interfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

将模型连接到 FlightGear 飞行模拟器

FlightGear Preconfigured 6DoF Animation 模块允许您将位置和姿态值驱动到 FlightGear 飞行模拟器载具，前提是分别给定经度（*`l`*）、纬度（*μ*）、高度（*`h`*）、滚转（*ϕ*）、俯仰（*`θ`*）和偏航（*`ψ`*）的双精度值。

该模块配置为 sim 查看设备。如果您使用 Simulink® Coder™ 为模型生成代码，并使用外部模式仿真连接到正在运行的目标代码，Simulink 软件可以实时从目标获取数据，并将位置和姿态数据传输到 FlightGear。有关详细信息，请参阅在外部模式下将 C/C++ S-Functions 用作 Sim 查看设备。

Aerospace Blockset™ 产品支持从 v2.6 开始的 FlightGear 版本。如果您使用的 FlightGear 版本早于 2.6，模型会显示来自 Simulink Upgrade Advisor 的通知。请考虑使用 Upgrade Advisor 升级您的 FlightGear 版本。有关详细信息，请参阅支持的 FlightGear 版本。
