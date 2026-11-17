---
type: simulink-block
title: 'Velocity Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'velocityconversion'
documentation_source_path: 'velocityconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Velocity Conversion

## 端口
```yaml
ports:
- name: Port_1
  summary: 速度 标量 | 数组
  direction: input
  data_types: double
- name: Port_1
  summary: 速度 标量 | 数组
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 速度 标量 | 数组

速度，指定为标量或数组，以初始速度单位表示。

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — 速度 标量 | 数组

速度，以最终速度单位返回为标量或数组。

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Initial unit
  summary: 输入单位 ft/s（默认）| m/s | km/s | in/s | km/h | mph | kts | ft/min
  group: ''
  block_parameter: IU
  type: character vector
  values: '''m/s'' | ''ft/s'' | ''km/s'' | ''in/s'' | ''km/h'' | ''mph'' | ''kts'' | ''ft/min'''
  default: '''ft/s'''
- name: Final unit
  summary: 输出单位 m/s（默认）| ft/s | km/s | in/s | km/h | mph | kts | ft/min
  group: ''
  block_parameter: OU
  type: character vector
  values: '''m/s'' | ''ft/s'' | ''km/s'' | ''in/s'' | ''km/h'' | ''mph'' | ''kts'' | ''ft/min'''
  default: '''m/s'''
```

### **Initial unit** — 输入单位 `ft/s`（默认）| `m/s` | `km/s` | `in/s` | `km/h` | `mph` | `kts` | `ft/min`

输入单位，指定为：

|  |  |
| --- | --- |
| `m/s` | 米每秒 |
| `ft/s` | 英尺每秒 |
| `km/s` | 千米每秒 |
| `in/s` | 英寸每秒 |
| `km/h` | 千米每小时 |
| `mph` | 英里每小时 |
| `kts` | 海里每小时 |
| `ft/min` | 英尺每分钟 |

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

#### 编程使用

|  |
| --- |
| **模块参数**：`IU` |
| **类型**：character vector |
| **值**：`'m/s'` | `'ft/s'` | `'km/s'` | `'in/s'` | `'km/h'` | `'mph'` | `'kts'` | `'ft/min'` |
| **默认值**：`'ft/s'` |

### **Final unit** — 输出单位 `m/s`（默认）| `ft/s` | `km/s` | `in/s` | `km/h` | `mph` | `kts` | `ft/min`

输出单位，指定为：

|  |  |
| --- | --- |
| `m/s` | 米每秒 |
| `ft/s` | 英尺每秒 |
| `km/s` | 千米每秒 |
| `in/s` | 英寸每秒 |
| `km/h` | 千米每小时 |
| `mph` | 英里每小时 |
| `kts` | 海里每小时 |
| `ft/min` | 英尺每分钟 |

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

#### 编程使用

|  |
| --- |
| **模块参数**：`OU` |
| **类型**：character vector |
| **值**：`'m/s'` | `'ft/s'` | `'km/s'` | `'in/s'` | `'km/h'` | `'mph'` | `'kts'` | `'ft/min'` |
| **默认值**：`'m/s'` |
## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

从速度单位转换为所需的速度单位

Velocity Conversion 模块计算从指定的输入速度单位到指定的输出速度单位的转换因子，并将该转换因子应用于输入信号。

Velocity Conversion 模块的端口标签根据从 **Initial unit** 和 **Final unit** 列表中选择的输入和输出单位而变化。
