---
type: simulink-block
title: 'Fixed-Wing UAV Point Mass'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Algorithms'
documentation_page: 'fixedwinguavpointmass'
documentation_source_path: 'ref/fixedwinguavpointmass.html'
language: zh-CN
chinese_source: worker-translation
---

# Fixed-Wing UAV Point Mass

## 端口
```yaml
ports:
- name: Lift
  summary: 升力标量
  direction: input
  data_types: double
- name: Drag
  summary: 阻力标量
  direction: input
  data_types: double
- name: Weight
  summary: 重力标量
  direction: input
  data_types: double
- name: Thrust
  summary: 推力标量
  direction: input
  data_types: double
- name: ɣa
  summary: 相对于气流的航迹角标量
  direction: input
  data_types: double
- name: μ
  summary: 滚转角标量
  direction: input
  data_types: double
- name: ɑ
  summary: 迎角标量
  direction: input
  data_types: double
- name: Vwind
  summary: 风矢量三元向量
  direction: input
  data_types: double
- name: V
  summary: 空速标量
  direction: output
  data_types: double
- name: G
  summary: 地速投影标量
  direction: output
  data_types: double
- name: Va
  summary: 相对于气流的速度矢量三元向量
  direction: output
  data_types: double
- name: Ve
  summary: 相对于地球的速度矢量，[North East Down] 方向三元向量
  direction: output
  data_types: double
- name: VENU
  summary: 相对于地球的速度矢量三元向量
  direction: output
  data_types: double
- name: Xe
  summary: 相对于地球的位置矢量三元向量
  direction: output
  data_types: double
- name: XENU
  summary: 相对于地球的位置矢量三元向量
  direction: output
  data_types: double
- name: γa
  summary: 相对于气流的航迹角标量
  direction: output
  data_types: double
- name: γ
  summary: 相对于地球的航迹角标量
  direction: output
  data_types: double
- name: χa
  summary: 相对于气流的航向角标量
  direction: output
  data_types: double
- name: χ
  summary: 相对于地球的航向角标量
  direction: output
  data_types: double
```

### 输入

### **Lift** — 升力标量

升力，指定为以力为单位的标量。

**数据类型：** `double`

### **Drag** — 阻力标量

阻力，指定为以力为单位的标量。

**数据类型：** `double`

### **Weight** — 重力标量

重力，指定为以力为单位的标量。

**数据类型：** `double`

### **Thrust** — 推力标量

推力，指定为以力为单位的标量。

**数据类型：** `double`

### **ɣa** — 相对于气流的航迹角标量

相对于气流的航迹角，指定为以弧度为单位的标量。

**数据类型：** `double`

### **μ** — 滚转角标量

滚转角，指定为以弧度为单位的标量。

**数据类型：** `double`

### **ɑ** — 迎角标量

迎角，指定为以弧度为单位的标量。

**数据类型：** `double`

### **Vwind** — 风矢量三元向量

沿气流运动方向的风矢量，指定为三元向量。

**数据类型：** `double`
### 输出

### **V** — 空速标量

空速，以标量形式返回。

**数据类型：** `double`

### **G** — 地速投影标量

相对于地球的地速（地面运动速度），以标量形式返回。

**数据类型：** `double`

### **Va** — 相对于气流的速度矢量三元向量

相对于气流的速度矢量，以三元向量形式返回。

**数据类型：** `double`

### **Ve** — 相对于地球的速度矢量，`[North East Down]` 方向三元向量

相对于地球的速度矢量，方向为 `[North East Down]`，以三元向量形式返回。

#### 依赖

要启用此端口，请将 **Reference frame orientation** 设置为
`[North East Down]`。

**数据类型：** `double`

### **VENU** — 相对于地球的速度矢量三元向量

相对于地球的速度矢量，方向为 `[East North Up]`，以三元向量形式返回。

#### 依赖

要启用此端口，请将 **Reference frame orientation** 设置为
`[East North Up]`。

**数据类型：** `double`

### **Xe** — 相对于地球的位置矢量三元向量

相对于地球的位置矢量，方向为 `[North East Down]`，以三元向量形式返回。

#### 依赖

要启用此端口，请将 **Reference frame orientation** 设置为
`[North East Down]`。

**数据类型：** `double`

### **XENU** — 相对于地球的位置矢量三元向量

相对于地球的位置矢量，方向为 `[East North Up]`，以三元向量形式返回。

#### 依赖

要启用此端口，请将 **Reference frame orientation** 设置为
`[East North Up]`。

**数据类型：** `double`

### **γa** — 相对于气流的航迹角标量

相对于气流的航迹角，以标量形式返回。

**数据类型：** `double`

### **γ** — 相对于地球的航迹角标量

相对于地球的航迹角，以标量形式返回。

**数据类型：** `double`

### **χa** — 相对于气流的航向角标量

相对于气流的航向角，以标量形式返回。

#### 依赖

要启用此端口，请将 **Degrees of Freedom** 设置为 `6th
Order (Coordinated Flight)`。

**数据类型：** `double`

### **χ** — 相对于地球的航向角标量

相对于地球的航向角，以标量形式返回。

#### 依赖

要启用此端口，请将 **Degrees of Freedom** 设置为 `6th
Order (Coordinated Flight)`。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 单位 Metric (MKS)（默认）| English (velocity in ft/s) | English (velocity in kts)
  group: ''
  block_parameter: units
  type: 字符向量
  values: '''Metric (MKS)'' | ''English (velocity in ft/s)'' | ''English (velocity in kts)'''
  default: '''Metric (MKS)'''
