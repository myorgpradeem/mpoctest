import requests

def cancel_team_invitations(team_id, headers):
    # Get list of pending invitations for the team
    response = requests.get(f'https://api.github.com/teams/{team_id}/invitations', headers=headers)
    if response.status_code == 200:
        invitations = response.json()
        for invitation in invitations:
            invitation_id = invitation['id']
            # Cancel the invitation
            cancel_response = requests.delete(f'https://api.github.com/teams/{team_id}/invitations/{invitation_id}', headers=headers)
            if cancel_response.status_code == 204:
                print(f"Invitation with ID {invitation_id} canceled successfully.")
            else:
                print(f"Failed to cancel invitation with ID {invitation_id}: {cancel_response.text}")
    else:
        print(f"Failed to retrieve invitations for team ID {team_id}: {response.text}")

def cancel_all_team_invitations(organization, headers):
    # Get list of teams in the organization
    response = requests.get(f'https://api.github.com/orgs/{organization}/teams', headers=headers)
    if response.status_code == 200:
        teams = response.json()
        for team in teams:
            team_id = team['id']
            print(f"Cancelling invitations for team '{team['name']}' (ID: {team_id})")
            cancel_team_invitations(team_id, headers)
    else:
        print(f"Failed to retrieve teams for organization {organization}: {response.text}")

# Authentication
headers = {
    'Authorization': 'Bearer ${{ secrets.API_TOKEN }}',  # Replace with your OAuth token
    'Accept': 'application/vnd.github.v3+json'
}

# Specify the organization name
organization = 'myorgpradeem'

cancel_all_team_invitations(organization, headers)
