---
type: simulink-block
title: 'PassThrough'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'passthrough'
documentation_source_path: 'ref/passthrough.html'
language: zh-CN
chinese_source: worker-translation
---

# PassThrough

## 端口
```yaml
ports:
- name: WaveIn
  summary: 输入基带信号 标量 | 向量
  direction: input
  data_types: double
- name: WaveOut
  summary: 未更改的输出电压 标量 | 向量
  direction: output
  data_types: double
```

### 输入

### **WaveIn** — 输入基带信号 标量 | 向量

输入基带信号，可以是逐样本指定的标量信号，也可以是冲激响应向量信号。

**数据类型：** `double`
### 输出

### **WaveOut** — 未更改的输出电压 标量 | 向量

未更改的输出电压。PassThrough 模块不以任何方式修改输入电压，并返回与输入相同的输出。

**数据类型：** `double`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

无修改地传播基带信号

PassThrough 模块无任何修改地传递输入信号。
该模块在 SerDes 系统中用作占位模块，并作为用户自定义模块的模板，以供在 SerDes Toolbox™ 中使用。
