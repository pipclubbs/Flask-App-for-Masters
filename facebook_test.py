# import facebook
import requests

token = "EAAElUOF2ZABoBO4yYlKyFv6V8V0sTnbOEWcBtw7S6oy24wZA8O84mLZAj4atjJdcn1vRxZCSO9SmWJ1yDARYHZCvWl4W3dmNH0Oz6QANrGUryXMxSXgXQdzsrCDzBf2bA6zzlXXtnX0Fe5DOF5eitgL6r8AqyfPlt6G9bJcdqFME6WmBSFeBcT6zRLm040ZAx9GbxMT7FAWXQZD"


# Set up your Facebook App credentials
app_id = "322504286954522"
app_secret = "50738f199922f8e584333f0cadddbd77"
access_token = token

# Define the keywords to search for in group descriptions
keywords = ['climbing', 'bouldering']

# Initialize a list to store the results
results = []

# Iterate through the keywords and search for groups
for keyword in keywords:
    url = f'https://graph.facebook.com/v12.0/search?q={keyword}&type=group&access_token={access_token}'
    response = requests.get(url)
    data = response.json()

    print(data)

    if 'data' in data:
        for group in data['data']:
            group_id = group['id']
            group_name = group.get('name', 'N/A')
            group_description = group.get('description', 'N/A')

            results.append({
                'group_id': group_id,
                'group_name': group_name,
                'group_description': group_description
            })

# Print the results
for result in results:
    print(f"Group ID: {result['group_id']}")
    print(f"Group Name: {result['group_name']}")
    print(f"Group Description: {result['group_description']}")
    print()
