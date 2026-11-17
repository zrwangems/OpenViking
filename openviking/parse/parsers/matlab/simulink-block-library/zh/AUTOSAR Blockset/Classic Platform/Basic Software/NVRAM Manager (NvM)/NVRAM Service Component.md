---
type: simulink-block
title: 'NVRAM Service Component'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Basic Software / NVRAM Manager (NvM)'
documentation_page: 'nvramservicecomponent'
documentation_source_path: 'ref/nvramservicecomponent.html'
language: zh-CN
chinese_source: worker-translation
---

# NVRAM Service Component

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Block ID
  summary: 标识服务模块的 ID 1（默认）| 标量
  group: ''
- name: Maximum number of memory blocks
  summary: NvM 服务操作中使用的最大内存块数 10（默认）| 标量
  group: ''
- name: Initial Value
  summary: NvM 客户端端口的初始值 0（默认）| 实数有限标量或向量
  group: ''
```

### **Block ID** — 标识服务模块的 ID 1（默认）| 标量

RTE 选项卡表格列出了组件客户端端口及其到 NvM 服务模块 ID 的映射。表格中的每一行表示从基础软件调用方模块对 NvM 服务的一次调用。作用于同一 NvM 模块的调用使用相同的模块 ID。检查模块 ID 映射。有关将 NvM 客户端端口映射到模块 ID 的示例，请参阅 Simulate AUTOSAR Basic Software Services and Run-Time Environment。

### **Maximum number of memory blocks** — NvM 服务操作中使用的最大内存块数 10（默认）| 标量

指定 NvM 服务操作中使用的最大内存块数。

### **Initial Value** — NvM 客户端端口的初始值 0（默认）| 实数有限标量或向量

将 NvM 客户端端口的初始值指定为有限实值标量或向量。这些值必须是标量，或与输入信号具有相同的维度。
## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / NVRAM Manager (NvM)

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

### R2022b：NVRAM Service Component 模块的初始值

R2022b 使您能够为仿真期间由基础软件访问的 NVRAM 服务定义初始值。要配置初始值，您可以打开 NVRAM Service Component 模块参数，点击 **Initial Values** 选项卡，并为每个 NvM 客户端端口设置初始值。

## 描述

为仿真配置 AUTOSAR NVRAM 服务和运行时环境（RTE）

NVRAM Service Component 模块提供了 AUTOSAR 基础软件（BSW）调用方模块所支持的 NVRAM Manager（NvM）服务的参考实现。当与 NvM 调用方模块配合使用时，这些参考实现使您能够配置并运行 AUTOSAR NvM 服务调用的系统级或组合级仿真。

该模块具有预填充的参数，包括 RTE 模块 ID 参数和 NvM **NVRAM Properties** 参数。检查参数设置，并根据您使用 NvM 服务操作的方式考虑是否需要修改。
