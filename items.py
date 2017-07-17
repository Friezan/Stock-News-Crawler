from collections import OrderedDict

from scrapy import Field, Item
import six

class OrderedItem(Item):
    def __init__(self, *args, **kwargs):
        self._values = OrderedDict()
        if args or kwargs:  # avoid creating dict for most common case
            for k, v in six.iteritems(dict(*args, **kwargs)):
                self[k] = v

class tickersItem(OrderedItem):
    Title = Field()
    PublishDate = Field()
    Description = Field()
    Link = Field()
