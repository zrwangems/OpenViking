---
type: simulink-block
title: 'Unit System Configuration'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'unitsystemconfiguration'
documentation_source_path: 'slref/unitsystemconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Unit System Configuration

## 端口

R2025b 中未记录。

## 参数

### **Disallowed unit systems** — 不允许的单位制 `SI` | `English` | `SI (extended)` | `CGS`

显示不允许的单位制列表。默认情况下，**Allow all unit systems** 复选框处于选中状态，所有单位制均被允许。

要将某个单位制指定为不允许，请在 **Allowed unit systems** 列中选中它，然后单击 **<< Disallow**。

#### 依赖关系

要启用对此参数的更改，必须先清除 **Allow all unit systems** 复选框。

### **Allowed unit systems** — 允许的单位制 `SI` | `English` | `SI (extended)` | `CGS`

显示允许的单位制列表。默认情况下，**Allow all unit systems** 复选框处于选中状态，所有单位制均被允许。

要将某个单位制指定为允许，请使用 **Allow >>** 和 **<< Disallow** 按钮在 **Disallowed unit systems** 和 **Allowed unit systems** 列之间移动单位制。

#### 依赖关系

要启用对此参数的更改，必须先清除 **Allow all unit systems** 复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `UnitSystems` |
| **类型：** 字符向量元胞数组 |
| **值：** 以下字符向量的元胞数组：`'SI'` | `'English'` | `'SI (extended)'` | `'CGS'` |
| **默认值：** `{'SI', 'English', 'SI (extended)', 'CGS'}` |

### **Allow all unit systems** — 允许所有单位制 `on`（默认）| `off`

选中此复选框时，允许所有单位制。要将允许的单位制限制为仅在 **Allowed unit systems** 列中指定的单位制，请清除此复选框。

#### 依赖关系

选中 **Allow all unit systems** 复选框会禁用 **Disallowed unit systems** 和 **Allowed unit systems** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `AllowAllUnitSystems` |
| **类型：** 字符向量 |
| **值：** `'on' | 'off'` |
| **默认值：** `'on'` |

## 所属库

Simulink / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2016a 中引入**

## 描述

将单位限制为指定的允许单位制

Unit System Configuration 模块指定组件的允许和不允许单位制。它限制子系统或顶层模型及其所有子级的单位制，除非在子级中用另一个 Unit System Configuration 模块覆盖。

此模块支持普通、加速和快速加速模式以及快速重启。
