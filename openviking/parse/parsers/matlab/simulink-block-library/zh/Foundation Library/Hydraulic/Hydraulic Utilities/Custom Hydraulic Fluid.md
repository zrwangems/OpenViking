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

该模块具有一个液压守恒端口。

## 参数

**Fluid density**
:   工作流体的密度。默认值为 850 kg/m^3。

**Kinematic viscosity**
:   工作流体的运动粘度。默认值为 1.8e-5
    m^2/s。

**Bulk modulus at atm. pressure and no gas**
:   工作流体的体积模量，在大气压下且无夹带空气。默认值为 8e8 Pa。

**Relative amount of trapped air**
:   流体中夹带的、未溶解气体的量。该量指定为标准条件下气体体积与腔室中流体体积之比。因此，参数值必须小于 1。
    在实际中，夹带空气的相对量总是大于 0。如果设置为 0，则假定为理想流体。默认值为 0.005。

**在具有流体可压缩性的模块中绝对压力低于绝对零度**
:   在仿真期间，软件检查绝对压力不会降至绝对零以下。此检查仅对液压回路中流体可压缩性重要的那些模块执行。此参数的值决定了模块在仿真期间如何处理超出范围的断言：

    - `Error` — 如果压力降至绝对零以下，仿真停止并收到错误消息。这是默认值。
    - `Warning` — 如果压力降至绝对零以下，会收到警告但仿真继续。在建模极端情况下可能发生气蚀的系统时使用此选项。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2023a: 将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。
Isothermal Liquid 库中的模块提供了更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将被移除）通过指定参数值来设置工作流体属性

Custom Hydraulic Fluid 模块允许您指定液压模块回路中使用的液压流体类型。它为回路中的所有液压模块提供液压流体属性，例如运动粘度、密度和体积模量。这些流体属性在仿真期间假定为常数。

Custom Hydraulic Fluid 模块允许您将流体属性（例如运动粘度、密度、体积模量和夹带空气的相对量）指定为模块参数。

Custom Hydraulic Fluid 模块有一个端口。您可以通过从主管路分支出一条连接线并将其连接到该端口，将其连接到液压图。当您将 Custom Hydraulic Fluid 模块连接到液压管路时，软件会自动识别连接到特定回路的液压模块，并将液压流体属性传播到回路中的所有液压模块。

图中的每个拓扑上不同的液压回路都需要指定工作流体的属性。您可以使用 Custom Hydraulic Fluid 模块或 Hydraulic Fluid 模块来指定这些属性，后者随 Simscape™ Fluids™ 库提供。如果没有 Hydraulic Fluid 模块或 Custom Hydraulic Fluid 模块连接到回路，则该回路中的液压模块使用默认流体，该流体等效于由具有默认参数值的 Custom Hydraulic Fluid 模块定义的流体。
