---
type: simulink-block
title: 'Turbofan Engine System'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Propulsion'
documentation_page: 'turbofanenginesystem'
documentation_source_path: 'turbofanenginesystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Turbofan Engine System

## 端口
```yaml
ports:
- name: Throttle position
  summary: 油门位置 标量 | 向量
  direction: input
  data_types: double
- name: Mach
  summary: 马赫数 标量
  direction: input
  data_types: double
- name: Altitude
  summary: 海拔高度 标量 | 向量
  direction: input
  data_types: double
- name: Initial thrust
  summary: 初始推力 标量 | 向量
  direction: input
  data_types: double
- name: Thrust
  summary: 推力 标量 | 向量
  direction: output
  data_types: double
- name: Fuel flow
  summary: 燃油流量 标量 | 向量
  direction: output
  data_types: double
```

### 输入

### **Throttle position** — 油门位置 标量 | 向量

油门位置，指定为标量或向量。该值可以从零变化到一，分别对应无油门和全油门。

**数据类型：** `double`

### **Mach** — 马赫数 标量

马赫数，指定为标量。

**数据类型：** `double`

### **Altitude** — 海拔高度 标量 | 向量

海拔高度，指定为标量或向量，单位由 **Units** 参数指定。

**数据类型：** `double`

### **Initial thrust** — 初始推力 标量 | 向量

初始推力，指定为标量或向量，单位由 **Units** 参数指定。

#### 依赖关系

要启用此端口，请将 **Initial thrust source** 设置为 `External`。

**数据类型：** `double`
### 输出

### **Thrust** — 推力 标量 | 向量

推力，返回为标量或向量，单位由 **Units** 参数指定。

**数据类型：** `double`

### **Fuel flow** — 燃油流量 标量 | 向量

燃油流量，返回为标量或向量，单位由 **Units** 参数指定的单位每秒。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 输入和输出单位 Metric (MKS)（默认）| English
  group: ''
  block_parameter: units
  type: 字符向量
  values: '''Metric (MKS)'' | ''English'''
  default: '''Metric (MKS)'''
- name: Initial thrust source
  summary: 初始推力来源 Internal（默认）| External
  group: ''
  block_parameter: ic_source
  type: 字符向量
  values: '''Internal'' | ''External'''
  default: '''Internal'''
- name: Initial thrust
  summary: 初始值 0（默认）| 标量
  group: ''
  block_parameter: IC
  type: 字符向量
  values: 双精度标量
  default: '''0'''
- name: Maximum sea-level static thrust
  summary: 海平面最大推力 45000（默认）| 标量
  group: ''
  block_parameter: Fmax
  type: 字符向量
  values: 双精度标量
  default: '''45000'''
- name: Fastest engine time constant at sea-level static (sec)
  summary: 海平面最快发动机时间 1（默认）| 标量
  group: ''
  block_parameter: tau
  type: 字符向量
  values: 双精度标量
  default: '''1'''
- name: Sea-level static thrust specific fuel consumption
  summary: 海平面推力比燃油消耗率 0.35（默认）| 标量
  group: ''
  block_parameter: SFC
  type: 字符向量
  values: 双精度标量
  default: '''0.35'''
- name: Ratio of installed thrust to uninstalled thrust
  summary: 表示损失的系数 0.9（默认）| 标量
  group: ''
  block_parameter: Nt
  type: 字符向量
  values: 双精度标量
  default: '''0.9'''
```

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English`

输入和输出单位，指定为：

| 单位 | 海拔高度 | 推力 | 燃油流量 |
| --- | --- | --- | --- |
| `Metric (MKS)` | 米 | 牛顿 | 千克每秒 |
| `English` | 英尺 | 磅力 | 磅质量每秒 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认值**：`'Metric (MKS)'` |

### **Initial thrust source** — 初始推力来源 `Internal`（默认）| `External`

初始推力，指定为：

|  |  |
| --- | --- |
| `Internal` | 使用 **Initial thrust** 参数的值。 |
| `External` | 使用外部输入作为初始推力值。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`ic_source` |
| **类型**：字符向量 |
| **值**：`'Internal'` | `'External'` |
| **默认值**：`'Internal'` |

### **Initial thrust** — 初始值 `0`（默认）| 标量

初始推力值，指定为双精度标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`IC` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'0'` |

### **Maximum sea-level static thrust** — 海平面最大推力 `45000`（默认）| 标量

海平面最大推力，指定为双精度标量，在马赫数为 0 时。

#### 编程使用

|  |
| --- |
| **模块参数**：`Fmax` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'45000'` |

### **Fastest engine time constant at sea-level static (sec)** — 海平面最快发动机时间 `1`（默认）| 标量

海平面最快发动机时间，指定为双精度标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`tau` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'1'` |

### **Sea-level static thrust specific fuel consumption** — 海平面推力比燃油消耗率 `0.35`（默认）| 标量

海平面推力比燃油消耗率，指定为双精度标量，单位为指定的质量单位每小时每指定的推力单位，在：

- 马赫数为 0
- 最大推力

#### 编程使用

|  |
| --- |
| **模块参数**：`SFC` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'0.35'` |

### **Ratio of installed thrust to uninstalled thrust** — 表示损失的系数 `0.9`（默认）| 标量

表示由于发动机安装导致的推力损失的系数，指定为双精度值。

#### 编程使用

|  |
| --- |
| **模块参数**：`Nt` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'0.9'` |
## 所属库

Aerospace Blockset / Propulsion

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现带控制器的涡扇发动机一阶表示

Turbofan Engine System 模块计算涡扇发动机和控制器在特定油门位置、马赫数和海拔高度下的推力和燃油质量流量。有关此系统的更多信息，请参阅算法。

Turbofan Engine System 模块图标显示从 **Units** 参数选择的输入和输出单位。
