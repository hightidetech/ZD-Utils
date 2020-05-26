import time,requests,sys,creds

session = requests.Session()
instance=creds.login['instance']
auth=creds.login['auth']
session.headers.update({'Authorization': 'Basic ' + auth})

def setTicketChurnStatus(ticketID):

  url = 'https://' + instance + '.zendesk.com/api/v2/tickets/' + str(ticketID) + '.json'
  session.headers.update({'Content-Type': 'application/json'})

  response=session.put(url, data='{"ticket": {"status": "solved", "custom_fields":[ {"id":"360009881451","value":"customer_churn"}, {"id":360008846611,"value":"web_app"}, {"id":360017327432,"value":"manager_app"}, {"id":360002722811,"value":"other"}, {"id":360009777152,"value":"customer"}, {"id":360019885252,"value":"fair_request"}, {"id":360009882971,"value":"manager"}],"comment": { "body": "Solving ticket for churned account", "author_id": 366900966271, "public": false}}}')
  #print(response.text)
  if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()
  
  data=response.json()["ticket"]
  return data["status"]

if __name__=='__setTicketChurnStatus__':
  sys.exit(main(sys.argv[1]))
