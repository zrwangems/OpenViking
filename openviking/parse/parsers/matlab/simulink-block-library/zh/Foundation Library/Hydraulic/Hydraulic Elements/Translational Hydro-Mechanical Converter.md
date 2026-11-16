---
type: simulink-block
title: 'Translational Hydro-Mechanical Converter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'translationalhydromechanicalconverter'
documentation_source_path: 'ref/translationalhydromechanicalconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Hydro-Mechanical Converter

## 端口

该模块具有以下端口：

`A`
:   与转换器入口关联的液压守恒端口。

`R`
:   与转换器活塞杆关联的机械平动守恒端口。

`C`
:   与转换器壳体关联的机械平动守恒端口。

`P`
:   物理信号输入端口，用于传递来自 Simscape™ Multibody™ 关节的位置信息。将此端口连接到关节的位置感测端口 **p**。有关详细信息，请参阅将 Simscape 网络连接到 Simscape Multibody 关节。要启用此端口，请将 **接口位移** 参数设置为 `Provide input signal from Multibody joint`。

## 参数

**活塞面积**
:   有效活塞面积。默认值为 `5e-4` m^2。

**转换器方向**
:   指定转换器相对于全局指定正方向的方向。根据在其入口施加压力时，转换器施加的是正方向还是负方向上的力，转换器可以有两种不同的安装方式：

    - `Pressure at A causes positive displacement of R relative to C` — 流体压力增加会导致端口 **R** 相对于端口 **C** 产生正位移。这是默认设置。
    - `Pressure at A causes negative displacement of R relative to C` — 流体压力增加会导致端口 **R** 相对于端口 **C** 产生负位移。

**可压缩性**
:   指定流体密度是视为恒定还是随压力变化。默认值为 `Off`，此时模块对理想转换器进行建模。如果选择 `On`，模块对话框会显示其他参数，使您无需添加任何额外模块即可对流体密度的动态变化进行建模。

**活塞位移**
:   选择确定端口 **R** 相对于端口 **C** 位移的方法：

    - `Calculate from velocity of port R relative to port C` — 根据模块方程，从相对端口速度计算位移。这是默认方法。
    - `Provide input signal from Multibody joint` — 启用输入物理信号端口 **p**，以传递来自 Multibody 关节的位移信息。仅当使用 Translational Multibody Interface 模块将转换器连接到 Multibody 关节时，才使用此方法。有关详细信息，请参阅如何传递位置信息。

    当 **可压缩性** 为 `On` 时，此参数启用。

**初始活塞位置**
:   活塞相对于缸盖的初始偏移量。当 **可压缩性** 为 `On` 且 **活塞位移** 为 `Calculate from velocity of port R relative to port C` 时，此参数启用。默认值为 `0` m。

**死区容积**
:   活塞位置为零时腔室中的流体体积。当 **可压缩性** 为 `On` 时，此参数启用。默认值为 `1e-4` m^3。

**比热比**
:   气体比热比。当 **可压缩性** 为 `On` 时，此参数启用。默认值为 `1.4`。

**初始压力**
:   腔室中的初始压力。此参数指定在仿真运行开始时计算模块初始状态所使用的初始条件。当 **可压缩性** 为 `On` 时启用。默认值为 `0`。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2023a: 将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅将 Hydraulic 模型升级为使用 Isothermal Liquid 模块。

## 描述

(将移除) 液压域与机械平动域之间的接口

`Translational Hydro-Mechanical Converter` 模块对理想转换器进行建模，该转换器将液压能转换为机械能（形式为转换器输出构件的平动），反之亦然。可压缩性选项使转换器考虑流体密度的动态变化。

使用此模块作为基本元素，您可以通过添加特定于应用的效果（例如泄漏、摩擦、硬限位等）来构建各种液压缸模型。

转换器根据以下方程进行仿真：

q=d(ρρl0V)dt=d(ρρl0)dtV+ρρl0⋅ε⋅(vR−vC)⋅A

F=ε⋅p⋅A

ρ={(α1−α)ρg0+ρl0(α1−α)(p0p+p0)1γ+e−pβlif compressibility is onρl0if compressibility is off

其中

|  |  |
| --- | --- |
| *q* | 流入转换器腔室的流量 |
| *A* | 有效活塞面积 |
| *v*R | 转换器活塞杆速度 |
| *v*C | 转换器壳体速度 |
| *F* | 转换器产生的力 |
| *p* | 转换器腔室中流体的表压 |
| *V* | 活塞体积 |
| *α* | 截留空气的相对量 |
| *ρ*l0 | 大气条件下的流体密度 |
| *ρ*g0 | 大气条件下的气体密度 |
| *p*0 | 大气压力 |
| *γ* | 比热比 |
| *β*l | 大气条件下且无气体时的体积模量 |
| *ε* | 转换器的机械方向（如果流体压力增加导致 R 相对于 C 产生正位移，则为 `1`；如果流体压力增加导致 R 相对于 C 产生负位移，则为 `-1`） |

活塞体积按以下公式计算

V=Vdead+A⋅(x0+x)dxdt=ε⋅(vR−vC)

其中

|  |  |
| --- | --- |
| *V*dead | 腔室死区容积 |
| *x*0 | 活塞初始位置 |
| *x* | 活塞相对于初始位置的位移 |

端口 A 是与转换器入口关联的液压守恒端口。端口 R 和 C 分别是与转换器活塞杆和壳体关联的平动机械守恒端口。

模块对话框没有 **源代码** 链接。要查看底层组件源代码，请在 MATLAB® 编辑器中打开以下文件：

- 对于不可压缩转换器实现 — `translational_converter_incompressible.ssc`
- 对于可压缩转换器实现 — `translational_converter_compressible.ssc`
