const { Octokit } = require('@octokit/rest');
const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });

async function commentOnIssue() {
  const issueNumber = process.env.GITHUB_REF.split('/')[2]; // Extract issue number from GITHUB_REF
  const commentBody = 'Thank you for opening this issue!';

  await octokit.issues.createComment({
    owner: 'pradeem',
    repo: 'mpoctest',
    issue_number: issueNumber,
    body: commentBody,
  });
}

commentOnIssue();
