---
type: simulink-block
title: 'Point Cloud Viewer'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'pointcloudviewer'
documentation_source_path: 'ref/pointcloudviewer.html'
language: en
---

# Point Cloud Viewer

## Ports
```yaml
ports:
- name: Location
  summary: Positions of points in 3-D coordinate space matrix | array
  direction: input
  data_types: single | double | uint8 | uint16
- name: Color
  summary: Color of point cloud [] (default) | matrix | array
  direction: input
  data_types: single | double | uint8 | uint16
- name: Intensity
  summary: Grayscale intensities [] (default) | vector | matrix | array
  direction: input
  data_types: single | double | uint8 | uint16
```

### Input

### **Location** — Positions of points in 3-D coordinate space matrix | array

Positions of the points in 3-D coordinate space, specified as:

- An *M*-by-3 matrix or
  *M*-by-*N*-by-3 array for a 3-D point
  cloud.
- An *M*-by-3-by-*T* or
  *M*-by-*N*-by-3-by-*T*
  array for a sequence of 3-D point clouds, where *T* is the
  total number of 3-D point clouds in the point cloud sequence.

Each array specifies the *x-*, *y-*,
and *z-* coordinates of a points in the point cloud, but the format
differs between unorganized point cloud and organized point clouds.

- For unorganized point clouds, you must specify **Location**
  as an *M*-by-3 or
  *M*-by-3-by-*T* array, where
  *M* is the total number of points, and each row provides the
  *xyz-*coordinates for a point.
- For organized point clouds, you must specify **Location** as
  an *M*-by-*N*-by-3 or an
  *M*-by-*N*-by-3-by-*T* array,
  where *M*×*N* is the total number of points, and
  the third dimension of the array provides the *x-*,
  *y-*, and *z-*coordinates for the
  corresponding point. Projective cameras, such as a Kinect or a lidar sensor, store
  points as an organized point cloud. An organized point cloud is laid out as a 2-D
  or a 3-D array of points that resembles an image- or video-like structure.

**Data Types:** `single` | `double` | `uint8` | `uint16`

### **Color** — Color of point cloud `[]` (default) | matrix | array

Point cloud color, specified as:

- An *M*-by-3 matrix or
  *M*-by-*N*-by-3 array for a 3-D point
  cloud.
- An *M*-by-3-by-*T* or
  *M*-by-*N*-by-3-by-*T*
  array for a sequence of 3-D point clouds, where *T* is the
  total number of 3-D point clouds in a point cloud sequence.

For an unorganized point cloud, specified as an
*M*-by-3 matrix or *M*-by-3-by-*T*
array, each row specifies the RGB color triplet for a point in the point cloud data.
For an organized point cloud, specified as an
*M*-by-*N*-by-3 or
*M*-by-*N*-by-3-by-*T* array,
each channel of the third dimension specifies the RGB color triplet for the
corresponding point in the point cloud data. You can specify the same color for all
points or a different color for each point.

- For the `single` or `double` data type, you
  must specify the **Color** RGB value in the range [0, 1].
- For the `uint8` data type, you must specify the
  **Color** RGB value in the range [0, 255].
- For the `uint16` data type, you must specify the
  **Color** RGB value in the range [0, 65535].

**Note**

Input to the **Color** port must have the same dimensions and
data type as the input to the **Location** port.

#### Dependencies

To enable this port, select the **File** >  **Location and Color Port** parameter.

**Data Types:** `single` | `double` | `uint8` | `uint16`

### **Intensity** — Grayscale intensities `[]` (default) | vector | matrix | array

*Since R2025a*

Grayscale intensities at each point, specified as:

- An *M*-by-1 vector for an unorganized point cloud or
  *M*-by-*N* matrix for an organized point
  cloud.
- An *M*-by-1-by-*T* array for a sequence of
  unorganized point clouds or
  *M*-by-*N*-by-*T* array for
  a sequence of organized point clouds. *T* is the total number
  of 3-D point clouds in a point cloud sequence.

**Note**

Input to the **Intensity** port must have the same data type
as input to the **Location** port.

#### Dependencies

To enable this port, select the **File** >  **Location and Intensity Port** parameter.

