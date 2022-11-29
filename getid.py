import requests
import json

class Dyna:
    '''type prod, test or sandbox to create the object .'''
    def __init__(self, environment):
        environments = {'prod': {'tenant': 'vew56977', 'token': 'dt0c01.MDZEK3EVIMFZ6W7DGBEEMALQ.GWXPA7KSB5SXIVMRNFHRSZK32WQJZESTMVLZWQ4DW74SFSA5K43UAFGPRZTWSBRB'},
                        'test': {'tenant': 'afd69158', 'token': 'dt0c01.W5OJNZVKPSRHEAQWASS3D446.OVISPSIRXXK2EO66SJSHN2LANNXQDZ2SE35BR4KZQLE3ILGYH24JSBE6EKICPE7R'}}

        self.urlbyschema = {'maintenance': "/api/v2/settings/objects?schemaIds=builtin%3Aalerting.maintenance-window&scopes=environment",
                           'servers': "builtin%3host"}

        self.environment = environment
        self.tenant = environments[environment]["tenant"]
        self.token = environments[environment]["token"]
        self.headers = {'Authorization': f'Api-token {self.token}', 'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.urlofenvironment = f"https://{self.tenant}.live.dynatrace.com"



    def get_objectlist(self,schema):
        '''Get list of object and Id's '''
        urltocall=f'{self.urlofenvironment}{self.urlbyschema[schema]}'
        try:
            print(f'triyng {urltocall} with {self.headers}')
            response= requests.get(urltocall, headers=self.headers)
            print(f'status :  {response.status_code}')
            jsonfetch= json.loads(response.content)
        except:
            print("error")
            raise

        else:
            with open(f'objectlist-{self.environment}-{schema}.json', 'w') as outfile:
                json.dump(jsonfetch,outfile)
            return jsonfetch
            # Using a JSON string
            #with open('json_data.json', 'w') as outfile:
            #    outfile.write(jsonfetch)

dynaprod=Dyna("prod")
dynatest=Dyna("test")

dynatest.get_objectlist("maintenance")
dynaprod.get_objectlist("maintenance")

print("done")

