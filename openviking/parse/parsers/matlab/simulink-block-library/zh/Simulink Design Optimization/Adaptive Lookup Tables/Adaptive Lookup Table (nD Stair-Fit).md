---
type: simulink-block
title: 'Adaptive Lookup Table (nD Stair-Fit)'
family: 'sldo'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'Adaptive Lookup Tables'
documentation_page: 'adaptivelookuptablendstairfit'
documentation_source_path: 'ref/adaptivelookuptablendstairfit.html'
language: zh-CN
chinese_source: worker-translation
---

# Adaptive Lookup Table (nD Stair-Fit)

## 端口

未在 R2025b 中记录。

## 参数

**表维度数**
:   自适应查找表的维度数。

**表断点 (cell array)**
:   一组一维向量，包含输入变量的可能模块输入值。每个输入行必须单调递增，但各行不必具有相同长度。例如，如果 **表维度数** 为 `3`，则可以按如下方式设置表断点：

    ```
    {[1 2 3], [5 7], [1 3 5 7]}
    ```

**将初始表设为输入**
:   选中此复选框会强制 Adaptive Lookup Table (nD Stair-Fit) 模块忽略 **表数据（初始值）** 参数，并创建一个新的输入端口 `Tin`。使用此端口输入表数据。

**表数据（初始值）**
:   初始表输出值。此 (n-D) 数组的大小必须为 (n-1)-by-(n-1) ... -by- (n-1)（D 次），其中 D 是维度数，n 是输入断点数。

**表编号数据**
:   分配给单元格的编号值。此向量必须与表数据数组大小相同，并且每个值都必须唯一。

**自适应方法**
:   选择 `Sample mean` 或 `Sample mean with forgetting`。Sample mean 对一个单元格内接收到的所有值求平均值。Sample mean with forgetting 为新数据赋予更大的权重。权重的大小由 **自适应增益** 参数确定。有关详细信息，请参阅“选择自适应方法”。

**自适应增益（0 到 1）**
:   一个 0 到 1 之间的数字，用于调节自适应过程中赋予新数据的权重。0 表示短记忆（最新数据成为表值），1 表示长记忆（对一个单元格内接收到的所有数据求平均值）。

**将自适应后的表设为输出**
:   选中此复选框会为自适应后的表创建一个额外的输出端口 `Tout`。

    **注意**

    Adaptive Lookup Table (n-D Stair Fit) 模块无法输出三维或更高维度的表。

**添加自适应启用/禁用/重置端口**
:   选中此复选框会创建一个额外的输入端口 `Enable`，用于启用、禁用或重置自适应查找表。应用于该端口的信号值为 `0` 时禁用自适应，信号值为 `1` 时启用自适应。将信号值设置为 `2` 会将表值重置为初始表数据。

**添加单元格锁定启用/禁用端口**
:   选中此复选框会创建一个额外的输入端口 `Lock`，用于在仿真运行期间仅更新指定的单元格。信号值为 `0` 时解锁指定的单元格，信号值为 `1` 时锁定指定的单元格。

**超出范围输入的操作**
:   选择 `Ignore`，或选择 `Adapt` 以在极端断点之外进行外推。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

任意维度的自适应查找表

Adaptive Lookup Table (nD Stair-Fit) 模块通过动态更新底层查找表来创建任意维度的自适应查找表。该模块使用系统的输出执行自适应调整。

每个索引参数都可以在一组自适应数据点内取值，这些数据点称为*断点*。每个维度中的断点定义一个*单元格*。其中一个维度内所有断点的集合定义一个*网格*。在 n 维情况下，每个单元格有 2n 个断点，并且是一个 (n-1) 超曲面。

您可以使用 Adaptive Lookup Table (nD Stair-Fit) 模块对具有 2 个或更多输入的时变系统进行建模。
