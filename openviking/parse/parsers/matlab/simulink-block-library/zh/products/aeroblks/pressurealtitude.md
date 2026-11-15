---
type: simulink-block
title: 'Pressure Altitude'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Atmosphere'
documentation_page: 'pressurealtitude'
documentation_source_path: 'pressurealtitude.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Altitude

## 端口

### 输入

### **Port\_1** — 静压标量 | 数组

静压，指定为标量或数组。

**数据类型：** `double`

### 输出

### **Port\_1** — 气压高度标量 | 数组

气压高度，返回为标量或向量。

**数据类型：** `double`

## 参数

### **Units** — 输入单位 `Metric (MKS)` (default) | `English`

输入单位，指定为：

| Units | Pstatic | Alt\_p |
| --- | --- | --- |
| `Metric (MKS)` | Pascal | Meters |
| `English` | Pound force per square inch | Feet |

#### 程序化使用

|  |
| --- |
| **模块参数**： `units` |
| **类型**： character vector |
| **值**： `'Metric (MKS)'` | `'English'` |
| **默认值**： `'Metric (MKS)'` |

### **Action for out-of-range input** — 超出范围模块行为 `None` (default) | `Warning` | `Error`

超出范围模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | Diagnostic Viewer 中显示警告，模型仿真继续。 |
| `Error` (default) | Diagnostic Viewer 中显示错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**： `action` |
| **类型**： character vector |
| **值**： `'None'` | `'Warning'` | `'Error'` |
| **默认值**： `'Warning'` |

## 所属库

Aerospace Blockset / Environment / Atmosphere

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

基于环境压力计算气压高度

Pressure Altitude 模块基于环境压力计算气压高度。气压高度是在 1976 年美国标准大气扩展委员会 (COESA) 标准大气中具有指定环境压力的高度。

气压高度也称为平均海平面 (MSL) 高度。

Pressure Altitude 模块图标端口标签会根据从 **Units** 列表中选择的输入和输出单位而变化。
