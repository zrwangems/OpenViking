---
type: simulink-block
title: 'J1939 Receive'
family: 'j1939'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'J1939'
documentation_page: 'j1939receive'
documentation_source_path: 'io_ref/j1939receive.html'
language: zh-CN
chinese_source: worker-translation
---

# J1939 Receive

## 端口

### 输出

### **Data** — 数据输出 double

根据 J1939 数据库文件中定义的 J1939 参数组，
该模块可以有多个数据输出信号端口。模块输出数据
类型为 double。

### **Msg Status** — 消息接收状态 0 | 1

当您在参数对话框中选择 **Output New Message Received status**
复选框时，如果从 CAN 总线接收到新
消息，此端口输出 `1`。否则，此端口输出
`0`。

## 参数

### **Config name** — 要关联的 J1939 网络配置的名称 `ConfigX`（默认值）| character vector

要关联的 J1939 网络配置的名称。此值用于
访问对应的 J1939 数据库。只有模型中定义且
与指定 J1939 网络配置关联的节点才会出现在 Node name 列表中。
如果找不到任何 J1939 网络配置，该选项显示 `none`。

### **Node name** — J1939 节点的名称 `NodeX`（默认值）| character vector

J1939 节点的名称。下拉列表包括模型中的所有节点，
包括自定义节点和数据库中的节点。

### **Parameter Group** — 来自数据库的参数组编号 (PGN) 和名称 character vector

来自数据库的参数组编号 (PGN) 和名称。此
列表的内容因 J1939 数据库文件指定的参数组而异。
默认值为所选节点的第一个参数组。

如果您在 J1939 数据库文件中更改了任何参数组设置，请打开
J1939 Receive 模块对话框，选择相同的 **Parameter Group**，
然后单击 **OK** 或 **Apply**。

### **Signals** — 参数组中定义的信号 array of character vectors

参数组中定义的信号。**Min** 和
**Max** 设置从数据库读取，但默认情况下该模块
不会裁剪超出此范围的信号值。

### **Source Address Filter** — 基于源地址筛选消息 `Allow all`（默认值）| `Allow only`

基于源地址筛选消息包括：

- `Allow only` — 指定单个源地址。
- `Allow all` — 接受来自任何源地址的消息。
  此选项为默认值。

### **Destination Address Filter** — 基于目标地址筛选消息 `global and node specific`（默认值）| `global only` | `node specific only`

基于目标地址筛选消息：

- `global only` — 仅接收广播消息。
- `node specific only` — 仅接收寻址到
  此节点的消息。
- `global and node specific` — 接收所有广播和
  节点寻址消息。此选项为默认值。

### **Sample time** — 仿真刷新率 `0.01`（默认值）| double

仿真刷新率。指定仿真期间该模块的采样时间。
此值定义 J1939 Receive
模块更新其输出端口的频率。如果该模块位于触发子系统内或继承
采样时间，请指定值 `-1`。您还可以为采样时间指定
MATLAB® 变量。默认值为 `0.01`
仿真秒。有关仿真采样时序的信息，请参阅什么是采样时间？。

### **Output New Message Received status** — 创建 Msg Status 输出 0（默认值）| 1

选中此复选框可创建 **Msg Status** 输出端口。其
输出信号指示新的传入消息：收到新消息时显示 1，没有新消息时
显示 0。

## 所属库

Simulink Real-Time / J1939 Communication Vehicle Network Toolbox / J1939 Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

接收 J1939 参数组消息

J1939 Receive 模块从配置的 CAN 设备接收 J1939 消息。J1939
数据库文件定义节点和参数组。您使用
J1939 Network Configuration 模块指定 J1939 数据库。

要使用此模块，您必须同时拥有 Vehicle Network Toolbox™ 和 Simulink® 软件的许可证。

J1939 通信模块支持使用 Simulink 加速器和快速加速器模式。您可以使用这些模式加速
Simulink 模型的执行。有关这些模式的详细信息，请参阅加速。

J1939 通信模块还支持部署能力有限的代码生成。代码生成需要与代码
生成目标兼容的 C++ 编译器。有关当前支持的编译器列表，请参阅支持的兼容编译器。
