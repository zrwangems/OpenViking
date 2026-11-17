---
type: simulink-block
title: 'Simulink-PS Converter'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: ''
documentation_page: 'simulinkpsconverter'
documentation_source_path: '../simscape/ref/simulinkpsconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulink-PS Converter

## 端口

### 输入

### **Port\_1** — 输入 Simulink 信号 标量 | 向量 | 矩阵

模块转换为输出物理信号的输入 Simulink 信号。

**数据类型：** `double`

### **Port\_2** — 输入 Simulink 信号的一阶导数，作为单独的 Simulink 信号提供 标量 | 向量 | 矩阵

在 **Port\_1** 处提供输入信号一阶导数的 Simulink 信号。

#### 依赖关系

要启用此端口，请将 **Provided signals** 参数设置为 `Input and first derivative` 或 `Input and first two derivatives`。

**数据类型：** `double`

### **Port\_3** — 输入 Simulink 信号的二阶导数，作为单独的 Simulink 信号提供 标量 | 向量 | 矩阵

在 **Port\_1** 处提供输入信号二阶导数的 Simulink 信号。

#### 依赖关系

要启用此端口，请将 **Provided signals** 参数设置为 `Input and first two derivatives`。

**数据类型：** `double`
### 输出

### **PS** — 输出物理信号，其类型由输入信号、目标端口和模块参数值决定 物理信号

输出物理信号。信号大小与 **Port\_1** 处输入信号的大小相匹配。信号单位由目标模块决定。**Input signal unit** 参数和 **Apply affine conversion** 复选框允许您对输入信号值应用缩放和线性偏移，以计算输出信号的正确值。

## 参数

### 单位

### **Input signal unit** — 指定信号值转换的缩放因子 `1`（默认）| `V` | `A` | `m^3/s` | `Pa` | `N` | `m` | `m/s` | `N*m` | `rad/s` | `rad` | `K` | `kg/s` | `J/s` | `kg` | `Wb` | `<unit expression>`

要分配给输入 Simulink 信号的单位，以便单位管理器执行必要的单位转换并相应地缩放信号值。这些单位必须与目标模块输入的预期默认单位一致。您可以从下拉列表中选择单位，或键入所需的单位名称（如 `rpm`），或有效的表达式（如 `mm/s`）。有关更多信息以及单位缩写列表，请参见 How to Specify Units in Block Dialogs 和 Unit Definitions。默认值为 `1`，表示不应用缩放。模块输出端的物理信号与 **Port\_1** 处输入 Simulink 信号的值相匹配，采用物理网络内目标模块所预期的单位。

### **Apply affine conversion** — 选择仿射温度单位的转换方法 off（默认）| on

此复选框仅适用于可以使用或不使用仿射偏移进行转换的单位，例如 `degC` 或 `degF`。如果输入信号表示以摄氏度或华氏度为单位的绝对温度，请选中此复选框。有关更多信息，请参见 Thermal Unit Conversions。

### 输入处理

### **Filtering and derivatives** — 指定如何提供输入信号的时间导数 `Provide signals`（默认）| `Filter input, derivatives calculated` | `Zero derivatives (piecewise constant)`

此参数用于决定是通过附加输入端口还是通过滤波来提供输入信号的时间导数：

- `Provide signals` — 通过 **Provided signals** 参数选择是仅提供输入信号，还是同时将输入信号的时间导数作为附加输入信号提供。默认的输入处理选项为 `Provide signals` 和 `Input only`。如果使用显式求解器，建议通过选择其他选项之一来提供输入导数。有关详细信息，请参阅 Filtering Input Signals and Providing Time Derivatives。
- `Filter input, derivatives calculated` — 通过低通滤波器对输入进行滤波，该滤波器同时提供输入导数。在这种情况下，输入信号在转换为物理信号之前被（通过滤波）修改。一阶滤波器提供一个导数，而二阶滤波器提供一阶和二阶导数。如果使用此选项，请设置适当的 **Input filtering time constant** 参数值。
- `Zero derivatives (piecewise constant)` — 如果输入信号是分段常数（例如阶跃），此选项允许您将输入导数显式设置为零。

