# ZD-Utils
 Useful utilities for reading and writing to/from Zendesk

In order to use these utilities, you must first create a local creds.py file
that looks like the following:

login = {
  'instance' : 'YOURINSTANCENAME',
  'auth' : 'YOURBASE64AUTHENTICATIONSTRING'
}

All of the utilitities require this file to be present and populated before they
will work correctly.

# get orgName from orgID
python -c 'from getOrgDetails import getOrgName; print getOrgName(############)'

# get orgMemberships from orgID
python -c 'from getOrgDetails import getOrgMemberships; print getOrgMemberships(############)'

# get orgOpenTicketIds from orgID
python -c 'from getOrgDetails import getOrgOpenTicketIds; print getOrgOpenTicketIds(############)'

# set userSuspension for userID
python -c 'from setUserDetails import setUserSuspension; print setUserSuspension(############)'

# set orgNotes for orgID 
python -c 'from setOrgDetails import setOrgNotes; print setOrgNotes(##########, "Churned on 01.01.2020")'

# churn entire org for orgID
./churnOrg -o "############" -d "01.01.2020"
