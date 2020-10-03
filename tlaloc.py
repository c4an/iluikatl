import  os
import  json
import  argparse

try:
    import  requests  
except ModuleNotFoundError as error:
        exception_type, exception_value, tb = sys.exc_info()
        print('Traceback (most recent call last):\n{}{}: {}\n'.format(''.join(traceback.format_tb(tb)), str(exception_type), str(exception_value)))
        print('Tlaloc was not able to make it rain because a required Python package was not found.\nRun `sh install.sh` to check and install Tlaloc\'s Python requirements.')
        sys.exit(1)

def github_list(user):
    r = requests.get(f"https://api.github.com/users/{user}/repos")
    data = json.loads(r.text)
    #print(data)
    for repos in data:
        repo=(repos['html_url'])
        stream = os.system(f'docker run --rm --name gitleaks zricethezav/gitleaks -v -r {repo}')
        #output = stream.read()
        #print(output)

def github_token_test(username,token,repo):
	repos_url = repo

	# create a re-usable session object with the user creds in-built
	gh_session = requests.Session()
	gh_session.auth = (username, token)

	# get the list of repos belonging to me
	repos = json.loads(gh_session.get(repos_url).text)

	# print the repo names
	for repo in repos:
	    print(repo['name'])

def github_get_users(repo)
	r = requests.get(f"https://api.github.com/users/{user}/repos")
	data = json.loads(r.text)
	#print(data)
    for repos in data:
        repo=(repos['html_url'])
        stream = os.system(f'docker run --rm --name gitleaks zricethezav/gitleaks -v -r {repo}')
        #output = stream.read()
        #print(output)

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', required=True, default=None, help='<Github user>', metavar='')
    #parser.add_argument('--module-name', required=False, default=None, help='<module name>', metavar='')
    #parser.add_argument('--data', required=False, default=None, help='<service name/all>', metavar='')
    #parser.add_argument('--module-args', default=None, help='<--module-args=\'--regions us-east-1,us-east-1\'>', metavar='')
    #parser.add_argument('--list-modules', action='store_true', help='List arguments')
    #parser.add_argument('--help', action='store_true', help='List tlaloc help window')
    #parser.add_argument('--module-info', action='store_true', help='List the tlaloc help window')
    args = parser.parse_args()

    if any([args.user]):
        github_list(args.user)
    else:
        print('When running Tlaloc a Github username is necessary')
        exit()
            
if __name__ == '__main__':
    run()
