# Add Funding Information to GitHub Projects

GitHub allows you to display a "Sponsor" button on your repository by creating a `.github/FUNDING.yml` file. This makes it easy for users to support your open-source work.

## Setup

Create a `.github/FUNDING.yml` file in your repository root:

```yaml
# .github/FUNDING.yml
github: YourGitHubUsername
patreon: YourPatreonUsername
open_collective: your-project
ko_fi: YourKoFiUsername
tidelift: npm/package-name
community_bridge: project-name
liberapay: YourLiberapayUsername
issuehunt: YourIssueHuntUsername
otechie: YourOtechieUsername
lfx_crowdfunding: project-name
custom: ["https://your-website.com/donate", "https://example.com"]
buy_me_a_coffee: YourBuyMeACoffeeUsername
```

## Supported platforms

GitHub supports multiple funding platforms:
- GitHub Sponsors (`github`)
- Patreon (`patreon`)
- Open Collective (`open_collective`)
- Ko-fi (`ko_fi`)
- Tidelift (`tidelift`)
- Community Bridge (`community_bridge`)
- Liberapay (`liberapay`)
- IssueHunt (`issuehunt`)
- Otechie (`otechie`)
- LFX Crowdfunding (`lfx_crowdfunding`)
- Buy Me a Coffee (`buy_me_a_coffee`)
- Custom URLs (`custom`)

## Example

```yaml
# .github/FUNDING.yml
github: CuriousLearner
buy_me_a_coffee: CuriousLearner
```

Once committed, GitHub will automatically display a "Sponsor" button on your repository's main page with links to your funding platforms.

## Important notes

**File location**: The file must be named exactly `FUNDING.yml` (or `FUNDING.yaml`) and placed in the `.github` directory at the repository root.

**Visibility**: The sponsor button appears on public repositories. It won't show on private repositories.

**Multiple accounts**: You can specify multiple usernames for platforms that support it (like GitHub Sponsors) by using an array:

```yaml
github: [user1, user2, user3]
```

**Custom URLs**: Use the `custom` field for any donation link not covered by the supported platforms (maximum of 4 custom URLs).

Use GitHub funding configuration to make it easy for the community to support your open-source contributions.
