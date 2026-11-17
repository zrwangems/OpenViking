---
type: simulink-block
title: 'J1939 Transmit'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'J1939'
documentation_page: 'j1939transmit'
documentation_source_path: 'io_ref/j1939transmit.html'
language: zh-CN
chinese_source: worker-translation
---

# J1939 Transmit

## 端口
```yaml
ports:
- name: Data
  summary: 输入数据信号
  direction: input
- name: Trigger
  summary: 使能报文发送 0 | 1
  direction: input
```

### 输入

### **Data** — 输入数据信号

根据 J1939 数据库文件中定义的 J1939 参数组和信号，该模块可以有多个数据输入端口。

### **Trigger** — 使能报文发送 0 | 1

使能该采样点的报文发送。值为 `1` 表示发送，值为 `0` 表示不发送。
## 参数
```yaml
parameters:
- name: Config name
  summary: 要关联的 J1939 网络配置名称 ConfigX（默认）| 字符向量
  group: ''
- name: Node name
  summary: J1939 节点名称 NodeX（默认）| 字符向量
  group: ''
- name: Parameter Group
  summary: 组编号（PGN）和名称 int8
  group: ''
- name: Signals
  summary: 参数组中定义的信号 字符向量数组
  group: ''
- name: PG Priority
  summary: 参数组优先级 int8
  group: ''
- name: Destination Address
  summary: 目标节点名称 int8
  group: ''
- name: Sample time
  summary: 仿真发送速率 -1（默认）| double
  group: ''
```

### **Config name** — 要关联的 J1939 网络配置名称 `ConfigX`（默认）| 字符向量

要关联的 J1939 网络配置名称。用于访问相应的 J1939 数据库。只有模型中定义并与指定 J1939 网络配置关联的节点才会出现在 Node name 列表中。如果未找到 J1939 网络配置，该选项显示 `none`。

### **Node name** — J1939 节点名称 `NodeX`（默认）| 字符向量

J1939 节点的名称。下拉列表包含模型中的所有节点，包括自定义节点和来自数据库的节点。

### **Parameter Group** — 组编号（PGN）和名称 int8

来自数据库的参数组编号（PGN）和名称。此列表的内容因 J1939 数据库文件指定的参数组而异。默认值为所选节点的第一个参数组。

如果在 J1939 数据库文件中更改了任何参数组设置，则必须打开 J1939 Transmit 模块对话框并选择相同的 **Parameter Group**，然后单击 **OK** 或 **Apply** 以更新模块中的参数组信息。

### **Signals** — 参数组中定义的信号 字符向量数组

参数组中定义的信号。**Min** 和 **Max** 设置从数据库中读取，但默认情况下该模块不会裁剪超出此范围的信号值。

### **PG Priority** — 参数组优先级 int8

参数组优先级，从数据库中读取。此优先级设置用于解决多个参数组同时在同一总线上发送时的冲突。如果发生冲突，优先级较低（值较高）的优先级组将停止发送。该值的范围为 0（最高优先级）到 7（最低优先级）。

### **Destination Address** — 目标节点名称 int8

目标节点的名称。默认值为数据库中定义的第一个节点，否则为 `Custom`。

对于自定义目标地址，可以将目标节点地址指定为 0–253。要广播到所有节点，请使用 `Custom` **Destination Address** 设置并将地址设为 `255`。

### **Sample time** — 仿真发送速率 `-1`（默认）| double

仿真发送速率，指定为仿真期间模块的采样时间。该值定义了 J1939 Transmit 模块发送报文的频率。当模块位于触发子系统内或继承采样时间时，使用默认值 `-1`。您也可以为采样时间指定 MATLAB® 变量。有关仿真采样时序的信息，请参阅 What Is Sample Time?。
## 所属库

Simulink Real-Time / J1939 Communication Vehicle Network Toolbox / J1939 Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

发送 J1939 报文

J1939 Transmit 模块发送一条 J1939 报文。J1939 数据库文件定义节点和参数组。您通过 J1939 Network Configuration 模块指定 J1939 数据库。

要使用此模块，您必须同时拥有 Vehicle Network Toolbox™ 和 Simulink® 软件的许可证。

J1939 通信模块支持使用 Simulink 加速模式和快速加速模式。您可以使用这些模式加速模型的执行。有关详细信息，请参阅 Acceleration。

J1939 通信模块还支持具有有限部署能力的代码生成。代码生成需要与代码生成目标兼容的 C++ 编译器。有关当前支持的编译器列表，请参阅 Supported and Compatible Compilers。
