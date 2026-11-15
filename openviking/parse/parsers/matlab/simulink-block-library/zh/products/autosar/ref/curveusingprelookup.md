---
type: simulink-block
title: 'Curve Using Prelookup'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Component Modeling / Component Development / AUTOSAR Calibration and Measurement Data'
documentation_page: 'curveusingprelookup'
documentation_source_path: 'ref/curveusingprelookup.html'
language: zh-CN
chinese_source: worker-translation
---

# Curve Using Prelookup

## 端口

### 输入

### **kf1** — 包含索引 `k` 和小数 `f` 的输入 `Ifx_DPResultU16_Type` | `Ifl_DPResultF32_Type`

**kf1** 端口的输入包含索引 `k` 和小数 `f`，指定为 `Ifx_DPResultU16_Type` 或 `Ifl_DPResultF32_Type`。

当 `目标例程库` 设置为 `IFX (fixed-point)` 时，端口设置为数据类型 `Ifx_DPResultU16_Type`。

当 `目标例程库` 设置为 `IFL (floating-point)` 时，端口设置为数据类型 `Ifl_DPResultF32_Type`。

### 输出

### **Port 1** — 一维函数的近似值 `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

一维函数的近似值，通过插值表数据计算，使用输入索引 `k` 和小数 `f` 的值。

当 `目标例程库` 设置为 `IFL (floating-point)` 时，唯一有效的数据类型是 `single`。

当 `目标例程库` 设置为 `IFX (fixed-point)` 时，`Port 1` 的值可以是以下数据类型之一：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 和定点数据类型。

**数据类型:** `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `fixed point`

## 参数

### **目标例程库** — 指示用于模块代码替换的 AUTOSAR 例程库 `IFX (fixed-point)` | `IFL (floating-point)`

如果为模型选择 AUTOSAR 4.x 代码替换库 (CRL)，则此模块生成的代码将从选定的 AUTOSAR 例程库进行替换。此参数使您可以选择定点 (IFX) 或浮点 (IFL) 代码替换和验证检查。

### **目标例程** — 用于代码替换的 AUTOSAR 库例程 `Ifx_IpoCur` | `Ifl_IpoCur`

此参数反映用于替换此模块所生成代码的 AUTOSAR 代码替换库 (CRL) 例程的名称。命名约定包括目标例程库、插值方法和模块类型。此参数仅供参考，不得编辑。

当 `目标例程库` 设置为 `IFX (fixed-point)` 时，值默认为 `Ifx_IpoCur`。

当 `目标例程库` 设置为 `IFL (floating-point)` 时，值默认为 `Ifl_IpoCur`。

### 表规格

### **数据规格** — 选择如何输入表数据 `Explicit values` (default) | `Lookup table object`

指定是直接输入表数据还是使用查找表对象。如果将此参数设置为：

- `Explicit values`，则对话框中将显示 **表数据** 参数和 **数据类型** 选项卡。
- `Lookup table object`，则对话框中将显示 **名称** 参数。

#### 编程使用

|  |
| --- |
| **模块参数:** `TableSpecification` |
| **类型:** character vector | string |
| **值:** `"Explicit values" | "Lookup table object"` |
| **默认值:** `"Explicit values"` |

### **名称** — `Simulink.LookupTable` 对象的名称 `Simulink.LookupTable` object

指定 `Simulink.LookupTable` 对象的名称。查找表对象引用 Simulink® 断点对象。如果 `Simulink.LookupTable` 对象不存在，请单击操作按钮  并选择 **创建**。新查找表对象的对应参数将用模块信息填充。

#### 依赖关系

要启用此参数，请将 **数据规格** 设置为 `Lookup table object`。

#### 编程使用

|  |
| --- |
| **模块参数:** `LookupTableObject` |
| **类型:** character vector |
| **值:** `Simulink.LookupTable` object |
| **默认值:** `'[]'` |

### **表数据** — 定义输出值的表 `[1 2 4]` (default) | character vector

输入输出值的表。

在仿真期间，矩阵大小必须是一维的。但是，在模块图编辑期间，您可以输入空矩阵（指定为 `[]`）或未定义的工作区变量。此方法允许您推迟为表数据指定大小正确的矩阵，并继续编辑模块图。

#### 依赖关系

要启用此参数，请将 **数据规格** 设置为 `Explicit values`。

#### 编程使用

|  |
| --- |
| **模块参数:** `Table` |
| **类型:** character vector |
| **值:** matrix of table values |
| **默认值:** `'[1 2 4]'` |

### **编辑表和断点** — 启动查找表编辑器对话框按钮

单击此按钮以打开查找表编辑器。

对于查找表对象，单击此按钮可让您编辑该对象并保存该对象的新值。

### 算法

### **插值方法** — 选择 `Linear point-slope` 或 `Flat` 插值方法 `Linear point-slope` (default) | `Flat`

指定模块用于插值表数据的方法。您可以选择 `Linear point-slope` 或 `Flat`。有关详细信息，请参阅插值方法。

#### 编程使用

|  |
| --- |
| **模块参数:** `InterpMode` |
| **类型:** character vector | string |
| **值:** `"Flat" | "Linear point-slope"` |
| **默认值:** `"Linear point-slope"` |

### **整数舍入模式** — 定点或浮点运算的舍入模式 `Zero` (default) | `Round`

指定在仿真期间或执行模型生成代码期间发生的定点或浮点查找表计算的舍入模式。

此选项不影响模块参数值的舍入。Simulink 会将此类值舍入到最接近的可表示整数值。

#### 依赖关系

仅当将其设置为 `Round` 时，此参数才可见。AUTOSAR 4.x 和用于 SIL 测试的主机库不支持整数舍入，并且默认情况下该参数处于隐藏状态。要启用 SIL 工作流，请将此设置更改为 `Zero`。

#### 编程使用

|  |
| --- |
| **模块参数:** `RndMode` |
| **类型:** character vector | string |
| **值:** `"Round" | "Zero"` |
| **默认值:** `"Zero"` |

### 数据类型

### **表数据** — 表数据的数据类型 `Inherit: Same as output` (default) | `Inherit: Inherit from 'Table data'` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

要启用此选项卡，请在 **表规格** 选项卡上，将 **数据规格** 设置为 `Explicit values`。

指定表数据类型。模块会验证所选类型是否与目标例程的规格兼容。

当 `目标例程库` 设置为 `IFL (floating-point)` 时，唯一有效的数据类型是 `single`。

当 `目标例程库` 设置为 `IFX (fixed-point)` 时，可以将数据类型设置为：

- 继承数据类型的规则：`Inherit: Same as output`、`Inherit: Inherit from 'Table data'`。
- 以下内置数据类型之一：`int8`、`uint8`、`int16`、`uint16`、`int32` 和 `uint32`。
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象。
- 计算结果为数据类型的表达式。例如，软件提供以下常见定点数据类型表达式：`fixdt(1,16)`、`fixdt(1,16,0)` 或 `fixdt(1,16,2^0,0)`。

单击 **显示数据类型助手** 按钮  以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型。

**提示**

对于以下情况，请指定与输出数据类型不同的表数据类型：

- 存储表数据的内存需求较低，因为使用的类型比输出信号小
- 在两个具有不同输出数据类型的 Curve 模块之间共享预缩放的表数据
- 在生成的代码中为具有不同输出数据类型的模块共享自定义存储表数据

#### 编程使用

|  |
| --- |
| **模块参数:** `TableDataTypeStr` |
| **类型:** character vector | string |
| **值:** `"Inherit: Inherit from 'Table data'" | "Inherit: Same as output" | "single" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "fixdt(1,16)" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"` |
| **默认值:** `"Inherit: Same as output"` |

