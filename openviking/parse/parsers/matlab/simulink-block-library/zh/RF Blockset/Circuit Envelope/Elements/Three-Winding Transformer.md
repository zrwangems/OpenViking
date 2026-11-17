---
type: simulink-block
title: 'Three-Winding Transformer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'threewindingtransformer'
documentation_source_path: 'ref/threewindingtransformer.html'
language: zh-CN
chinese_source: worker-translation
---

# Three-Winding Transformer

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Inductance L1
  summary: 第一个电感器的电感值 1e-6 H（默认）| 非负标量整数
  group: ''
- name: Inductance L2
  summary: 第二个电感器的电感值 1e-6 H（默认）| 非负标量整数
  group: ''
- name: Inductance L3
  summary: 第三个电感器的电感值 1e-6 H（默认）| 非负标量整数
  group: ''
- name: Inductance L3
  summary: 第三个电感器的电感值 1e-6 H（默认）| 非负标量整数
  group: ''
- name: Coefficient of coupling K12
  summary: 第一个和第二个电感器的耦合系数 0.9（默认）| 非负标量整数
  group: ''
- name: Coefficient of coupling K13
  summary: 第一个和第三个电感器的耦合系数 0.9（默认）| 非负标量整数
  group: ''
- name: Coefficient of coupling K23
  summary: 第二个和第三个电感器的耦合系数 0.9（默认）| 非负标量整数
  group: ''
```

### **Inductance L1** — 第一个电感器的电感值 `1e-6 H`（默认）| 非负标量整数

第一个电感器的电感值，指定为非负标量整数，单位为亨利。从对应的下拉菜单中指定电感的单位。

**数据类型：** `double`

### **Inductance L2** — 第二个电感器的电感值 `1e-6 H`（默认）| 非负标量整数

第二个电感器的电感值，指定为非负标量整数，单位为亨利。从对应的下拉菜单中指定电感的单位。

**数据类型：** `double`

### **Inductance L3** — 第三个电感器的电感值 `1e-6 H`（默认）| 非负标量整数

第三个电感器的电感值，指定为非负标量整数，单位为亨利。从对应的下拉菜单中指定电感的单位。

**数据类型：** `double`

### **Inductance L3** — 第三个电感器的电感值 `1e-6 H`（默认）| 非负标量整数

第三个电感器的电感值，指定为非负标量整数，单位为亨利。从对应的下拉菜单中指定电感的单位。

**数据类型：** `double`

### **Coefficient of coupling K12** — 第一个和第二个电感器的耦合系数 `0.9`（默认）| 非负标量整数

第一个和第二个电感器的互感耦合系数，指定为介于 `0` 和 `1` 之间的非负标量整数

**数据类型：** `double`

### **Coefficient of coupling K13** — 第一个和第三个电感器的耦合系数 `0.9`（默认）| 非负标量整数

第一个和第三个电感器的互感耦合系数，指定为介于 `0` 和 `1` 之间的非负标量整数

**数据类型：** `double`

### **Coefficient of coupling K23** — 第二个和第三个电感器的耦合系数 `0.9`（默认）| 非负标量整数

第二个和第三个电感器的互感耦合系数，指定为介于 `0` 和 `1` 之间的非负标量整数

**数据类型：** `double`

**注意**

RF Blockset 环境可识别的最小非零电感值为 `1e-18` `H`。在仿真期间，对于指定在 `0` 和 `1e-18` `H` 之间的任何电感值和互感值，模块将使用 `1e-18` `H` 的值。
## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算 RF 信号之和

Three-Winding Transformer 模块在电路包络仿真环境中对三个耦合电感器进行建模。

该模块实现以下关系

v1(t)=L1ddt[i1(t)]+M12ddt[i2(t)]+M13ddt[i3(t)]v2(t)=M12ddt[i1(t)]+L2ddt[i2(t)]+M23ddt[i3(t)]v3(t)=M13ddt[i1(t)]+M23ddt[i2(t)]+L3ddt[i3(t)]Mpq=KpqLpLq

其中：

- *L*1、*L*2 和 *L*3 表示电感。
- *Mpq* 表示第 *p* 个和第 *q* 个电感器之间的互感，其耦合系数为 *Kpq*。
- *v*1(*t*)、*v*2(*t*) 和 *v*3(*t*) 表示在时间 *t* 时电感器端子两端的电压。
- *i*1(*t*)、*i*2(*t*) 和 *i*3(*t*) 表示在时间 *t* 时流过电感器的电流。该模块使用标准点号表示法来指示相对于正电压的正电流流动方向。

RF Blockset™ 电流和电压信号由 Configuration 模块中指定的每个频率 *fk* 处的同相 (*Ik*) 和正交 (*Qk*) 分量组成：

i(t)=∑{fk}(iIk(t)+j⋅iQk(t))ej(2πfk)tv(t)=∑{fk}(vIk(t)+j⋅vQk(t))ej(2πfk)t
