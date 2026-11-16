---
type: simulink-block
title: 'Constant Volume Hydraulic Chamber'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'constantvolumehydraulicchamber'
documentation_source_path: 'ref/constantvolumehydraulicchamber.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Volume Hydraulic Chamber

## 端口

该模块有一个与腔室入口关联的液压守恒端口。

## 参数

**Chamber specification**
:   该参数可以有两个值之一：`By volume` 或
    `By length and diameter`。如果腔室由圆形管道形成，推荐使用值 `By length
    and diameter`。如果该参数设置为 `By volume`，则不考虑壁顺应性。该参数的默认值为
    `By volume`。

**Chamber wall type**
:   该参数可以有两个值之一：`Rigid wall` 或
    `Flexible wall`。如果该参数设置为
    `Rigid wall`，则不考虑壁顺应性，这可以提高计算效率。对于软管和金属
    管道，推荐使用值
    `Flexible wall`，因为顺应性可能影响系统行为。该参数的默认值为
    `Rigid wall`。如果
    **Chamber specification** 参数设置为
    `By length and diameter`，则使用该参数。

**Chamber volume**
:   腔室中的流体体积。默认值为
    `1e-4` m^3。如果
    **Chamber specification** 参数设置为
    `By volume`，则使用该参数。

**Chamber internal diameter**
:   圆柱腔室的内径。默认值为
    `0.01` m。如果
    **Chamber specification** 参数设置为
    `By length and diameter`，则使用该参数。

**Cylindrical chamber length**
:   圆柱腔室的长度。默认值为
    `1` m。如果 **Chamber
    specification** 参数设置为 `By length and
    diameter`，则使用该参数。

**Static pressure-diameter coefficient**
:   系数 *`Kp`*，它
    建立稳态条件下压力与内径之间的关系。该参数可通过解析法或
    实验确定。默认值为 `1.2e-12` m/Pa。如果
    **Chamber wall type** 设置为
    `Flexible wall`，则使用该参数。

**Viscoelastic process time constant**
:   传递函数中将管道内径与
    压力变化相关联的时间常数。使用此参数，模拟的弹性或
    粘弹性过程用一阶滞后近似。该参数
    通过实验确定或由制造商提供。默认
    值为 `0.01` s。如果
    **Chamber wall type** 设置为 `Flexible
    wall`，则使用该参数。

**Specific heat ratio**
:   气体比热比。默认值为
    `1.4`。

 受限参数

当模型处于受限编辑模式时，不能修改以下
参数：

- **Chamber specification**
- **Chamber wall type**

所有其他模块参数均可修改。可修改模块参数的实际集合取决于模型进入受限模式时 **Tube cross
section type** 和 **Chamber wall type** 参数的值。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

### R2023a: 将移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将移除）恒定体积的液压容量

Constant Volume Hydraulic Chamber 模块对固定体积
腔室进行建模，该腔室具有刚性或柔性壁，可用于液压阀、泵、歧管、
管道、软管等。在需要考虑某种
形式的流体可压缩性的模型中，使用此模块。可以使用模块参数选择流体
可压缩性的适当表示。

流体可压缩性在其最简单形式下根据以下
方程模拟：

Vf=Vc+VcEp

q=VcE⋅dpdt

其中

|  |  |
| --- | --- |
| *q* | 进入腔室的流量 |
| *V*f | 腔室中的流体体积 |
| *V*c | 腔室几何体积 |
| *E* | 流体体积模量 |
| *p* | 腔室中流体的表压 |

如果腔室中的压力可能降至负值并接近
空化极限，则必须增强上述方程。在此模块中，通过
将腔室中的流体表示为液体与少量夹带、未溶解气体的混合物来实现（见 [1, 2]）。混合物
体积模量确定为：

E=El1+α(papa+p)1/n1+αpa1/nn·(pa+p)n+1nEl

其中

