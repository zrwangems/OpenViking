---
type: simulink-block
title: 'Component'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Architectures, Requirements, and Allocations / Author Architecture Models'
documentation_page: 'component'
documentation_source_path: 'ref/component.html'
language: zh-CN
chinese_source: official
---

# Component

## 端口

### 输入

### **Source** — 来自其他组件的输入连接 接口

如果连接到源组件，则端口上的接口是共享的。
### 输出

### **Destination** — 与其他组件的输出连接 接口

如果连接到目标组件，则端口上的接口是共享的。
### 物理

### **Physical** — 与另一个组件的物理连接 物理接口

如果连接到另一个组件，则端口上的物理接口是共享的。

## 参数

R2025b 官方文档未提供。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2019a 中推出**

## 描述

为架构模型添加组件

使用 Component 模块来表示架构模型层次结构中任何一级的结构或行为元素。

为模块添加端口，以便与其他组件连接。为端口定义接口，使用构造型添加与组件相关的属性，并定义参数。

Component block

添加或连接 System Composer™ 组件：

- 从**建模**选项卡或调色板中添加一个 Component 架构模块。您也可以点击并拖动画布上的方框，然后选择 Component 模块。
- 要添加端口，请选择组件的一条边，然后从菜单中选择一个方向：`Input`、`Output` 或 `Physical`
- 点击并拖动端口以创建连接。连接到另一个组件。您还可以创建一个新组件来完成连接。
- 要将 Component 模块连接到架构或组合模型根端口，可从组件端口拖动到包含模型的边界。释放连接时，会在边界创建一个根端口。
- 要添加组件级参数，请使用参数编辑器工具。

**注意**

您可以为组件添加封装图标，以说明组件所代表的系统。有关详细信息，请参阅在组件上添加封装图标。
