---
type: simulink-block
title: 'XCP UDP Bypass'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'XCP / UDP'
documentation_page: 'xcpudpbypass'
documentation_source_path: 'io_ref/xcpudpbypass.html'
language: zh-CN
chinese_source: worker-translation
---

# XCP UDP Bypass

## 端口
```yaml
ports:
- name: Function-call
  summary: 旁路函数调用的函数调用
  direction: output
```

### 输出

### **Function-call** — 旁路函数调用的函数调用

将函数调用输出端口连接到包含一个数据采集列表的函数调用子系统。
## 参数
```yaml
parameters:
- name: Task Priority
  summary: QNX Neutrino 调度器中的任务优先级 191（默认）| 整数
  group: ''
- name: Sample Time
  summary: 采样时间 -1（默认）| double
  group: ''
```

### **Task Priority** — QNX Neutrino 调度器中的任务优先级 191（默认）| 整数

选择 QNX Neutrino 调度器的任务优先级。

### **Sample Time** — 采样时间 `-1`（默认）| double

选择采样时间。有关详细信息，请参阅子系统中的采样时间。
## 所属库

Vehicle Network Toolbox / XCP Communication / UDP Simulink Real-Time / XCP / UDP

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

XCP 通信模块支持代码生成，但部署可移植性有限，仅能在主机或 Simulink Real-Time 目标上运行。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关详细信息，请参阅支持的兼容编译器。

## 版本历史

**在 R2020b 中引入**

## 描述

将函数调用输出端口连接到函数调用子系统

XCP UDP Bypass 模块将函数调用输出端口连接到包含一个数据采集列表的函数调用子系统。当下游数据采集列表有新数据可用时，该模块发出函数调用。

将下游函数调用子系统视为旁路任务：

在 Simulink® Real-Time™ 中，旁路任务以指定的任务优先级异步执行。

在 Simulink 中，该模块以指定的采样率定期检查数据采集数据，并相应地执行旁路任务。
