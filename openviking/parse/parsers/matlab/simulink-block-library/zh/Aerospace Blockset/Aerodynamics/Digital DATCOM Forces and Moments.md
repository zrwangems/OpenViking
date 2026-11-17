---
type: simulink-block
title: 'Digital DATCOM Forces and Moments'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Aerodynamics'
documentation_page: 'digitaldatcomforcesandmoments'
documentation_source_path: 'digitaldatcomforcesandmoments.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital DATCOM Forces and Moments

## 端口
```yaml
ports:
- name: Port_1
  summary: 迎角标量
  direction: input
  data_types: double
- name: Port_2
  summary: 侧滑角标量
  direction: input
  data_types: double
- name: Port_3
  summary: 马赫数标量
  direction: input
  data_types: double
- name: Port_4
  summary: 高度标量
  direction: input
  data_types: double
- name: Port_5
  summary: 动压标量
  direction: input
  data_types: double
- name: Port_6
  summary: 速度三元向量
  direction: input
  data_types: double
- name: Port_7
  summary: 迎角变化率标量
  direction: input
  data_types: double
- name: Port_8
  summary: 机体角速率三元向量
  direction: input
  data_types: double
- name: Port_9
  summary: 地面高度标量
  direction: input
  data_types: double
- name: Port_10
  summary: 操纵面偏转标量
  direction: input
  data_types: double
- name: Port_1
  summary: 重心处的气动力三元向量
  direction: output
  data_types: double
- name: Port_2
  summary: 重心处的气动力矩三元向量
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 迎角标量

迎角，指定为标量。

**数据类型：** `double`

### **Port\_2** — 侧滑角标量

侧滑角，指定为标量，单位为弧度。

**数据类型：** `double`

### **Port\_3** — 马赫数标量

马赫数，指定为标量。

**数据类型：** `double`

### **Port\_4** — 高度标量

高度，指定为标量，使用选定的长度单位。

**数据类型：** `double`

### **Port\_5** — 动压标量

动压，指定为标量，使用选定的压力单位。

**数据类型：** `double`

### **Port\_6** — 速度三元向量

速度，指定为三元向量，使用选定的速度单位和选定的力坐标系。

**数据类型：** `double`

### **Port\_7** — 迎角变化率标量

迎角变化率，指定为标量，单位为弧度每秒。

#### 依赖关系

当 Digital DATCOM 输入中使用 DAMP Control Card 时出现。

**数据类型：** `double`

### **Port\_8** — 机体角速率三元向量

机体角速率，指定为三元向量，单位为弧度每秒。

#### 依赖关系

当 Digital DATCOM 输入中使用 DAMP Control Card 时出现。

**数据类型：** `double`

### **Port\_9** — 地面高度标量

地面高度，指定为标量，使用选定的长度单位。

#### 依赖关系

当 Digital DATCOM 输入中使用 GRNDEF Namelist 时出现。

**数据类型：** `double`

### **Port\_10** — 操纵面偏转标量

操纵面偏转，指定为标量，单位为弧度。

#### 依赖关系

当 Digital DATCOM 输入中使用 ASYFLP 或 SYMFLP 和 GRNDEF namelist 时出现。

**数据类型：** `double`
### 输出

### **Port\_1** — 重心处的气动力三元向量

重心处的气动力，返回为三元向量，使用选定的坐标系：机体坐标系（*F*、*F*yx 和 *F*z）或风坐标系（*F*D、*F*y 和 *F*L）。

**数据类型：** `double`

### **Port\_2** — 重心处的气动力矩三元向量

重心处的气动力矩，返回为三元向量，使用机体坐标系（*M*x、*M*y 和 *M*z）。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 单位 Metric (MKS)（默认）| English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: 字符向量
  values: '''Metric (MKS)'' | ''English (Velocity in ft/s)'' | ''English (Velocity in kts)'''
  default: '''Metric (MKS)'''
- name: Digital DATCOM structure
  summary: Digital DATCOM 数据结构 factstruct{1}（默认）| 结构体
  group: ''
  block_parameter: dcase
  type: 字符向量
  values: factstruct{1} | 结构体
  default: factstruct{1}
- name: Force axes
  summary: 气动力坐标系 Body（默认）| Wind
  group: ''
  block_parameter: fmode
  type: 字符向量
  values: '''Body'' | ''Wind'''
  default: '''Body'''
- name: Interpolation method
  summary: 插值方法 None - flat（默认）| Linear
  group: ''
  block_parameter: imethod
  type: 字符向量
  values: '''None (flat)'' | ''Linear'''
  default: '''None (flat)'''
- name: Extrapolation method
  summary: 外推方法 None - clip（默认）| Linear
  group: ''
  block_parameter: emethod
  type: 字符向量
  values: '''None (flat)'' | ''Linear'''
  default: '''None (flat)'''
- name: Process out-of-range input
  summary: 处理超出范围的输入 Clip to Range（默认）| Linear Extrapolation
  group: ''
  block_parameter: rmethod
  type: 字符向量
  values: '''Clip to Range'' | ''Linear Extrapolation'''
  default: '''Clip to Range'''
- name: Action for out-of-range input
  summary: 超出范围输入的模块行为 None（默认）| Warning | Error
  group: ''
  block_parameter: action
  type: 字符向量
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
```

