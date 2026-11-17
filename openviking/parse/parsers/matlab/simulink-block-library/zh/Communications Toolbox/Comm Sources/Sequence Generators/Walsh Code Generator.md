---
type: simulink-block
title: 'Walsh Code Generator'
family: 'comm-sources'
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

未在 R2025b 中提供文档。

## 参数

**码长**
:   一个整数标量，必须为 2 的幂，用于指定输出码的长度。

**码索引**
:   取值范围为 [0, 1, ... , N - 1] 的整数标量，其中 N 为
    **码长**，用于指定输出码的过零次数。

**采样时间**
:   正标量以 seconds 为单位指定输出信号各采样点之间的时间。如果将采样时间设置为 `-1`，
    输出信号将从下游继承采样时间。有关 **采样时间** 与 **每帧采样数**
    参数之间关系的信息，请参阅“采样时序”。

**每帧采样数**
:   每帧采样数，指定为正整数，表示输出数据一个通道中每帧的采样数。如果 **每帧采样数**
    大于 **码长**，则循环重复该码。有关 **采样时间** 与
    **每帧采样数** 之间关系的信息，请参阅“采样时序”。

**输出数据类型**
:   模块的输出类型可指定为 `int8` 或 `double`。默认情况下，
    模块将其设置为 `double`。

## 所属库

未在 R2025b 中提供文档。

## 模块特性

未在 R2025b 中提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

### R2020a：现有模型会自动将此模块更新为当前版本

从 R2020a 开始，Simulink® 不再允许您使用 R2015b 之前提供的 Walsh Code Generator 模块版本。

现有模型会自动更新，以加载“源模块输出连续时间采样的帧，但不使用帧属性”中所述的 Walsh Code Generator 模块版本。有关模块转发的更多信息，请参阅“使用转发表保持库模块的兼容性 (Simulink)”。

## 描述

从正交码集生成 Walsh 码

Walsh 码定义为一组 *N* 个码，记为 *W*j，其中 *j* = 0, 1,
... , *N* - 1，并具有以下属性：

- *W*j 取值为 +1 和 -1。
- 对于所有 *j*，*W*j[0] = 1。
- 对于 *j* = 0, 1, ... , *N* - 1，*W*j 恰好有 *j* 次过零。
- WjWkT={0j≠kNj=k
- 每个码 W*j* 关于其中点均呈偶对称或奇对称。

Walsh 码由 *N* 阶 Hadamard 矩阵定义。Walsh Code Generator 模块输出 Hadamard 矩阵中由
**Walsh 码索引** 指定的一行，该索引必须是范围 [0,
..., *N* - 1] 内的整数。如果将 **Walsh 码索引** 设置为整数 *j*，则对于 *j* = 0, 1, ... , *N* -
1，输出码恰好有 *j* 次过零。

但是请注意，Walsh Code Generator 模块中的索引方式与 Hadamard Code Generator 模块中的索引方式不同。如果设置 Walsh Code Generator 模块中的 **Walsh
码索引** 和 Hadamard Code Generator 模块中的 **码索引** 参数，这两个模块将输出不同的码。
