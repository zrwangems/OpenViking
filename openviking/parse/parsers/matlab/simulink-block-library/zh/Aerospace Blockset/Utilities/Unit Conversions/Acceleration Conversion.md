---
type: simulink-block
title: 'Acceleration Conversion'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Unit Conversions'
documentation_page: 'accelerationconversion'
documentation_source_path: 'accelerationconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Acceleration Conversion

## 端口
```yaml
ports:
- name: Port_1
  summary: 加速度 标量 | 数组
  direction: input
  data_types: double
- name: Port_1
  summary: 加速度 标量 | 数组
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 加速度 标量 | 数组

加速度，指定为标量或数组，采用初始加速度单位。

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

**数据类型：** `double`
### 输出

### **Port\_1** — 加速度 标量 | 数组

加速度，以标量或数组形式返回，采用最终加速度单位。

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Initial unit
  summary: 输入单位 ft/ss（默认）| m/s2 | km/s2 | in/s2 | km/h-s | mph/s | G's
  group: ''
  block_parameter: IU
  type: 字符向量
  values: '''ft/s^s | ''m/s^2'' | ''km/s^2'' | ''in/s^2'' | ''km/h-s'' | ''mph/s'' | ''G''s'''
  default: '''ft/s2'''
- name: Final unit
  summary: 输出单位 ft/s^2'（默认）| m/s^2 | km/s^2 | in/s^2 | km/h-s | mph/s | G's
  group: ''
  block_parameter: OU
  type: 字符向量
  values: '''ft/s^2'' | ''m/s^2'' | ''km/s^2'' | ''in/s^2'' | ''km/h-s'' | ''mph/s'' | ''G''s'''
  default: '''ft/s2'''
```

### **Initial unit** — 输入单位 `ft/ss`（默认）| `m/s2` | `km/s2` | `in/s2` | `km/h-s` | `mph/s` | `G's`

输入单位，指定为：

|  |  |
| --- | --- |
| `m/s`2 | 米每二次方秒 |
| `ft/s`2 | 英尺每二次方秒 |
| `km/s`2 | 千米每二次方秒 |
| `in/s`2 | 英寸每二次方秒 |
| `km/h-s` | 千米每小时每秒 |
| `mph-s` | 英里每小时每秒 |
| `G's` | g 单位 |

#### 依赖关系

输入端口标签取决于 **Initial unit** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**：`IU` |
| **类型**：字符向量 |
| **值**：`'ft/s^s` | `'m/s^2'` | `'km/s^2'` | `'in/s^2'` | `'km/h-s'` | `'mph/s'` | `'G's'` |
| **默认值**：`'ft/s2'` |

### **Final unit** — 输出单位 `ft/s^2'`（默认）| `m/s^2` | `km/s^2` | `in/s^2` | `km/h-s` | `mph/s` | `G's`

输出单位，指定为：

|  |  |
| --- | --- |
| `m/s`2 | 米每二次方秒 |
| `ft/s`2 | 英尺每二次方秒 |
| `km/s`2 | 千米每二次方秒 |
| `in/s`2 | 英寸每二次方秒 |
| `km/h-s` | 千米每小时每秒 |
| `mph-s` | 英里每小时每秒 |
| `G's` | g 单位 |

#### 依赖关系

输出端口标签取决于 **Final unit** 设置。

#### 编程用法

|  |
| --- |
| **模块参数**：`OU` |
| **类型**：字符向量 |
| **值**：`'ft/s^2'` | `'m/s^2'` | `'km/s^2'` | `'in/s^2'` | `'km/h-s'` | `'mph/s'` | `'G's'` |
| **默认值**：`'ft/s2'` |
## 所属库

Aerospace Blockset / Utilities / Unit Conversions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

将加速度单位转换为所需的加速度单位

Acceleration Conversion 模块计算从指定的输入加速度单位到指定的输出加速度单位的转换因子，并将该转换因子应用于输入信号。

Acceleration Conversion 模块的端口标签会根据从 **Initial unit** 和 **Final unit** 参数中选择的输入和输出单位而变化。
