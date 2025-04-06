# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:09:39 2025

@author: user
"""
import openai
import os
from linebot.models import TextMessage

# =============================================================================
# 沒錯！你目前使用的是 OpenAI 官方的 Python 套件（openai），也就是直接使用 OpenAI 的原生 SDK。
# 這種方式比較「低階」，控制細節比較多、彈性也高，但也需要你自己處理一些像是 function call、streaming、retry 等邏輯。
# =============================================================================

def ask_openai(message):
    openai.api_key = os.environ["openai_apikey"]
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages = [
        { "role": "system", "content": "You are a helpful assistant." },
        { "role": "system", "content": "請盡量回覆的字數少於100字以內" },
        {
            "role": "user",
            "content": f"{message}",
        },
    ],
        # prompt = message,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.8,
        # handle_parsing_errors=True,
    )  
    answer = response.choices[0].message.content.strip()
    return(answer)