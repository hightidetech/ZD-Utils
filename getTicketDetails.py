import time,requests,sys,creds

session = requests.Session()
instance=creds.login['instance']
auth=creds.login['auth']
session.headers.update({'Authorization': 'Basic ' + auth})

def getTicketStatus(ticketID):

  url = 'https://' + instance + '.zendesk.com/api/v2/tickets/' + str(ticketID) + '.json'
  session.headers.update({'Content-Type': 'application/json'})

  response=session.get(url)
  #print(response.text)
  if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()
  
  data=response.json()
  return data

if __name__=='__getTicketStatus__':
  sys.exit(main(sys.argv[1]))
