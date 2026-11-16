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
chinese_source: official
---

# System Requirements

## 端口

R2025b 官方文档未提供。

## 参数

**模块标题**
:   模型中系统需求列表的标题。默认标题是 `System Requirements`。您可以输入自定义标题，例如 `Engine Requirements`。

## 所属库

Requirements Toolbox

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2006a 之前推出**

## 描述

列出 Simulink 模型中的系统需求

System Requirements 模块列出了与模型或子系统相关的系统级需求。该模块是动态填充的。它显示与模型中模块出现的层次级别相关的系统需求。它没有列出与模型中各个块相关的需求。要在 System Requirements 模块中列出所需的需求链接：

1. 右键点击模型的背景。
2. 选择**此级别的需求**。
3. 从上下文菜单的顶部，验证您想要列出的所有需求是否出现在 System Requirements 模块中。

您可以将此模块放置在模型中的任何位置。它不连接到其他 Simulink® 块。在给定的子系统中只能有一个 System Requirements 模块。

当您将此模块插入到您的 Simulink 模型中时，它会填充系统需求。

A System Requirements block with one requirement

列出的每个需求都是指向需求文档的活动链接。双击需求标签时，相关的需求文档将在其编辑器窗口中打开，并滚动到目标位置。
