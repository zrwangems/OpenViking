---
type: simulink-block
title: 'SLRT Overload Options'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2023b
official_category: 'Target Management'
documentation_page: 'slrtoverloadoptions'
documentation_source_path: 'io_ref/slrtoverloadoptions.html'
language: zh-CN
chinese_source: worker-translation
---

# SLRT Overload Options

## 端口
```yaml
ports:
- name: TID
  summary: 任务 ID int
  direction: input
- name: Count
  summary: 过载计数 int
  direction: output
```

### 输入

### **TID** — 任务 ID int

将模型中的任意信号连接到 TID（任务 ID）端口，该模块会将过载选项应用于该信号执行所在的模型任务。

**示例：**
`1`
### 输出

### **Count** — 过载计数 int

所选模型速率的 CPU 过载计数。
## 参数
```yaml
parameters:
- name: Startup Duration
  summary: 选择用于忽略 CPU 过载的启动步数 1（默认）| int
  group: ''
- name: Source
  summary: 选择启动期间的 CPU 过载输入 Tunable Parameter（默认）| Input Port
  group: ''
- name: Max Overloads
  summary: 选择最大 CPU 过载数 0（默认）| int
  group: ''
- name: Source
  summary: 选择启动后的 CPU 过载输入 Tunable Parameter（默认）| Input Port
  group: ''
- name: Enable TET Output
  summary: 启用输出 TET 数据 off（默认）| on
  group: ''
```

### **Startup Duration** — 选择用于忽略 CPU 过载的启动步数 `1`（默认）| int

忽略过载的启动执行步数。

#### 编程使用

```
startupDur
```

### **Source** — 选择启动期间的 CPU 过载输入 `Tunable Parameter`（默认）| `Input Port`

启动期间模型速率的 CPU 过载来源可以是可调参数或模块输入端口。

#### 编程使用

```
startupDurSrc
```

### **Max Overloads** — 选择最大 CPU 过载数 `0`（默认）| int

在执行停止之前接受的过载数。每个子速率都有单独的过载计数器。每个计数器分别与 **Max Overloads** 进行比较，而不是与计数器之和进行比较。

#### 编程使用

```
maxOverload
```

### **Source** — 选择启动后的 CPU 过载输入 `Tunable Parameter`（默认）| `Input Port`

启动后模型速率的 CPU 过载来源可以来自可调参数或模块输入端口。

#### 编程使用

```
maxOverloadSrc
```

### **Enable TET Output** — 启用输出 TET 数据 `off`（默认）| `on`

启用后，CPU 过载数据将输出，以便在 TET 监视器和 Simulation Data Inspector 中显示。

#### 编程使用

```
TETFlag
```
## 所属库

Simulink Real-Time / Target Management

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

选择 CPU 过载选项

SLRT Overload Options 模块为通过 TID 端口标识的模型速率配置 CPU 过载选项。该模块输出所标识速率的当前 CPU 过载计数。如果 **Enable TET Output** 参数为 `on`，则该模块输出 TET 数据，您可以在 Simulation Data Inspector 中将其标记为数据记录。

SLRT Overload Options 模块的图像，其中可选的 TET 输出已标记为在 Simulation Data Inspector 中记录
