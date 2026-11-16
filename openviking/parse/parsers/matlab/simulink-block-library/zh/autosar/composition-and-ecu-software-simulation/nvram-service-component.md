---
type: simulink-block
title: 'NVRAM Service Component'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'nvramservicecomponent'
documentation_source_path: 'ref/nvramservicecomponent.html'
language: zh-CN
chinese_source: official
---

# NVRAM Service Component

## 端口

R2025b 官方文档未提供。

## 参数

### **模块 ID** — 标识服务模块的 ID 1 (默认) | 标量

RTE 选项卡下的表列出了组件客户端端口及其到 NvM 服务模块 ID 的映射。表中的每行表示一个从基础软件调用方模块对 NvM 服务的调用。作用于同一 NvM 模块的多个调用使用相同的模块 ID。检查模块 ID 映射。有关将 NvM 客户端端口映射到模块 ID 的示例，请参阅对 AUTOSAR 基础软件服务和运行时环境进行仿真。

### **最大内存块数** — 在 NvM 服务操作中使用的最大内存块数 10 (默认) | 标量

指定在 NvM 服务操作中使用的最大内存块数。

### **初始值** — NvM 客户端端口的初始值 0 (默认) | 实数有限标量或向量

将 NvM 客户端端口的初始值指定为有限实数值标量或向量。值必须为标量，或具有与输入信号相同的维度。

## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / NVRAM Manager (NvM)

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2017b 中推出**

### R2022b: NVRAM Service Component 模块的初始值

R2022b 使您能够定义在仿真期间由基础软件访问的 NVRAM 服务的初始值。要配置初始值，您可以打开 NVRAM Service Component 模块参数，点击**初始值**选项卡，并为每个 NvM 客户端端口设置初始值。

## 描述

配置 AUTOSAR NVRAM 服务和运行时环境 (RTE) 以进行模拟

NVRAM Service Component 模块提供由 AUTOSAR 基础软件 (BSW) 调用方模块支持的 NVRAM Manager (NvM) 服务的参考实现。当与 NvM 调用方模块结合使用时，参考实现使您能够配置和运行 AUTOSAR NvM 服务调用的系统级或组合级仿真。

该模块具有预填的参数，包括 RTE 模块 ID 参数和 NvM **NVRAM 属性**参数。请检查参数设置，并根据您使用 NvM 服务操作的方式考虑是否需要修改。
