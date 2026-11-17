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
chinese_source: worker-translation
---

# J1939 Receive

## 端口
```yaml
ports:
- name: Data
  summary: 数据输出 double
  direction: output
- name: Msg Status
  summary: 消息接收状态 0 | 1
  direction: output
```

### 输出

### **Data** — 数据输出 double

根据 J1939 数据库文件中定义的 J1939 参数组，该模块可以有多个数据输出信号端口。模块输出数据类型为 double。

### **Msg Status** — 消息接收状态 0 | 1

当您在参数对话框中选择 **Output New Message Received status** 复选框时，当从 CAN 总线接收到新消息时，此端口输出 `1`。否则，此端口输出 `0`。
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
  summary: 来自数据库的参数组编号（PGN）和名称 字符向量
  group: ''
- name: Signals
  summary: 参数组中定义的信号 字符向量数组
  group: ''
- name: Source Address Filter
  summary: 基于源地址过滤消息 Allow all（默认）| Allow only
  group: ''
- name: Destination Address Filter
  summary: 基于目标地址过滤消息 global and node specific（默认）| global only | node specific only
  group: ''
- name: Sample time
  summary: 仿真刷新率 0.01（默认）| double
  group: ''
- name: Output New Message Received status
  summary: 创建 Msg Status 输出 0（默认）| 1
  group: ''
```

### **Config name** — 要关联的 J1939 网络配置名称 `ConfigX`（默认）| 字符向量

要关联的 J1939 网络配置名称。此值用于访问相应的 J1939 数据库。只有模型中定义并与指定 J1939 网络配置关联的节点才会出现在 Node name 列表中。如果未找到 J1939 网络配置，该选项显示 `none`。

### **Node name** — J1939 节点名称 `NodeX`（默认）| 字符向量

J1939 节点名称。下拉列表包含模型中的所有节点，包括自定义节点和来自数据库的节点。

### **Parameter Group** — 来自数据库的参数组编号（PGN）和名称 字符向量

来自数据库的参数组编号（PGN）和名称。此列表的内容因 J1939 数据库文件指定的参数组而异。默认值为所选节点的第一个参数组。

如果您在 J1939 数据库文件中更改了任何参数组设置，请打开 J1939 Receive 模块对话框，选择相同的 **Parameter Group**，然后单击 **OK** 或 **Apply**。

### **Signals** — 参数组中定义的信号 字符向量数组

参数组中定义的信号。**Min** 和 **Max** 设置从数据库中读取，但默认情况下该模块不会裁剪超出此范围的信号值。

### **Source Address Filter** — 基于源地址过滤消息 `Allow all`（默认）| `Allow only`

基于源地址过滤消息的选项包括：

- `Allow only` — 指定单个源地址。
- `Allow all` — 接受来自任何源地址的消息。此选项为默认值。

### **Destination Address Filter** — 基于目标地址过滤消息 `global and node specific`（默认）| `global only` | `node specific only`

基于目标地址过滤消息的选项包括：

- `global only` — 仅接收广播消息。
- `node specific only` — 仅接收发往此节点的消息。
- `global and node specific` — 接收所有广播消息和节点寻址消息。此选项为默认值。

### **Sample time** — 仿真刷新率 `0.01`（默认）| double

仿真刷新率。指定仿真期间模块的采样时间。此值定义了 J1939 Receive 模块更新其输出端口的频率。如果模块位于触发子系统内或继承采样时间，请指定值 `-1`。您也可以为采样时间指定 MATLAB® 变量。默认值为 `0.01` 仿真秒。有关仿真采样时序的信息，请参阅 Timing in Hardware Interface Models。

### **Output New Message Received status** — 创建 Msg Status 输出 0（默认）| 1

选中此复选框以创建 **Msg Status** 输出端口。其输出信号指示新的传入消息，接收到新消息时显示 1，没有新消息时显示 0。
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

J1939 Receive 模块从配置的 CAN 设备接收 J1939 消息。J1939 数据库文件定义节点和参数组。您通过 J1939 Network Configuration 模块指定 J1939 数据库。

要使用此模块，您必须同时拥有 Vehicle Network Toolbox™ 和 Simulink® 软件的许可证。

J1939 通信模块支持使用 Simulink 加速和快速加速模式。您可以使用这些模式加速 Simulink 模型的执行。有关这些模式的详细信息，请参阅 Acceleration (Simulink)。

J1939 通信模块还支持具有有限部署能力的代码生成。代码生成需要与代码生成目标兼容的 C++ 编译器。有关当前支持的编译器列表，请参阅 Supported and Compatible Compilers。