### **Provided signals** — 启用附加输入端口以提供输入信号的时间导数 `Input only`（默认）| `Input and first derivative` | `Input and first two derivatives`

此参数允许您将输入信号的时间导数作为附加输入信号提供：

- `Input only` — 仅提供输入信号。这是默认值。如果选择此选项，模块具有一个 Simulink 输入端口和一个物理信号输出端口。
- `Input and first derivative` — 如果选择此选项，Simulink-PS Converter 模块上会出现一个附加的 Simulink 输入端口，用于连接提供输入导数的信号。
- `Input and first two derivatives` — 如果选择此选项，Simulink-PS Converter 模块上会出现两个附加的 Simulink 输入端口，用于连接提供输入导数的信号。

#### 依赖关系

要启用此参数，请将 **Filtering and derivatives** 设置为 `Provide signals`。

### **Input filtering order** — 指定通过滤波提供的输入信号时间导数的数量 `First-order filtering`（默认）| `Second-order filtering`

此参数允许您指定通过滤波提供的输入信号时间导数的数量：

- `First-order filtering` — 仅提供一阶导数。
- `Second-order filtering` — 提供一阶和二阶导数。

#### 依赖关系

要启用此参数，请将 **Filtering and derivatives** 设置为 `Filter input, derivatives calculated`。

### **Input filtering time constant (in seconds)** — 控制输入信号滤波的时间常数 `0.001`（默认）| 正标量

指定滤波器时间常数（以秒为单位），用于控制输入信号的滤波。滤波后的输入跟随真实输入但经过平滑处理，并具有与时间常数同量级的滞后。为此参数选择值时，请考虑系统动态特性，并将时间常数设置为不大于仿真期间所关注的最小时间间隔的值。选择非常小的时间常数的代价是滤波后的输入信号将更接近真实输入信号，但会增加系统的刚性并减慢仿真速度。

#### 依赖关系

要启用此参数，请将 **Filtering and derivatives** 设置为 `Filter input, derivatives calculated`。

## 所属库

Simscape / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

将 Simulink 输入信号转换为物理信号

Simulink-PS Converter 模块将输入的 Simulink® 信号转换为物理信号。使用此模块可将 Simulink 信号源或其他 Simulink 模块连接到 Simscape™ 物理网络的输入。

### 模型画布上的模块图标显示

为了在传达信号转换的同时占用最少的画布空间，模块图标会根据是否连接到其他模块而动态变化。

| 当模块为... | 模块图标 |
| --- | --- |
| 未连接 |  |
| 连接到其他模块 |  |

模块图标还会根据 **Input filtering order** 参数的值而变化，以指示是否对输入信号应用了滤波。

| 输入滤波阶数 | 未连接模块图标 | 已连接模块图标 |
| --- | --- | --- |
| `First-order filtering` |  |  |
| `Second-order filtering` |  |  |

### 单位转换与检查

Simscape 单位管理器自动处理物理网络内的单位传播与检查，并执行必要的单位转换操作。

Simulink-PS Converter 模块输出端口处的物理信号作为该模块所连接的 Simscape 物理网络的输入信号。物理信号单位必须与目标模块输入端口（即连接到 Simulink-PS Converter 模块输出端口的输入端口）所期望的单位一致。

Simulink 信号单位不会传播到物理网络中。**Input signal unit** 参数允许您为输入信号值指定物理单位，以便 Simscape 单位管理器执行必要的单位转换并相应地缩放输出物理信号。

**注意**

如果您还将物理单位指定为连接到该模块输入端的 Simulink 信号的属性，软件会检查这两个单位是否匹配。有关详细信息，请参阅 Working with Simulink Units。

