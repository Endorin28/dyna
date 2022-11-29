import requests
import json

class Dyna:
    '''type prod, test or sandbox to create the object .'''
    def __init__(self, name):
        environments = {'prod': {'tenant': 'vew56977', 'token': 'dt0c01.MDZEK3EVIMFZ6W7DGBEEMALQ.GWXPA7KSB5SXIVMRNFHRSZK32WQJZESTMVLZWQ4DW74SFSA5K43UAFGPRZTWSBRB'},
                        'test': {'tenant': 'afd69158', 'token': 'dt0c01.W5OJNZVKPSRHEAQWASS3D446.OVISPSIRXXK2EO66SJSHN2LANNXQDZ2SE35BR4KZQLE3ILGYH24JSBE6EKICPE7R'}}
        objectschema = {'maintenance': "builtin%3Aalerting.maintenance-window",
                        'servers': "builtin%3host"}

        self.name = name
        self.tenant = environments[name]["tenant"]
        self.token = environments[name]["token"]
        self.schemaneeded = objectschema['maintenance']
        self.headers = {'Authorization': f'Api-token {self.token}', 'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.urlofobjectinfosfromschema = f"https://{self.tenant}.live.dynatrace.com/api/v2/settings/objects?schemaIds={self.schemaneeded}&scopes=environment"
        self.url = f"https://{self.tenant}.live.dynatrace.com/api/v1/synthetic/monitors"
        self.urlsynthmonitor = f"https://{self.tenant}.live.dynatrace.com/api/v1/synthetic/monitors"



    def listobjects(self,schema):
        '''list the synth test '''
        try:
            print(f"triyng {self.urlofobjectinfosfromschema} with {self.headers}")
            response= requests.get(self.urlofobjectinfosfromschema, headers=self.headers)
            print(f'status :  {response.status_code}')
            jsonfetch= json.loads(response.content)
        except:
            print("error")
            raise

        else:
            with open(f'objectlist{self.schemaneeded}_{self.name}.json', 'w') as outfile:
                json.dump(jsonfetch,outfile)
            return jsonfetch
            # Using a JSON string
            #with open('json_data.json', 'w') as outfile:
            #    outfile.write(jsonfetch)

    def get_objectlist(self,schemaasked):
        '''get the url list inside each synth test'''
        #get list
        list={}
        objectlist = self.listobjects(schemaasked)
'''       
            for monitor in synth_monitor_list["monitors"]:
            #print(f'checking {monitor["name"]} with id {monitor["entityId"]}')
            url_to_fetch=f'https://{self.tenant}.live.dynatrace.com/api/v1/synthetic/monitors/{monitor["entityId"]}'
            fetched= json.loads((requests.get(url_to_fetch, headers=self.headers)).content)
            print("**********" * 15)
            print(f'{monitor["name"]}')
            if fetched["type"] != "BROWSER":
                for request in fetched["script"]["requests"]:
                    print(f'url : {request["url"]}')

'''
dynaprod=Dyna("prod")
dynatest=Dyna("test")

dynatest.get_objectlist("maintenance")

