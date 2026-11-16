---
type: simulink-block
title: 'Ramp'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Library Routines / Math Operations'
documentation_page: 'ramp'
documentation_source_path: 'ref/ramp.html'
language: zh-CN
chinese_source: worker-translation
---

# Ramp

## 端口

### 输入

### **u** — 输入信号标量

输入信号用于生成斜坡信号，指定为标量。

**数据类型:** `single`

### **R** — 复位端口标量

用于将输出信号复位到初始条件的选项，指定为标量。

#### 依赖项

要启用此端口，请选中 **显示复位端口** 参数。

**数据类型:** `Boolean`

### **rs** — 上升斜率标量

输出信号增大的速率，指定为标量。

#### 依赖项

要启用此端口，请将 **上升斜率** 参数的 **源** 字段设置为 `Input port`。

**数据类型:** `single`

### **fs** — 下降斜率标量

输出信号减小的速率，指定为标量。

#### 依赖项

要启用此端口，请将 **下降斜率** 参数的 **源** 字段设置为 `Input port`。

**数据类型:** `single`
### 输出

### **Port\_1** — 输出信号标量

输出信号，以标量形式返回。

**数据类型:** `single`

## 参数

### **上升斜率** — 输出增大的值 `Dialog` | `Input port`

将此参数的 **源** 字段指定为以下值之一。

- `Dialog` — 使用此参数的 **值** 字段设置斜率。
- `Input port` — 使用 **rs** 端口设置斜率。模块使用来自此端口的值作为斜率。

#### 编程使用

|  |
| --- |
| **模块参数:** `RiseSlope` |
| **类型:** character vector |
| **值:** 实数有限非负值 |
| **默认值:** `'1'` |

#### 编程使用

|  |
| --- |
| **模块参数:** `RiseSlopeSource` |
| **类型:** character vector |
| **值:** `'Dialog' | 'Input port'` |
| **默认值:** `'Dialog'` |

### **下降斜率** — 输出标量的减小值

将此参数的 **源** 字段指定为以下值之一。

- `Dialog` — 使用此参数的 **值** 字段设置斜率。
- `Input port` — 使用 **fs** 端口设置斜率。模块使用来自此端口的值作为斜率。

#### 编程使用

|  |
| --- |
| **模块参数:** `FallSlope` |
| **类型:** character vector |
| **值:** 实数有限非负值 |
| **默认值:** `'1'` |

#### 编程使用

|  |
| --- |
| **模块参数:** `FallSlopeSource` |
| **类型:** character vector |
| **值:** `'Dialog' | 'Input Port'` |
| **默认值:** `'Dialog'` |

### **显示复位端口** — 添加 `R` 输入端口的选项 `'off'`（默认）| `'on'`

启用 **R** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数:** `ShowResetPort` |
| **类型:** character vector |
| **值:** `'off' | 'on'` |
| **默认值:** `'off'` |

### **初始条件** — 输出信号的初始值 `0`（默认）| double

输出信号的初始条件，指定为 double。默认值为 `0`。

当选中 **显示复位端口** 时，初始条件设置为 **初始条件** 参数中指定的值。

#### 编程使用

|  |
| --- |
| **模块参数:** `InitialCondition` |
| **类型:** character vector |
| **值:** 实数有限值 |
| **默认值:** `'0'` |

### **采样时间** — 采样周期 `-1`（默认）| `[-1, 0]` | 向量

以秒为单位指定采样周期。

有关指定离散采样时间的详细信息，请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数:** `SampleTime` |
| **类型:** character vector |
| **值:** 实数有限值 |
| **默认值:** `'-1'` |

## 所属库

AUTOSAR Blockset / Classic Platform / Library Routines / Math Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2025a: AUTOSAR 代码替换库支持 Release 4.0 之后的架构

从 25a 开始，AUTOSAR 代码替换库支持 AUTOSAR 4.0 之后的 AUTOSAR 架构版本。要使用最新的 AUTOSAR 例程，请在模型配置参数对话框的 **代码生成** > **接口** 窗格中，将 **代码替换库** 指定为 `AUTOSAR 4.x`。

## 描述

生成遵循由上升或下降斜率约束的输入值的信号

Mathematical Floating point Library (MFL) Ramp 模块生成一个信号，该信号从指定值开始，并按指定速率变化，直到达到输入信号的值。模块参数 **上升斜率**、**下降斜率**、**初始条件** 和 **采样时间**，以及输入信号 **u** 决定输出信号的特征。

当您为 AUTOSAR 模型选择 `AUTOSAR 4.x` 代码替换库 (CRL) 时，模型会将为此模块生成的代码替换为对以下 AUTOSAR 库例程的调用：

- `Mfl_Ramp_InitState`
- `Mfl_Ramp_SetParam`
- `Mfl_RampCalc`
- `Mfl_RampOut_f32`
