import time,requests,sys,creds

session = requests.Session()
instance=creds.login['instance']
auth=creds.login['auth']
session.headers.update({'Authorization': 'Basic ' + auth})

def setMoreOrgTags(orgID, tag):

  url = 'https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '/tags.json'
  entity = '{ "tags": ["'+ tag + '"] }'
  session.headers.update({'Content-Type': 'application/json'})

  response=session.put(url, data='{ "tags": ["' + tag + '"] }')
  #print(response.text)
  if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()
  
  data=response.json()
  return data["tags"]

if __name__=='__setMoreOrgTags__':
  sys.exit(main(sys.argv[1]))


def setOrgNotes(orgID, note):
 
  url = 'https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '.json'
  entity = '{"organization": {"notes": " + note + "}}'
  session.headers.update({'Content-Type': 'application/json'})

  response=session.put(url, data='{"organization": {"notes": "'  + note + '"}}')
  #print(response.text)
  if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()
 
  data=response.json()["organization"]
  return data["notes"]


if __name__=='__setOrgNotes__':
  sys.exit(main(sys.argv[1]))

def setOrgAccountStatusField(orgID, status):

  url = 'https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '.json'
  entity = '{"organization": {"organization_fields": {"account_status":" + status + "}}'
  session.headers.update({'Content-Type': 'application/json'})

  response=session.put(url, data='{"organization": {"organization_fields": {"account_status":"' + status + '"}}')
  #print(response.text)
  if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

  data=response.json()["organization"]["organization_fields"]
  return data["account_status"]

if __name__=='__setOrgAccountStatusField__':
  sys.exit(main(sys.argv[1]))

def setOrgExternalID(orgID, extID):
  url = 'https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '.json'
  entity = '{"organization": {"external_id":" + extID + "}}'
  session.headers.update({'Content-Type': 'application/json'})

  response=session.put(url, data='{"organization": {"external_id":"' + extID + '"}}')
  #print(response.text)
  if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

  data=response.json()["organization"]
  return data["external_id"]

if __name__=='__setOrgExternalID':
  sys.exit(main(sys.argv[1]))

def setOrgSupportLevel(orgID, orgSL):

  url = 'https://' + instance + '.zendesk.com/api/v2/organizations/' + str(orgID) + '.json'
  entity = '{"organization": {"organization_fields": {"support_level":" + orgSL + "}}'
  session.headers.update({'Content-Type': 'application/json'})

  response=session.put(url, data='{"organization": {"organization_fields": {"support_level":"' + orgSL + '"}}')
  #print(response.text)
  if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

  data=response.json()["organization"]["organization_fields"]
  return data["support_level"]


if __name__=='__setOrgSupportLevel__':
  sys.exit(main(sys.argv[1]))