**Data Types:** `single` | `double` | `uint8` | `uint16`
## Parameters
```yaml
parameters:
- name: Open at Start of Simulation
  summary: Open Point Cloud Viewer window at start of simulation on (default) | off
  group: File
- name: Location Port
  summary: Enable point location as input on (default) | off
  group: File
- name: Location and Color Port
  summary: Enable point location and color as input off (default) | on
  group: File
- name: Location and Intensity Port
  summary: Enable point location and intensity as input off (default) | on
  group: File
- name: Display the full path
  summary: Display full path of source data in title bar off (default) | on
  group: File > Configuration > Edit > Core
- name: Bring All Point Cloud Viewer Windows Forward
  summary: Bring all Point Cloud Viewer windows to front of display off (default) | on
  group: View
- name: Simulation Toolbar
  summary: Show simulation toolbar on (default) | off
  group: View
- name: Status Bar
  summary: Show status bar on (default) | off
  group: View
- name: Highlight Simulink Block
  summary: Highlight Point Cloud Viewer block off (default) | on
  group: View
- name: Run
  summary: View entire point cloud sequence off (default) | on
  group: Simulation
- name: Continue
  summary: Continue viewing the point cloud sequence off (default) | on
  group: Simulation
- name: Stop
  summary: Stop viewing the point cloud sequence off (default) | on
  group: Simulation
- name: Drop Frames to Improve Performance
  summary: Reduce frame rate of input point cloud sequence on (default) | off
  group: Simulation
```

### File

### **Open at Start of Simulation** — Open Point Cloud Viewer window at start of simulation `on` (default) | `off`

Select this parameter to display the Point Cloud Viewer window at the start of the
simulation. Clear this parameter to prevent the Point Cloud Viewer window from opening
at the start of the simulation.

### **Location Port** — Enable point location as input `on` (default) | `off`

Select this parameter to enable the **Location** port for
inputting the 3-D point cloud coordinates. If you select this parameter, the
**Location and Color Port** and **Location and Intensity
Port** parameters clear automatically.

### **Location and Color Port** — Enable point location and color as input `off` (default) | `on`

Select this parameter to enable both the **Location** and
**Color** input ports. If you select this parameter, the
**Location Port** and **Location and Intensity
Port** parameters clear automatically.

### **Location and Intensity Port** — Enable point location and intensity as input `off` (default) | `on`

*Since R2025a*

Select this parameter to enable both the **Location** and
**Intensity** input ports. If you select this parameter, the
**Location Port** and **Location and Color Port**
parameters clear automatically.

### File > Configuration > Edit > Core

The Point Cloud Viewer Configuration dialog box enables you to change the behavior and
appearance of the graphic user interface (GUI).

- To open the Configuration dialog box and edit parameters, select **File** > **Configuration**  > **Edit**.

The **Core** tab in the Configuration dialog box lists the general
settings of the GUI.

- In the **Core** tab, select `General UI`
  and click **Properties** to open the General UI Properties dialog
  box.

### **Display the full path** — Display full path of source data in title bar `off` (default) | `on`

Select this parameter to display the model name and full path to the source data
in the title bar of the Point Cloud Viewer window. If you clear this parameter, the
window displays a shortened name.

### Tools > Point Cloud Information

The Point Cloud Information dialog box displays information about the input point cloud
sequence. This information includes **Source type**, **Source
name**, **Frame size**, **Source data type**,
and **Display data type**.

### View

### **Bring All Point Cloud Viewer Windows Forward** — Bring all Point Cloud Viewer windows to front of display `off` (default) | `on`

Select this parameter to bring all the Point Cloud Viewer windows forward, in
front of all other open windows behind.

### **Simulation Toolbar** — Show simulation toolbar `on` (default) | `off`

Select this parameter to show the simulation toolbar on the Point Cloud Viewer
window.

Simulation toolbar

To perform a relevant operation using the simulation toolbar, select the
corresponding feature as described in the table.

