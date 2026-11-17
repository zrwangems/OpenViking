---
type: simulink-block
title: 'J1939 Network Configuration'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'J1939'
documentation_page: 'j1939networkconfiguration'
documentation_source_path: 'io_ref/j1939networkconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# J1939 Network Configuration

## 端口

R2025b 中未记录。

## 参数

### **Configuration name** — 为此 J1939 网络配置定义名称 `ConfigX`（默认）| 字符向量

默认值为 `ConfigX`，其中数字 `X` 根据现有模块的数量从 1 开始递增。

### **Database File** — 指定相对于当前文件夹的 J1939 数据库文件名 未设置（默认）| 字符向量

示例文件名，如果文件位于当前文件夹中，请输入 `J1939.dbc`；否则请输入包含文件名的完整路径，例如 `C:\work\J1939.dbc`。

数据库文件定义 J1939 参数组和节点。此文件必须采用 Vector Informatik GmbH 定义的 DBC 文件格式。

### **Enable address claiming** — 启用标准地址声明过程 on（默认）| off

选中（勾选开启）时，此参数允许 J1939 Node Configuration 模块使用标准地址声明过程来动态分配总线上节点的地址。

## 所属库

Simulink Real-Time / J1939 Communication Vehicle Network Toolbox / J1939 Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

定义 J1939 网络配置名称和数据库文件

J1939 Network Configuration 模块用于定义配置名称并指定关联的用户提供的 J1939 数据库。每个模型中可包含多个此模块，每个模块对应 CAN 总线上的一个唯一配置。

要使用此模块，您必须同时拥有 Vehicle Network Toolbox™ 和 Simulink® 软件的许可证。

J1939 通信模块支持使用 Simulink 加速模式和快速加速模式。您可以使用这些模式加速 Simulink 模型的执行。有关这些模式的详细信息，请参阅 Acceleration。

J1939 通信模块还支持具有有限部署能力的代码生成。代码生成需要与代码生成目标兼容的 C++ 编译器。有关当前支持的编译器列表，请参阅 Supported and Compatible Compilers。
