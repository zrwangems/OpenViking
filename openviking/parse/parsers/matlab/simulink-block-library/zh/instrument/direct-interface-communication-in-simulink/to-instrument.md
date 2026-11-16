---
type: simulink-block
title: 'To Instrument'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: 'Direct Interface Communication in Simulink'
documentation_page: 'toinstrument'
documentation_source_path: 'toinstrument.html'
language: zh-CN
chinese_source: worker-translation
---

# To Instrument

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

**早于 R2006a 引入**

### R2024b：错误

当此模块添加到模型时，它会抛出错误。打开任何包含此模块的现有模型都会导致错误。由于此错误，模型无法进行仿真。您仍可以打开模块参数对话框并查看参数值。

请改用特定接口的模块：

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

与 Query Instrument 和 To Instrument 相比，这些特定接口的模块都支持附加属性并具有改进的性能。

### R2023b：将被移除

Query Instrument 和 To Instrument 模块将在未来版本中移除。

## 描述

（将被移除）将仿真数据发送到仪器
