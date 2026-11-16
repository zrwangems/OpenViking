---
type: simulink-block
title: 'Connection Label'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Utility Blocks'
documentation_page: 'connectionlabel'
documentation_source_path: 'ref/connectionlabel.html'
language: zh-CN
chinese_source: worker-translation
---

# Connection Label

## 端口

### 守恒

### **Port\_1** — 连接端口，未指定类型的守恒端口

守恒连接端口。默认情况下，此端口未指定类型。

您可以通过将端口连接到子系统中另一个模块的守恒端口，或连接到 Simscape Bus 端口来定义端口类型。建立连接后，同一子系统中具有相同标签的其他 Connection Label 模块只能连接到相同类型的端口。

## 参数

### **Label** — 连接标签的名称 `Label1`（默认） | character vector | string

标签名称，用于建立虚拟连接。如果模型的同一子系统中的两个或多个 Connection Label 模块具有相同的标签，则连接到它们的模块的守恒端口的行为就像它们物理连接一样。

此参数的值作为标签显示在模型画布上的模块图标旁边。

## 所属库

Simscape / Utilities RF Blockset / Circuit Envelope / Utilities

## 模块特性

R2025b 中未记载。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

守恒端口之间的虚拟连接

Connection Label 模块允许您在 Simscape™ 守恒端口之间指定虚拟连接，类似于 Simulink® 图中的 Goto 和 From 模块。这些连接线是无方向的，这意味着虚拟连接的所有侧都使用相同类型的模块。

您还可以使用 Connection Label 模块指定其他类型的无方向端口之间的虚拟连接，例如 Simscape Bus 端口或 Simscape Multibody™ frame、geometry 和 belt-cable 端口。

虚拟连接由标签名称建立。如果模型子系统中的两个或多个 Connection Label 模块具有相同的标签，则连接到它们的其他模块的守恒端口的行为就像它们物理连接一样。虚拟连接不能跨子系统边界。

标签名称显示在模型画布上的模块图标旁边。您可以使用 **Label** 参数指定标签名称。

使用 Connection Label 模块可以通过断开缠结的连接线来减少图面杂乱。

您可以选择一个 Connection Label 模块来突出显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请将鼠标悬停在省略号上。然后，从操作栏中选择 **Related Blocks** Related Blocks 按钮。当多个模块对应于所选模块时，将打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示该相关模块的打开的图或新选项卡。
