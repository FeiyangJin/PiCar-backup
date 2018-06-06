import paramiko

with pysftp.Connection('192.168.1.157', username='pi', password='iLIKEpie314!') as sftp:
    with sftp.cd('socketTest'):             # temporarily chdir to public
        sftp.put('timer_accuracy.csv')  # upload file to public/ on remote
        #sftp.get('remote_file')         # get a remote file
