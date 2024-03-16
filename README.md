curl -L -X PUT -H "Accept: application/vnd.github+json" -H "Authorization: Bearer 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" -H "X-GitHub-Api-Version: 2022-11-28"  https://api.github.com/user/installations/48299343/repositories/767945234

name: Issue Comment Variables

on:
  issue_comment:
    types: [created]

jobs:
  process-comment:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Debug Comment Content
      run: |
          echo "Comment Content: ${{ github.event.comment.body }}"

    - name: Extract Variables
      id: extract
      run: |
        echo "${{ github.event.comment.body }}" > comment.txt
        cat comment.txt  # Check the content of comment.txt
        VAR_NAME=$(cat comment.txt | cut -d' ' -f2)  # Extract the variable using cut
        echo "Extracted Variable: $VAR_NAME"
        echo "VAR_NAME=$VAR_NAME" >> $GITHUB_ENV  # Set the environment variable using Environment Files

    - name: Use Variables
      run: |
        curl -L -X PUT -H "Accept: application/vnd.github+json" -H "Authorization: Bearer ${{ secrets.API_TOKEN }}" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/orgs/myorgpradeem/teams/myteam/memberships/$VAR_NAME
