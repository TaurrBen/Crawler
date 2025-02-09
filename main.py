# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：  
# 1. 不得用于任何商业用途。  
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。  
# 3. 不得进行大规模爬取或对平台造成运营干扰。  
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。   
# 5. 不得用于任何非法或不当的用途。
#   
# 详细许可条款请参阅项目根目录下的LICENSE文件。  
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。  

# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : main.py
# Time       ：2025.2.8 23:23
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import asyncio
import sys

import cmdArg
import config
import abstractBaseClass
class CrawlerFactory:
    CRAWLERS = {
        # "xhs": XiaoHongShuCrawler,
        # "dy": DouYinCrawler,
        # "ks": KuaishouCrawler,
        "bili": BilibiliCrawler,
        # "wb": WeiboCrawler,
        # "tieba": TieBaCrawler,
        # "zhihu": ZhihuCrawler
    }

    @staticmethod
    def create_crawler(platform: str) -> abstractBaseClass.AbstractCrawler:
        crawler_class = CrawlerFactory.CRAWLERS.get(platform)
        if not crawler_class:
            raise ValueError("Invalid Media platform Currently only supported xhs or dy or ks or bili ...")
        return crawler_class()

async def main():
    # parse cmd
    await cmdArg.parse_cmd()

    crawler = CrawlerFactory.create_crawler(platform=config.PLATFORM)
    await crawler.start()

if __name__ == '__main__':
    try:
        # asyncio.run(main())
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        sys.exit()