| Feature | Description |
| --- | --- |
| Run | Start the simulation, and view the point cloud sequence. |
| Step Forward | Start the simulation, view one frame of the point cloud sequence, and pause. |
| Stop | Stop the simulation. |
| Highlight Simulink Block | Highlight the Point Cloud Viewer block with a blue background in the Simulink model. |
| Snapshot (Freeze Display) | Freeze Point Cloud Viewer window to enable you take a snapshot of the window using the **Print** or **Print Preview** option in **File** menu.  **Note**  Unselect this option to return the Point Cloud Viewer window to an active state from a frozen state. |
| Settings | Enable the **Settings** pane on the Point Cloud Viewer window. |
| Colorbar *(since R2025a)* | View the color bar in the Point Cloud Viewer window.  By default, the Point Cloud Viewer window does not display the color bar. To view the color bar, click **Colorbar** on the simulation toolbar. To hide the color bar, click **Colorbar** again.  **Dependencies**  To enable this parameter, select the **File** >  **Location Port** or **File** >  **Location and Intensity Port** parameter. |

### **Status Bar** — Show status bar `on` (default) | `off`

Select this parameter to show the status bar on the Point Cloud Viewer window. The
status bar, at the bottom of the Point Cloud Viewer window, shows this information
about the point cloud sequence.

- Dimension
- Organization
- Status of the window during simulation
- Timestamp of the current frame

### **Highlight Simulink Block** — Highlight Point Cloud Viewer block `off` (default) | `on`

Highlight the Point Cloud Viewer block in blue in the Simulink model.

### Simulation

To access this parameter, select the **Simulation** menu in the Point
Cloud Viewer window.

### **Run** — View entire point cloud sequence `off` (default) | `on`

Select this parameter to start the simulation and view the point cloud sequence
continuously from the first to the last frame. You can also perform this action by
clicking **Run** on the simulation toolbar.

### **Continue** — Continue viewing the point cloud sequence `off` (default) | `on`

Select this parameter to continue viewing the point cloud sequence till the last
frame. To enable the **Continue** parameter, start the simulation by
clicking **Step Forward** on simulation toolbar.

### **Stop** — Stop viewing the point cloud sequence `off` (default) | `on`

Select this parameter to stop the display of the point cloud sequence. You can
also perform this action by clicking **Stop** on the simulation
toolbar.

### **Drop Frames to Improve Performance** — Reduce frame rate of input point cloud sequence `on` (default) | `off`

Select this parameter to reduce the frame rate of the input streaming point cloud
sequence to improve the performance of the simulation. If you clear this parameter,
the block displays every frame in the input point cloud sequence signal during the
simulation.
## Libraries

Computer Vision Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

### R2025a: Visualize point cloud data using intensity values

The block now supports an **Intensity** input port to visualize streaming point
cloud data using intensity values. To enable this port, select the **File** >  **Location and Intensity Port** parameter.

### R2025a: View color bar for point cloud data

You can now view the color bar by selecting the **Colorbar** button
on the simulation toolbar. This button is available when you select the **File** >  **Location Port** or **File** >  **Location and Intensity Port** parameter.

### R2025a: View point cloud across full extent of axes

The block now automatically adjusts the default axes limits based on the input point
cloud data. Automatic adjustment enables you to view the point cloud across full extent of
the axes.

## Description

Visualize streaming point cloud data sequence

The Point Cloud Viewer block creates a Point Cloud Viewer window to display
a sequence of 3-D point cloud data that streams from a device such as a
Microsoft® Kinect® or a lidar sensor.
The Point Cloud Viewer block also provides simulation controls in the Point Cloud Viewer
window to play, pause, and step through the streaming point cloud data sequence.

Point cloud viewer window

### Features of Point Cloud Viewer

- Playback control — Control streaming playback of a point cloud sequence using
  the **Run**, **Step Forward**, and
  **Stop** buttons.
- Set axis limits — Limit the display of the 3-D point cloud data by setting the
  *x*-, *y*-, and *z*-axis
  limits.
- Set background color — Set the background color of the viewer window against which
  to display of point cloud data.
- Vertical axis direction control — Set the vertical axis direction of the point
  cloud data to upward-positive or downward-positive.
- View plane control — Set the view plane to change the viewing angle of the point
  cloud data.
- Analyze point cloud data — Inspect point cloud data using the **Data
  Tips** option on the axes toolbar of the Point Cloud Viewer window.
- View colorbar — View the colorbar in the Point Cloud Viewer window using the
  **Colorbar** button on the simulation toolbar.
