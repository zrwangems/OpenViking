---
type: simulink-block
title: 'Pilot Joystick'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Animation Support Utilities'
documentation_page: 'pilotjoystick'
documentation_source_path: 'pilotjoystick.html'
language: zh-CN
chinese_source: worker-translation
---

# Pilot Joystick

## 端口
```yaml
ports:
- name: roll
  summary: 滚转范围 [-1, 1]
  direction: output
  data_types: double
- name: pitch
  summary: 俯仰范围 [-1, 1]
  direction: output
  data_types: double
- name: yaw
  summary: 偏航范围 [-1, 1]
  direction: output
  data_types: double
- name: throttle
  summary: 油门范围 [0, 1]
  direction: output
  data_types: double
```

### 输出

### **roll** — 滚转范围 [-1, 1]

滚转指令，指定在范围 [-1, 1] 内，对应于操纵杆向左和向右方向。

#### 依赖关系

要启用此端口，请将 **Output configuration** 设置为
`FourAxis`。

**数据类型：** `double`

### **pitch** — 俯仰范围 [-1, 1]

俯仰指令，指定在范围 [-1, 1] 内，对应于操纵杆向前或向下以及向后或向上方向。

#### 依赖关系

当 **Output
configuration** 参数设置为
`FourAxis` 时，此输出端口启用。

**数据类型：** `double`

### **yaw** — 偏航范围 [-1, 1]

偏航指令，指定在范围 [-1, 1] 内，对应于操纵杆向左扭转和向右扭转方向。

#### 依赖关系

要启用此端口，请将 **Output configuration** 设置为
`FourAxis`。

**数据类型：** `double`

### **throttle** — 油门范围 [0, 1]

油门指令，指定在范围 [0, 1] 内，对应于操纵杆最小和最大位置。

#### 依赖关系

要启用此端口，请将 **Output configuration** 设置为
`FourAxis`。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Joystick ID
  summary: 操纵杆 ID Joystick1（默认）| Joystick2 | Joystick3 | Joystick4 | Joystick5 | Joystick6 | Joystick7 | Joystick8 | Joystick9
    | Joystick10 | Joystick11 | Joystick12 | Joystick13 | Joystick14 | Joystick15 | Joystick16 | None
  group: ''
  block_parameter: JoystickID
  type: 字符向量
  values: Joystick1 | Joystick2 | Joystick3 | Joystick4 | Joystick5 | Joystick6 | Joystick7 | Joystick8 | Joystick9 | Joystick10
    | Joystick11 | Joystick12 | Joystick13 | Joystick14 | Joystick15 | Joystick16 | None
  default: '''Joystick1'''
- name: Output configuration
  summary: 操纵杆输出配置 FourAxis（默认）| AllOutputs
  group: ''
  block_parameter: OutputConfiguration
  type: 字符向量
  values: FourAxis | AllOutputs
  default: '''FourAxis'''
- name: Sample time
  summary: 采样时间 1/30（默认）| -1 | 标量
  group: ''
  block_parameter: SampleTime
  type: 字符向量
  values: 标量
  default: '''1/30'''
```

### **Joystick ID** — 操纵杆 ID `Joystick1`（默认）| `Joystick2` | `Joystick3` | `Joystick4` | `Joystick5` | `Joystick6` | `Joystick7` | `Joystick8` | `Joystick9` | `Joystick10` | `Joystick11` | `Joystick12` | `Joystick13` | `Joystick14` | `Joystick15` | `Joystick16` | `None`

将操纵杆 ID 指定为

- `Joystick1`
- `Joystick2`
- `Joystick3`
- `Joystick4`
- `Joystick5`
- `Joystick6`
- `Joystick7`
- `Joystick8`
- `Joystick9`
- `Joystick10`
- `Joystick11`
- `Joystick12`
- `Joystick13`
- `Joystick14`
- `Joystick15`
- `Joystick16`
- `None`

#### 程序化使用

|  |
| --- |
| **模块参数**：`JoystickID` |
| **类型**：字符向量 |
| **值**：`Joystick1` | `Joystick2` | `Joystick3` | `Joystick4` | `Joystick5` | `Joystick6` | `Joystick7` | `Joystick8` | `Joystick9` | `Joystick10` | `Joystick11` | `Joystick12` | `Joystick13` | `Joystick14` | `Joystick15` | `Joystick16` | `None` |
| **默认值**：`'Joystick1'` |

### **Output configuration** — 操纵杆输出配置 `FourAxis`（默认）| `AllOutputs`

操纵杆输出配置，指定为
`FourAxis` 或
`AllOutputs`。有关
`AllOutputs` 配置的更多信息，请参阅 Pilot Joystick All。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OutputConfiguration` |
| **类型**：字符向量 |
| **值**：`FourAxis` | `AllOutputs` |
| **默认值**：`'FourAxis'` |

### **Sample time** — 采样时间 `1/30`（默认）| `-1` | 标量

指定采样时间（-1 表示继承），指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1/30'` |
## 所属库

Aerospace Blockset / Animation / Animation Support Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

### R2023b：Pilot Joystick 模块更新

Pilot Joystick 模块现在支持最多 16 个操纵杆。

## 描述

在 Windows 平台上提供操纵杆接口

Pilot Joystick 模块为 Windows® 平台提供飞行员操纵杆接口。滚转、俯仰、偏航和油门分别映射到操纵杆的
*X*、*Y*、*R* 和
*Z* 通道。

Pilot Joystick 和 Pilot Joystick All 模块是同一模块的替代配置。

- Pilot Joystick — 输出四个轴。
- Pilot Joystick All — 输出所有通道。

要生成可部署代码，请从 **Code Generation** > **Toolchain** 中选择一个配置参数 Microsoft®
Visual Studio® C++ `nmake` 工具链。
