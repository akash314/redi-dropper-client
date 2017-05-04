# Adding Data 
1.) Clone the repository with:

    $ git clone git@github.com:ctsit/redi-dropper-client.git

2.) Then edit the app/config.py file to add the details about the redcap instance, for eg:
```sh
    REDCAP_API_URL = 'http://***/redcap/api/'
    REDCAP_API_TOKEN = 'C**************0'
    REDCAP_DEMOGRAPHICS_SUBJECT_ID = 'ptid'
```

3.) Then start vagrant:

    $ cd redi-dropper-client/vagrant
    $ vagrant up
    $ open the browser at https://localhost:7088/ (accept the "Your connection is not private" message)


Refer this [readme] for addtional info.

4.) Then attach to vagrant and connect to MySQL 

```sh
    $ vagrant ssh
    $ mysql 
```
5.) Run the following SQL commands to start adding images to the RED-I dropper database:

```sh
#Use an actual redcap id for the field sbjRedcapID
INSERT INTO Subject (sbjID, sbjRedcapID, sbjAddedAt) Values (1,10001,NOW());
INSERT INTO Event(evtID, evtRedcapArm, evtRedcapEvent,evtAddedAt)  VALUES (1,1,1,NOW());
INSERT INTO SubjectFile (sbjID, evtID, sfFileName, sfFileCheckSum, sfFileSize, sfUploadedAt, usrID,sfFileType) VALUES (1, 1, 'test_file.png', md5('a'), '1234', NOW(), 1, 'MRI');
```




   [readme]: <https://github.com/ctsit/redi-dropper-client/blob/master/docs/README.md>
   
