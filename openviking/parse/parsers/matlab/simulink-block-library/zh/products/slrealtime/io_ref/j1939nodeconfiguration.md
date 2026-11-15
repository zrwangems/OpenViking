---
type: simulink-block
title: 'J1939 Node Configuration'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / J1939'
documentation_page: 'j1939nodeconfiguration'
documentation_source_path: 'io_ref/j1939nodeconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# J1939 Node Configuration

## 端口

### 输出

### **Address** — 返回节点的有效地址 int8

当您在对话框中选中 **输出当前节点地址** 复选框时，此可选输出端口存在。

### **AC Status** — 指示节点地址声明的成功 (1) 或失败 (0) 0 | 1

当您在对话框中选中 **输出地址声明状态** 复选框时，此可选输出端口存在。

## 参数

### **配置名称** — 要与此节点关联的 J1939 网络配置的 ID `ConfigX`（默认）| character vector

要访问相应的 J1939 数据库，请使用此 ID。

### **节点名称** — 此 J1939 节点的名称 `NodeX`（默认）| character vector

如果未找到 J1939 网络配置，或关联的数据库中未定义节点，则可用列表显示 `none`。如果要创建自定义节点，则节点名称在其 J1939 网络配置中必须唯一。

### **报文** — 与 J1939 协议一致的数据库文件定义的九个网络属性 vector array

除非您要定义自定义节点，否则这些参数为只读：

- **允许任意地址** — 允许/禁止节点在站地址不可用时切换到任意地址。如果此选项为 off，并且节点失去其地址声明，则该节点将静默。

  **节点地址** — 站地址，Decimal，8-bit。
- **行业组** — Decimal，3-bit。
- **车辆系统** — Decimal，7-bit。
- **车辆系统实例** — 标识给定网络中给定车辆系统的某一个特定实例。如果网络中仅存在某个车辆系统的一个实例，则此字段必须设置为 0，以将其定义为第一个实例。Decimal，4-bit。
- **功能 ID** — Decimal，8-bit。
- **功能实例** — 标识车辆系统和给定网络中给定函数的特定实例。如果网络中仅存在某个函数的一个实例，则此字段必须设置为 0，以将其定义为第一个实例。Decimal，5-bit。
- **ECU 实例** — 当多个电子控制单元 (ECU) 参与执行单个功能时，使用此 3-bit 字段。如果特定控制器应用 (CA) 仅使用一个 ECU，则此字段必须设置为 0，以将其定义为第一个实例。
- **制造商代码** — Decimal，11-bit。
- **标识号** — Decimal，21-bit。

### **采样时间** — 仿真刷新率 0.01（默认）| double

指定仿真期间模块的采样时间。此值定义 J1939 Node Configuration 更新其可选输出端口的频率。如果模块位于触发子系统内或继承采样时间，请指定值 `-1`。您还可以为采样时间指定 MATLAB® 变量。默认值为 `0.01` simulation seconds。有关仿真采样计时的信息，请参阅 What Is Sample Time?。

### **输出当前节点地址** — 启用或禁用 Address 端口显示 `off`（默认）| `on`

启用或禁用 **Address** 输出端口以显示有效地址。有效地址不同于预定义的站地址。如果选中 **允许任意地址**，则发生名称冲突，并且当前节点具有较低优先级。输出信号为 0 到 253 的 double 值。默认情况下，此端口处于禁用状态。

### **输出地址声明状态** — 启用或禁用地址声明 AC Status 显示 `off`（默认）| `on`

启用或禁用地址声明 **AC Status** 输出端口以显示地址声明的成功情况。输出值为二进制，1 表示成功，0 表示失败。默认情况下，此端口处于禁用状态。

## 所属库

Simulink Real-Time / J1939 Communication Vehicle Network Toolbox / J1939 Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2015b 中引入**

## 描述

使用地址和网络管理属性配置 J1939 节点

J1939 Node Configuration 模块用于定义节点并将其与特定网络配置关联。除非您要创建和配置自定义节点，否则其报文信息将从该配置的数据库中读取。

要使用此模块，您必须同时拥有 Vehicle Network Toolbox™ 和 Simulink® 软件的许可证。

J1939 通信模块支持使用 Simulink 加速模式和快速加速模式。您可以使用这些模式加快 Simulink 模型的执行速度。有关这些模式的详细信息，请参阅 Acceleration。

J1939 通信模块还支持具有有限部署功能的代码生成。代码生成需要与代码生成目标兼容的 C++ 编译器。有关当前支持的编译器列表，请参阅 Supported and Compatible Compilers。
