---
type: simulink-block
title: 'Walsh Code Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Sequence Generators'
documentation_page: 'walshcodegenerator'
documentation_source_path: 'ref/walshcodegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Walsh Code Generator

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Code length**
:   整数标量，为 2 的幂，用于指定输出码的长度。

**Code index**
:   范围为 [0, 1, ... , N - 1] 的整数标量，其中 N 为 **Code length**，用于指定输出码中零交叉的数量。

**Sample time**
:   正标量，用于指定输出信号每个采样之间的时间（以秒为单位）。如果将采样时间设置为 `-1`，则输出信号从下游继承采样时间。有关 **Sample time** 与 **Samples per frame** 参数之间关系的信息，请参阅
    Sample Timing。

**Samples per frame**
:   每帧采样数，指定为正整数，表示输出数据一个通道中每帧的采样数。如果 **Samples per frame** 大于 **Code length**，则码会循环重复。有关 **Sample time** 与 **Samples per frame** 之间关系的信息，请参阅 Sample Timing。

**输出数据类型**
:   模块的输出类型可指定为 `int8` 或 `double`。默认情况下，模块将其设置为 `double`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2020a：现有模型会自动将此模块更新为当前版本

从 R2020a 开始，Simulink® 不再允许使用 R2015b 之前可用的 Walsh Code Generator 模块版本。

现有模型会自动更新，以加载 Source blocks output frames of contiguous time samples but do not use frame attribute 中公布的 Walsh Code Generator 模块版本。有关模块转发的详细信息，请参阅 Maintain Compatibility of Library Blocks Using Forwarding Tables (Simulink)。

## 描述

从正交码集合生成 Walsh 码

Walsh 码定义为一组 *N* 个码，记为 *W*j，其中 *j* = 0, 1, ... , *N* - 1，这些码具有以下属性：

- *W*j 取值为 +1 和 -1。
- 对于所有 *j*，*W*j[0] = 1。
- 对于 *j* = 0, 1, ... , *N* - 1，*W*j 恰好有 *j* 个零交叉。
- WjWkT={0j≠kNj=k
- 每个码 W*j* 相对于其中点要么为偶函数，要么为奇函数。

Walsh 码使用阶数为 *N* 的 Hadamard 矩阵定义。Walsh Code Generator 模块输出由 **Walsh code index** 指定的 Hadamard 矩阵的一行，该索引必须是范围 [0, ..., *N* - 1] 中的整数。如果将 **Walsh code index** 设置为整数 *j*，则输出码对于 *j* = 0, 1, ... , *N* - 1 恰好有 *j* 个零交叉。

但请注意，Walsh Code Generator 模块中的索引与 Hadamard Code Generator 模块中的索引不同。如果在 Walsh Code Generator 模块中设置 **Walsh code index**，并在 Hadamard Code Generator 模块中设置 **Code index parameter**，则这两个模块输出的码不同。
