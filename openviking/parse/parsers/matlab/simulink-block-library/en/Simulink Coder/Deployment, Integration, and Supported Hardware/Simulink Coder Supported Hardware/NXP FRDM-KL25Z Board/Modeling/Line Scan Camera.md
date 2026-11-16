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
language: en
---

# Line Scan Camera

## Ports

Not documented in R2025b.

## Parameters

**Camera**
:   Select Camera 0 or Camera 1.

**Sample time**
:   Specify how often this block reads the line scan camera data.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Read the data from a line scan camera

Read the data from the selected line scan camera. The block input specifies the
exposure time of the camera in milliseconds. The block input accepts values between 0–150
ms. The block output emits a [1x128] array of uint16 values. Setting an exposure time
greater than the sample time of this block can cause nondeterministic behavior.

During simulations, this block output emits emulated camera data in the form of an
array of [1x128] uint16 values. The data emulated is similar to what the camera produces,
when a dark line moves from left to right on a white background in the form of a sine
wave.

You can change the simulation behavior by opening the block code and by modifying it
in the `stepImpl` function.

To modify the block code, perform the following steps:

1. Go to the MATLAB® prompt and enter the following command.

   `edit freedomboard.LinescanCamera`
2. Modify the following code in the `stepImpl` function.

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
3. Save the MATLAB file.
4. Change the MATLAB current directory to the folder that contains LinescanCamera.m
   file.
5. Create a protected function file for the MATLAB file using the following command in the MATLAB prompt.

   `pcode freedomboard.LinescanCamera`
6. Run the following commands in the MATLAB prompt

   `clear pcode`

   `clear classes`

   `rehash toolboxcache`.

The block is updated with your new simulation behavior.
