# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 10:10:39 2025

@author: USER
"""


"""
git clone https://github.com/Dao-AILab/flash-attention.git

cd flash-attention

pip install . 
"""



import torch

print(torch.version.cuda)

torch.cuda.is_available()

torch.cuda.device_count()

# 列出所有可用的 GPU
if torch.cuda.is_available():
    num_gpus = torch.cuda.device_count()
    for i in range(num_gpus):
        print(f"cuda:{i} - {torch.cuda.get_device_name(i)}")
else:
    print("No GPU available, using CPU.")
    
    
    
