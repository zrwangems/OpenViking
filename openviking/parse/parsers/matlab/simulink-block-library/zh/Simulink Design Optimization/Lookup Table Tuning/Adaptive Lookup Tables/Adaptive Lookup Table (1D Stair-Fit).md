---
type: simulink-block
title: 'Adaptive Lookup Table (1D Stair-Fit)'
family: 'sldo'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'Lookup Table Tuning / Adaptive Lookup Tables'
documentation_page: 'adaptivelookuptable1dstairfit'
documentation_source_path: 'ref/adaptivelookuptable1dstairfit.html'
language: zh-CN
chinese_source: worker-translation
---

# Adaptive Lookup Table (1D Stair-Fit)

## 端口

R2025b 中未提供文档。

## 参数

**第一个输入（行）断点集**
:   由模块可能的输入值组成的向量。
    输入向量必须单调递增。

**将初始表设为输入**
:   选中此复选框会强制 Adaptive Lookup Table (1D Stair-Fit) 模块忽略 **表数据（初始）** 参数，并创建一个新的输入端口 `Tin`。使用此端口输入表数据。

**表数据（初始）**
:   初始表输出值。此向量的大小必须为 N-1，其中 N 是断点数。

**表编号数据**
:   分配给单元格的编号值。此向量必须与表数据向量的大小相同，并且每个值都必须唯一。

**自适应方法**
:   选择以下选项之一：

    - `Sample mean` — 对在一个单元格内接收到的所有值求平均值。
    - `Sample mean (with forgetting)` — 为新数据赋予更大的权重。权重由 **自适应增益** 参数确定。

    有关详细信息，请参阅“选择自适应方法”。

**自适应增益（0 到 1）**
:   一个介于 0 和 1 之间的数值，用于调节自适应过程中赋予新数据的权重。0 表示短记忆（最新数据成为表值），1 表示长记忆（对在一个单元格内接收到的所有数据求平均值）。

**将自适应后的表设为输出**
:   选中此复选框会为自适应后的表创建一个附加输出端口 `Tout`。

**添加自适应启用/禁用/重置端口**
:   选中此复选框会创建一个附加输入端口 `Enable`，用于启用、禁用或重置自适应查找表。当施加到该端口的信号值为 `0` 时，将禁用自适应；信号值为 `1` 时，将启用自适应。将信号值设置为 `2` 会将表值重置为初始表数据。

**添加单元格锁定启用/禁用端口**
:   选中此复选框会创建一个附加输入端口 `Lock`，用于在仿真运行期间仅更新指定的单元格。信号值为 `0` 时解锁指定的单元格，信号值为 `1` 时锁定指定的单元格。

**对超出范围输入执行的操作**
:   选择 `Ignore`，或选择 `Adapt`，通过外推来处理最外侧断点之外的输入。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中推出**

## 描述

一维自适应查表

Adaptive Lookup Table (1D Stair-Fit) 模块通过动态更新底层查找表来创建一维自适应查找表。该模块使用您系统的输出 *y* 进行自适应调整。

每个索引参数 *u* 都可以在一组自适应数据点中取值，这些数据点称为 *断点*。每个维度中的两个断点定义一个 *单元格*。某一维度中所有断点的集合定义一个 *网格*。在一维情况下，每个单元格有两个断点，且该单元格是一条线段。

您可以使用 Adaptive Lookup Table (1D Stair Fit) 模块对具有一个输入的时变系统进行建模。
