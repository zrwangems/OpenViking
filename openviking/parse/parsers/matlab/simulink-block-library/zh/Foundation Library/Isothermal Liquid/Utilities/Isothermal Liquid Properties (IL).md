---
type: simulink-block
title: 'Isothermal Liquid Properties (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Utilities'
documentation_page: 'isothermalliquidpropertiesil'
documentation_source_path: 'ref/isothermalliquidpropertiesil.html'
language: zh-CN
chinese_source: worker-translation
---

# Isothermal Liquid Properties (IL)

## 端口

### 守恒

### **A** — 等温液体连接端口

等温液体守恒端口，用于将模块连接到网络。您可以将其连接到框图中等温液体连接线上的任意点。当您将 Isothermal Liquid Properties (IL) 模块连接到连接线时，软件会自动识别连接到特定回路的等温液体模块，并将液体属性传播到回路中的所有模块。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：为清晰起见重命名了参数

为清晰起见，**Pressure outside valid range** 参数已重命名为 **Pressure below minimum valid value**。

当该参数首次引入时，它在多个流体域中具有相同的名称。然而，等温液体域没有指定最大允许压力的参数，只有 **Minimum valid pressure** 参数。这纯粹是名称更改，模块功能没有改变。

### R2023a：在仿真期间流体属性超出范围时控制模块行为

以前，如果流体属性在仿真期间超出有效范围，模块会返回错误。您现在可以使用新的 **Pressure outside valid range** 参数来控制流体属性在仿真期间超出范围时的模块行为。

**Minimum valid pressure** 参数的默认值已从 0.1 Pa 更改为 1 Pa。

## 描述

等温液体的物理属性

Isothermal Liquid Properties (IL) 模块定义液体属性，这些属性作为连接到回路的所有模块的全局参数。默认液体为水。

图中的每个拓扑上不同的等温液体回路都可以连接一个 Isothermal Liquid Properties (IL) 模块。如果回路未连接 Isothermal Liquid Properties (IL) 模块，则该回路中的模块使用对应于默认 Isothermal Liquid Properties (IL) 模块参数值的属性。

Isothermal Liquid Properties (IL) 模块提供建模选项选择：

- 混合物体积模量：常数或压力的线性函数
- 夹带空气：零、常数或压力的线性函数

用于计算各种液体属性的方程取决于所选的等温液体模型。有关详细信息，请参阅 Isothermal Liquid Modeling Options。

### 理想流体模型

夹带空气是流体中捕获的未溶解气体的相对量。夹带空气为零的流体是理想的，即它代表纯液体。

在其默认配置中，Isothermal Liquid Properties (IL) 模块对具有恒定体积模量的理想流体进行建模：

- **Isothermal bulk modulus model** 为 `Constant`
- **Entrained air model** 为 `Constant`
- **Entrained air-to-liquid volumetric ratio at atmospheric pressure** 为 `0`

在此模型中，假设液体体积模量为常数，因此液体密度随液体压力呈指数增长：

ρL=ρL0⋅ep−p0βL，

其中：

- *β*L 是液体体积模量。
- *ρ*L 是液体密度。
- *ρ*L0 是参考压力下的液体密度。
- *p* 是液体压力。
- *p*0 是参考压力。默认情况下，模块假设参考压力为大气压 `0.101325 MPa`，但您可以指定不同的值。

在液体压力可能在宽范围内变化的系统中，恒定体积模量的假设不再有效，您可以使用 **Isothermal bulk modulus model** 参数将液体体积模量定义为压力的线性函数：

βL=βL0+Kβp(p−p0)，

其中：

- *β*L0 是参考压力下的液体体积模量。
- *K*βp 是体积模量与压力增加之间的比例系数。

如果液体压力降至参考压力 *p*0 以下，则前一方程中的液体体积模量值可能变为负值，这是非物理的。为确保液体体积模量始终为正，请使用 **Minimum valid pressure** 参数指定最小有效压力 *p*min：

pmin>p0−βL0Kβp。

如果液体压力降至 **Minimum valid pressure** 参数值以下，仿真将发出错误。

### 含夹带空气的流体模型

在实践中，工作流体是液体和少量夹带空气的混合物。要对这种类型的流体进行建模，请为 **Entrained air-to-liquid volumetric ratio at atmospheric pressure** 参数指定非零值，但将 **Entrained air model** 保持为 `Constant`。

给定压力下的混合物密度定义为液体和夹带空气的总质量除以该压力下液体和夹带空气总体积。虽然混合物的总质量随压力变化而守恒，但混合物体积不保持恒定。夹带空气由体积分数给出：

α0=Vg0Vg0+VL0，

其中：

- *α*0 是参考（大气）压力下的夹带空气与液体体积比。
- *V*g0 是参考压力下的空气体积。
- *V*L0 是参考压力下的纯液体体积。

假设夹带空气遵循理想气体定律。液体中空气的压缩或膨胀是多方过程，其中空气压力和液体压力相同：

Vg=Vg0(p0p)1/n，

其中：

- *V*g 是空气体积。
- *n* 是空气多方指数。

要对空气溶解到流体中的效应进行建模，请选中 **Model air dissolution** 复选框。

空气溶解到流体中的过程由亨利定律描述。在压力小于或等于参考压力 *p*0（假设等于大气压）时，假设所有空气都被夹带。在压力等于或高于压力 *p*c 时，所有夹带空气都已溶解到液体中。在 *p*0 和 *p*c 之间的压力下，未因溶解而损失的夹带空气体积分数 *θ(p)* 是压力的线性函数，并由三阶多项式函数近似，以平滑地连接三个压力区域之间的密度和体积模量值：

θ(p)={1,p≤p00,p≥pc1−(3(pc−ppc−p0)2−2(pc−ppc−p0)3),p0<p<pc。

### 数据可视化

该模块提供将指定的流体属性（密度和等温体积模量）绘制为压力函数的选项。绘制属性可让您在仿真模型之前可视化数据。

要绘制数据，请在模型中右键单击 Isothermal Liquid Properties (IL) 模块，然后从上下文菜单中选择 **Foundation Library** > **Plot Fluid Properties**。使用绘图顶部的下拉列表选择要可视化的流体属性。单击 **Reload** 按钮以在模块参数更新后重新生成绘图。

**Isothermal Liquid Properties Plot**
