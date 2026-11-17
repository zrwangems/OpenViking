---
type: simulink-block
title: 'Entity Output Switch'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entityoutputswitch'
documentation_source_path: 'ref/entityoutputswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Output Switch

## 端口

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

进入模块的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **control** — 传入控制实体 标量

传入控制实体的输入控制端口，该控制实体确定从模块离开的实体的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出实体 标量 | 向量 | 矩阵

离开模块的实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_2** — 输出实体 标量 | 向量 | 矩阵

离开模块的实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## 参数

### **Number of output ports** — 指定输出端口数量 2（默认）| 标量

实体离开的输出端口数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberOutputPorts` |
| **类型**：character vector |
| **值**：`'2'` | scalar |
| **默认值**：`'2'` |

### **Switching criterion** — 选择切换准则 `First port that is not blocked`（默认）| `Round robin` | `From control port` | `From attribute` | `Equiprobable`

选择输出端口之间的切换准则。

- 要将实体输出到第一个未被阻塞的端口，请选择 `First port
  即未被阻塞`。

  假设一个示例，到达 Entity Output Switch 模块的实体通过第一个未被阻塞的实体输出端口离开，只要至少有一个实体输出端口未被阻塞。这种方法的一个日常示例是，单个人群队列等待由多个银行柜员、收银员、呼叫中心代表等之一提供服务。队列中的每个人都希望尽快前进到第一个可用的服务提供者，而不偏好其中任何一个。
- 要以轮询方式在输出端口之间输出实体，请选择
  `Round robin`。
- 选择 `From control port` 以让控制端口确定实体离开的选定端口。将出现一个控制端口，用于输入携带数据的匿名实体，其值大于
  `0` 且小于或等于输出端口数量，以确定活动端口。
- 要指定确定输出端口的属性，请选择
  `From attribute`。属性值大于
  `0` 且小于或等于输出端口数量，以确定活动端口。

  考虑包裹根据指定收件人的位置在多个配送车辆之间进行分拣的情况。如果每个包裹是一个实体，则可以将数据附加到每个实体以指示其收件人的位置。
- 要随机选择实体离开的输出端口，请选择
  `Equiprobable`。设置 **Seed** 以生成随机数并确定活动输出端口。

**注意**

模块将双精度值舍入为小于或等于其值的最接近整数作为端口选择。例如，值 `0.3`
被舍入为 `0`，这不是端口选择的有效值。

#### 编程使用

|  |
| --- |
| **模块参数**：`SwitchingCriterion` |
| **类型**：character vector |
| **值**：`'First port that is not blocked'` | `'Round robin'` | `'From control port'` | `'From attribute'` | `'Equiprobable'` |
| **默认值**：`'First port that is not blocked'` |

### **Initial port selection** — 指定仿真开始时的输出端口 1（默认）| 标量

选择实体离开时的初始端口。

#### 依赖关系

当 **Switching criterion** 设置为 `Round robin` 或 `From control port` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialPortSelection` |
| **类型**：字符向量 |
| **值**：`'1'` | 标量 |
| **默认值**：`'1'` |

### **Switch Attribute name** — 指定确定输出端口的属性 `Attribute1`（默认）| 字符向量

指定用于切换输出端口的属性名称。

#### 依赖关系

当 **Switching criterion** 设置为 `From attribute` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`SwitchAttributeName` |
| **类型**：字符向量 |
| **值**：`'Attribute1'` | 字符向量 |
| **默认值**：`'Attribute1'` |

### **Seed** — 指定种子 `34567`（默认）| 标量

指定随机数生成器的种子以确定输出端口。

#### 依赖关系

当 **Switching criterion** 设置为 `Equiprobable` 时，此参数可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`Seed` |
| **类型**：字符向量 |
| **值**：`'34567'` | 标量 |
| **默认值**：`'34567'` |

## 所属库

SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

输出实体

Entity Output Switch 模块允许您在多个实体输出端口中为实体的离开选择一个输出端口。所选端口可以在仿真过程中发生变化，您可以选择在输出端口之间切换的准则。

以下是一些可能使用输出开关的场景：

- 实体基于效率或公平性考虑前进到多个队列之一。例如，飞机根据队列长度前进到多条跑道之一，或者顾客前进到多个收银员中第一个可用的收银员。

  比较不同的效率或公平性方法，通过测试不同的规则来确定输出开关的所选输出端口，可能是您仿真系统目标的一部分。有关示例，请参阅 Route Vehicles Using an Entity Output Switch Block。
- 实体根据其特征前进到特定目的地。例如，包裹根据指定收件人的位置前进到多辆配送车辆之一。
- 实体在首选路径被阻塞时使用备用路径。例如，通信网络在到发射机的路径被阻塞时丢弃数据包，仿真收集有关丢弃数据包的统计信息。

或者，您可以使用 Entity Gate 模块来控制特定实体路径上实体的流动。有关详细信息，请参阅 Using Entity Priority to Sequence Departures。

### 限制

实体输出端口的总数必须小于 128。要对超过 128 个端口进行建模，请并行或串联使用多个 Entity Output Switch 模块。
