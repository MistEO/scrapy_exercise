from scrapy import cmdline

name = 'bilibili_hot_anime'
cmd = 'scrapy crawl {0} -o bilibili.csv'.format(name)
cmdline.execute(cmd.split())