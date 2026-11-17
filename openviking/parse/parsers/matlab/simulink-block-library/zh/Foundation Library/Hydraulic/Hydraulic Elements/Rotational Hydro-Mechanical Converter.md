---
type: simulink-block
title: 'Rotational Hydro-Mechanical Converter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'rotationalhydromechanicalconverter'
documentation_source_path: 'ref/rotationalhydromechanicalconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Hydro-Mechanical Converter

## 端口
```yaml
ports: []
```

该模块具有以下端口：

`A`
:   与转换器入口关联的液压守恒端口。

`S`
:   与转换器轴关联的机械旋转守恒端口。

`C`
:   与转换器壳体关联的机械旋转守恒端口。

`P`
:   物理信号输入端口，用于传递来自 Simscape™ Multibody™ 关节的位置信息。将此端口连接到关节的位置传感端口 **q**。有关详细信息，请参阅 Connecting Simscape Networks to Simscape Multibody Joints。要启用此端口，请将 **Interface rotation** 参数设置为 `Provide input signal from Multibody joint`。
## 参数
```yaml
parameters: []
```

**Displacement**
:   有效转换器排量。默认值为 `1.2e-4` m^3/rad。

**Converter orientation**
:   指定转换器相对于全局指定正方向的方向。转换器可以以两种不同方式安装，取决于当其入口施加压力时，它是在正方向还是负方向上产生扭矩：

    - `Pressure at A causes positive displacement of R relative to C` — 流体压力增加导致端口 **R** 相对于端口 **C** 产生正旋转。这是默认值。
    - `Pressure at A causes negative displacement of R relative to C` — 流体压力增加导致端口 **R** 相对于端口 **C** 产生负旋转。

**Compressibility**
:   指定流体密度是视为恒定还是随压力变化。默认值为 `Off`，此时模块对理想换能器进行建模。如果选择 `On`，模块对话框将显示附加参数，使您能够对流体密度的动态变化进行建模，而无需添加任何额外模块。

**Shaft rotation**
:   选择确定端口 **R** 相对于端口 **C** 旋转的方法：

    - `Calculate from velocity of port R relative to port C` — 基于模块方程，根据相对端口速度计算旋转。这是默认方法。
    - `Provide input signal from Multibody joint` — 启用输入物理信号端口 **q**，以传递来自 Multibody 关节的旋转信息。仅当您通过使用 Rotational Multibody Interface 模块将转换器连接到 Multibody 关节时，才使用此方法。有关详细信息，请参阅 How to Pass Position Information。

    当 **Compressibility** 为 `On` 时，此参数启用。

**Initial shaft angle**
:   活塞相对于缸盖的初始偏移。当 **Compressibility** 为 `On` 且 **Shaft rotation** 为 `Calculate from velocity of port R relative to port C` 时，此参数启用。默认值为 `0`。

**Dead volume**
:   零活塞位置时腔室中的流体体积。当 **Compressibility** 为 `On` 时，此参数启用。默认值为 `1e-4` m^3。

**Specific heat ratio**
:   气体比热比。当 **Compressibility** 为 `On` 时，此参数启用。默认值为 `1.4`。

**Initial pressure**
:   腔室中的初始压力。此参数指定用于在仿真运行开始时计算模块初始状态的初始条件。当 **Compressibility** 为 `On` 时，此参数启用。默认值为 `0`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2023a：将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将被移除）液压域与机械旋转域之间的接口

Rotational Hydro-Mechanical Converter 模块对理想换能器进行建模，该换能器将液压能转换为机械能（以转换器轴旋转运动的形式），反之亦然。在物理上，该转换器表示单作用旋转叶片执行器的主要组件。可压缩性选项使转换器能够考虑流体密度的动态变化。

使用此模块作为基本元件，您可以通过添加特定于应用的效应（如泄漏、摩擦、硬限位等）来构建各种旋转执行器。

转换器根据以下方程进行仿真：

q=d(ρρl0V)dt=d(ρρl0)dtV+ρρl0⋅ε⋅(ωS−ωC)⋅D

T=ε⋅p⋅D

ρ={(α1−α)ρg0+ρl0(α1−α)(p0p+p0)1γ+e−pβlif compressibility is onρl0if compressibility is off

其中

|  |  |
| --- | --- |
| *q* | 流向转换器腔室的流量 |
| *D* | 转换器排量，即每单位角度旋转轴所需的流体体积 |
| ωS | 转换器轴角速度 |
| ωC | 转换器壳体角速度 |
| *T* | 轴上的扭矩 |
| *p* | 转换器腔室中流体的表压 |
| *V* | 活塞体积 |
| *α* | 截留空气的相对量 |
| *ρ*l0 | 大气条件下的流体密度 |
| *ρ*g0 | 大气条件下的气体密度 |
| *p*0 | 大气压力 |
| *γ* | 比热比 |
| *β*l | 大气条件下且无气体时的体积模量 |
| *ε* | 转换器的机械方向（如果流体压力增加导致 R 相对于 C 正旋转，则为 `1`；如果流体压力增加导致 R 相对于 C 负旋转，则为 `-1`） |

活塞体积根据以下公式计算

V=Vdead+D⋅(θ0+θ)dθdt=ε⋅(ωS−ωC)

其中

|  |  |
| --- | --- |
| *V*dead | 腔室死区体积 |
| *θ*0 | 轴初始角度 |
| *θ* | 轴从初始位置的旋转 |

端口 A 是与转换器入口关联的液压守恒端口。端口 S 和 C 分别是与转换器轴和壳体关联的机械旋转守恒端口。端口 A 处的压力按照 **Converter orientation** 参数指定的方向产生扭矩。

模块对话框没有 **Source code** 链接。要查看底层组件源代码，请在 MATLAB® 编辑器中打开以下文件：

- 对于不可压缩转换器实现 — `rotational_converter_incompressible.ssc`
- 对于可压缩转换器实现 — `rotational_converter_compressible.ssc`
