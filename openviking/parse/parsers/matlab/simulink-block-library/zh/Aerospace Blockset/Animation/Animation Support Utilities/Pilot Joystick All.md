---
type: simulink-block
title: 'Pilot Joystick All'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Animation Support Utilities'
documentation_page: 'pilotjoystickall'
documentation_source_path: 'pilotjoystickall.html'
language: zh-CN
chinese_source: worker-translation
---

# Pilot Joystick All

## 端口
```yaml
ports:
- name: analog
  summary: 模拟输出范围 [-1, 1] | 范围 [ 0, 1]
  direction: output
  data_types: double
- name: buttons
  summary: 包含 32 个按钮状态的按钮标志字
  direction: output
  data_types: uint32
- name: POV
  summary: 视点帽
  direction: output
  data_types: double
```

### 输出

### **analog** — 模拟输出范围 [-1, 1] | 范围 [ 0, 1]

模拟输出，根据以下内容返回：

| 数组编号 | 通道 | 输出范围 | 操纵杆 | 描述 |
| --- | --- | --- | --- | --- |
| `1` | X | [-1, 1] | [左, 右] | 滚转指令 |
| `2` | Y | [-1, 1] | [前进/下降, 后退/上升] | 俯仰指令 |
| `3` | Z | [ 0, 1] | [最小, 最大] | 油门指令 |
| `4` | R | [-1, 1] | [左, 右] | 偏航指令 |
| `5` | U | [ 0, 1] | [最小, 最大] | U 通道值 |
| `6` | V | [ 0, 1] | [最小, 最大] | V 通道值 |

**数据类型：** `double`

### **buttons** — 包含 32 个按钮状态的按钮标志字

按钮输出，返回为包含 buttons 通道上最多 32 个按钮状态的标志字。位 0 是按钮 1，位 1 是按钮 2，依此类推。

**数据类型：** `uint32`

### **POV** — 视点帽

视点，返回为 POV 通道上以度数为单位的帽值。零度为正前方，90 度为左方，依此类推。

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
  summary: 操纵杆输出配置 AllOutputs（默认）| FourAxis
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

#### 编程使用

|  |
| --- |
| **模块参数**：`JoystickID` |
| **类型**：字符向量 |
| **值**：`Joystick1` | `Joystick2` | `Joystick3` | `Joystick4` | `Joystick5` | `Joystick6` | `Joystick7` | `Joystick8` | `Joystick9` | `Joystick10` | `Joystick11` | `Joystick12` | `Joystick13` | `Joystick14` | `Joystick15` | `Joystick16` | `None` |
| **默认值**：`'Joystick1'` |

### **Output configuration** — 操纵杆输出配置 `AllOutputs`（默认）| `FourAxis`

操纵杆输出配置，指定为 `FourAxis` 或 `AllOutputs`。有关 `AllOutputs` 配置的更多信息，请参阅 Pilot Joystick All。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputConfiguration` |
| **类型**：字符向量 |
| **值**：`FourAxis` | `AllOutputs` |
| **默认值**：`'FourAxis'` |

### **Sample time** — 采样时间 `1/30`（默认）| `-1` | 标量

指定采样时间（-1 表示继承），指定为标量。

#### 编程使用

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

**在 R2007a 中引入**

### R2023b：Pilot Joystick All 模块更新

Pilot Joystick All 模块现在支持最多 16 个操纵杆。

## 描述

在 Windows 平台上以 All Outputs 配置提供操纵杆接口

Pilot Joystick All 模块为 Windows® 平台提供飞行员操纵杆接口。滚转、俯仰、偏航和油门分别映射到操纵杆的 *X*、*Y*、*R* 和 *Z* 通道。

Pilot Joystick 和 Pilot Joystick All 模块是同一模块的替代配置。

- Pilot Joystick — 输出四个轴。
- Pilot Joystick All — 输出所有通道。

要生成可部署代码，请从 **Code Generation** > **Toolchain** 中选择一个配置参数 Microsoft® Visual Studio® C++ `nmake` 工具链。
