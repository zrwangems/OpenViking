---
type: simulink-block
title: 'Environment'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Virtual Vehicles'
documentation_page: 'environment'
documentation_source_path: 'ref/environment.html'
language: zh-CN
chinese_source: worker-translation
---

# Environment

## 端口

### 输入

### **ExtEnv** — 外部驾驶员参考 `Bus`

外部环境信号。

#### 依赖项

要创建此端口，请选择 **Environment**。

### **ExtGrd** — 外部驾驶员命令 `Bus`

外部地面信号。

#### 依赖项

要创建此端口，请选择 **Ground**。
### 输出

### **Env** — 环境信号 `Bus`

包含环境信号的 Bus。

## 参数

### **Environment** — 启用外部环境输入 `off` (默认) | `on`

指定创建外部环境输入端口 `ExtEnv`。

### **Ground** — 启用外部地面输入 `off` (默认) | `on`

指定创建外部地面输入端口 `ExtGnd`。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

配置环境

Environment 模块实现环境模型，包括道路坡度、风速以及环境温度和压力。该子系统包含生成特定于环境和地形的信号的变体。选择 **Environment** 以输入外部环境信号。选择 **Ground** 以输入外部地面信号。

此外，您可以在运行时将工作区变量 `ExtEnvSwitch` 和 `ExtGndSwitch` 设置为 `true` 或 `false`，以控制外部或内部生成的信号。当运行需要外部和内部机动的多个仿真，或覆盖标称模型生成的信号时，请考虑使用这些开关值。
