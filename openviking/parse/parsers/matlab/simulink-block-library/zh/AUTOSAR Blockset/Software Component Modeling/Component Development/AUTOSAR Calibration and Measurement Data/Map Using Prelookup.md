---
type: simulink-block
title: 'Map Using Prelookup'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Component Modeling / Component Development / AUTOSAR Calibration and Measurement Data'
documentation_page: 'mapusingprelookup'
documentation_source_path: 'ref/mapusingprelookup.html'
language: zh-CN
chinese_source: worker-translation
---

# Map Using Prelookup

## 端口

### 输入

### **kf1** — 包含索引 `k` 和小数 `f` 的输入 `Ifx_DPResultU16_Type` | `Ifl_DPResultF32_Type`

**kf1** 端口的输入包含索引 `k` 和小数 `f`，指定为 `Ifx_DPResultU16_Type` 或 `Ifl_DPResultF32_Type`。

当 `Targeted Routine Library` 设置为 `IFX (fixed-point)` 时，该端口设置为数据类型 `Ifx_DPResultU16_Type`。

当 `Targeted Routine Library` 设置为 `IFL (floating-point)` 时，该端口设置为数据类型 `Ifl_DPResultF32_Type`。

### **kf2** — 包含索引 `k` 和小数 `f` 的输入 `Ifx_DPResultU16_Type` | `Ifl_DPResultF32_Type`

**kf2** 端口的输入包含索引 `k` 和小数 `f`，指定为 `Ifx_DPResultU16_Type` 或 `Ifl_DPResultF32_Type`。

当 `Targeted Routine Library` 设置为 `IFX (fixed-point)` 时，该端口设置为数据类型 `Ifx_DPResultU16_Type`。

当 `Targeted Routine Library` 设置为 `IFL (floating-point)` 时，该端口设置为数据类型 `Ifl_DPResultF32_Type`。

### 输出

### **Port 1** — 二维函数逼近 标量 | 向量 | 矩阵

通过使用输入索引 `k` 和小数 `f` 的值对表数据进行插值计算得到的二维函数逼近。

当 `Targeted Routine Library` 设置为 `IFL (floating-point)` 时，唯一有效的数据类型是 `single`。

当 `Targeted Routine Library` 设置为 `IFX (fixed-point)` 时，`Port 1` 的值可以是以下数据类型之一：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 以及定点数据类型。

**数据类型：** `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `fixed point`

## 参数

### **目标例程库** — 指示用于模块代码替换的 AUTOSAR 例程库 `IFX (fixed-point)` | `IFL (floating-point)`

如果为模型选择 AUTOSAR 4.x 代码替换库 (CRL)，则从此模块生成的代码将由所选 AUTOSAR 例程库替换。此参数使您可以选择定点 (IFX) 或浮点 (IFL) 代码替换和验证检查。

### **目标例程** — 用于代码替换的 AUTOSAR 库例程 `Ifx_IpoMap` | `Ifl_IpoMap`

此参数反映用于替换此模块生成代码的 AUTOSAR 代码替换库 (CRL) 例程的名称。命名约定包含目标例程库、插值方法和模块类型。此参数仅供参考，不得编辑。

当 `Targeted Routine Library` 设置为 `IFX (fixed-point)` 时，该值默认为 `Ifx_IpoMap`。

当 `Targeted Routine Library` 设置为 `IFL (floating-point)` 时，该值默认为 `Ifl_IpoMap`。

### 表设定

### **数据设定** — 选择如何输入表数据 `Explicit values`（默认） | `Lookup table object`

指定是直接输入表数据还是使用查找表对象。如果将此参数设置为：

- `Explicit values`，对话框中会显示 **表数据** 参数和 **数据类型** 选项卡。
- `Lookup table object`，对话框中会显示 **名称** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TableSpecification` |
| **类型：** character vector | string |
| **值：** `"Explicit values" | "Lookup table object"` |
| **默认值：** `"Explicit values"` |

### **名称** — `Simulink.LookupTable` 对象的名称 `Simulink.LookupTable` 对象

指定 `Simulink.LookupTable` 对象的名称。查找表对象引用 `Simulink.Breakpoint` 对象。如果 `Simulink.LookupTable` 对象不存在，请单击操作按钮并选择 **Create**。新查找表对象的对应参数将使用模块信息填充。

#### 依赖项

要启用此参数，请将 **数据设定** 设置为 `Lookup table object`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LookupTableObject` |
| **类型：** character vector |
| **值：** `Simulink.LookupTable` object |
| **默认值：** `'[]'` |

### **表数据** — 定义输出值表 `[4 5 6;16 19 20;10 18 23]`（默认） | character vector

输入输出值表。

在仿真期间，矩阵大小必须为二维。但是，在模块图编辑期间，您可以输入空矩阵（指定为 `[]`）或未定义的工作区变量。此方法允许您推迟为表数据指定维度正确的矩阵，并继续编辑模块图。

#### 依赖项

要启用此参数，请将 **数据设定** 设置为 `Table and breakpoints`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Table` |
| **类型：** character vector |
| **值：** 表值矩阵 |
| **默认值：** `'[4 5 6;16 19 20;10 18 23]'` |

