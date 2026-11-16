---
type: simulink-block
title: 'J1939 Receive'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'J1939 Communication'
documentation_page: 'j1939receive'
documentation_source_path: 'ug/j1939receive.html'
language: zh-CN
chinese_source: official
---

# J1939 Receive

## 端口

### 输出

### **Data** — 数据输出 双精度值

根据 J1939 数据库文件中定义的 J1939 参数组，该模块可以具有多个数据输出信号端口。模块输出数据类型是 double。

### **Msg Status** — 报文接收状态 0 | 1

当在参数对话框中选中**输出新报文接收状态**复选框时，此端口在从 CAN 总线收到新报文时输出 `1`。否则，此端口输出 `0`。

## 参数

### **配置名称** — 要关联的 J1939 网络配置的名称 `ConfigX` (默认) | 字符向量

要关联的 J1939 网络配置的名称。此值用于访问对应的 J1939 数据库。只有在模型中定义并与指定的 J1939 网络配置关联的节点才会显示在“节点名称”列表中。如果找不到 J1939 网络配置，则该选项显示 `none`。

### **节点名称** — J1939 节点的名称 `NodeX` (默认) | 字符向量

J1939 节点的名称。下拉列表包括模型中的所有节点，包括自定义节点和来自数据库的节点。

### **参数组** — 来自数据库的参数组编号 (PGN) 和名称 字符向量

来自数据库的参数组编号 (PGN) 和名称。此列表的内容取决于 J1939 数据库文件指定的参数组。默认值为所选节点的第一个参数组。

如果更改 J1939 数据库文件中的任何参数组设置，请打开 J1939 Receive 模块对话框并选择相同的**参数组**，然后点击**确定**或**应用**。

### **信号** — 参数组中定义的信号 字符向量数组

参数组中定义的信号。系统会从数据库中读取**最小值**和**最大值**设置，但默认情况下模块不会去除超出此范围的信号值。

### **源地址过滤器** — 基于源地址过滤报文 `Allow all` (默认) | `Allow only`

基于源地址过滤报文的选项有：

- `Allow only` - 指定一个源地址。
- `Allow all` - 接受来自任何源地址的报文。此选项是默认选项。

### **目标地址过滤器** — 基于目标地址过滤出报文 `global and node specific` (默认) | `global only` | `node specific only`

基于目标地址过滤出报文：

- `global only` - 仅接收广播报文。
- `node specific only` - 仅接收发往此节点的报文。
- `global and node specific` - 接收所有广播和发往节点的报文。此选项是默认选项。

### **采样时间** — 仿真刷新率 `0.01` (默认) | 双精度值

仿真刷新率。指定仿真期间模块的采样时间。此值定义 J1939 Receive 模块更新其输出端口的频率。如果该模块位于触发子系统内或继承采样时间，请指定值 `-1`。您还可以为采样时间指定一个 MATLAB® 变量。默认值为 `0.01` 仿真秒。有关仿真采样时间的信息，请参阅硬件接口模型中的计时。

### **输出新报文接收状态** — 创建 Msg Status 输出 0 (默认) | 1

选中此复选框可创建一个 **Msg Status** 输出端口。其输出信号指示是否有新传入的报文，如果接收到新报文则显示 1，没有新报文时则显示 0。

## 所属库

Simulink Real-Time / J1939 Communication Vehicle Network Toolbox / J1939 Communication

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2015b 中推出**

## 描述

接收 J1939 参数组报文

J1939 Receive 模块从配置的 CAN 设备接收 J1939 报文。J1939 数据库文件定义节点和参数组。使用 J1939 Network Configuration 模块指定 J1939 数据库。

要使用此模块，您必须拥有 Vehicle Network Toolbox™ 和 Simulink® 软件的许可证。

J1939 通信模块支持使用 Simulink 加速和快速加速模式。通过使用这些模式，您可以加快 Simulink 模型的执行速度。有关这些模式的详细信息，请参阅加速 (Simulink)。

J1939 通信模块还支持具有有限部署功能的代码生成。代码生成需要与代码生成目标兼容的 C++ 编译器。有关支持的编译器的当前列表，请参阅支持和兼容的编译器。
