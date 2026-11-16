---
type: simulink-block
title: 'Hydraulic Piston Chamber'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'hydraulicpistonchamber'
documentation_source_path: 'ref/hydraulicpistonchamber.html'
language: zh-CN
chinese_source: worker-translation
---

# Hydraulic Piston Chamber

## 端口

该模块具有以下端口：

`A`
:   与腔室入口关联的液压守恒端口。

`P`
:   控制活塞位移的物理信号端口。

## 参数

**活塞面积**
:   有效活塞面积。默认值为 `5e-4` m^2。

**活塞初始位置**
:   活塞相对于缸盖的初始偏移。默认值为 0。

**腔室方向**
:   指定腔室相对于全局指定的正方向的方向。腔室可以两种不同方式安装，具体取决于正方向上的活塞运动是增加还是减小腔室体积。如果正方向上的活塞运动减小腔室体积，请将该参数设置为 `Positive displacement decreases volume`。默认值为 `Positive displacement increases volume`。

**腔室死区体积**
:   活塞位置为零时腔室中的流体体积。默认值为 `1e-4` m^3。

**比热比**
:   气体比热比。默认值为 `1.4`。

 受限参数

当模型处于受限编辑模式时，不能修改以下参数：

- **腔室方向**

所有其他模块参数均可修改。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

### R2023a：将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅将液压模型升级为使用 Isothermal Liquid 模块。

## 描述

（将被移除）液压缸中的可变容积液压容量

**注意**

从 R2014a 版本开始，可以直接在 hydro-mechanical converter 模块中指定流体可压缩性。建议不要使用连接到转换器的 Hydraulic Piston Chamber 模块，而是使用转换器模块对话框中的 **可压缩性** 参数，因为新方法提供更准确的结果，并且 Hydraulic Piston Chamber 模块可能会在未来版本中移除。

Hydraulic Piston Chamber 模块对由液压缸活塞形成的腔室中的流体可压缩性进行建模。流体被视为液体和少量夹带、未溶解气体的混合物。将此模块与 Translational Hydro-Mechanical Converter 模块一起使用。Hydraulic Piston Chamber 模块仅考虑由流体可压缩性引起的流量。用于产生活塞速度的流体体积在 Translational Hydro-Mechanical Converter 模块中计入。

腔室根据以下方程进行仿真（见 [1, 2]）：

q=V0+A(x0+x·or)E·dpdt

E=El1+α(papa+p)1/n1+αpa1/nn·(pa+p)n+1nEl

其中

|  |  |
| --- | --- |
| *q* | 由流体可压缩性引起的流量 |
| *V*0 | 死区体积 |
| *A* | 有效活塞面积 |
| *x*0 | 活塞初始位置 |
| *x* | 活塞从初始位置的位移 |
| *or* | 相对于全局指定正方向的腔室方向。如果正方向上的位移增加腔室体积，*or* 等于 1。如果正方向上的位移减小腔室体积，*or* 等于 –1。 |
| *E* | 流体体积模量 |
| *E*l | 纯液体体积模量 |
| *p* | 腔室中流体的表压 |
| *p*α | 大气压力 |
| *α* | 大气压力下的相对气体含量，*α* = *V*G/*V*L |
| *V*G | 大气压力下的气体体积 |
| *V*L | 液体体积 |
| *n* | 气体比热比 |

将流体表示为液体和气体混合物的主要目的是引入空化的近似模型，当压力降至流体蒸气饱和水平以下时，腔室中会发生空化。如下方图表所示，混合物的体积模量随着表压接近零而减小，从而显著减慢进一步的压力变化。在远高于零的表压下，少量未溶解气体实际上对系统行为没有影响。

空化本质上是一个热力学过程，需要考虑多相流体、热传递等，因此无法用 Simscape™ 软件准确仿真。但模块中实现的简化版本足以在压力降至危险水平以下时发出信号，并防止通常在负压下发生的计算失败。

如果压力降至绝对真空（–101325 Pa）以下，仿真停止并显示错误消息。

Port A 是与腔室入口关联的液压守恒端口。Port P 是控制活塞位移的物理信号端口。

模块正方向为从 port A 到参考点。这意味着如果流量流入腔室，则流量为正。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
