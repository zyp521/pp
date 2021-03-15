from scrapy import cmdline

cmdline.execute('scrapy crawl menu_spider'.split())

from scrapy.core.engine import ExecutionEngine