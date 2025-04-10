import asyncio
import json
import os
import datetime
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import LLMExtractionStrategy
from pydantic import BaseModel, Field
import openai
from dotenv import load_dotenv

load_dotenv()

class FraudNewsSchema(BaseModel):
    reported_date: str = Field(..., description="The date the article or case occurred.")
    victim_gender: str = Field(..., description="ender of the victim (e.g., Male, Female, if the date is not available, then null.")
    victim_age: int = Field(..., description="Age of the victim. if the date is not available, then null.")
    fraud_type: str = Field(..., description="Type of fraud (e.g., phishing, investment scam. if the date is not available, then null.")
    fraud_details: str = Field(..., description="Specific tactics or messages used by the fraudsters. if the date is not available, then shownull.")
    financial_loss: str = Field(..., description="Total monetary loss suffered by the victim. if the date is not available, then null.")
    fraud_report: str = Field(..., description="original report full text of the news. if the date is not available, then null.")

async def main():
    # Set up the web crawler
    async with AsyncWebCrawler(verbose = True) as crawler:
        result = await crawler.arun(
            url = 'https://www.ettoday.net/news/20250114/2891866.htm',
            word_count_threshold = 1,
            extraction_strategy = LLMExtractionStrategy(
                provider = "openai/gpt-4o-mini" ,  api_token = os.getenv('OPENAI_API_KEY'),
                schema = FraudNewsSchema.schema(),
                extraction_type = "schema",
                instruction = """Extract and summarize the following key points from the given web page content related to fraud news. Provide the information in a structured format:
                                1. Reported Date: The date the news article was published or the fraud case occurred.
                                2. Victim Information: Gender and age of the victim(s) involved in the case. if the date is not available, then null.
                                3. Fraud Type: The specific type of fraud mentioned in the news, such as phishing, investment scam, online shopping scam, etc. if the date is not available, then null.
                                4. Fraud Details: Any specific messages, phrases, or tactics used by the fraudsters to deceive the victim(s). if the date is not available, then null.
                                5. Financial Loss: The total monetary loss suffered by the victim(s) due to the fraud. if the date is not available, then null.
                                6. Fraud Report: The original report full text of the news article or case. if the date is not available, then null.

                                Output the information in original language in a structured schema format with fields for each of the above key points.
                            """
            ),
            bypass_cache = True,
        )
        print(result.extracted_content)


# class OpenAIModelFee(BaseModel):
#     model: str = Field(..., description="Name for the OpenAI Model")
#     input_fee: str = Field(..., description="Fee for input token for the OpenAI Model")
#     output_fee: str = Field(..., description="Fee for output token for the OpenAI Model")

# async def main():
#     async with AsyncWebCrawler(verbose=True) as crawler:
#         # 確保 API 金鑰已設置
#         if not os.getenv('OPENAI_API_KEY'):
#             raise ValueError("OPENAI_API_KEY environment variable not set.")

#         result = await crawler.arun(
#             url='http://www.openai.com/api/pricing/',
#             word_count_threshold = 2,
#             extraction_strategy = LLMExtractionStrategy(
#             #use models supported by litellm - https://github.com/BerriAI/litellm
#             #provider="openai/gpt-4o", api_token=os.getenv('OPENAI_API_KEY'),
#             #provider="grop/11ama-3.1-78b-versatile", api_token="gsk_jDJX112crO140406767RMcojoodFFVWLKVFPypopZrAly204 )",
#             provider = "gpt-4o-mini" , api_token = os.getenv('OPENAI_API_KEY'),
#             #base_url="http://localhost:11434",
#             schema = OpenAIModelFee.schema(),
#             extraction_type="schema",
#             instruction = """From the crawled content, extract all mentioned model names along with their fees for input and output tokens.
#             Do not miss any model in the entire content. One extracted model json format should be like this:
#             {model_name": "GPT-4", "input_fee': "USS18.69 / 1M tokens", "output_fee": "USS39.88 / 1M tokens"}."""
#         ),
#         bypass_cache = True,
#     )
        
#     print(result.extracted_content)

if __name__ == "__main__":
    asyncio.run(main())