- name: 参考坐标系方向
  summary: 参考坐标系 [North East Down]（默认）| [East North Up]
  group: ''
  block_parameter: frame
  type: 字符向量
  values: '''[East North Up]'' | ''[North East Down]'''
  default: '''[North East Down]'''
- name: 自由度
  summary: 自由度 6th Order (Coordinated Flight)（默认）| 4th Order (Longitudinal)
  group: ''
  block_parameter: order
  type: 字符向量
  values: '''4th Order (Longitudinal)'' | ''6th Order (Coordinated Flight)'''
  default: '''6th Order (Coordinated Flight)'''
- name: 初始横向距离
  summary: 初始东向（地球）横向距离位置 0（默认）| 标量
  group: ''
  block_parameter: east
  type: 字符向量
  values: 标量
  default: '''0'''
- name: 初始纵向距离
  summary: 初始北向（地球）纵向距离 0（默认）| 标量
  group: ''
  block_parameter: north
  type: 字符向量
  values: 标量
  default: '''0'''
- name: 初始高度
  summary: 初始高度 0（默认）| 标量
  group: ''
  block_parameter: altitude
  type: 字符向量
  values: 标量
  default: '''0'''
- name: 初始空速
  summary: 初始空速 50（默认）| 标量
  group: ''
  block_parameter: '''airspeed'''
  type: 字符向量
  values: 标量
  default: '''50'''
- name: 初始航迹角
  summary: 初始航迹角 0（默认）| 标量
  group: ''
  block_parameter: gamma
  type: 字符向量
  values: 标量
  default: '''0'''
- name: 初始航向角
  summary: 初始航向角 0（默认）| 标量
  group: ''
  block_parameter: chi
  type: 字符向量
  values: 标量
  default: '''0'''
- name: 质量
  summary: 质点质量 10（默认）| 标量
  group: ''
  block_parameter: mass
  type: 字符向量
  values: 标量
  default: '''10'''
```

### **Units** — 单位 `Metric (MKS)`（默认）| `English (velocity in ft/s)` | `English (velocity in kts)`

输入和输出单位，指定如下：

| 单位 | 力 | 速度 | 位置 | 质量 |
| --- | --- | --- | --- | --- |
| `Metric (MKS)` | newtons | meters per second | meters | kilograms |
| `English (velocity in ft/s)` | pounds | feet per second | feet | slugs |
| `English (velocity in kts)` | pounds | knots | feet | slugs |

#### 程序化使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English (velocity in ft/s)'` | `'English (velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **参考坐标系方向** — 参考坐标系 `[North East Down]`（默认）| `[East North Up]`

用于输入端口和输出端口的参考坐标系，指定为 `[East North Up]` 或 `[North East Down]`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`frame` |
| **类型**：字符向量 |
| **值**：`'[East North Up]'` | `'[North East Down]'` |
| **默认值**：`'[North East Down]'` |

### **自由度** — 自由度 `6th Order (Coordinated Flight)`（默认）| `4th Order (Longitudinal)`

自由度，指定为 `4th Order (Longitudinal)` 或 `6th Order (Coordinated Flight)`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`order` |
| **类型**：字符向量 |
| **值**：`'4th Order (Longitudinal)'` | `'6th Order (Coordinated Flight)'` |
| **默认值**：`'6th Order (Coordinated Flight)'` |

### **初始横向距离** — 初始东向（地球）横向距离位置 `0`（默认）| 标量

在 `[North East Down]` 方向下的初始东向（地球）位置，指定为标量。

#### 依赖关系

此参数的方向指定取决于 **参考坐标系方向** 和 **自由度** 设置：

| 初始横向距离 | 参考坐标系方向 | 自由度 |
| --- | --- | --- |
| East | [North East Down] | 6th Order (Coordinated Flight) |
| North | [East North Up] | 6th Order (Coordinated Flight) |

#### 程序化使用

|  |
| --- |
| **模块参数**：`east` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **初始纵向距离** — 初始北向（地球）纵向距离 `0`（默认）| 标量

质点模型的初始北向（地球）纵向距离，指定为标量。

#### 依赖关系

此参数的方向指定取决于 **参考坐标系方向** 和 **自由度** 设置：

| 初始纵向距离 | 参考坐标系方向 | 自由度 |
| --- | --- | --- |
| North | [North East Down] | 6th Order (Coordinated Flight) |
| North | [North East Down] | 4th Order (Longitudinal) |
| East | [East North Up] | 6th Order (Coordinated Flight) |
| East | [East North Up] | 4th Order (Longitudinal) |

#### 程序化使用

|  |
| --- |
| **模块参数**：`north` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **初始高度** — 初始高度 `0`（默认）| 标量

质点模型的初始高度，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`altitude` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **初始空速** — 初始空速 `50`（默认）| 标量

质点模型的初始空速，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`'airspeed'` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'50'` |

### **初始航迹角** — 初始航迹角 `0`（默认）| 标量

质点模型的初始航迹角，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`gamma` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **初始航向角** — 初始航向角 `0`（默认）| 标量

质点模型的初始航向角，指定为标量。

#### 依赖关系

要启用此参数，请将 **自由度** 设置为 `6th Order (Coordinated Flight)`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`chi` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **质量** — 质点质量 `10`（默认）| 标量

质点模型的质量，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`mass` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'10'` |
## 所属库

UAV Toolbox / Algorithms Aerospace Blockset / Equations of Motion / Point Mass

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

在协调飞行中积分四阶或六阶质点运动方程

Fixed-Wing Point Mass 模块在协调飞行中积分四阶或六阶质点运动方程。
