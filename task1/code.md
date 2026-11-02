# Environmental Monitoring Data Analyzer

## 1. Problem Statement

Environmental Monitoring Data Analyzer is used to analyze air-quality or water-quality readings collected from different locations. Using nested lists (2D matrices), the program calculates the average, maximum, and minimum readings. It also classifies observations as Safe, Moderate, or Dangerous based on the supplied threshold values.

## 2. Algorithm

1. Start the program.
2. Initialize location names and environmental readings using nested lists.
3. Enter the threshold values.
4. Calculate the average reading for each location.
5. Find the minimum and maximum readings.
6. Compare each reading with the threshold values.
7. Classify readings as Safe, Moderate, or Dangerous.
8. Display the average, minimum, maximum, and classification.
9. Stop the program.

## 3. Flowchart (Mermaid Code)

\#chatgpt-mermaid-\_r_cq\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_cq\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_cq\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_cq\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_cq\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_cq\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_cq\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_cq\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_cq\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_cq\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_cq\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_cq\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_cq\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_cq\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_cq\_ p{margin:0;}#chatgpt-mermaid-\_r_cq\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_cq\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_cq\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_cq\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_cq\_ .label text,#chatgpt-mermaid-\_r_cq\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_cq\_ .node rect,#chatgpt-mermaid-\_r_cq\_ .node circle,#chatgpt-mermaid-\_r_cq\_ .node ellipse,#chatgpt-mermaid-\_r_cq\_ .node polygon,#chatgpt-mermaid-\_r_cq\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_cq\_ .rough-node .label text,#chatgpt-mermaid-\_r_cq\_ .node .label text,#chatgpt-mermaid-\_r_cq\_ .image-shape .label,#chatgpt-mermaid-\_r_cq\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_cq\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_cq\_ .rough-node .label,#chatgpt-mermaid-\_r_cq\_ .node .label,#chatgpt-mermaid-\_r_cq\_ .image-shape .label,#chatgpt-mermaid-\_r_cq\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_cq\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_cq\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_cq\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_cq\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_cq\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_cq\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_cq\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_cq\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_cq\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_cq\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_cq\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_cq\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_cq\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_cq\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_cq\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_cq\_ .icon-shape,#chatgpt-mermaid-\_r_cq\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_cq\_ .icon-shape p,#chatgpt-mermaid-\_r_cq\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_cq\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_cq\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_cq\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_cq\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_cq\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_cq\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_cq\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_cq\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_cq\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_cq\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_cq\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_cq\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_cq\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_cq\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_cq\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_cq\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_cq\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_cq\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_cq\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_cq\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_cq\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_cq\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_cq\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_cq\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_cq\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_cq\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_cq\_ .node rect,#chatgpt-mermaid-\_r_cq\_ .node circle,#chatgpt-mermaid-\_r_cq\_ .node ellipse,#chatgpt-mermaid-\_r_cq\_ .node polygon,#chatgpt-mermaid-\_r_cq\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_cq\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_cq\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_cq\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_cq\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_cq\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput Location Names andReadingsInput Threshold ValuesInitialize ResultsSelect Each LocationCalculate Average ReadingFind Minimum and MaximumSelect Each ReadingReading <= Safe Limit?Classify as SafeReading <= Moderate Limit?Classify as ModerateClassify as DangerousMore Readings?Display ResultsMore Locations?StopYesNoYesNoYesNoYesNo

## 4. Python Source Code

```
locations = ["Location A", "Location B", "Location C"]readings = [    [20, 30, 40, 35],    [50, 60, 70, 65],    [80, 90, 100, 95]]safe_limit = 40moderate_limit = 70for i in range(len(locations)):    data = readings[i]    avg = sum(data) / len(data)    minimum = min(data)    maximum = max(data)    print("\nLocation:", locations[i])    print("Average:", avg)    print("Minimum:", minimum)    print("Maximum:", maximum)    for value in data:        if value <= safe_limit:            status = "Safe"        elif value <= moderate_limit:            status = "Moderate"        else:            status = "Dangerous"        print(value, "-", status)
```

## 5. Sample Input

```
Locations: Location A, Location B, Location C

Readings:
[
 [20, 30, 40, 35],
 [50, 60, 70, 65],
 [80, 90, 100, 95]
]

Safe Limit: 40
Moderate Limit: 70
```

## 6. Sample Output

```
Location: Location A
Average: 31.25
Minimum: 20
Maximum: 40
20 - Safe
30 - Safe
40 - Safe
35 - Safe

Location: Location B
Average: 61.25
Minimum: 50
Maximum: 70
50 - Moderate
60 - Moderate
70 - Moderate
65 - Moderate

Location: Location C
Average: 91.25
Minimum: 80
Maximum: 100
80 - Dangerous
90 - Dangerous
100 - Dangerous
95 - Dangerous
```

Note: This is a simple educational example using sample environmental readings and illustrative thresholds.
