import time,requests,sys,creds

session = requests.Session()
instance=creds.login['instance']
auth=creds.login['auth']
session.headers.update({'Authorization': 'Basic ' + auth})

def setUserSuspension(userID):

  url = 'https://' + instance + '.zendesk.com/api/v2/users/' + str(userID) + '.json'
  entity = '{"user": {"suspended": true}}'
  session.headers.update({'Content-Type': 'application/json'})

  response=session.put(url, data='{"user": {"suspended": true}}')
  #print(response.text)
  if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()
  
  data=response.json()["user"]
  return data["suspended"]

if __name__=='__setUserSuspension__':
  sys.exit(main(sys.argv[1]))
