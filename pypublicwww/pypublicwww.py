# encoding: utf8
from .lib import *
import xmltodict
import urllib
import json

class PyPublicWWW:

    def __init__(self, apikey, debug=False, timeout=5):
        self.api_key = apikey
        self.base_url = 'https://publicwww.com/'
        self.timeout = timeout

    def info(self):
        data=self.check_apikey()
        try:
            rdata = xmltodict.parse('<plan_status>'+data['data']+'</plan_status>')
            return json.dumps(rdata['plan_status'])
        except:
            return("Respuesta invalida: "+data['data'])

    def check_apikey(self):
        return self._action('profile/api_status.xml', 'GET')

    def _complete_url(self, action, querystring=None, csv=None, snippets=None):
        if querystring:
            action = action + urllib.parse.quote(str(querystring).encode('utf-8'),safe='') + "/"
        if csv:
            if snippets:
                return "{}{}?export=csvsnippetsu&delimiterColumns=$$&key={}".format(self.base_url, action, self.api_key)
            else:
                return "{}{}?export=csvu&key={}".format(self.base_url, action, self.api_key)
        else:
            return "{}{}?key={}".format(self.base_url, action, self.api_key)

    def _req(self, action, method, querystring=None, csv=None, snippets=None ):
        session = retry_session(retries=3)
        kwargs = {"timeout": self.timeout}
        res = session.request(method, self._complete_url(action,querystring,csv,snippets), **kwargs)
        return session, res

    def _action(self, action, method, querystring=None, csv=None, snippets=None, retries=1):
        for i in range(retries):
            try:
                s, r = self._req(action, method, querystring=querystring, csv=csv, snippets=snippets)
                break
            except requests.exceptions.ReadTimeout as e:
                if i >= retries-1:
                    raise e
        if not r.status_code in [200, 201, 204]:
            raise UnexpectedError(r.status_code, r.text)

        return {"status_code": r.status_code, "data": r.text}

    def _search_websites(self, querystring, csv=None, snippets=None):
        if querystring:
            data=self._action('websites/', 'GET', querystring, csv, snippets)
            if csv:
               if snippets:
                   cleandata= 'url,ranking,snippets'
                   for line in data['data'].split('\n'):
                       if line:
                           newline= line.split("$$")
                           newline[2]=newline[2].replace('"',"'")
                           newline[2]= "\""+newline[2]+"\""
                           cleandata= cleandata+"\n"+','.join(newline)
               else:
                   fieldnames= 'url,ranking'
                   cleandata=fieldnames+"\n"+data['data'].replace(';',',')
               return cleandata
            else:
                try:
                    rdata = xmltodict.parse('<doc>'+data['data']+'</doc>')
                    return rdata
                except:
                    return("Respuesta invalida: "+data['data'])
        return "No query string"
