import scrapy

class Citas Spider(scrapy.Spider): 
    name = "citas"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response): 
        for cita in response.css("div.quote"):
            yield {
                "texto":cita.css("span.text::text").get(),
                "autor": cita.xpath("span/small/text()").get()
            }


        print(response.css("div.quote"))