---
type: simulink-block
title: 'Reluctance Force Actuator'
family: 'magnetic'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Elements'
documentation_page: 'reluctanceforceactuator'
documentation_source_path: 'ref/reluctanceforceactuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Reluctance Force Actuator

## 端口

该模块具有以下端口：

`N`
:   与模块北端子相关联的磁守恒端口。

`S`
:   与模块南端子相关联的磁守恒端口。

`R`
:   与杆相关联的机械平动守恒端口。

`C`
:   与外壳相关联的机械平动守恒端口。

## 参数

**初始气隙**
:   仿真开始时气隙的厚度或长度。
    默认值为 `2` mm。

**最小气隙**
:   气隙的最小值，磁阻力的作用方向为使气隙闭合。
    该参数值必须大于 0。默认值为 `1e-4` mm。

**横截面积**
:   所建模部分的面积。默认值为 `0.01` m^2。

**材料的相对磁导率**
:   该部分材料的相对磁导率。默认值为 `1`。

**接触刚度**
:   用于对最小气隙位置处的硬限位进行建模的刚度。
    默认值为 `10e6` N/m。

**接触阻尼**
:   用于对最小气隙位置处的硬限位进行建模的阻尼。
    默认值为 500 N/(m/s)。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

基于磁阻力的磁动势装置

Reluctance Force Actuator 模块对基于磁阻力的通用磁动势装置进行建模。

该模块基于以下方程：

F=−0.5⋅Φ2⋅dℜdx

ℜ(x)=xμ0⋅μr⋅A

u=dx

其中

|  |  |
| --- | --- |
| *F* | 磁阻力 |
| *Φ* | 磁路中的磁通 |
| ℜ | 磁阻 |
| *x* | 气隙的厚度或长度 |
| *μ*0 | 磁导率常数 |
| *μ*r | 材料的相对磁导率 |
| *A* | 所建模部分的横截面积 |
| *u* | 速度 |

连接 N 和 S 是磁守恒端口，连接 C 和 R 是机械平动守恒端口。执行器产生的磁力用于闭合气隙，因此，当合力从 C 作用到 R 时，该力为负。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅“设置模块变量的优先级和初始目标”。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的**标称值**部分。有关详细信息，请参阅“修改模块变量的标称值”。