|  |  |
| --- | --- |
| *E*l | 纯液体体积模量 |
| *p*α | 大气压力 |
| *α* | 大气压力下的相对气体含量，*α* = *V*G/*V*L |
| *V*G | 大气压力下的气体体积 |
| *V*L | 液体体积 |
| *n* | 气体比热比 |

将流体表示为液体和气体混合物的主要目的是
引入空化的近似模型，当压力降至流体蒸气饱和水平
以下时，该模型会在腔室中发生。如下图所示，混合物体积
模量随着表压接近零而减小，从而显著
减缓进一步的压力变化。在远高于零的表压下，少量
未溶解气体实际上对系统行为没有影响。

要重现此图，请将以下脚本复制并粘贴到您的 MATLAB® Command Window 中：

```
% Parameters
p_atm    = 1.01325e5;            % Atmospheric pressure [Pa]
pressure = -1.01325e5:1e3:5e6;   % Pressure (gauge) [Pa]
alpha    = 0:2e-3:0.01;          % Relative amount of trapped air
k_sh     = 1.4;                  % Specific heat ratio
bulk     = 1.24285e+09;          % Bulk modulus at atmospheric pressure and no gas [Pa]

% Absolute pressure
p_abs = p_atm + pressure;
% Relative absolute pressure
p_nom = (p_atm./p_abs).^(1/k_sh);
p_den = p_nom .* bulk ./ (k_sh .* p_abs);
% Instantaneous bulk modulus
bulk_inst = bulk * (1+ bsxfun(@times, alpha', p_nom)) ./ (1 + bsxfun(@times, alpha', p_den));

% Reuse figure if it exists, else create new figure
if ~exist('h1_bulk_modulus', 'var') || ~isgraphics(h1_bulk_modulus, 'figure')
    h1_bulk_modulus = figure('Name', 'h1_bulk_modulus');
end
figure(h1_bulk_modulus)
clf(h1_bulk_modulus)
legend_label = cell(length(alpha),1);

for i=1:length(alpha)
    plot(pressure, bulk_inst(i,:))
    hold on
    legend_label{i,1} = ['alpha = ',num2str(alpha(i))];
end

grid on
xlabel('Pressure (Pa)')
ylabel('Bulk modulus (Pa)')
title('Bulk modulus vs. pressure at different air contents')
legend(legend_label, 'Location', 'Best')
hold off
```

空化本质上是一个热力学过程，需要考虑
多相流体、热传递等，因此无法使用 Simscape™ 软件准确模拟。但
模块中实现的简化版本足以在压力降至危险水平以下时发出信号，并防止
通常在负压下发生的计算失败。

如果压力降至绝对真空（–101325 Pa）以下，仿真停止并
显示错误消息。

如果腔室壁具有明显顺应性，则必须进一步
增强上述方程，将腔室几何体积表示为压力的函数：

Vc=πd2/4·L

d(s)=Kp1+τsp(s)

其中

|  |  |
| --- | --- |
| *d* | 圆柱腔室的内径 |
| *L* | 圆柱腔室的长度 |
| *K*p | 比例系数（m/Pa） |
| *τ* | 时间常数 |
| *s* | 拉普拉斯算子 |

系数 *`Kp`* 建立
稳态条件下压力与内径之间的关系。对于
金属管，该系数可计算为（见 [2]）：

Kp=dEM(D2+d2D2−d2+ν)

其中

|  |  |
| --- | --- |
| *D* | 管道外径 |
| *E*M | 管道材料的弹性模量（杨氏模量） |
| *ν* | 管道材料的泊松比 |

对于软管，该系数可由制造商提供。

管道中，尤其是软管中的膨胀和收缩过程，是
非线性弹性与粘弹性变形的复杂组合。此过程
在模块中用一阶滞后近似，其时间常数通过
经验确定（例如，参见 [3]）。

因此，通过选择适当的值，可以使用此模块实现四种不同的流体
可压缩性模型：

- 刚性壁腔室，流体中无夹带气体
- 带顺应壁的圆柱腔室，流体中无夹带气体
- 刚性壁腔室，流体含夹带气体
- 带顺应壁的圆柱腔室，流体含夹带气体

该模块允许两种指定腔室尺寸的方法：

- `By volume` — 将此选项用于具有刚性壁的圆柱形或非圆柱形腔室。只需知道腔室体积。此腔室类型不考虑壁顺应性。
- `By length and diameter` — 将此选项用于具有刚性或顺应壁的圆柱形腔室，例如圆管或软管。

该模块有一个与腔室入口关联的液压守恒端口。模块
正方向从其端口指向参考点。这意味着
如果流量流入腔室，则流量为正。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用
模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。
使用基于标称值的系统缩放可提高仿真鲁棒性。标称
值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal
Values** 部分。有关详细
信息，请参阅 Modify Nominal Values for a Block Variable。
