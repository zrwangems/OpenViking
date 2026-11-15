---
type: simulink-block
title: 'C2803x LIN Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c2803xlintransmit'
documentation_source_path: 'ref/c2803xlintransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# C2803x LIN Transmit

## 端口

R2025b 中未记录。

## 参数

**Send checksum**
:   选中此复选框，以在校验字节的最后一个数据字段中包含校验和。LIN 2.0 实现需要此校验和。
    
    默认值为未选中（disabled）。

**Physical bus error interrupt**
:   LIN 控制器节点检测物理总线何时无法传送有效消息。例如，如果总线短路到地或短路到 VBAT。这会在网络上的所有 LIN 节点中置位物理总线错误标志。如果启用 **Physical bus error interrupt**，LIN 发送节点会响应物理总线错误标志生成中断。

**Bit error interrupt**
:   如果启用此选项，LIN 节点会比较其发送的数据和 LIN 总线上的数据。
    
    默认值为 `Disabled`。
    
    TXRX Error Detector Bit Monitor 会比较 LIN 发送 (LINTX) 和接收 (LINRX) 引脚上的数据位。如果数据不匹配，Bit Monitor 会置位位错误标志。启用此选项时，位错误标志还会产生位错误中断。

**Transmit buffer interrupt**
:   如果启用此选项，LIN 节点会在生成校验和并设置 Transmitter buffer register ready 标志时生成中断。
    
    默认值为 `Disabled`。

**Send checksum**
:   选中此复选框，以在校验字节的最后一个数据字段中包含校验和。LIN 2.0 实现需要此校验和。
    
    默认值为未选中（disabled）。

**Physical bus error interrupt**
:   LIN 控制器节点检测物理总线何时无法传送有效消息。例如，如果总线短路到地或短路到 VBAT。这会在网络上的所有 LIN 节点中置位物理总线错误标志。如果启用 **Physical bus error interrupt**，LIN 发送节点会响应物理总线错误标志生成中断。

**Bit error interrupt**
:   如果启用此选项，LIN 节点会比较其发送的数据和 LIN 总线上的数据。
    
    默认值为 `Disabled`。
    
    TXRX Error Detector Bit Monitor 会比较 LIN 发送 (LINTX) 和接收 (LINRX) 引脚上的数据位。如果数据不匹配，Bit Monitor 会置位位错误标志。启用此选项时，位错误标志还会产生位错误中断。

**Transmit buffer interrupt**
:   如果启用此选项，LIN 节点会在生成校验和并设置 Transmitter buffer register ready 标志时生成中断。
    
    默认值为 `Disabled`。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

通过串行通信接口 (SCI) 从目标向主机传输数据

# C2803x LIN Transmit

通过串行通信接口 (SCI) 从目标向主机传输数据

Local Interconnect Network (LIN) 总线实现了一个用于分布式汽车和工业应用的串行通信协议。特别是，LIN 服务于不需要 CAN 协议提供的带宽或鲁棒性的低成本应用。

C2803x LIN Transmit 模块接收三个输入：

- **ID**：为 LIN 发送节点设置 LIN ID 的值。
- **TX ID Mask**：为 LIN 发送节点设置 LIN ID mask 的值。
- **Data**：将此输入连接到数据源。

**注意**

许多 LIN 特定设置位于你的模型的 **Hardware Implementation** > **Target hardware resources** 下的 **Peripherals** > **LIN** 中。验证这些设置是否满足你的应用需求。

- C2803x LIN Transmit 模块
