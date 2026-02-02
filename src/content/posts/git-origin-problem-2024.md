---
title: Git Authentication Problem Notes
published: 2024-11-12
tags:
  - Git
category: IT 除錯紀錄
---
## Situation
在Linux系統中，將遠端`origin`設定好，準備`push`上去時，系統提示輸入`Username for 'https://github.com'`跟`Password for 'https://<my account>/'`，照著輸入完之後，居然跳出：

```
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/<my account>/<my repo>/'
```
但是，當我轉而使用windows的cmd操作`push`時，卻連密碼都沒問我，就成功推送了。

## Solution
### REF_1 
[GitHub/Discussions: "github respiratory authentication failed"](https://github.com/orgs/community/discussions/29193)

> From August 13, 2021, GitHub is no longer accepting account passwords when authenticating Git operations. You need to add a PAT (Personal Access Token) instead, and you can follow the below method to add a PAT on your system.

> Create Personal Access Token on GitHub  
> From your GitHub account, go to `Settings => Developer Settings => Personal Access Token => Generate New Token (Give your password) => Fillup the form => click Generate token => Copy the generated Token`, it will be something like `ghp_sFhFsSHhTzMDreGRLjmks4Tzuzgthdvfsrta`

這個操作是要我生成PAT(就是存取用Token)，於是我照做了。
我生成了[StudyingSpace Repo Access For Local Git](https://github.com/settings/personal-access-tokens/2995466) ，到期日是2024/4/22。

### REF_2 
[GitHub/Docs: "Using a personal access token on the command line"](https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#using-a-personal-access-token-on-the-command-line)
```bash
git clone https://HOSTNAME/USERNAME/REPO.git
>> Username: YOUR_USERNAME
>> Password: YOUR_PERSONAL_ACCESS_TOKEN
```
照做之後，果然可以成功push了。但是，還有個小問題：每次進行操作，都要輸入一次`Username`跟`Password`，超級麻煩。

### REF_3 
[GitHub/Docs: "Caching your GitHub credentials in Git"](https://docs.github.com/en/enterprise-server@3.9/get-started/getting-started-with-git/caching-your-github-credentials-in-git)
我用了 GitHub CLI 的HTTPS協定授權，最後總算是成功設定自動授權，以後就可以自由使用remote的各種功能了。

## REF_4 
[StackOverflow](https://stackoverflow.com/questions/35942754/how-can-i-save-username-and-password-in-git)
```bash
git config --global credential.helper store
```

這個方法要簡便的多，也不用額外安裝任何東西，只是記住密碼而已。