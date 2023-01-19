import scrapy
import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from riotwatcher import LolWatcher
from MetaSraper.items import champItem
from scrapy.loader import ItemLoader
class MetaSpider(scrapy.Spider):
    name = 'metaspider'
    
    #Create list of champs in alphabetical order
    lol_watcher = LolWatcher('RGAPI-015be226-822c-4707-aea2-822651265044') #replace with tag
    versions = lol_watcher.data_dragon.versions_for_region('na1')
    champions_version = versions['n']['champion']
    current_champ_list = lol_watcher.data_dragon.champions(champions_version)['data']
    champNames = [x for x in current_champ_list]
    
    #Create urls list
    start_urls = []
    
    for x in champNames:
        start_urls.append('https://www.metasrc.com/aram/champion/' + x.lower())
        
    
    
    logging.getLogger('scrapy').setLevel(logging.WARNING)
    def parse(self, response):
        currItem = ItemLoader(item = champItem(), response = response)
        
        champName = response.request.url.split('/')[-1];
        #print (champName)
        champRelations = {};
        
        
        champdivs = response.xpath('//div[@class=" _c8xw44 _cu8r22"]')
        for node in champdivs:
            if("team" in node.xpath(".//h2/text()").get()):
                aElements = node.xpath(".//a")
                for i in aElements.xpath('.//div[contains(@class, "_95ecnz")]'):
                    
                    reChamp = i.attrib['data-search-terms-like'].split("|")[1] #name of relating Champ
                    
                    reStat = i.xpath('.//div[@class=" _9581uw"]/text()').get()
                    if(reStat == None):
                        champRelations[reChamp] = 0.0;
                    else:
                        champRelations[reChamp] = reStat;
                    
                    #nums = node.xpath('.//div[@class=" _9581uw"]/text()')
                    #node has no children but is siblings with data
        
        
        currItem.add_value('relations', champRelations.copy())
        currItem.add_value('name', champName)
        yield currItem.load_item();

