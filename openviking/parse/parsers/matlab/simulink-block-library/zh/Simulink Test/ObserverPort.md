---
type: simulink-block
title: 'Observer Port'
family: 'sltest'
product_id: 'sltest'
product_name: 'Simulink Test'
documentation_release: R2025b
official_category: ''
documentation_page: 'observerport'
documentation_source_path: 'ref/observerport.html'
language: zh-CN
chinese_source: worker-translation
---

# Observer Port

## 端口
```yaml
ports:
- name: Port_1
  summary: 映射信号 标量 | 向量
  direction: output
  data_types: double | single | Boolean | base integer | fixed point | enumerated | non-virtual bus
```

### 输出

### **Port\_1** — 映射信号 标量 | 向量

通过 Observer Port 流入 Observer 模型的映射信号。

**数据类型：** `double` | `single` | `Boolean` | `base integer` | `fixed point` | `enumerated` | `non-virtual bus`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink Test

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

以无线方式连接信号以用于验证

在 Observer 模型中包含 Observer Port 模块，以将信号从系统模型映射到 Observer 模型。Observer Port 模块只能在链接到 Observer Reference 模块的模型中使用。