### **编辑表和断点** — 启动 Lookup Table Editor 对话框按钮

单击此按钮以打开 Lookup Table Editor。

对于查找表对象，单击此按钮可编辑该对象并为该对象保存新值。

### 算法

### **插值方法** — 选择插值方法 `Linear point-slope`（默认） | `Flat` | `Nearest`

指定模块用于对表数据进行插值的方法。您可以选择 `Linear point-slope`、`Flat` 或 `Nearest`。有关这些方法的详细信息，请参阅 Interpolation Methods。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InterpMode` |
| **类型：** character vector | string |
| **值：** `"Flat" | "Linear point-slope" | "Nearest"` |
| **默认值：** `"Linear point-slope"` |

### **整数舍入模式** — 定点或浮点运算的舍入模式 `Zero`（默认） | `Round`

指定在仿真期间或执行从模型生成的代码期间发生的定点或浮点查找表计算的舍入模式。

此选项不影响模块参数值的舍入。Simulink™ 会将此类值舍入到最接近的可表示整数值。

#### 依赖项

仅当设置为 `Round` 时，此参数才可见。AUTOSAR 4.x 和用于 SIL 测试的主机库不支持整数舍入，并且默认情况下隐藏。要在使用 AUTOSAR 4.x 代码替换库时启用 SIL 工作流，请将此设置更改为 `Zero`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMode` |
| **类型：** character vector | string |
| **值：** `"Round" | "Zero"` |
| **默认值：** `"Zero"` |

### 数据类型

### **表数据** — 表数据的数据类型 `Inherit: Same as output`（默认） | `Inherit: Inherit from 'Table data'` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定表数据类型。模块将验证所选类型是否与目标例程的规范兼容。

当 `Targeted Routine Library` 设置为 `IFL (floating-point)` 时，唯一有效的数据类型是 `single`。

当 `Targeted Routine Library` 设置为 `IFX (fixed-point)` 时，您可以将表数据类型设置为：

- 继承数据类型的规则：`Inherit: Same as output`、`Inherit: Inherit from 'Table data'`。
- 以下内置数据类型之一：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`。
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象。
- 求值结果为数据类型的表达式。例如，软件提供以下定点数据类型表达式：`fixdt(1,16)`、`fixdt(1,16,0)` 或 `fixdt(1,16,2^0,0)`。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

**提示**

在以下情况下，指定不同于输出数据类型的表数据类型：

- 降低存储表数据的内存需求，该表数据使用比输出信号更小的类型
- 在具有不同输出数据类型的两个 Curve 模块之间共享预缩放的表数据
- 在生成的代码中为具有不同输出数据类型的模块共享自定义存储表数据

#### 依赖项

要启用此选项卡，请在 **表设定** 选项卡上，将 **数据设定** 设置为 `Explicit values`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TableDataTypeStr` |
| **类型：** character vector | string |
| **值：** `"Inherit: Inherit from 'Table data'" | "Inherit: Same as output" | "single" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "fixdt(1,16)" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"` |
| **默认值：** `"Inherit: Same as output"` |

## 所属库

AUTOSAR Blockset / Classic Platform / Library Routines / Interpolation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2025a：整数舍入模式被隐藏

**整数舍入模式** 设置为 `"Zero"` 并默认隐藏，因为 AUTOSAR 4.x 和用于 SIL 测试的主机库仅支持 `"Zero"`。

### R2025a：AUTOSAR 代码替换库支持 4.0 发行版之后的架构

从 25a 开始，AUTOSAR 代码替换库支持 AUTOSAR 4.0 之后的 AUTOSAR 架构版本。要使用最新的 AUTOSAR 例程，请在模型配置参数对话框的 **代码生成** > **接口** 窗格中，将 **代码替换库** 指定为 `AUTOSAR 4.x`。

## 描述

使用先前计算出的索引和小数值来加速二维函数逼近

Map Using Prelookup 模块旨在与 Prelookup 模块配合使用。此模块允许一个 Prelookup 结果驱动多个插值结果。Prelookup 模块计算索引和区间小数，以指定其输入值 `u` 与断点数据集的关系，并将得到的索引和小数值馈入 Map Using Prelookup 模块以对二维表进行插值。Prelookup 和 Map Using Prelookup 模块具有分布式算法，当一起使用时，执行与 Map 模块相同的算法操作，但提供更大的灵活性以及更高效的仿真和代码生成。

如果为 AUTOSAR 模型选择 AUTOSAR 4.x 代码替换库 (CRL)，则从此模块生成的代码将替换为在模块参数对话框中配置的 AUTOSAR 库例程。