## 所属库

AUTOSAR Blockset / Classic Platform / Library Routines / Interpolation

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2025a: 整数舍入模式处于隐藏状态

**整数舍入模式** 设置为 `"Zero"` 并且默认隐藏，因为 AUTOSAR 4.x 和用于 SIL 测试的主机库仅支持 `"Zero"`。

### R2025a: AUTOSAR 代码替换库支持 Release 4.0 之后的模式

从 25a 开始，AUTOSAR 代码替换库支持 AUTOSAR 4.0 之后的 AUTOSAR 模式版本。要使用最新的 AUTOSAR 例程，请在模型配置参数对话框的 **代码生成** > **接口** 窗格中，将 **代码替换库** 指定为 `AUTOSAR 4.x`。

## 描述

使用先前计算的索引和小数值来加速一维函数的近似

Curve Using Prelookup 模块旨在与 Prelookup 模块一起使用。此模块使预查找结果能够驱动多个插值结果。

Prelookup 模块计算索引和区间小数，这些值指定其输入值 `u` 与断点数据集的关系，并将得到的索引和小数值馈入 Curve Using Prelookup 模块以插值一维表。

Prelookup 和 Curve Using Prelookup 模块具有分布式算法，当一起使用时，它们执行与 Curve 模块相同的算法操作。通过一起使用 Prelookup 和 Curve Using Prelookup 模块，与仅使用 Curve 模块相比，您可以获得更大的灵活性以及更高效的仿真和代码生成。

如果为 AUTOSAR 模型选择 AUTOSAR 4.x 代码替换库 (CRL)，则此模块生成的代码将替换为在模块参数对话框中配置的 AUTOSAR 库例程。
