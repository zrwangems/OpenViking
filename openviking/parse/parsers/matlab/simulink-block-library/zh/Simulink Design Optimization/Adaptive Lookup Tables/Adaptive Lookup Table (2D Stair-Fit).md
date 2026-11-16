---
type: simulink-block
title: 'Adaptive Lookup Table (2D Stair-Fit)'
family: 'sldo'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'Adaptive Lookup Tables'
documentation_page: 'adaptivelookuptable2dstairfit'
documentation_source_path: 'ref/adaptivelookuptable2dstairfit.html'
language: zh-CN
chinese_source: worker-translation
---

# Adaptive Lookup Table (2D Stair-Fit)

## 端口

在 R2025b 中未提供文档说明。

## 参数

**第一个输入（行）断点集**
:   一个值向量，其中包含第一个输入变量可能的模块输入值。
    第一个输入向量必须单调递增。

**第二个输入（列）断点集**
:   一个值向量，其中包含第二个输入变量可能的模块输入值。
    第二个输入向量必须单调递增。

**将初始表设为输入**
:   选中此复选框会强制 Adaptive Lookup Table (2D Stair-Fit)
    模块忽略 **表数据（初始）** 参数，并创建一个新的输入端口 `Tin`。
    使用此端口输入表数据。

**表数据（初始）**
:   初始表输出值。此 2-by-2 矩阵的大小必须为
    (n-1)-by-(m-1)，其中 n 是第一个输入断点的数量，
    m 是第二个输入断点的数量。

**表编号数据**
:   分配给单元格的编号值。此矩阵必须与表数据矩阵大小相同，
    并且每个值都必须唯一。

**自适应方法**
:   选择 `Sample mean` 或 `Sample mean with forgetting`。
    Sample mean 对一个单元格内接收到的所有值求平均值。
    Sample mean with forgetting 会赋予新数据更大的权重。
    权重的大小由 **自适应增益** 参数决定。有关详细信息，
    请参阅“选择自适应方法”。

**自适应增益（0 到 1）**
:   一个 0 到 1 之间的数字，用于调节自适应过程中赋予新数据的权重。
    0 表示短记忆（最后的数据成为表值），1 表示长记忆
    （对一个单元格中接收到的所有数据求平均值）。

**将自适应后的表设为输出**
:   选中此复选框会为自适应后的表创建一个额外的输出端口 `Tout`。

**添加自适应启用/禁用/重置端口**
:   选中此复选框会创建一个额外的输入端口 `Enable`，
    用于启用、禁用或重置自适应查找表。应用到该端口的信号值为
    `0` 时禁用自适应，信号值为 `1` 时启用自适应。
    将信号值设置为 `2` 会将表值重置为初始表数据。

**添加单元格锁定启用/禁用端口**
:   选中此复选框会创建一个额外的输入端口 `Lock`，
    用于在仿真运行期间仅更新指定的单元格。信号值为 `0`
    时解锁指定的单元格，信号值为 `1` 时锁定指定的单元格。

**针对超出范围输入的操作**
:   `Ignore`，或 `Adapt`（通过外推到最外侧断点之外）。

## 所属库

在 R2025b 中未提供文档说明。

## 模块特性

在 R2025b 中未提供文档说明。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

二维自适应查表

Adaptive Lookup Table (2D Stair-Fit) 模块通过动态更新底层查找表来创建二维自适应查找表。
该模块使用系统的输出 *y* 进行自适应调整。

每个索引参数 *u* 都可以从一组自适应数据点中取值，这些数据点称为*断点*。
每个维度中的两个断点定义一个*单元格*。其中一个维度中所有断点的集合定义一个*网格*。
在二维情况下，每个单元格有四个断点，并且是一个平面。

您可以使用 Adaptive Lookup Table (2D Stair-Fit) 模块对具有两个输入的时变系统进行建模。
