# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 03:28:52 2025

@author: user
"""

# search tools
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

search.invoke("台灣新竹縣2025/4/5溫度幾度?")


search.invoke("2025年台灣總統是誰?")
