---
type: simulink-block
title: 'Connection Port'
family: 'utilities'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: ''
documentation_page: 'connectionport'
documentation_source_path: 'ref/connectionport.html'
language: zh-CN
chinese_source: worker-translation
---

# Connection Port

## 端口

R2025b 中未记录。

## 参数

PMC Port mask

#### PMC\_Port：用于子系统的物理建模连接端口模块

### **Port number** — 连接器端口编号 `1`（默认）| 标量

此字段用于标记由该模块创建的子系统连接器端口。单个子系统边界上的多个连接器端口需要不同的编号作为标签。

### **Port location on parent subsystem** — 父子系统上的端口位置。可选值：`left`（默认）| `Right`

使用此参数选择端口放置在父子系统边界的哪一侧。

## 所属库

RF Blockset / Equivalent Baseband / Input RF Blockset / Circuit Envelope / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2021b：Connection Port 模块图标已更新

从 R2021b 开始，Connection Port 模块图标已更新。当您打开在 R2021b 之前创建的包含 Connection Port 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

用于 RF 子系统的连接端口

Connection Port 模块放置在由 RF Blockset™ Equivalent Baseband 模块组成的子系统内部，在子系统边界上创建一个开放的圆形物理建模连接器端口 open round physical modeling connector。当它连接到连接线时，该端口变为实心 Solid physical modeling connector。

您可以使用连接线而非普通 Simulink® 信号线，将各个由 RF Blockset Equivalent Baseband 模块构成的模块和子系统相互连接。这些模块和子系统锚定在开放的圆形物理建模连接器端口 Round physical modeling connector ports 上。由 RF Blockset Equivalent Baseband 模块构建的子系统自动具有此类开放的圆形物理建模连接器端口。您可以通过向子系统中添加 Connection Port 模块来添加额外的连接器端口。
