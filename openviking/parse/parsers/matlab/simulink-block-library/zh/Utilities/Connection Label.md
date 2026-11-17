---
type: simulink-block
title: 'Connection Label'
family: 'circuit-envelope'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: 'Circuit Envelope / Utilities'
documentation_page: 'connectionlabel'
documentation_source_path: '../simrf/ref/connectionlabel.html'
language: zh-CN
chinese_source: worker-translation
---

# Connection Label

## 端口

### 输入

### **Port\_1** — 连接端口 未类型化电路包络端口

电路包络连接端口。默认情况下，此端口为未类型化。

您通过将此端口连接到子系统内另一个模块的电路包络端口来定义端口类型。建立连接后，同一子系统中具有相同标签的其他 Connection Label 模块只能连接到相同类型的端口。

## 参数

### **Label** — 连接标签的名称 `Label1`（默认） | character vector | string

标签名称，用于建立虚拟连接。如果模型同一子系统中的两个或多个 Connection Label 模块具有相同标签，则连接到它们的模块的电路包络端口表现得如同物理连接一样。

此参数的值在模型画布上显示为模块图标旁边的标签。

## 所属库

RF Blockset / Circuit Envelope / Utilities Simscape / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022a 中引入**

## 描述

电路包络端口之间的虚拟连接

Connection Label 模块允许您指定电路包络端口之间的虚拟连接，类似于 Simulink® 图中的 Goto 和 From 模块。这些连接线是无方向的，这意味着虚拟连接的所有端都使用相同类型的模块。

虚拟连接由标签名称建立。如果模型子系统中的两个或多个 Connection Label 模块具有相同标签，则连接到它们的其他模块的电路包络端口表现得如同物理连接一样。虚拟连接不能跨越子系统边界。标签名称显示在模型画布上模块图标旁边。

您可以使用 **Label** 参数指定标签名称。

使用 Connection Label 模块断开缠结的连接线，以减少图杂乱。

您可以选择 Connection Label 模块以突出显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请将鼠标悬停在省略号上。然后，从操作栏中选择 **Related Blocks**
Related Blocks 按钮。当多个模块与所选模块对应时，将打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将切换到显示该相关模块的打开的图或新选项卡。
