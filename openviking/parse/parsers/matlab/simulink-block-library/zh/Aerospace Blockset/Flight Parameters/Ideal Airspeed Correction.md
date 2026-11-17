---
type: simulink-block
title: 'Ideal Airspeed Correction'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'idealairspeedcorrection'
documentation_source_path: 'idealairspeedcorrection.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Airspeed Correction

## 端口
```yaml
ports:
- name: TAS
  summary: 真实输入空速标量
  direction: input
  data_types: double
- name: EAS
  summary: 等效输入空速标量
  direction: input
  data_types: double
- name: CAS
  summary: 校准输入空速标量
  direction: input
  data_types: double
- name: a
  summary: 声速标量
  direction: input
  data_types: double
- name: P0
  summary: 静压标量
  direction: input
  data_types: double
- name: EAS
  summary: 等效输出空速标量
  direction: output
  data_types: double
- name: CAS
  summary: 校准输出空速标量
  direction: output
  data_types: double
- name: TAS
  summary: 真实输出空速标量
  direction: output
  data_types: double
```

### 输入

### **TAS** — 真实输入空速标量

真实输入空速，指定为标量，单位由 **Units** 参数指定。

#### 依赖关系

要启用此端口，请将 **Airspeed input** 设置为 `TAS`。

**数据类型：** `double`

### **EAS** — 等效输入空速标量

等效输入空速，指定为标量，单位由 **Units** 参数指定。

#### 依赖关系

要启用此端口，请将 **Airspeed input** 设置为 `EAS`。

**数据类型：** `double`

### **CAS** — 校准输入空速标量

校准输入空速，指定为标量，单位由 **Units** 参数指定。

#### 依赖关系

要启用此端口，请将 **Airspeed input** 设置为 `EAS`。

**数据类型：** `double`

### **a** — 声速标量

声速，指定为标量，单位由 **Units** 参数指定。

**数据类型：** `double`

### **P0** — 静压标量

静压，指定为标量，单位由 **Units** 参数指定。

**数据类型：** `double`
### 输出

### **EAS** — 等效输出空速标量

等效输出空速，以标量形式返回，单位由 **Units** 参数指定。

#### 依赖关系

要启用此端口，请将 **Airspeed input** 设置为 `TAS` 或 `CAS`，并将 **Airspeed output** 设置为 `EAS`。

**数据类型：** `double`

### **CAS** — 校准输出空速标量

校准输出空速，以标量形式返回，单位由 **Units** 参数指定。

#### 依赖关系

要启用此端口，请将 **Airspeed input** 设置为 `TAS` 或 `EAS`，并将 **Airspeed output** 设置为 `CAS`。

**数据类型：** `double`

### **TAS** — 真实输出空速标量

真实输出空速，以标量形式返回，单位由 **Units** 参数指定。

#### 依赖关系

要启用此端口，请将 **Airspeed input** 设置为 `CAS` 或 `EAS`，并将 **Airspeed output** 设置为 `TAS`。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 单位 Metric (MKS)（默认）| English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: 字符向量
  values: '''Metric (MKS)'' | ''English'''
  default: '''Metric (MKS)'''
- name: Airspeed input
  summary: 空速输入类型 TAS（默认）| EAS | CAS
  group: ''
  block_parameter: vel_in
  type: 字符向量
  values: '''TAS'' | ''EAS'' | ''CAS'''
  default: '''TAS'''
- name: Airspeed output
  summary: 空速输出类型 EAS（默认）| CAS | TAS
  group: ''
  block_parameter: vel_out_tas、vel_out_cas、vel_out_eas，取决于输入速度类型 vel_in。有关详细信息，请参阅空速输出类型表。
  type: 字符向量
  values: '''EAS'' | ''CAS''''TAS'''
  default: '''EAS'''
- name: Method
  summary: 计算转换因子的方法 Table Lookup（默认）| Equation
  group: ''
  block_parameter: method
  type: 字符向量
  values: '''Table Lookup'' | ''Equation'''
  default: '''Table Lookup'''
