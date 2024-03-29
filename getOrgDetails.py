import time,requests, sys, creds

session = requests.Session()
instance=creds.login['instance']
auth=creds.login['auth']
session.headers.update({'Authorization': 'Basic ' + auth})

def getOrgName(orgID):

  url='https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '.json'

  response=session.get(url)
  if response.status_code != 200:
      print('Status:', response.status_code, 'Problem with the request. Exiting.')
      exit()
  data=response.json()["organization"]["name"]
  return data

if __name__=='__getOrgName__':
    sys.exit(main(sys.argv[1]))

def getOrgMemberships(orgID):
  
  url='https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '/organization_memberships.json'
  output = ''

  while url:
    #print("Fetching Data for " + url);
    response=session.get(url)
    #print(data.headers)
    if response.status_code != 200:
       print('Status:', response.status_code, 'Problem with the request. Exiting.')
       exit()
    data=response.json()
    for user in data['organization_memberships']:
      output += str(user['user_id']) + '\n'
    url = data['next_page']
  return output    

#    with open('userids.txt', mode='w') as f:
#      f.write(output)


if __name__=='__getOrgMemberships__':
    sys.exit(main(sys.argv[1]))

def getOrgOpenTicketIds(orgID):

  url='https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '/tickets.json'
  output = ''

  while url:
    #print("Fetching Data for " + url);
    response=session.get(url)
    #print(data.headers)
    if response.status_code != 200:
       print('Status:', response.status_code, 'Problem with the request. Exiting.')
       exit()
    data=response.json()
    for ticket in data['tickets']:
      ticket_status = ticket['status']
      if (ticket_status != "closed"):
        output += str(ticket['id']) + '\n'
    url = data['next_page']
  return output


if __name__=='__getOrgOpenTicketIds__':
    sys.exit(main(sys.argv[1]))

def getOrgSupportLevel(orgID):

  url='https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '.json'

  response=session.get(url)
  if response.status_code != 200:
      print('Status:', response.status_code, 'Problem with the request. Exiting.')
      exit()
  data=response.json()["organization"]["organization_fields"]["support_level"]
  return data


if __name__=='__getOrgAccountStatus':
    sys.exit(main(sys.argv[1]))

def getOrgAccountStatus(orgID):

  url='https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '.json'

  response=session.get(url)
  if response.status_code != 200:
      print('Status:', response.status_code, 'Problem with the request. Exiting.')
      exit()
  data=response.json()["organization"]["organization_fields"]["account_status"]
  return data


if __name__=='__getOrgAccountStatus':
    sys.exit(main(sys.argv[1]))

def getOrgNotes(orgID):

  url='https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '.json'

  response=session.get(url)
  if response.status_code != 200:
      print('Status:', response.status_code, 'Problem with the request. Exiting.')
      exit()
  data=response.json()["organization"]["notes"]
  return data


if __name__=='__getOrgNotes':
    sys.exit(main(sys.argv[1]))

def getOrgAccountType(orgID):

  url='https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '.json'

  response=session.get(url)
  if response.status_code != 200:
      print('Status:', response.status_code, 'Problem with the request. Exiting.')
      exit()
  data=response.json()["organization"]["organization_fields"]["account_type"]
  return data

if __name__=='__getOrgAccountType':
    sys.exit(main(sys.argv[1]))

def getOrgExternalID(orgID):

  url='https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '.json'

  response=session.get(url)
  if response.status_code != 200:
      print('Status:', response.status_code, 'Problem with the request. Exiting.')
      exit()
  data=response.json()["organization"]["external_id"]
  return data

if __name__=='__getOrgExternalID':
    sys.exit(main(sys.argv[1]))

def getOrgCreatedDate(orgID):

  url='https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '.json'

  response=session.get(url)
  if response.status_code != 200:
      print('Status:', response.status_code, 'Problem with the request. Exiting.')
      exit()
  data=response.json()["organization"]["created_at"]
  return data.split('T')[0]


if __name__=='__getOrgCreatedDate':
    sys.exit(main(sys.argv[1]))
