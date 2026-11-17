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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**First input (row) breakpoint set**
:   包含第一个输入变量可能的模块输入值的向量。第一个输入向量必须单调递增。

**Second input (column) breakpoint set**
:   包含第二个输入变量可能的模块输入值的向量。第二个输入向量必须单调递增。

**将初始表设为输入**
:   选中此复选框会强制 Adaptive Lookup Table (2D Stair-Fit) 模块忽略 **表数据（初始）** 参数，并创建一个新的输入端口 `Tin`。使用此端口输入表数据。

**表数据（初始）**
:   初始表输出值。此 2×2 矩阵的大小必须为 (n-1)×(m-1)，其中 n 是第一个输入断点的数量，m 是第二个输入断点的数量。

**表编号数据**
:   分配给单元格的编号值。此矩阵必须与表数据矩阵大小相同，且每个值必须唯一。

**Adaptation method**
:   选择 `Sample mean` 或 `Sample mean with forgetting`。Sample mean 对单元格内接收到的所有值求平均。Sample mean with forgetting 对新数据赋予更大的权重。权重的大小由 **Adaptation gain** 参数决定。有关详细信息，请参阅 Selecting an Adaptation Method。

**Adaptation gain (0 to 1)**
:   一个 0 到 1 之间的数字，用于调节自适应过程中赋予新数据的权重。0 表示短记忆（最后一个数据成为表值），1 表示长记忆（对单元格内接收到的所有数据求平均）。

**将适配表设为输出**
:   选中此复选框会为自适应表创建一个额外的输出端口 `Tout`。

**Add adaptation enable/disable/reset port**
:   选中此复选框会创建一个额外的输入端口 `Enable`，用于启用、禁用或重置自适应查找表。施加到该端口的信号值为 `0` 时禁用自适应，信号值为 `1` 时启用自适应。将信号值设置为 `2` 会将表值重置为初始表数据。

**Add cell lock enable/disable port**
:   选中此复选框会创建一个额外的输入端口 `Lock`，用于在仿真运行期间仅更新指定的单元格。信号值为 `0` 时解锁指定的单元格，信号值为 `1` 时锁定指定的单元格。

**超出范围输入的操作**
:   通过外推超出极端断点来 `Ignore` 或 `Adapt`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

二维自适应查找表

Adaptive Lookup Table (2D Stair-Fit) 模块通过动态更新底层查找表来创建二维自适应查找表。该模块使用系统的输出 *y* 来进行自适应。

每个索引参数 *u* 可以在称为*断点*的一组自适应数据点中取值。每个维度中的两个断点定义一个*单元格*。其中一个维度中所有断点的集合定义一个*网格*。在二维情况下，每个单元格有四个断点，并且是一个平坦表面。

您可以使用 Adaptive Lookup Table (2D Stair-Fit) 模块对具有两个输入的时变系统进行建模。
