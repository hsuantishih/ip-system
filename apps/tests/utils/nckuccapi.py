from zeep import Client, Settings
from zeep.plugins import HistoryPlugin
from zeep.xsd import Element, ComplexType, String, Sequence
from lxml import etree

# 建立 NckuCcApi 物件
class NckuCcApi:
    # 設定 soap client 參數
    def __init__(self):
        # wsdl url
        self.wsdl_url = 'http://140.116.249.154/~dondon/nckuccapi/nckuccapi.wsdl'
        # header apikey
        self.api_element = 'apikey'
        self.api_key = 'kaizujduewjudyus'
        self.header = ComplexType(Sequence([Element(self.api_element, String())]))
        self.header_value = self.header(apikey=self.api_key)
        # client settings
        self.settings = Settings(strict=False, xml_huge_tree=True)
        self.history = HistoryPlugin()
        # 命名空間
        self.namespaces = {
            'SOAP-ENV': 'http://schemas.xmlsoap.org/soap/envelope/',
            'ns1': 'http://www.cc.ncku.edu.tw/nckuccapi/',
            'ns2': 'http://xml.apache.org/xml-soap',
            'SOAP-ENC': 'http://schemas.xmlsoap.org/soap/encoding/',
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            'xsd': 'http://www.w3.org/2001/XMLSchema'
        }

    # 設定 header
    def SetApiKey(self):
        self.client = Client(self.wsdl_url, settings=self.settings, plugins=[self.history])
        self.client.set_default_soapheaders([self.header_value])

    # PrettyPrintXML 函式
    def PrettyPrintXML(self, xml_str):
        self.xml_str = xml_str
        pretty_xml_str = etree.tostring(xml_str, encoding='unicode', pretty_print=True)
        # print(pretty_xml_str)
    
    # 編輯 getuserinfo
    def GetUserInfo(self, userid):
        self.SetApiKey()

        data = {}
        try:
            self.client.service.getuserinfo(userid)
            root = self.history.last_received['envelope']
            self.PrettyPrintXML(root)

            # 處理資料
            for item in root.find('./SOAP-ENV:Body/ns1:getuserinfoResponse/return/item', namespaces=self.namespaces):
                key = item.find('key').text
                value = item.find('value').text
                data[key] = value
            
            # print("查詢成功")

        except:
            data = {}
            # print("查無資料")

        return data
    
    # 編輯 authenticate
    def Authenticate(self, userid, password):
        if userid == "" or password == "":
            return {}

        self.SetApiKey()
        self.client.service.authenticate(userid, password)
        root = self.history.last_received['envelope']
        self.PrettyPrintXML(root)

        # 處理資料
        data = {}
        for item in root.find('./SOAP-ENV:Body/ns1:authenticateResponse/return', namespaces=self.namespaces):
            key = item.find('key').text
            value = item.find('value').text
            data[key] = value

        return data