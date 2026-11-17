---
type: simulink-block
title: 'Turbofan Engine System'
family: 'propulsion'
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

### 输入

### **Throttle position** — Throttle position 标量 | 向量

Throttle position，指定为标量或向量。此值可在零到一之间变化，分别对应无油门和全油门。

**数据类型：** `double`

### **Mach** — 马赫数标量

马赫数，指定为标量。

**数据类型：** `double`

### **Altitude** — Altitude 标量 | 向量

Altitude，指定为标量或向量，采用 **Units** 参数中指定的单位。

**数据类型：** `double`

### **Initial thrust** — Initial thrust 标量 | 向量

Initial thrust，指定为标量或向量，采用 **Units** 参数中指定的单位。

#### 依赖关系

要启用此端口，请将 **Initial thrust source** 设置为 `External`。

**数据类型：** `double`

### 输出

### **Thrust** — Thrust 标量 | 向量

Thrust，返回为标量或向量，采用 **Units** 参数中指定的单位。

**数据类型：** `double`

### **Fuel flow** — Fuel flow 标量 | 向量

Fuel flow，返回为标量或向量，采用 **Units** 参数中指定的单位每秒。

**数据类型：** `double`

## 参数

### **Units** — 输入和输出单位 `Metric (MKS)`（默认） | `English`

输入和输出单位，指定为：

| Units | Altitude | Thrust | Fuel Flow |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Newtons | Kilograms per second |
| `English` | Feet | Pound force | Pound mass per second |

#### 程序化使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English'` |
| **默认值**: `'Metric (MKS)'` |

### **Initial thrust source** — 初始推力源 `Internal`（默认） | `External`

Initial thrust，指定为：

|  |  |
| --- | --- |
| `Internal` | 使用 **Initial thrust** 参数的值。 |
| `External` | 使用外部输入作为初始推力值。 |

#### 程序化使用

|  |
| --- |
| **模块参数**: `ic_source` |
| **类型**: character vector |
| **值**: `'Internal'` | `'External'` |
| **默认值**: `'Internal'` |

### **Initial thrust** — 初始 `0`（默认） | 标量

初始推力值，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `IC` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'0'` |

### **Maximum sea-level static thrust** — 海平面最大推力 `45000`（默认） | 标量

海平面最大推力，指定为 double 标量，在 Mach 值为 0 时。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Fmax` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'45000'` |

### **Fastest engine time constant at sea-level static (sec)** — 海平面最快发动机时间 `1`（默认） | 标量

海平面最快发动机时间，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `tau` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'1'` |

### **Sea-level static thrust specific fuel consumption** — 海平面推力比油耗 `0.35`（默认） | 标量

海平面推力比油耗，指定为 double 标量，以指定的质量单位每小时每指定的推力单位表示，在以下条件下：

- Mach 值为 0
- 最大推力

#### 程序化使用

|  |
| --- |
| **模块参数**: `SFC` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'0.35'` |

### **Ratio of installed thrust to uninstalled thrust** — 表示损失的系数 `0.9`（默认） | 标量

表示因发动机安装导致的推力损失的系数，指定为 double 值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Nt` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'0.9'` |

## 所属库

Aerospace Blockset / Propulsion

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现带控制器的涡扇发动机的一阶表示

Turbofan Engine System 模块在特定油门位置、马赫数和高度下，计算涡扇发动机及控制器的推力和燃油质量流量。有关此系统的详细信息，请参阅算法。

Turbofan Engine System 模块图标显示从 **Units** 参数中选择的输入和输出单位。
