---
type: simulink-block
title: 'J1939 Node Configuration'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'J1939'
documentation_page: 'j1939nodeconfiguration'
documentation_source_path: 'io_ref/j1939nodeconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# J1939 Node Configuration

## 端口

### 输出

### **Address** — 返回节点的有效地址 int8

当您在对话框中选择 **Output current node address** 复选框时，此可选输出端口存在。

### **AC Status** — 指示节点地址声明的成功 (1) 或失败 (0) 0 | 1

当您在对话框中选择 **Output address claim status** 复选框时，此可选输出端口存在。

## 参数

### **Config name** — 要与此节点关联的 J1939 网络配置的 ID `ConfigX`（默认）| 字符向量

要访问相应的 J1939 数据库，请使用此 ID。

### **Node name** — 此 J1939 节点的名称 `NodeX`（默认）| 字符向量

如果未找到 J1939 网络配置或关联数据库中未定义节点，则可用列表显示 `none`。如果您正在创建自定义节点，则节点名称在其 J1939 网络配置中必须唯一。

### **Message** — 由与 J1939 协议一致的数据库文件定义的九个网络属性 向量数组

除非您正在定义自定义节点，否则这些参数为只读：

- **Allow arbitrary address** — 允许/禁止节点在站地址不可用时切换到任意地址。如果此选项关闭且节点失去其地址声明，则节点将静默。

  **Node Address** — 站地址，十进制，8 位。
- **Industry Group** — 十进制，3 位。
- **Vehicle System** — 十进制，7 位。
- **Vehicle System Instance** — 标识给定网络中给定车辆系统的特定出现。如果网络中仅存在某个车辆系统的一个实例，则此字段必须设置为 0 以将其定义为第一个实例。十进制，4 位。
- **Function ID** — 十进制，8 位。
- **Function Instance** — 标识车辆系统和给定网络中给定功能的特定出现。如果网络中仅存在某个功能的一个实例，则此字段必须设置为 0 以将其定义为第一个实例。十进制，5 位。
- **ECU Instance** — 当多个电子控制单元 (ECU) 参与执行单个功能时，使用此 3 位字段。如果特定控制器应用 (CA) 仅使用一个 ECU，则此字段必须设置为 0 以将其定义为第一个实例。
- **Manufacturer Code** — 十进制，11 位。
- **Identity Number** — 十进制，21 位。

### **Sample time** — 仿真刷新率 0.01（默认）| double

指定仿真期间模块的采样时间。此值定义 J1939 Node Configuration 更新其可选输出端口的频率。如果模块位于触发子系统内或继承采样时间，请指定值 `-1`。您还可以为采样时间指定 MATLAB® 变量。默认值为 `0.01` 仿真秒。有关仿真采样时序的信息，请参阅 What Is Sample Time?。

### **Output current node address** — 启用或禁用 Address 端口显示 `off`（默认）| `on`

启用或禁用 **Address** 输出端口以显示有效地址。有效地址与预定义站地址不同。如果选择了 **Allow arbitrary address**，则发生名称冲突，并且当前节点具有较低优先级。输出信号为 0 到 253 的 double 值。此端口默认禁用。

### **Output address claim status** — 启用或禁用地址声明 AC Status 显示 `off`（默认）| `on`

启用或禁用地址声明 **AC Status** 输出端口以显示地址声明的成功。输出值为二进制，1 表示成功，0 表示失败。此端口默认禁用。

## 所属库

Simulink Real-Time / J1939 Communication Vehicle Network Toolbox / J1939 Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

使用地址和网络管理属性配置 J1939 节点

J1939 Node Configuration 模块用于定义节点并将其与特定网络配置关联。除非您创建并配置自定义节点，否则其 Message information 将从该配置的数据库中读取。

要使用此模块，您必须同时拥有 Vehicle Network Toolbox™ 和 Simulink® 软件的许可证。

J1939 通信模块支持使用 Simulink 加速模式和快速加速模式。您可以使用这些模式加速 Simulink 模型的执行。有关这些模式的详细信息，请参阅 Acceleration。

J1939 通信模块还支持具有有限部署能力的代码生成。代码生成需要与代码生成目标兼容的 C++ 编译器。有关当前支持的编译器列表，请参阅 Supported and Compatible Compilers。
