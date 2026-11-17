---
type: simulink-block
title: 'Moments about CG due to Forces'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Mass Properties'
documentation_page: 'momentsaboutcgduetoforces'
documentation_source_path: 'momentsaboutcgduetoforces.html'
language: zh-CN
chinese_source: worker-translation
---

# Moments about CG due to Forces

## 端口
```yaml
ports:
- name: F
  summary: 施加的力 三元向量
  direction: input
  data_types: double
- name: CG
  summary: 重心 三元向量
  direction: input
  data_types: double
- name: CP
  summary: 力的作用点 三元向量
  direction: input
  data_types: double | bus
- name: M
  summary: 重心处的力矩 三元向量
  direction: output
  data_types: double
```

### 输入

### **F** — 施加的力 三元向量

施加在点 CP 处的力，指定为三元向量。

**数据类型：** `double`

### **CG** — 重心 三元向量

重心，指定为三元向量。

**数据类型：** `double`

### **CP** — 力的作用点 三元向量

力的作用点，指定为三元向量。

**数据类型：** `double` | `bus`
### 输出

### **M** — 重心处的力矩 三元向量

重心处沿 *x* 轴、*y* 轴和 *z* 轴的力矩，以三元向量形式返回。

**数据类型：** `double`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Aerospace Blockset / Mass Properties

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算由施加在某一点（非重心）的力引起的绕重心的力矩

Moments about CG due to Forces 模块计算由施加在点 CP 处（而非重心处）的力引起的绕重心的力矩。
