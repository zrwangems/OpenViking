---
type: simulink-block
title: 'PassThrough'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Design and Simulate SerDes Systems / Signal Modification'
documentation_page: 'passthrough'
documentation_source_path: 'ref/passthrough.html'
language: zh-CN
chinese_source: worker-translation
---

# PassThrough

## 端口

### 输入

### **WaveIn** — 输入基带信号 标量 | 向量

输入基带信号，可以是按样本指定的标量信号，或冲激响应向量信号。

**数据类型：** `double`
### 输出

### **WaveOut** — 未改变的输出电压 标量 | 向量

未改变的输出电压。PassThrough 模块不以任何方式修改输入电压，并返回与输入相同的输出。

**数据类型：** `double`

## 参数

未在 R2025b 中记录。

## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

不作修改地传播基带信号

PassThrough 模块不作任何修改地传递输入信号。此模块在 SerDes 系统中用作占位符，并用作供在 SerDes Toolbox™ 中使用的用户编写模块的模板。
