---
type: simulink-block
title: 'Line Scan Camera'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'linescancamera'
documentation_source_path: 'freedomboard/ref/linescancamera.html'
language: zh-CN
chinese_source: worker-translation
---

# Line Scan Camera

## 端口

R2025b 中未提供文档。

## 参数

**相机**
:   选择 Camera 0 或 Camera 1。

**采样时间**
:   指定此模块读取线阵相机数据的频率。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2014b 中推出**

## 描述

读取线阵相机的数据

从所选的线阵相机读取数据。模块输入以毫秒为单位指定相机的曝光时间。模块输入可接受 0–150 ms 范围内的值。模块输出一个由 uint16 值组成的 [1x128] 数组。如果设置的曝光时间大于此模块的采样时间，可能会导致非确定性行为。

在仿真期间，此模块会以由 uint16 值组成的 [1x128] 数组形式输出仿真相机数据。该仿真数据类似于当一条深色线在白色背景上以正弦波形式从左向右移动时相机所产生的数据。

您可以通过打开模块代码并在 `stepImpl` 函数中修改该代码来更改仿真行为。

要修改模块代码，请执行以下步骤：

1. 在 MATLAB® 提示符下输入以下命令。

   `edit freedomboard.LinescanCamera`
2. 修改 `stepImpl` 函数中的以下代码。

   ```
     elseif ( coder.target('Sfun') )
            cameraData = uint16(zeros(1,128));
   				% example Simulation code
             % background light intensity
             bkgIntensity  = 18000;
             % intensity of the line to follow
             lineIntinsity =  3500;

             ambientOffset = (bkgIntensity - lineIntinsity)*0.75;

            	% specify how many pixels wide the line should be
            lineWidth = 46;
            create a curve to simulate the ambient light reflecting off of
            the track baseBluntness = 1.25;
            baseLine = int16( (sqrt((1+baseBluntness^2)./...
            (1+baseBluntness^2*sin((0:pi/127:pi)).^2))...
             .*sin(0:pi/127:pi))...
              * (bkgIntensity-ambientOffset)) + ambientOffset;

             % calculate the position of the start of the dip created by
             % the dark line on the track.  This is how we control the position
             of the line at each simulated sample
               startIdx = uint8(sin((pi/200)*obj.simSampleNum)*63+64);
             % calculate the end index of the darkDip, but make sure it
             % does not exceed the length of the array (128)
             if((startIdx + uint8(lineWidth-1)) > uint8(128))
              endIdx = uint8(128);
              else
               endIdx = startIdx + uint8(lineWidth-1);
             end

             % create a curve which emulates the dark line's affect on the camera
             baseHeight = double(baseLine(startIdx:endIdx));
             baseHeight = [baseHeight, repmat(bkgIntensity, 1,
              lineWidth - length(baseHeight))];
             bluntness = 1.75;
             darkDip  = uint16( (sqrt((1+bluntness^2)./...
             (1+bluntness^2*sin((0:pi/(lineWidth-1):pi)).^2))...
             .*sin(0:pi/(lineWidth-1):pi))...
             .* (baseHeight - lineIntinsity*0.75));

             % combine the darkDip and the baseLine at the calculated location
    cameraData(:) = baseLine;
    cameraData(startIdx:endIdx) = cameraData(startIdx:endIdx) -
    darkDip(1:endIdx-startIdx+1);
             % threshold the dip so that we have a flat section at the line
             cameraData(cameraData < lineIntinsity) = lineIntinsity;

              % add noise to the data
              noise = randi(lineIntinsity*0.05, size(cameraData), 'uint16');
   cameraData(mod(1:length(cameraData), 2) == 0) =
   cameraData(mod(1:length(cameraData), 2) == 0)
   - noise(mod(1:length(cameraData), 2) == 0);
   cameraData(mod(1:length(cameraData), 2) ~= 0) =
   cameraData(mod(1:length(cameraData), 2) ~= 0)
   + noise(mod(1:length(cameraData), 2) == 0);

             % iterate the simulation Sample Number
             obj.simSampleNum = obj.simSampleNum + 1;
   	  end
   ```
3. 保存 MATLAB 文件。
4. 将 MATLAB 当前目录更改为包含 LinescanCamera.m 文件的文件夹。
5. 在 MATLAB 提示符下使用以下命令，为该 MATLAB 文件创建一个受保护的函数文件。

   `pcode freedomboard.LinescanCamera`
6. 在 MATLAB 提示符下运行以下命令：

   `clear pcode`

   `clear classes`

   `rehash toolboxcache`。

此模块将更新，并采用您的新仿真行为。
