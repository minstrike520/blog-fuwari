# How to Setup Your Obsidian Posts Repository

To complete the decoupling of your posts from the blog, follow these steps in your **Obsidian Notes (Posts) Repository**.

## 1. Prepare GitHub Secrets
In your **Obsidian Posts Repository**, go to `Settings` -> `Secrets and variables` -> `Actions` and add the following secret:
*   `BLOG_DEPLOY_TOKEN`: A GitHub Personal Access Token (PAT) with `repo` scope. This is needed to trigger the blog's repository dispatch.

## 2. Create the Trigger Workflow
Create a file named `.github/workflows/trigger-blog-deploy.yml` in your **Obsidian Posts Repository** with the following content:

```yaml
name: Trigger Blog Deploy

on:
  push:
    branches:
      - main  # or your default branch name

jobs:
  dispatch:
    runs-on: ubuntu-latest
    steps:
      - name: Repository Dispatch
        uses: peter-evans/repository-dispatch@v3
        with:
          token: ${{ secrets.BLOG_DEPLOY_TOKEN }}
          repository: your-username/blog-fuwari  # <--- UPDATE THIS to your blog repo path
          event-type: update-posts
```

## 3. Blog Repository Configuration
In your **Blog Repository** (`blog-fuwari`), go to `Settings` -> `Secrets and variables` -> `Actions` and add these secrets:
*   `POSTS_REPOSITORY`: The full name of your posts repository (e.g., `your-username/my-obsidian-notes`).
*   `PAT_FOR_CHECKOUT`: The same PAT used above (or another one) that has access to read the posts repository.

## 4. Local Development
To preview your Obsidian notes in the blog locally:
1. Open your terminal in the `blog-fuwari` directory.
2. Run the following command (replace the path with your actual Obsidian vault posts path):
   ```bash
   ln -s /path/to/your/obsidian/vault/posts src/content/posts/obsidian
   ```
   *Note: Since we updated `.gitignore`, these files won't be committed to the blog repo.*

## 5. Frontmatter Compliance
Ensure your Obsidian notes have the required frontmatter in `src/content/config.ts`:
```yaml
---
title: "My Post Title"
published: 2024-04-29
description: "A short description"
tags: ["tag1", "tag2"]
category: "My Category"
---
```
