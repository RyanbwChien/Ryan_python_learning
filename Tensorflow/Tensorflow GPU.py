# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:10:35 2025

@author: USER
"""

import tensorflow as tf

print("TensorFlow 版本:", tf.__version__)
print("可用的 GPU:", tf.config.list_physical_devices('GPU'))
