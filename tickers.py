#-----=====Empery Scraper | Yahoo Based Feed=====-----#
#Version 4.0 | Martin Ortega Jr. | martin.ortega@emperyam.com | 6/22/17
import scrapy
import collections

from collections import OrderedDict
from scrapy.spiders import XMLFeedSpider
from tickers.items import tickersItem
class Spider(XMLFeedSpider):
    name = "NewsScraper"
    allowed_domains = ["yahoo.com"]
    start_urls = (
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=ABIO,ACFN,AEMD,AEZS,AITB,AJX,AU,AKER,AMRS,AMPE,APDN,APHB,APOP,ARGS,ARTH,ASM,AUMN,AUPH,AVL,AXPW',
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=BGMD,BIOA,BIOC,BLDP,BLPH,BPMX,BPTH,BSTG,BTX',
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=CANF,CBIO,CCCR,CDTI,CERC,CERE,CFRX,CGIX,CHEK,CNIT,COGT,CRMD,CTRV,CTSO,CYDY,CYRN,CYRX,CHFS',
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=DRIO,DRWI,DXTR,GALE,GALT,GBSN,GEVO,EARK,EARS,EDAP,EKSO,EMAN,ENCR,ENPT,ETRM,EVOK,EYEG,FCEL,FTFT',
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=GNMX,GNUS,GPL,HIPP,HSGX,HTM,IDXG,IMMU,IMRN,IMUC,INNV,INVT,IPCI,INPX,JAGX,KDMN,KTOV,LQMT',
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=MBOT,MBVX,MCZAF,MDGS,MRDN,MRIC,MTST,MVIS',
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=NBY,NNVC,NTRP,NVIV,NWBO,OHRP,OPGN,OPTT,ORPN,OXGN',
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=PGRX,PLXP,PTN,QRH,RGSE,RNN,RNVA,ROKA,RVX,ROKA,RVX,RWLK,RXII',
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=SANW,SBOT,SCON,SCYX,SHIP,SPHS,SRAX,STDY,SUNW,SYN,TBIO,TEUM,TMPS,TOPS,TPIVD,TRXC,TTNP',
        'https://feeds.finance.yahoo.com/rss/2.0/headline?s=UNXL,UQM,URRE,UUUU,VBLT,VGZ,VKTX,VTGN,WINT,XGTI,XTNT,XXII,ZSAN',
                  )
    itertag = 'item'
    def parse_node(self, response, node):
        item = collections.OrderedDict()
        item['Title'] = node.xpath(
            'title/text()').extract_first()
        item['PublishDate'] = node.xpath(
            'pubDate/text()').extract_first()
        item['Description'] = node.xpath(
            'description/text()').extract_first()      
        item['Link'] = node.xpath(
            'link/text()').extract_first()
        return item