- name: Subsonic airspeeds only
  summary: 用于亚音速空速 off（默认）| on
  group: ''
  block_parameter: SubOnly
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Action for out-of-range input
  summary: 超出范围输入时的模块行为 None（默认）| Warning | Error
  group: ''
  block_parameter: action
  type: 字符向量
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''None'''
```

### **Units** — 单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为：

| 单位 | 空速输入 | 声速 | 气压 | 空速输出 |
| --- | --- | --- | --- | --- |
| `Metric (MKS)` | 米每秒 | 米每秒 | 帕斯卡 | 米每秒 |
| `English (Velocity in ft/s)` | 英尺每秒 | 英尺每秒 | 磅力每平方英寸 | 英尺每秒 |
| `English (Velocity in kts)` | 节 | 节 | 磅力每平方英寸 | 节 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认值**：`'Metric (MKS)'` |

### **Airspeed input** — 空速输入类型 `TAS`（默认）| `EAS` | `CAS`

空速输入类型，指定为：

|  |  |
| --- | --- |
| `TAS` | 真实空速 |
| `EAS` | 等效空速 |
| `CAS` | 校准空速 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`vel_in` |
| **类型**：字符向量 |
| **值**：`'TAS'` | `'EAS'` | `'CAS'` |
| **默认值**：`'TAS'` |

### **Airspeed output** — 空速输出类型 `EAS`（默认）| `CAS` | `TAS`

空速输出类型，指定为：

| 空速输入 | 空速输出 |
| --- | --- |
| `TAS` | EAS（等效空速） |
| CAS（校准空速） |
| `EAS` | TAS（真实空速） |
| CAS（校准空速） |
| `CAS` | TAS（真实空速） |
| EAS（等效空速） |

#### 程序化使用

|  |
| --- |
| **模块参数**：`vel_out_tas`、`vel_out_cas`、`vel_out_eas`，取决于输入速度类型 `vel_in`。有关详细信息，请参阅空速输出类型表。 |
| **类型**：字符向量 |
| **值**：`'EAS'` | `'CAS'``'TAS'` |
| **默认值**：`'EAS'` |

### **Method** — 计算转换因子的方法 `Table Lookup`（默认）| `Equation`

计算转换因子的方法，指定为：

|  |  |
| --- | --- |
| `Table Lookup` | （默认）根据模块输入查找或估算表值来生成输出空速。如果选中 **Subsonic airspeeds only** 复选框，Ideal Airspeed Correction 模块生成的代码包含亚音速（Mach < 1）查找表数据。如果清除 **Subsonic airspeeds only** 复选框，Ideal Airspeed Correction 模块生成的代码包含所有（Mach < 5）查找表数据。超过 Mach 5 时，模块使用 `equation` 方法。在以下任一情况下不建议使用 `Table Lookup` 方法：- 声速小于 200 m/s 或大于 350 m/s。- 静压小于 1000 Pa 或大于 106,500 Pa。在这些情况下使用 `Table Lookup` 方法会导致不准确。 |
| `Equation` | 直接使用模块输入值计算输出空速。涉及超音速空速（大于 Mach 1）的计算需要迭代计算。如果函数在 30 次迭代内未找到解，则显示错误消息。模块生成的代码中不包含查找表数据。 |

Ideal Airspeed Correction 模块在以下任一情况下自动使用 `Equation` 方法：

- **Airspeed input** 设置为 `TAS` 且 **Airspeed output** 设置为 `EAS` 的转换。
- **Airspeed input** 设置为 `EAS` 且 **Airspeed output** 设置为 `TAS` 的转换。
- 模块输入空速大于海平面声速的五倍（约 1700 m/s）时的转换。

#### 程序化使用

|  |
| --- |
| **模块参数**：`method` |
| **类型**：字符向量 |
| **值**：`'Table Lookup'` | `'Equation'` |
| **默认值**：`'Table Lookup'` |

### **Subsonic airspeeds only** — 用于亚音速空速 `off`（默认）| `on`

选中此复选框可仅将此模块用于亚音速空速（空速小于 Mach 1）应用。选中此复选框可提高性能。

模块生成代码的方式如下：

- 如果选中此复选框，当 **Method** 设置为 `Table Lookup` 时，Ideal Airspeed Correction 模块生成的代码包含亚音速（Mach < 1）查找表数据。

  选中此复选框会显示 **Action for out-of-range input** 参数。
- 如果清除此复选框，当 **Method** 设置为 `Table Lookup` 时，Ideal Airspeed Correction 模块生成的代码包含所有（Mach < 5）查找表数据。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SubOnly` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Action for out-of-range input** — 超出范围输入时的模块行为 None（默认）| `Warning` | `Error`

超出范围输入时的模块行为，即空速大于 Mach 1 时，指定如下。

| 值 | 描述 |
| --- | --- |
| `None` | 不显示警告或错误。 |
| `Warning` | 显示警告并指示空速大于 Mach 1。 |
| `Error` | 显示错误并指示空速大于 Mach 1。 |

#### 依赖关系

仅当选中 **Subsonic airspeeds only** 复选框时，此参数才启用。

#### 程序化使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'None'` |
## 所属库

Aerospace Blockset / Flight Parameters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算等效空速 (EAS)、校准空速 (CAS) 或真实空速 (TAS) 之间的相互转换

Ideal Airspeed Correction 模块从以下其他两种空速之一计算其中一种空速：

- 等效空速 (EAS)
- 校准空速 (CAS)
- 真实空速 (TAS)
