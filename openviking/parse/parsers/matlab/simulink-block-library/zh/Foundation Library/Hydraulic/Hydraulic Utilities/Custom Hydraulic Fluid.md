---
type: simulink-block
title: 'Custom Hydraulic Fluid'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Utilities'
documentation_page: 'customhydraulicfluid'
documentation_source_path: 'ref/customhydraulicfluid.html'
language: zh-CN
chinese_source: worker-translation
---

# Custom Hydraulic Fluid

## 端口

该模块有一个液压守恒端口。

## 参数

**流体密度**
:   工作流体的密度。默认值为 850 kg/m^3。

**运动黏度**
:   工作流体的运动黏度。默认值为 1.8e-5 m^2/s。

**大气压（atm.）且无气体时的体积模量**
:   工作流体的体积模量，在大气压（atm.）且无夹带空气时。默认值为 8e8 Pa。

**截留空气的相对量**
:   流体中夹带的、未溶解气体的量。该量指定为标准条件下气体体积与腔室中流体体积之比。因此，该参数值必须小于 1。实际上，截留空气的相对量始终大于 0。如果设置为 0，则假定为理想流体。默认值为 0.005。

**具有流体可压缩性的模块中低于绝对零的绝对压力**
:   在仿真期间，软件会检查绝对压力不会降至绝对零以下。此检查仅对液压回路中流体可压缩性重要的那些模块执行。该参数的值确定模块在仿真期间如何处理超出范围断言：

    - `Error` — 如果压力降至绝对零以下，仿真会停止，您会收到错误消息。这是默认值。
    - `Warning` — 如果压力降至绝对零以下，您会收到警告，但仿真继续。在对极端情况下可能发生气蚀的系统建模时，使用此选项。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成：使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2023a：将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的准确性、可用性和数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将被移除）通过指定参数值设置的工作流体属性

Custom Hydraulic Fluid 模块允许您指定液压模块回路中使用的液压流体类型。它为回路中的所有液压模块提供液压流体属性，例如运动黏度、密度和体积模量。这些流体属性在仿真期间假定为常量。

Custom Hydraulic Fluid 模块允许您将流体属性（例如运动黏度、密度、体积模量和夹带空气的相对量）指定为模块参数。

Custom Hydraulic Fluid 模块有一个端口。您可以通过从主管路分支出连接线并将其连接到该端口，从而将其连接到液压图。当您将 Custom Hydraulic Fluid 模块连接到液压管路时，软件会自动识别连接到特定回路的液压模块，并将液压流体属性传播到该回路中的所有液压模块。

图中的每个拓扑上不同的液压回路都需要指定工作流体的属性。您可以使用 Custom Hydraulic Fluid 模块或 Hydraulic Fluid 模块来指定这些属性；后者随 Simscape™ Fluids™ 库提供。如果回路中未连接 Hydraulic Fluid 模块或 Custom Hydraulic Fluid 模块，则该回路中的液压模块使用默认流体，该流体等效于由采用默认参数值的 Custom Hydraulic Fluid 模块定义的流体。
