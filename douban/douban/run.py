from scrapy import cmdline

name = 'douban_ajax'
cmd = 'scrapy crawl {0} -o douban.csv'.format(name)
cmdline.execute(cmd.split())