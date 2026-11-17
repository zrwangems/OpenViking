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

该模块有一个与腔体入口关联的液压守恒端口。

## 参数

**Chamber specification**
:   该参数可以有两个值之一：`By volume` 或
    `By length and diameter`。如果腔体由圆形管道构成，推荐使用
    `By length and diameter`。如果该参数设置为 `By volume`，则不
    考虑壁面柔度。该参数的默认值为
    `By volume`。

**Chamber wall type**
:   该参数可以有两个值之一：`Rigid wall` 或
    `Flexible wall`。如果该参数设置为
    `Rigid wall`，则不考虑壁面柔度，这可以提高计算效率。对于软管和金属
    管道，推荐使用 `Flexible wall`，因为柔度可能影响系统行为。该参数的默认值为
    `Rigid wall`。当 **Chamber specification** 参数设置为
    `By length and diameter` 时，使用该参数。

**Chamber volume**
:   腔体中流体的体积。默认值为
    `1e-4` m^3。当 **Chamber specification** 参数设置为
    `By volume` 时，使用该参数。

**Chamber internal diameter**
:   圆柱形腔体的内径。默认值为
    `0.01` m。当 **Chamber specification** 参数设置为
    `By length and diameter` 时，使用该参数。

**Cylindrical chamber length**
:   圆柱形腔体的长度。默认值为
    `1` m。当 **Chamber specification** 参数设置为 `By length and
    diameter` 时，使用该参数。

**Static pressure-diameter coefficient**
:   系数 *`Kp`*，用于建立稳态条件下压力与内径之间的关系。
    该参数可以通过解析方法或实验方法确定。默认值为 `1.2e-12` m/Pa。当
    **Chamber wall type** 设置为 `Flexible wall` 时，使用该参数。

**Viscoelastic process time constant**
:   将管道内径与压力变化相关联的传递函数中的时间常数。通过该参数，所模拟的弹性或
    粘弹性过程用一阶滞后近似。该参数通过实验确定或由制造商提供。默认值为
    `0.01` s。当 **Chamber wall type** 设置为 `Flexible
    wall` 时，使用该参数。

**Specific heat ratio**
:   气体比热比。默认值为
    `1.4`。

 受限参数

当您的模型处于受限编辑模式时，您无法修改以下参数：

- **Chamber specification**
- **Chamber wall type**

所有其他模块参数均可修改。可修改模块参数的实际集合取决于模型进入受限模式时的 **Tube cross
section type** 和 **Chamber wall type** 参数值。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

### R2023a: 将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。
Isothermal Liquid 库中的模块提供了更高的精度、可用性和
数值性能。

有关更新模型的更多信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将移除）恒定体积的液压容量

恒定体积液压腔模块对具有刚性或柔性壁的固定体积腔进行建模，用于液压阀、泵、歧管、管道、软管等。在需要考虑某种形式的流体可压缩性的模型中使用此模块。您可以使用模块参数选择适当的流体可压缩性表示方式。

流体可压缩性以其最简单的形式根据以下方程进行仿真：

Vf=Vc+VcEp

q=VcE⋅dpdt

其中

|  |  |
| --- | --- |
| *q* | 流入腔的流量 |
| *V*f | 腔内的流体体积 |
| *V*c | 腔的几何体积 |
| *E* | 流体体积模量 |
| *p* | 腔内流体的表压 |

如果腔内的压力可能降至负值并接近气蚀极限，则必须对上述方程进行增强。在此模块中，这是通过将腔内的流体表示为液体和少量夹带的不溶解气体的混合物来实现的（参见 [1, 2]）。混合物的体积模量确定为：

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

将流体表示为液体和气体混合物的主要目的是引入气蚀的近似模型，当压力降至流体蒸气饱和水平以下时，腔内会发生气蚀。如下图所示，混合物的体积模量随着表压接近零而减小，从而显著减缓进一步的压力变化。在远高于零的表压下，少量未溶解气体对系统行为实际上没有影响。

要重现此图，请将以下脚本复制并粘贴到您的 MATLAB® 命令窗口中：

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

气蚀本质上是一个热力学过程，需要考虑多相流体、热传递等，因此无法用 Simscape™ 软件精确仿真。但模块中实现的简化版本足以在压力降至危险水平以下时发出信号，并防止通常在负压下发生的计算失败。

如果压力降至绝对真空（–101325 Pa）以下，仿真将停止并显示错误消息。

如果腔壁具有明显的柔量，则必须通过将腔的几何体积表示为压力的函数来进一步增强上述方程：

Vc=πd2/4·L

d(s)=Kp1+τsp(s)

其中

|  |  |
| --- | --- |
| *d* | 圆柱腔的内径 |
| *L* | 圆柱腔的长度 |
| *K*p | 比例系数（m/Pa） |
| *τ* | 时间常数 |
| *s* | 拉普拉斯算子 |

系数 *`Kp`* 建立了稳态条件下压力与内径之间的关系。对于金属管，该系数可计算为（参见 [2]）：

Kp=dEM(D2+d2D2−d2+ν)

其中

|  |  |
| --- | --- |
| *D* | 管道外径 |
| *E*M | 管道材料的弹性模量（杨氏模量） |
| *ν* | 管道材料的泊松比 |

对于软管，该系数可由制造商提供。

管道中尤其是软管中的膨胀和收缩过程是非线性弹性变形和粘弹性变形的复杂组合。此过程在模块中用一阶滞后近似，其时间常数由经验确定（例如，参见 [3]）。

因此，通过选择适当的值，您可以使用此模块实现四种不同的流体可压缩性模型：

- 刚性壁腔，流体中无夹带气体
- 柔性壁圆柱腔，流体中无夹带气体
- 刚性壁腔，流体中含夹带气体
- 柔性壁圆柱腔，流体中含夹带气体

该模块允许两种指定腔尺寸的方法：

- 按体积 — 将此选项用于具有刚性壁的圆柱形或非圆柱形腔。您只需要知道腔的体积。此腔类型不考虑壁的柔量。
- 按长度和直径 — 将此选项用于具有刚性或柔性壁的圆柱形腔，例如圆管或软管。

该模块有一个与腔入口关联的液压守恒端口。模块正方向从其端口指向参考点。这意味着如果流量流入腔，则流量为正。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真的鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
