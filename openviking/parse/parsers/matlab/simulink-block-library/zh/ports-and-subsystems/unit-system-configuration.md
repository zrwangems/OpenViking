---
type: simulink-block
title: 'Unit System Configuration'
family: ports-and-subsystems
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'unitsystemconfiguration'
language: zh-CN
chinese_source: worker-translation
---

# Unit System Configuration



将单位限制为指定的允许单位系统

## 库

Simulink / Ports & Subsystems

## 说明

Unit System Configuration 模块为组件指定允许和不允许的单位系统。它限制某个子系统或顶层模型及其所有子级的单位系统，除非在子级中用另一个 Unit System Configuration 模块覆盖它。

此模块支持普通、加速和快速加速模式以及快速重启。

## 参数

### **不允许的单位系统** — 不允许的单位系统 `SI` | `English` | `SI (extended)` | `CGS`

显示不允许的单位系统列表。默认情况下，**允许所有单位系统** 复选框处于选中状态，并且允许所有单位系统。

要将某个单位系统指定为不允许，请在 **允许的单位系统** 列中选择它，然后单击 **<< 不允许**。

#### 依赖关系

要启用对此参数的更改，必须先清除 **允许所有单位系统** 复选框。

### **允许的单位系统** — 允许的单位系统 `SI` | `English` | `SI (extended)` | `CGS`

显示允许的单位系统列表。默认情况下，**允许所有单位系统** 复选框处于选中状态，并且允许所有单位系统。

要将某个单位系统指定为允许，请使用 **允许 >>** 和 **<< 不允许** 按钮在 **不允许的单位系统** 和 **允许的单位系统** 列之间移动单位系统。

#### 依赖关系

要启用对此参数的更改，必须先清除 **允许所有单位系统** 复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `UnitSystems` |
| **类型：** 字符向量元胞数组 |
| **值：** 以下字符向量的元胞数组：`'SI'` | `'English'` | `'SI (extended)'` | `'CGS'` |
| **默认：** `{'SI', 'English', 'SI (extended)', 'CGS'}` |

### **允许所有单位系统** — 允许所有单位系统 `on`（默认） | `off`

选中此复选框时，允许所有单位系统。要将允许的单位系统限制为仅在 **允许的单位系统** 列中指定的那些单位系统，请清除此复选框。

#### 依赖关系

选中 **允许所有单位系统** 复选框会禁用 **不允许的单位系统** 和 **允许的单位系统** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `AllowAllUnitSystems` |
| **类型：** 字符向量 |
| **值：** `'on' | 'off'` |
| **默认：** `'on'` |

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
