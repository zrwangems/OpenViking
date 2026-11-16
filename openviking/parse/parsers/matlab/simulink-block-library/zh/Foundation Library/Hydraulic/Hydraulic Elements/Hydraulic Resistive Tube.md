---
type: simulink-block
title: 'Hydraulic Resistive Tube'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'hydraulicresistivetube'
documentation_source_path: 'ref/hydraulicresistivetube.html'
language: zh-CN
chinese_source: worker-translation
---

# Hydraulic Resistive Tube

## 端口

模块具有以下端口：

`A`
:   与管道入口关联的液压守恒端口。

`B`
:   与管道出口关联的液压守恒端口。

## 参数

**Tube cross section type**
:   管道横截面的类型：`Circular` 或 `Noncircular`。对于圆形管道，您指定其内径。对于非圆形管道，您指定其水力直径和管道横截面积。该参数的默认值为 `Circular`。

**Tube internal diameter**
:   管道内径。如果 **Tube cross section type** 设置为 `Circular`，则使用该参数。默认值为 `0.01` m。

**Noncircular tube cross-sectional area**
:   管道横截面积。如果 **Tube cross section type** 设置为 `Noncircular`，则使用该参数。默认值为 `1e-4` m^2。

**Noncircular tube hydraulic diameter**
:   管道横截面的水力直径。如果 **Tube cross section type** 设置为 `Noncircular`，则使用该参数。默认值为 `0.0112` m。

**Geometrical shape factor**
:   用于计算层流下的摩擦因子。管道横截面的形状决定该值。对于具有非圆形横截面的管道，请将该因子设置为适当的值，例如正方形为 56，同心环为 96，矩形 (2:1) 为 62，等等 [1]。默认值为 `64`，对应于具有圆形横截面的管道。

**Tube length**
:   管道几何长度。默认值为 `5` m。

**Aggregate equivalent length of local resistances**
:   此参数表示与管道相关的所有局部阻力的总等效长度。您可以通过向管道几何长度加上所有局部阻力的总等效长度，来考虑局部阻力（例如弯头、管件、armature、入口/出口损失等）造成的压力损失。默认值为 `1` m。

**Internal surface roughness height**
:   管道内表面的粗糙度高度。该参数通常由数据表或制造商目录提供。默认值为 `1.5e-5` m，对应于拉制管。

**Laminar flow upper margin**
:   指定层流流态开始转变为湍流时所对应的雷诺数。数学上，这是充分发展层流时的最大雷诺数。默认值为 `2000`。

**Turbulent flow lower margin**
:   指定湍流流态被认为充分发展时所对应的雷诺数。数学上，这是湍流时的最小雷诺数。默认值为 `4000`。

 受限参数

当您的模型处于受限编辑模式时，不能修改以下参数：

- **Tube cross section type**

所有其他模块参数均可修改。实际可修改的模块参数集取决于模型进入受限模式时 **Tube cross section type** 参数的值。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

### R2023a: 将移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将移除）仅考虑摩擦损失的液压管道

Hydraulic Resistive Tube 模块对具有圆形和非圆形横截面的液压管道进行建模，并且仅考虑阻力特性。换句话说，该模块基于稳态流体动量条件这一基本假设开发。模型中既不考虑流体可压缩性，也不考虑流体惯性，这意味着无法研究水锤等特性。如有必要，您可以使用其他模块向模型中添加流体可压缩性、流体惯性及其他效应，从而生成更全面的模型。

也不考虑端部效应，假设流动沿整个管道长度充分发展。为考虑局部阻力，例如弯头、管件、入口和出口损失等，将所有阻力转换为各自的等效长度，然后将所有阻力的总长度加到管道几何长度上。

摩擦造成的压力损失使用 Darcy 方程计算，其中损失与取决于流态的摩擦因子以及流量的平方成正比。湍流流态下的摩擦因子使用 Haaland 近似确定（见 [1]）。从层流到湍流流态过渡期间的摩擦因子通过在两种流态极端点之间进行线性插值确定。根据这些假设，管道按照以下方程进行仿真：

p=f(L+Leq)DHρ2A2q⋅|q|

f={Ks/Refor Re<=ReLfL+fT−fLReT−ReL(Re−ReL)for ReL<Re<ReT1(−1.8log10(6.9Re+(r/DH3.7)1.11))2for Re>=ReT

Re=q⋅DHA⋅ν

其中

|  |  |
| --- | --- |
| *p* | 由于摩擦沿管道产生的压力损失 |
| *q* | 通过管道的流量 |
| *Re* | 雷诺数 |
| *Re*L | 层流时的最大雷诺数 |
| *Re*T | 湍流时的最小雷诺数 |
| *K*s | 表征管道横截面的形状因子 |
| *f*L | 层流边界处的摩擦因子 |
| *f*T | 湍流边界处的摩擦因子 |
| *A* | 管道横截面积 |
| *D*H | 管道水力直径 |
| *L* | 管道几何长度 |
| *L*eq | 局部阻力的总等效长度 |
| *r* | 管道内表面粗糙度高度 |
| *ν* | 流体运动粘度 |

模块的正方向为从端口 A 到端口 B。这意味着如果流动从 A 流向 B，则流量为正，且压力损失确定为 p=pA−pB。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真的鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
