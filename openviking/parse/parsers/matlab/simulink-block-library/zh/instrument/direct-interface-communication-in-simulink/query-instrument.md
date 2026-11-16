---
type: simulink-block
title: 'Query Instrument'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: 'Direct Interface Communication in Simulink'
documentation_page: 'queryinstrument'
documentation_source_path: 'queryinstrument.html'
language: zh-CN
chinese_source: worker-translation
---

# Query Instrument

## 端口

在 R2025b 中未记录。

## 参数

在 R2025b 中未记录。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

### R2024b: 错误

将模块添加到模型时，此模块会抛出错误。打开任何包含此模块的现有模型都会导致错误。由于此错误，无法对模型进行仿真。您仍然可以打开模块参数对话框并查看参数值。

请改用特定于接口的模块：

- Serial
  Configuration
- Serial Receive
- Serial Send
- TCP/IP
  Receive
- TCP/IP Send
- UDP Receive
- UDP Send
- VISA

这些特定于接口的模块都支持附加属性，并且与 Query Instrument 和 To Instrument 相比具有改进的性能。

### R2023b: 将被移除

Query Instrument 和 To Instrument Simulink 模块将被移除。

## 描述

（将被移除）查询或读取仪器数据
