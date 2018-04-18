from scrapy import Field


class EsRsguidesItem(Field):
    DOCUMENT_ID = Field()
    TITLE = Field()
    CONTENT = Field()
    SOURCE = Field()
    SUBJECTS = Field()
    START_DATE = Field()
    END_DATE = Field()
    pass
