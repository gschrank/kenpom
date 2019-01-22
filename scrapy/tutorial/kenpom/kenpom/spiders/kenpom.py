import scrapy, datetime

class QuotesSpider(scrapy.Spider):
    name = "kenpom"
    start_urls = [
        'https://kenpom.com/',
    ]

# parses respnse based on css
    def parse(self, response):
        for kenpom in response.xpath('//*[@id="ratings-table"]/tbody'):
            yield {
                'rank': kenpom.xpath('tr/td[1]/text()').extract(),
                'team': kenpom.xpath('tr/td[2]/a/text()').extract(),
                'conf': kenpom.xpath('tr/td[3]/text()').extract(),
                'record': kenpom.xpath('tr/td[4]/text()').extract(),
                'adjem': kenpom.xpath('tr/td[5]/text()').extract(),
                'adjo': kenpom.xpath('tr/td[6]/text()').extract(),
                'adjd': kenpom.xpath('tr/td[8]/text()').extract(),
                'adjt': kenpom.xpath('tr/td[10]/text()').extract(),
                'luck': kenpom.xpath('tr/td[12]/text()').extract(),
                'sos-adjem': kenpom.xpath('tr/td[14]/text()').extract(),
                'sos-oppo': kenpom.xpath('tr/td[16]/text()').extract(),
                'sos-oppd': kenpom.xpath('tr/td[18]/text()').extract(),
                'ncsos-adjem': kenpom.xpath('tr/td[20]/text()').extract(),
            }
#//*[@id="ratings-table"]/tbody[1]/tr[1]/td[1]

#output date "+%d_%m_%y"
# follows relative links until no more
        #next_page = response.css('li.next a::attr(href)').extract_first()
        #print(next_page)
        #if next_page is not None:
            #yield response.follow(next_page, callback=self.parse)
            #print(response.follow(next_page, callback=self.parse))
