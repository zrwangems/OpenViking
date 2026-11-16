---
type: simulink-block
title: 'C2803x LIN Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2803x'
documentation_page: 'c2803xlinreceive'
documentation_source_path: 'ref/c2803xlinreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# C2803x LIN Receive

## 端口

R2025b 中未记录。

## 参数

**数据类型**
:   选择 LIN 模块输出到模型的数据类型。可用选项包括 `single`、`int8`、`uint8`、`int16`、`uint16`、`int32` 或 `uint32`。要解释数据，数据类型和数据长度必须与发送 LIN 节点的数据输入相匹配。

    默认值为 `int16`。

**数据长度**
:   设置 LIN 模块输出到模型的数据长度。此值以 **数据类型** 的倍数衡量。例如，如果 **数据类型** 为 `int16` 且 **数据长度** 为 `int16`，则 LIN 模块向模型输出的数据长度为

    1 x int16

    如果将 **数据长度** 设置为大于 1 的值，模块会将数据作为向量输出。

    要解释数据，数据类型和数据长度必须与发送 LIN 节点的数据输入相匹配。

    默认值为 1。

    **注意**

    在环回配置中，最大数据长度不能超过 8 bytes。如果传入和传出数据的总和超过 LIN 模块的硬件缓冲区长度，模块将丢弃传入的数据字节。

**初始输出**
:   设置 LIN 节点接收到数据之前，DATA 端口输出到模型的初始值。

    默认值为 `0`。

**连接超时时的操作**
:   指定当连接超时时，LIN 模块在 DATA 端口上输出什么。选项包括：

    - `Output the last received value` — DATA 端口输出 LIN 节点接收到的最后一个数据值。
    - `Output custom value` — DATA 端口输出由 **连接超时时的输出值** 定义的值。

    默认值为 `Output the last received value`。

    如果 LIN 节点尚未接收到数据，并且将此参数设置为 `Output the last received value`，则 DATA 端口输出 **初始输出** 值。

**连接超时时的输出值**
:   指定当 **连接超时时的操作** 设置为 `Output custom value` 且发生连接超时时，DATA 端口输出的自定义值。

**启用阻塞模式**
:   如果启用（选中）此复选框，目标应用程序会停止并等待 LIN 节点接收数据后再继续。如果禁用此选项，应用程序会继续运行，不会等待数据到达。

    默认值为 disabled（未选中）。

**验证校验和**
:   如果启用（选中）此选项，LIN 节点会验证其接收到的校验和。

    默认值为 disabled（未选中）。

**输出接收状态**
:   启用（选中）此复选框会向 LIN Receive 模块添加一个 `status` 输出，如下图所示。

    对于 LIN 节点接收到的每条消息，`status` 输出会报告以下值：

    - `0`：无错误。
    - `-1`：模块等待接收数据时发生超时。
    - `-2`：无法接收。
    - 其他状态值表示 SCI Flags Register 的最高 8 位。将这些值从十进制转换为二进制。然后参考 *TMS320F2803x Piccolo Local Interconnect Network (LIN) Module* 中的 Table 14. SCI Flags Register (SCIFLR) Field Descriptions 来确定这些值的含义，文献编号 SPRUGE2，可从 Texas Instruments® 网站获取。

**接收缓冲区中断**
:   如果启用此选项，SCI 节点在接收到完整帧后会生成中断。默认值为 `Disabled`。

**校验和错误中断**
:   如果启用此选项，当传入消息包含无效校验和时，LIN 模块会生成中断。

    默认值为 `Disabled`。

    TXRX Error Detector Checksum Calculator 会验证传入消息的校验和。在经典 LIN 实现中，校验和仅覆盖数据字段。对于符合 LIN 2.0 的消息，校验和包括 ID 字段和数据字段。如果启用此选项，Checksum Calculator 在检测到校验和错误（例如由 LIN 消息冲突引起的错误）时会生成中断。

**帧错误中断**
:   如果启用此选项，当发生帧错误时，LIN 模块会生成中断。

    默认值为 `Disabled`。

**溢出错误中断**
:   如果启用此选项，当发生溢出错误时，LIN 模块会生成中断。

    默认值为 `Disabled`。

**ID 奇偶校验错误中断**
:   如果启用此选项，当 LIN 模块接收到无效 ID 时，会生成 ID-Parity 中断。

    默认值为 `Disabled`。

    如果启用此选项，还需在 Hardware Implementation -> Target Hardware Resources 中启用 **Parity mode**。

**ID 匹配中断**
:   如果启用此选项，当 LIN 节点验证其接收到的消息中的 ID 时，LIN 模块会生成中断。

    默认值为 `Disabled`。

**采样时间**
:   设置模块的输入采样时间 `Ts`。

    默认值为 `0.1` seconds。

**数据类型**
:   选择 LIN 模块输出到模型的数据类型。可用选项包括 `single`、`int8`、`uint8`、`int16`、`uint16`、`int32` 或 `uint32`。要解释数据，数据类型和数据长度必须与发送 LIN 节点的数据输入相匹配。

    默认值为 `int16`。

