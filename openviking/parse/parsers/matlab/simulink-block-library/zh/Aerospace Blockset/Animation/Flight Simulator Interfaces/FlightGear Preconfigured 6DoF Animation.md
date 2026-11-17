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
```yaml
ports:
- name: l,μ,h,ϕ,θ,ψ
  summary: 经度、纬度、高度、滚转角、俯仰角和偏航角向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point | enumerated | bus
```

### 输入

### **l,μ,h,ϕ,θ,ψ** — 经度、纬度、高度、滚转角、俯仰角和偏航角向量

经度、纬度、高度、滚转角、俯仰角和偏航角，以双精度指定为向量。经度和纬度的单位为度（西经/北纬），高度的单位为米（高于平均海平面），姿态值的单位为弧度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Destination IP address
  summary: 目标 IP 地址 127.0.0.1（默认）| 标量
  group: ''
  block_parameter: DestinationIpAddress
  type: 字符向量
  values: 标量
  default: '''127.0.0.1'''
- name: Destination port
  summary: 目标端口 标量
  group: ''
  block_parameter: DestinationPort
  type: 字符向量
  values: 标量
  default: '''5502'''
- name: Sample time
  summary: 采样时间 1/30（默认）| 标量
  group: ''
  block_parameter: SampleTime
  type: 字符向量
  values: 标量
  default: '''1/30'''
```

### **Destination IP address** — 目标 IP 地址 `127.0.0.1`（默认）| 标量

运行 FlightGear 软件的机器的目标 IP 地址，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`DestinationIpAddress` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'127.0.0.1'` |

### **Destination port** — 目标端口 标量

运行 FlightGear 软件的机器的目标端口，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`DestinationPort` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'5502'` |

### **Sample time** — 采样时间 1/30（默认）| 标量

采样时间，指定为标量（–1 表示继承）。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
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

FlightGear Preconfigured 6DoF Animation 模块允许您分别根据经度（*`l`*）、纬度（*μ*）、高度（*`h`*）、滚转角（*ϕ*）、俯仰角（*θ*）和偏航角（*ψ*）的双精度值，将位置和姿态值驱动到 FlightGear 飞行模拟器载具。

该模块配置为 sim 查看设备。如果您使用 Simulink® Coder™ 为模型生成代码，并使用外部模式仿真连接到正在运行的目标代码，Simulink 软件可以实时从目标获取数据，并将位置和姿态数据传输到 FlightGear。有关详细信息，请参阅 Use C/C++ S-Functions as Sim Viewing Devices in External Mode。

Aerospace Blockset™ 产品支持从 v2.6 开始的 FlightGear 版本。如果您使用的 FlightGear 版本低于 2.6，模型会显示来自 Simulink Upgrade Advisor 的通知。请考虑使用 Upgrade Advisor 升级您的 FlightGear 版本。有关详细信息，请参阅 Supported FlightGear Versions。
