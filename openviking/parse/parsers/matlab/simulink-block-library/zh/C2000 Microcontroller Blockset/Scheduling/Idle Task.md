---
type: simulink-block
title: 'Idle Task'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Scheduling'
documentation_page: 'idletaskblock'
documentation_source_path: 'ref/idletaskblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Idle Task

## 端口
```yaml
ports:
- name: Port_1
  summary: 仅用于仿真的端口 标量
  direction: input
  data_types: SoCData
- name: data
  summary: 空闲任务数据向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | bus
```

### 输入

### **Port\_1** — 仅用于仿真的端口 标量

将一个或多个仿真中断源连接到此仿真输入。

#### 依赖关系

此端口仅在启用 **Enable simulation port** 参数时出现。

**数据类型：** `SoCData`
### 输出

### **data** — 空闲任务数据向量

空闲任务的输出是一个 uint16 值向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `bus`
## 参数
```yaml
parameters:
- name: Task numbers
  summary: 通过编号标识所创建的任务 double（默认）| single | int8 | int16 | int32 | int64 | int64 | uint8 | uint16 | uint32 | uint64 | uint64
    | Boolean | bus
  group: ''
- name: Preemption flags
  summary: 存储缓冲区数量 1（默认）| 正整数
  group: ''
- name: Enable simulation port
  summary: 启用外设仿真端口以进行阻塞 off（默认）| on
  group: ''
```

### **Task numbers** — 通过编号标识所创建的任务 `double`（默认）| `single` | `int8` | `int16` | `int32` | `int64` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `uint64` | `Boolean` | `bus`

通过编号标识所创建的任务。输入一个整数向量即可指定所需数量的任务。默认值为 [1,2]，表示下游子系统具有两个函数。

输入的值决定了下游子系统中函数的执行顺序，而输入值的数量对应于下游子系统中的函数数量。

输入的向量所包含的元素数量应与下游子系统中的函数数量相同。该向量最多可包含 16 个元素，且值必须在 0 到 15 之间（含 0 和 15）。

向量中第一个元素的值决定了子系统中第一个函数的执行顺序，第二个元素的值决定了子系统中第二个函数的执行顺序，依此类推。

例如，在此字段中输入 [2,3,1] 表示有三个函数要执行，第三个函数最先执行，第一个函数第二个执行，第二个函数第三个执行。函数执行完毕后，Idle Task 模块会循环返回，并按相同顺序重复执行这些函数。

### **Preemption flags** — 存储缓冲区数量 `1`（默认）| 正整数

较高优先级的中断可以抢占优先级较低的中断。为了便于您控制抢占，可使用抢占标志来指定某个中断是否可以被抢占。

输入 `1` 表示该中断可以被抢占。输入 `0` 表示该中断不能被抢占。当 **Task numbers** 包含多个任务时，您可以通过输入一个标志值向量来为每个任务分配不同的抢占标志，该向量与 **Task numbers** 中任务的顺序相对应。如果 **Task numbers** 包含多个任务，而您在此处只输入一个标志值，则该状态适用于所有任务。

在默认设置 `[0 1]` 下，**Task numbers** 中优先级为 `1` 的任务不可被抢占，而优先级为 `2` 的任务可以被抢占。

### **Enable simulation port** — 启用外设仿真端口以进行阻塞 `off`（默认）| `on`

选中此选项后，Simulink 软件会向 Idle Task 模块添加一个输入端口。此端口仅用于仿真。将一个或多个仿真中断源连接到此仿真输入。

**注意**

选中此复选框可在 Simulink 软件中测试异步中断处理行为。
## 所属库

C2000 Microcontroller Blockset / Scheduling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

创建自由运行任务

Idle Task 模块及其所连接的子系统指定一个或多个作为后台任务执行的函数。通过 Idle Task 模块执行的任务具有最低优先级，低于基本速率任务的优先级。

### 向量化输出

模块输出由一组向量组成——任务编号向量和抢占标志向量。抢占标志向量的长度必须与任务编号向量的长度相同，除非抢占标志向量只有一个元素。抢占标志的值决定了给定中断（及任务）是否可被抢占。抢占会覆盖优先级排序。优先级较低但不可抢占的任务可以抢占优先级较高但可抢占的任务。

当抢占标志向量只有一个元素时，该元素值适用于下游子系统中的函数，具体由任务编号向量中的任务编号定义。如果抢占标志向量的元素数量与任务编号向量的元素数量相同，则任务编号向量中定义的每个任务都具有由抢占标志向量中对应元素的值所定义的抢占状态。
