---
type: simulink-block
title: 'Variant Connector'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: ''
documentation_page: 'variantconnector'
documentation_source_path: '../simscape/ref/variantconnector.html'
language: zh-CN
chinese_source: worker-translation
---

# Variant Connector

## 端口

### 守恒端口

### **Port\_1** — 条件端口 无类型 conserving 端口

此端口位于模块左侧，并用矩形标记。在仿真期间，如果与该模块关联的变体选择求值为 `true`，则连接到此端口的所有组件都将变为活动状态。如果与该模块关联的变体选择求值为 `false`，则连接到此端口的所有组件都将变为非活动状态。

默认情况下，此端口为无类型。您可以通过将此端口连接到另一个模块的 conserving 端口、网络中的组件或 Simscape Bus 端口来定义此端口的类型。

### **Port\_2** — 连接端口 无类型 conserving 端口

Conserving 连接端口。默认情况下，此端口为无类型。

您可以通过将端口连接到另一个模块的 conserving 端口、网络中的组件或 Simscape Bus 端口来定义该端口的类型。

## 参数

### **Connector Type** — 连接器模块的类型 `Leaf`（默认）| `Primary` | `Nonprimary`

根据要停用的组件选择连接器类型。

- `Leaf`：如果要停用连接到该模块的所有组件，请将 **Connector Type** 设置为 `Leaf`。

  例如，在此模型中，与 Variant Connector 模块 ConneBlk1 关联的变体条件为 `A == 1`。与 Variant Connector 模块 ConneBlk2 关联的变体条件为 `B == 1`。在仿真期间，当 `A == 1` 求值为 `true` 且 `B == 1` 求值为 `false` 时，连接到 ConneBlk1 模块的所有组件都将变为活动状态，而连接到 ConneBlk2 模块的所有组件都将变为非活动状态。

  停用连接到 Leaf 类型 Variant Connector 模块的所有组件
- `Primary and Nonprimary`：如果要将变体条件的传播限制到一组组件，请使用 primary 和 nonprimary 连接器模块创建 Bounded region。要形成有界区域，primary 和 nonprimary 连接器模块必须具有相同的 **Connector Tag** 属性。

  当您将 **Connector Type** 设置为 `Primary` 或 `Nonprimary` 时，模块的连接器标签将显示在模块图标上。primary 连接器模块的连接器标签以双线显示，nonprimary 连接器模块的连接器标签以单线显示。

  一个 primary Variant Connector 模块以及所有与该 primary 模块具有相同 **Connector Tag** 的 nonprimary Variant Connector 模块构成一组相关模块。

  您可以选择一个 primary 或 nonprimary Variant Connector 模块，以高亮显示所有相关的 Variant Connector 模块。

  在模型画布中高亮显示的模块也会在小地图中高亮显示。

  要在打开的图中显示相关模块，请暂停在选中后出现的省略号上。然后，从操作栏中选择 **Related Blocks** Related Blocks 按钮。。当多个模块对应于所选模块时，将打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示该相关模块的已打开图或新选项卡。

不同连接器类型的 Variant Connector 模块的模块图标

### **Connector Tag** — 有界区域的唯一标识符 `A`（默认）| 以字母开头、不包含空格或特殊字符且长度最多为 2048 个字符的有效 MATLAB® 标识符

在 **Connector Tag** 参数中指定一个标识符。具有相同标签的 primary 和 nonprimary 连接器模块构成一个 Bounded region。

#### 依赖关系

要启用此参数，请将 **Connector Type** 设置为 `Primary` 或 `Nonprimary`。

### **变体控制表达式** — 全局工作区中可用的变体控制 `true`（默认）| 布尔条件表达式

显示全局工作区中可用的变体控制。变体控制可以是包含常规 MATLAB 变量的布尔条件表达式，也可以是表示布尔条件表达式的 `Simulink.VariantExpression` 对象。

要编辑变体名称，请双击 **变体控制表达式** 单元格并输入变体控制表达式。编辑变体控制名称后，点击 **应用**。

当与模块关联的变体控制求值为 `true` 时，连接到该模块的所有组件将变为活动状态。

#### 程序化使用

|  |
| --- |
| **模块参数：** `VariantControls` |
| **类型：** 字符向量元胞数组 |
| **值：** 与变体选择关联的变体控制 |
| **默认：** `'Variant'` |

### **条件（只读）** — 变体控制的条件 无默认值

此只读字段基于全局工作区中关联变体控制的条件。在 `Simulink.VariantExpression` 参数对话框或全局工作区中创建或更改变体条件。

有关详细信息，请参阅 `Simulink.VariantExpression`。

### **在模块上显示变体条件** — 在模块图标上显示变体条件 关（默认）| 开

选择 **在模块上显示变体条件** 以在模块图标上显示与模块关联的变体条件。

### **在变体管理器中打开模块** — 打开变体管理器窗口 无默认值

点击 **在变体管理器中打开模块** 以打开变体管理器。

## 所属库

Simscape / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

代码仅针对模型中的活动模块生成。非活动模块不参与代码生成。

## 版本历史

**在 R2020b 中引入**

## 描述

从网络中移除或断开物理组件

变体连接器模块允许您在物理网络中定义变体选择。变体选择允许您从仿真中排除某些组件，而无需从物理网络中实际移除这些组件。要断开的组件必须连接到与条件数据关联的端口。在仿真期间，变体条件会传播到物理网络中的所有已连接组件。如果与模块关联的变体控制求值为 `true`，则连接到该模块的所有组件将变为活动状态。如果变体控制求值为 `false`，则连接到该模块的所有组件将变为非活动状态。
