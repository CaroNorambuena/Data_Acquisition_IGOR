# Data_Acquisition_IGOR

Igor Pro by WaveMetrics is an interactive software designed for scientists and engineers that enables data analysis, image processing, and the creation of high-quality graphics for publication. It is notable for its ability to handle large datasets, custom programming, curve fitting, and instrument control. It is frequently used in fields such as electrophysiology, physics, and various engineering disciplines (https://www.wavemetrics.com/).

In neurophysiology, neuronal activity is recorded in the brain using multiple electrodes. Each electrode corresponds to a channel. A single experiment can store a large amount of neuronal activity data (time vs. voltage) distributed across multiple channels. These experiments are saved as data packages in Igor, where each package contains the acquired dataset divided by channels.

Given the importance of Python in data analysis, a converter was developed to transform Igor data into a Python-compatible format. This made it possible to generate a single CSV file containing neuronal activity recorded across 32 channels. As a result, the data can be handled as a single DataFrame, which simplifies analysis and opens the door to machine learning applications.

Link to download the files corresponding to the project data: 
https://drive.google.com/drive/folders/1dBVd0imK2-w_8OA76Pd0Jzmq8ys_aBdX?usp=sharing
