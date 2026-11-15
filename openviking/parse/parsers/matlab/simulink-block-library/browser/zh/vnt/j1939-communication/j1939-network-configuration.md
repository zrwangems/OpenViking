---
type: simulink-block
title: 'J1939 Network Configuration'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'J1939 Communication'
documentation_page: 'j1939networkconfiguration'
documentation_source_path: 'ug/j1939networkconfiguration.html'
language: zh-CN
chinese_source: official
---

# J1939 Network Configuration

## 端口

R2025b 官方文档未提供。

## 参数

### **配置名称** — 定义此 J1939 网络配置的名称 `ConfigX` (默认) | 字符向量

默认值为 `ConfigX`，其中数字 `X` 从 1 开始，随现有模块的数量递增。

### **数据库文件** — 基于相对于当前文件夹的路径指定 J1939 数据库文件名 未设置 (默认) | 字符向量

示例文件名，如果文件位于当前文件夹中，请输入 `J1939.dbc`；否则输入具有文件名的完整路径，例如 `C:\work\J1939.dbc`。

数据库文件定义 J1939 参数组和节点。此文件必须采用 Vector Informatik GmbH 定义的 DBC 文件格式。

### **启用地址声明** — 启用标准地址声明过程 on (默认) | off

选择（选中）后，此参数允许 J1939 Node Configuration 模块使用标准地址声明过程来动态分配总线上节点的地址。

## 所属库

Simulink Real-Time / J1939 Communication Vehicle Network Toolbox / J1939 Communication

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2015b 中推出**

## 描述

定义 J1939 网络配置名称和数据库文件

您可以在 J1939 Network Configuration 模块中定义配置名称并指定相关联的由用户提供的 J1939 数据库。对于每个模型，可以包含多个模块，其中每个模块对应于 CAN 总线上的一个唯一配置。

要使用此模块，您必须拥有 Vehicle Network Toolbox™ 和 Simulink® 软件的许可证。

J1939 通信模块支持使用 Simulink 加速和快速加速模式。通过使用这些模式，您可以加快 Simulink 模型的执行速度。有关这些模式的详细信息，请参阅加速 (Simulink)。

J1939 通信模块还支持具有有限部署功能的代码生成。代码生成需要与代码生成目标兼容的 C++ 编译器。有关支持的编译器的当前列表，请参阅支持和兼容的编译器。