### **Units** — 单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为：

| 单位 | 力 | 力矩 | 长度 | 速度 | 压力 |
| --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Newton | Newton-  meter | Meters | Meters per second | Pascal |
| `English (Velocity in ft/s)` | Pound | Foot-pound | Feet | Feet per second | Pound per square inch |
| `English (Velocity in kts)` | Pound | Foot-pound | Feet | Knots | Pound per square inch |

#### 程序化使用

|  |
| --- |
| **模块参数**： `units` |
| **类型**：字符向量 |
| **值**： `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**： `'Metric (MKS)'` |

### **Digital DATCOM structure** — Digital DATCOM 数据结构 `factstruct{1}`（默认）| 结构体

包含 Digital DATCOM 数据的 MATLAB® 结构体。此结构体由 `datcomimport` 函数生成。要在生成的输出文件中包含动导数，请使用 `damp` 关键字调用 `datomimport` 函数。

有关创建 Digital DATCOM 结构体的详细信息，请参阅 Import from USAF Digital DATCOM Files。此示例展示了如何使用 Aerospace Toolbox 软件将美国空军（USAF）Digital DATCOM 文件导入 MATLAB 环境。

#### 程序化使用

|  |
| --- |
| **模块参数**： `dcase` |
| **类型**：字符向量 |
| **值**： `factstruct{1}` | 结构体 |
| **默认值**： `factstruct{1}` |

### **Force axes** — 气动力坐标系 `Body`（默认）| `Wind`

气动力坐标系，指定为 `Body` 或 `Wind`。

#### 程序化使用

|  |
| --- |
| **模块参数**： `fmode` |
| **类型**：字符向量 |
| **值**： `'Body'` | `'Wind'` |
| **默认值**： `'Body'` |

### **Interpolation method** — 插值方法 `None - flat`（默认）| `Linear`

插值方法，指定为 `None (flat)` 或 `Linear`。模块使用插值方法对 **Digital DATCOM structure** 中的静态和动态稳定性系数进行插值。

#### 程序化使用

|  |
| --- |
| **模块参数**： `imethod` |
| **类型**：字符向量 |
| **值**： `'None (flat)'` | `'Linear'` |
| **默认值**： `'None (flat)'` |

### **Extrapolation method** — 外推方法 `None - clip`（默认）| `Linear`

外推方法，指定为 `None (clip)` 或 `Linear`。模块使用外推方法对 **Digital DATCOM structure** 中的静态和动态稳定性系数进行外推。

#### 程序化使用

|  |
| --- |
| **模块参数**： `emethod` |
| **类型**：字符向量 |
| **值**： `'None (flat)'` | `'Linear'` |
| **默认值**： `'None (flat)'` |

### **Process out-of-range input** — 处理超出范围的输入 `Clip to Range`（默认）| `Linear Extrapolation`

处理超出范围输入的操作，`Linear Extrapolation` 或 `Clip to Range`。

#### 程序化使用

|  |
| --- |
| **模块参数**： `rmethod` |
| **类型**：字符向量 |
| **值**： `'Clip to Range'` | `'Linear Extrapolation'` |
| **默认值**： `'Clip to Range'` |

### **Action for out-of-range input** — 超出范围输入的模块行为 `None`（默认）| `Warning` | `Error`

超出范围输入的模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 诊断查看器中出现警告，模型仿真继续。 |
| `Error`（默认） | 诊断查看器中出现错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**： `action` |
| **类型**：字符向量 |
| **值**： `'None'` | `'Warning'` | `'Error'` |
| **默认值**： `'Warning'` |
## 所属库

Aerospace Blockset / Aerodynamics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006b 中引入**

## 描述

使用 Digital DATCOM 静态和动态稳定性导数计算气动力和气动力矩

Digital DATCOM Forces and Moments 模块使用 Digital DATCOM 中的气动系数计算重心处的气动力和气动力矩。

Digital DATCOM Forces and Moments 模块的端口标签会根据从 **Units** 列表中选择的输入和输出单位而变化。
