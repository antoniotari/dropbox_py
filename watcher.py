import sys,os,dropbox,json,time
import traceback
APP_KEY = 'v5t1lconfa03p2i'
APP_SECRET = 'n6f5mali66l0i9y'
TOKEN_FILENAME = 'token.txt'
client = None
action = 'run'
def run():
	if action == 'run':
		if len(sys.argv) > 2:
			waitingPeriod = int(sys.argv[2])
		haveTokenFile = os.path.isfile(TOKEN_FILENAME)
		if haveTokenFile is True:
			tFile = open(TOKEN_FILENAME,'r')
			createClient(tFile.read())
		else:
			get_token()

def get_token():
	global client
	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(APP_KEY,APP_SECRET)
	authorize_url = flow.start()
	print "Open the following in your browser..."
	print authorize_url
	token = raw_input("... and then enter your authorization code here: ").strip()
	access_token, user_id = flow.finish(token)
	print access_token
	
	#store the token
	storeToken = open(TOKEN_FILENAME,'w')
	storeToken.write(access_token)
	storeToken.close()
	
	#client = dropbox.client.DropboxClient(access_token)
	createClient(access_token)
	print client.account_info()

def createClient(token):
	global client
	try:
		client = dropbox.client.DropboxClient(token)
		load_list_of_watched_files_and_folders();
	except Exception,e:
		print "error accessing dropbox "
		print(traceback.format_exc())
		get_token()
		

def load_list_of_watched_files_and_folders():
	print 'pass'	

if __name__ == '__main__':
	run()
