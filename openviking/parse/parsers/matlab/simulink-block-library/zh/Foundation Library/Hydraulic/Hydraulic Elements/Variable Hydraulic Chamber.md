---
type: simulink-block
title: 'Variable Hydraulic Chamber'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'variablehydraulicchamber'
documentation_source_path: 'ref/variablehydraulicchamber.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Hydraulic Chamber

## 端口

该模块具有以下端口：

`A`
:   与腔室入口关联的液压守恒端口。

`V`
:   提供腔室体积变化的物理信号端口。

## 参数

**腔室死区容积**
:   腔室中流体的最小体积。默认值为
    `1e-4` m^3。

**比热比**
:   气体比热比。默认值为
    `1.4`。

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

### R2023a: 将移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅将液压模型升级为使用 Isothermal Liquid 模块。

## 描述

（将移除）可压缩流体的可变体积液压容量

Variable Hydraulic Chamber 模块对可变体积腔室中的流体可压缩性进行建模。流体被视为液体与少量夹带、未溶解气体的混合物。将此模块与 Translational Hydro-Mechanical Converter 模块一起使用。

**注意**

Variable Hydraulic Chamber 模块仅考虑由流体可压缩性引起的流量。用于产生活塞速度所消耗的流体体积在 Translational Hydro-Mechanical Converter 模块中计入。

腔室根据以下方程进行仿真（见 [1, 2]）：

q=V0+VE·dpdt

E=El1+α(papa+p)1/n1+αpa1/nn·(pa+p)n+1nEl

其中

|  |  |
| --- | --- |
| *q* | 由流体可压缩性引起的流量 |
| *V*0 | 腔室中流体的初始体积 |
| *V* | 腔室体积变化，通过端口 V 提供 |
| *E* | 流体体积模量 |
| *E*l | 纯液体体积模量 |
| *p* | 腔室中流体的表压 |
| *p*α | 大气压 |
| *α* | 大气压下的相对气体含量，*α* = *V*G/*V*L |
| *V*G | 大气压下的气体体积 |
| *V*L | 液体体积 |
| *n* | 气体比热比 |

将流体表示为液体与气体混合物，其主要目的是引入气穴的近似模型；当压力降至流体蒸气饱和水平以下时，腔室中会发生气穴。如下图所示，混合物的体积模量随着表压趋近于零而减小，从而显著减缓进一步的压力变化。在远高于零的表压下，少量未溶解气体实际上对系统行为没有影响。

有关如何复现此图的信息，请参阅 Constant Volume Hydraulic Chamber。

气穴本质上是一个热力学过程，需要考虑多相流体、热传递等，因此无法使用 Simscape™ 软件准确仿真。但模块中实现的简化版本足以在压力降至危险水平以下时发出信号，并防止通常在负压下发生的计算失败。

如果压力降至绝对真空（–101325 Pa）以下，仿真将停止并显示错误消息。

端口 A 是与腔室入口关联的液压守恒端口。端口 V 是提供腔室体积变化的物理信号端口。

模块正方向是从端口 A 到参考点。这意味着如果流量流入腔室，则流量为正。

### 变量

使用 **变量** 选项卡在仿真前设置模块变量的优先级和初始目标值。有关详细信息，请参阅为模块变量设置优先级和初始目标。
