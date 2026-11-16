---
type: simulink-block
title: 'SLRT Overload Options'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Execution Parameters'
documentation_page: 'slrtoverloadoptions'
documentation_source_path: 'io_ref/slrtoverloadoptions.html'
language: zh-CN
chinese_source: official
---

# SLRT Overload Options

## 端口

### 输入

### **TID** — 任务 ID int

将模型中的任意信号连接至 TID（任务 ID）端口，该模块即会将过载选项应用于执行该信号的模型任务。

**示例:**  `1`
### 输出

### **Count** — 过载计数 int

所选型号速率的 CPU 超载计数。

## 参数

### **Startup Duration** — 选择启动步骤以忽略 CPU 过载 `1` (默认) | int

忽略重载的初始化执行步骤的数量。

#### 编程用法

```
startupDur
```

### **Source** — 启动时选择 CPU 过载输入 `Tunable Parameter` (默认) | `Input Port`

模型速率在启动期间的 CPU 过载源可能是可调参数或模块输入端口。

#### 编程用法

```
startupDurSrc
```

### **Max Overloads** — 选择最大 CPU 负载 `0` (默认) | int

在执行终止前允许的超载次数。每个子速率都有一个独立的超载计数器。每个计数器都与 **Max Overloads** 单独比较，而非与计数器的总和进行比较。

#### 编程用法

```
maxOverload
```

### **Source** — 启动后选择 CPU 过载输入 `Tunable Parameter` (默认) | `Input Port`

模型启动后 CPU 负载过高的根源可能来自可调参数或模块输入端口。

#### 编程用法

```
maxOverloadSrc
```

### **Enable TET Output** — 启用输出 TET 数据 `off` (默认) | `on`

启用后，CPU 过载数据将输出至 TET 监控器和仿真数据检查器进行显示。

#### 编程用法

```
TETFlag
```

## 所属库

Simulink Real-Time / Target Management

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

## 描述

选择 CPU 过载选项

SLRT Overload Options 模块用于配置通过 TID 端口识别的模型速率的 CPU 过载选项。该模块输出当前 CPU 超载计数，对应已识别的速率。如果 **Enable TET Output** 参数为 `on`，则该模块输出 TET 数据，您可在仿真数据检查器中将其标记为数据记录对象。

The SLRT Overload Options block may include an optional TET output you can mark for logging in the Simulation Data Inspector.
