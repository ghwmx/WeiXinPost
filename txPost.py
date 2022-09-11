from requests import post

header = {'Authorization': 'token ghp_M0W4F4******************',
              "Accept": "application/vnd.github.everest-preview+json"}
r2 = post(f'https://api.github.com/repos/用户名/仓库名/actions/workflows/工作流文件名.yml/dispatches',
              data='{"ref": "main"}',
              headers=header
              )