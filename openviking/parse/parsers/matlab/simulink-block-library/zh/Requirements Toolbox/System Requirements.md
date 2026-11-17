---
type: simulink-block
title: 'System Requirements'
family: 'slrequirements'
product_id: 'slrequirements'
product_name: 'Requirements Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'systemrequirements'
documentation_source_path: 'ref/systemrequirements.html'
language: zh-CN
chinese_source: worker-translation
---

# System Requirements

## 端口

R2025b 中未记录。

## 参数

**模块标题**
:   模型中系统需求列表的标题。默认标题为 `System Requirements`。您可以输入自定义标题，例如 `Engine Requirements`。

## 所属库

Requirements Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

在 Simulink 模型中列出系统需求

System Requirements 模块列出与模型或子系统关联的系统级需求。此模块是动态填充的。它显示与模块在模型中所处层级相关联的系统需求。它不会列出与模型中各个模块相关联的需求。要在 System Requirements 模块中列出所需的需求链接：

1. 右键单击模型的背景。
2. 选择 **Requirements at This Level**。
3. 从上下文菜单顶部，确认您想要列出的所有需求都显示在 System Requirements 模块中。

您可以将此模块放置在模型中的任意位置。它不会连接到其他 Simulink® 模块。在给定的子系统中，您只能有一个 System Requirements 模块。

当您将此模块插入 Simulink 模型时，它会填充系统需求。

包含一个需求的 System Requirements 模块

列出的每个需求都是指向需求文档的活动链接。当您双击需求标签时，关联的需求文档会在其编辑器窗口中打开，并滚动到目标位置。
