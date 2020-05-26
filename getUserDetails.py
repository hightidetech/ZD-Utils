import time,requests,sys,creds

session = requests.Session()
instance=creds.login['instance']
auth=creds.login['auth']
session.headers.update({'Authorization': 'Basic ' + auth})

def getUserEmail(userID):
  
  url = 'https://' + instance + '.zendesk.com/api/v2/users/' + str(userID) + '.json'

  response=session.get(url)
  if response.status_code != 200:
      print('Status:', response.status_code, 'Problem with the request. Exiting.')
      exit()
  data=response.json()["user"]
  return data["email"]

if __name__=='__getUserEmail__':
  sys.exit(main(sys.argv[1]))