**数据长度**
:   设置 LIN 模块输出到模型的数据长度。此值以 **数据类型** 的倍数衡量。例如，如果 **数据类型** 为 `int16` 且 **数据长度** 为 `int16`，则 LIN 模块向模型输出的数据长度为

    1 x int16

    如果将 **数据长度** 设置为大于 1 的值，模块会将数据作为向量输出。

    要解释数据，数据类型和数据长度必须与发送 LIN 节点的数据输入相匹配。

    默认值为 1。

    **注意**

    在环回配置中，最大数据长度不能超过 8 bytes。如果传入和传出数据的总和超过 LIN 模块的硬件缓冲区长度，模块将丢弃传入的数据字节。

**初始输出**
:   设置 LIN 节点接收到数据之前，DATA 端口输出到模型的初始值。

    默认值为 `0`。

**连接超时时的操作**
:   指定当连接超时时，LIN 模块在 DATA 端口上输出什么。选项包括：

    - `Output the last received value` — DATA 端口输出 LIN 节点接收到的最后一个数据值。
    - `Output custom value` — DATA 端口输出由 **连接超时时的输出值** 定义的值。

    默认值为 `Output the last received value`。

    如果 LIN 节点尚未接收到数据，并且将此参数设置为 `Output the last received value`，则 DATA 端口输出 **初始输出** 值。

**连接超时时的输出值**
:   指定当 **连接超时时的操作** 设置为 `Output custom value` 且发生连接超时时，DATA 端口输出的自定义值。

**启用阻塞模式**
:   如果启用（选中）此复选框，目标应用程序会停止并等待 LIN 节点接收数据后再继续。如果禁用此选项，应用程序会继续运行，不会等待数据到达。

    默认值为 disabled（未选中）。

**验证校验和**
:   如果启用（选中）此选项，LIN 节点会验证其接收到的校验和。

    默认值为 disabled（未选中）。

**输出接收状态**
:   启用（选中）此复选框会向 LIN Receive 模块添加一个 `status` 输出，如下图所示。

    对于 LIN 节点接收到的每条消息，`status` 输出会报告以下值：

    - `0`：无错误。
    - `-1`：模块等待接收数据时发生超时。
    - `-2`：无法接收。
    - 其他状态值表示 SCI Flags Register 的最高 8 位。将这些值从十进制转换为二进制。然后参考 *TMS320F2803x Piccolo Local Interconnect Network (LIN) Module* 中的 Table 14. SCI Flags Register (SCIFLR) Field Descriptions 来确定这些值的含义，文献编号 SPRUGE2，可从 Texas Instruments® 网站获取。

**接收缓冲区中断**
:   如果启用此选项，SCI 节点在接收到完整帧后会生成中断。默认值为 `Disabled`。

**校验和错误中断**
:   如果启用此选项，当传入消息包含无效校验和时，LIN 模块会生成中断。

    默认值为 `Disabled`。

    TXRX Error Detector Checksum Calculator 会验证传入消息的校验和。在经典 LIN 实现中，校验和仅覆盖数据字段。对于符合 LIN 2.0 的消息，校验和包括 ID 字段和数据字段。如果启用此选项，Checksum Calculator 在检测到校验和错误（例如由 LIN 消息冲突引起的错误）时会生成中断。

**帧错误中断**
:   如果启用此选项，当发生帧错误时，LIN 模块会生成中断。

    默认值为 `Disabled`。

**溢出错误中断**
:   如果启用此选项，当发生溢出错误时，LIN 模块会生成中断。

    默认值为 `Disabled`。

**ID 奇偶校验错误中断**
:   如果启用此选项，当 LIN 模块接收到无效 ID 时，会生成 ID-Parity 中断。

    默认值为 `Disabled`。

    如果启用此选项，还需在 Hardware Implementation -> Target Hardware Resources 中启用 **Parity mode**。

**ID 匹配中断**
:   如果启用此选项，当 LIN 节点验证其接收到的消息中的 ID 时，LIN 模块会生成中断。

    默认值为 `Disabled`。

**采样时间**
:   设置模块的输入采样时间 `Ts`。

    默认值为 `0.1` seconds。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

通过目标上的本地互连网络 (LIN) 模块接收数据

# C2803x LIN Receive

通过目标上的本地互连网络 (LIN) 模块接收数据

本地互连网络 (LIN) 总线为分布式汽车和工业应用实现了一种串行通信协议。特别地，LIN 服务于不需要 CAN 协议提供的带宽或鲁棒性的低成本应用。

LIN Receive 模块配置目标以从 LINRX 或 LINTX 引脚接收标量或向量数据。

每个 C2803x 目标有一个 LIN 模块。对于每个模块，您的模型中只能包含一个 LIN Transmit 和一个 LIN Receive 模块。

C2803x LIN Transmit 模块有三个输入：

- **ID**：设置 LIN 发送节点的 LIN ID 值。
- **TX ID Mask**：设置 LIN 发送节点的 LIN ID 掩码值。
- **Data**：将此输入连接到数据源。

有关更多信息和示例，请参阅：

- 配置 LIN 通信
- 基于 LIN 的 PWM 占空比控制

**注意**

许多 LIN 特定设置位于模型的 Hardware Implementation -> Target Hardware Resources 中的 **Peripherals** > **LIN** 下。请验证这些设置满足应用程序的要求。

- C2803x LIN Receive block
