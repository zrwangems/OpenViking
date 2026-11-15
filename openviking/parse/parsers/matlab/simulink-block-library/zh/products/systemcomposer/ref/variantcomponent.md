---
type: simulink-block
title: 'Variant Component'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Architectures, Requirements, and Allocations / Variant Components in Architecture Models'
documentation_page: 'variantcomponent'
documentation_source_path: 'ref/variantcomponent.html'
language: zh-CN
chinese_source: official
---

# Variant Component

## 端口

### 输入

### **Source** — 来自其他组件的输入连接 接口

如果连接到源组件，则端口上的接口是共享的。
### 输出

### **Destination** — 与其他组件的输出连接 接口

如果连接到目标组件，则端口上的接口是共享的。

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

添加替代设计的组件

使用 Variant Component 模块为一个组件创建多个设计方案。

为模块添加端口，以便与其他组件连接。为端口定义接口，使用构造型添加与组件相关的属性，并定义参数。

Variant Component block

添加或连接 System Composer™ 组件：

- 从**建模**选项卡或调色板中添加一个 Variant Component 架构模块。您也可以点击并拖动画布上的方框，然后选择 Variant Component 模块。您也可以从 Component 模块或 Reference Component 模块创建变体组件。右键点击组件，选择**添加变体选择项**。
- 要添加端口，请选择组件的一条边，然后从菜单中选择一个方向：`Input` 或 `Output`
- 点击并拖动端口以创建连接。连接到另一个组件。您还可以创建一个新组件来完成连接。
- 要将 Variant Component 模块连接到架构或组合模型根端口，可从组件端口拖动到包含模型的边界。释放连接时，会在边界创建一个根端口。

**注意**

您可以为组件添加封装图标，以说明组件所代表的系统。有关详细信息，请参阅在组件上添加封装图标。

管理 Variant Component 选择项：

- 默认情况下，创建 Variant Component 模块时会创建两个变体选择项。右键点击 Variant Component 模块并选择 **变体** > **标签模式活动选择项**，然后选择活动选择项。
- 要添加额外的变体选择项，请右键点击 Variant Component 模块，然后选择 **变体** > **添加变体选择项**。
- 双击 Variant Component 模块，设计其中的变体。
- 使用变体管理器可在复杂的模型层次结构中轻松切换变体选择项。右键点击 Variant Component 图模块，然后选择 **变体** > **在变体管理器中打开**。有关详细信息，请参阅Variant Manager for Simulink。