换句话说，**Input signal unit** 参数并不决定输出物理信号的单位，它仅提供一个缩放值。输出物理信号单位由目标模块推断。默认目标模块单位为米-千克-秒或 MKS（SI）。如果您将 Simulink-PS Converter 模块保持为无单位，并将 **Input signal unit** 参数设置为 `1`，则该模块不对输入信号应用缩放。如果您指定了不同的单位，且这些单位与目标模块输入所期望的默认单位一致，则单位管理器会将这些单位附加到输入 Simulink 信号值上，并在将信号提供给目标模块时执行必要的单位转换。

在下图中，Ideal Torque Source 模块期望在其 **S** 端口上接收以 N\*m 为单位的扭矩信号。Constant 源模块为该输入信号提供值。如果您将 Simulink-PS Converter 模块保持为无单位，则 Ideal Torque Source 模块将生成 1000 N\*m 的扭矩。此示例中其他模块的参数经过选择，使得 Ideal Torque Sensor 模块的输出值等于 Ideal Torque Source 模块生成的扭矩，因此 Display 模块将显示值 1000。如果您将 Simulink-PS Converter 模块中的 **Input signal unit** 参数值更改为 `N*cm`，单位管理器将执行转换，Ideal Torque Source 模块将生成 10 N\*m 的扭矩；Display 模块中的扭矩值变为 10，如图所示。

当输入信号与热力学变量相关且包含温度单位时，您必须决定是否需要应用仿射转换。有关详细信息，请参阅 When to Apply Affine Conversion。通常，如果输入信号表示相对温度，即温度变化，则需要应用线性转换，Δ*Tnew* = *L* \* Δ*Told*（默认方法）。但是，如果输入信号表示绝对温度，则需要应用仿射转换，*Tnew* = *L* \* *Told* + *O*。

例如，在下面图中所示的 Simulink-PS Converter 模块中，如果您在 **Input signal unit** 字段中键入 `degC` 并选中 **Apply affine conversion** 复选框，则 Ideal Temperature Source 模块生成的温度等于 293.15 K。但是，如果您清除 **Apply affine conversion** 复选框，则 Ideal Temperature Source 模块的输出为 20 K。

**注意**

无类型输入不支持仿射单位。如果您在 Simulink-PS Converter 模块中指定了仿射单位，然后将其直接连接到无类型输入端口，则信号值将转换为相应的基本单位，并使用该值执行进一步的数学运算。

### 输入处理

在仿真模型时，您可能需要为某些输入信号提供时间导数，尤其是在使用显式求解器时。提供所需输入导数的一种方法是通过低通滤波器对输入进行滤波。输入滤波使输入信号更平滑，通常能改善模型性能。额外的好处是，Simscape 引擎会计算滤波后输入的时间导数。一阶滤波器提供一个导数，而二阶滤波器提供一阶和二阶导数。如果使用输入滤波，为滤波器时间常数选择合适的值非常重要。

滤波器时间常数控制输入信号的滤波。滤波后的输入跟随真实输入，但经过平滑处理，并带有一个与您所选时间常数同量级的滞后。将时间常数设置为不大于您所关注系统中最小时间间隔的值。如果选择非常小的时间常数，滤波后的输入信号会更接近真实输入信号。然而，这个滤波后的输入信号会增加系统的刚性并减慢仿真速度。

除了使用输入滤波之外，您还可以直接作为额外的 Simulink 信号为输入信号提供时间导数。如果提供的导数与输入信号不一致，那么仿真过程中某些量可能会不正确。

对于分段常数信号，您还可以将输入导数显式设置为零。对于真正分段常数的信号（例如阶跃信号），请使用此选项。如果您有一个以离散采样时间采样的连续输入信号，将输入导数设置为零可能会产生不正确的仿真结果。请使用另外两个选项之一：要么对输入进行滤波，要么将时间导数作为单独信号提供。
