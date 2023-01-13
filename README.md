# PS4BOT 1.0

#### HARDWARE
- [x] [JAILBROKEN PS4](https://www.youtube.com/channel/UCm9COMxXKm05BQWNv-IpyPg)
- [x] [PC/WINDOWS](https://www.microsoft.com/en-us/windows)

#### REQUIREMENTS
- [x] [PYTHON](https://www.python.org/downloads/release/python-3107/)
- [x] [PIP](https://pip.pypa.io/en/stable/installation/)
- [x] [GIT](https://git-scm.com/downloads)
- [x] [SAVE MOUNTER](https://github.com/AGraber/Playstation-4-Save-Mounter/releases/tag/1.9)

#### INSTALLATION
- [x] [RAPPTZ DISCORD.PY](https://github.com/Rapptz/discord.py)
- [x] [PYZIPPER](https://pypi.org/project/pyzipper/)

#### RESOURCES
- [x] [DISCORD BOT TUTORIAL](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
  
- [x] [JAILBREAK TUTORIAL](https://www.youtube.com/watch?v=yVFbo23BCK4)
- [x] [SAVE MOUNTER TUTORIAL](https://www.youtube.com/watch?v=qG8f7MONemw)
- [x] [VISUAL STUDIO CODE](https://code.visualstudio.com/download)
- [x] [KARO HOST EXPLOIT](http://karo218.ir/900CM/index.html)
- [x] [SenpaiSensei#3928 DISCORD SERVER](https://discord.gg/c5MYGyspDE)

---

## SET UP ENVIRONMENT
1. __CREATE PROJECT FOLDER:__ Enter `git clone https://github.com/xSenpaiSensei/ps4bot.git` in the desired terminal directory of the bot.

2. __CHANGE DIRECTORY:__ Change terminal directory in the ***ps4Bot*** folder `cd ps4Bot`
3. __CREATE ENV:__             `python -m venv env`
4. __ACTIVATE ENV:__           `.\env\Scripts\activate`
5. __INSTALL:__ `py -3 -m pip install --target=C:\Users\owner\documents\ps4Bot\env\Lib\site-packages -U discord.py[voice] pyzipper`
6. __CHANGE VARIABLES:__ In __main.py__ add `my_token` and `client_id` variables from your [Developer Portal](https://discord.com/developers/applications)
7. __RUN PYTHON FILE:__ Enter `python main.py` into the terminal


> NOTES: 
> - REPLACE: `C:\Users\owner\documents\ps4Bot\env\Lib\site-packages` with the directory to your env site packages folder.
> - Use `py -3 -m pip install --target=C:\Users\owner\documents\ps4Bot\env\Lib\site-packages package_name` to install future packages directly into your virtual environment
---

## FEATURES

### __COMMAND:__ `/default`
  - This command allows you set the resigners main default configurations.
    * 1. **RESIGN ID:** Users unique playstation network ID.
    * 2. **FOLDER ID:** The playstation account user folder ID.
    * 3. **ZIP FOLDER:** Name of the zip folder for the downloaded files.
    * 4. **ZIP PASSWORD:** The password chosen to lock the zip folder.
    * 5. **IP ADDRESS:** The IP Address of the playstation.

  - **action subcommand: [SECOND, THIRD, FOURTH]**
    - Selecting this subcommand allows you to configure the Second, Third, and Fourth default configurations.

    > **NOTES:** 
    > - Must use if there is no current default configuration set
    > - Second, third, and fourth configurations will be created when you use the action subcommand.
    > - If no value is entered, the current configuration value will be re-used.
    >   - This allows you to change some values without being forced to re-enter the ones you want to stay the same.
    > - The ENV python interpretor may have to be configured if the imports are not being read. Search how to configure for your individual code editor.

---

### __COMMAND:__ `/resign`

  - This command allows your to resign a mounted save. A list will be displayed that shows the playstation accounts user folder ID numbers so you may copy the one where the save is mounted to enter into the form. 
  - There are preset options that you may enter to get different results.
  - If no value is entered in any slot, the value from the selected configuration will be used.

    * 1. **RESIGN ID:**
          - (Example: `7ab47cdd5d7287123`)

          - Enter the value `1`: 
            - This will use the values that were entered in the last resign.
            - If the zip folder name is reused it will add a random capital letter to the end of the name.
            - (Last Used: `Game-Save-3918`)(Result: `Game-Save-3918H`)

          - Enter the value `2`, `3`, `4`:
            - This will use the Second, Third, or Fourth configuration values.
            - The configuration must be set first using `/default` and the action subcommands.

    * 2. **FOLDER ID:**
          - (Example: `1176bbc6`)

          - Enter the user folder ID that was copied from the user list that was previously displayed.
          - This is used to download the encrypted game file after the save is unmounted.
          - If only one playstation account is used for resigning this will be left blank to use the default configuration, in this case `/quickresign` can be always used to skip the user folder id list.

     * 3. **ZIP FOLDER:**
          - (Example: `Game-Save`)

          - Enter the zip folder name that will be used when downloading the decrypted and encrypted file.
          - The name will always have an additional random 4 digits at the end of the name you choose. This help prevents folders with the same name getting over written while creating a unique identifier. ! There is a very small chance the same number will repeat and overwrite if the same names are repeatedly used ! (Result: `Game-Save-3918`)
          - When the files are downloaded, an additional letter is added at the beginning of the numbers, a "D" for decrypted files and an "E" for encrypted files. This is to prevent the zip folders from over writing each other if moved or downloaded into the same folder. This prefix will not be added to the last used configuration. (Result: `Game-Save-D3918` and `Game-Save-E3918`)

    * 4. **ZIP PASSWORD:**
          - (Example: `Mypassword1`)

          - Do NOT enter a value to skip the zip folder password option.
          - Enter the value `1`: 
            - This is to use the default password that is set in the selected configuration.
          - Enter the value `2`: 
            - This will generate a random password with letters and numbers that is 8 places long. (Example: `a7847usx`)
          - A copy of the password will be sent to the resigner through direct message.

     * 5. **IP ADDRESS:**
         - (Example: `192.168.1.123`)

          -  Set the playstation IP address.
          -  Will probably be removed in the next version since the IP address will likely be used from the default configurations every time.

    > **NOTES:**
    > - Save must be mounted to download the decrypted file and unmounted to download the encrypted file.
    > - Some values may be entered while others are left blank to use a combination of custom values, default values, and preset options.
    > - The list of user folder id's is useful for consistently using saves from different playstation user accounts. It is also helpful to keep different copies of the same game on different accounts without having to reupload them since only one copy of the same game can exist on an account at a time.

### __COMMAND:__ `/quickresign`

   - This allows you to skip the user folder id list and go straight to the resign form.
   - It is mainly used if the default configuration values are going to be used or the folder id is already known.
   - If only one account is used to resign this command will be used more than `/resign`

### __COMMAND:__ `/usernames`
  - This will give a list of the playstation accounts user folder id's.
  - The same list that is displayed when `/resign` is used.
  - There is a current issue where the user name of the playstation account may repeat itself. Hopefully this will be solved in 2.0
    - `username[:len(username) // 2]` Solves the issue but all accounts have to be doubled. In my case scenario, non of them were doubled until I deleted the accounts and remade new ones. So some of them were not doubled, if I were to add this code to those listings, it would cut in half the usernames that are not doubled. 

### __RESULTS:__
1. **RESIGN RESULT:**
 - Both options may be selected if the save is properly mounted and then unmounted.
 - If the save is NOT properly unmounted before selecting the *DOWNLOAD UNMOUNTED FILES* selection, the file will be corrupted.
 - If this happens by mistake, RESELECT *DOWNLOAD MOUNTED FILES* then unmount the save properly and select *DOWNLOAD UNMOUNTED FILES* again.
 - If an option is selected multiple times it will overwrite the previous file in that folder

2. **DECRYPTED & ENCRYPTED DOWNLOAD RESULT:**
- The files will be listed.
- The download location of the file will be listed.
 - There are two optional buttons:
   - *SEND FILE* sends a custom message followed by the downloaded zip file.
   - *SEND PASSWORD* will send a custom message that includes the download file name and password.
   - The download & password button disables after the first click.
   - If no password was entered the password button will disable with a *NO PASSWORD* label.

# ERRORS
Check the terminal for any errors occur during the process for full details. Not all errors have been set up to be shown in discord messages such as *TOO MANY CONNECTIONS.*

- **SAVE IS NOT MOUNTED:** Attempting to resign or download a resigned decrypted file without the save mounted will result in this error.

- **MAKE SURE DIRECTORY IS CORRECT:** If the wrong user folder ID is entered during the resign form, attempting to download the encrypted file will result in this error.
- **TOO MANY CONNECTIONS:** Attempting to resign or download a file while also having multiple connections to the playstation with a different FTP will result in this error, for example being connected to the ps4 on FileZilla in more than one tab.
- **FILE NOT FOUND:** Attempting to send a downloaded file that was removed from the original folder or any other directory issues.
- **MOUNTED SAVE FILE DIRECTORY NOT FOUND EVEN THOUGH SAVE IS MOUNTED:** The original mounted location is `/mnt/sandbox/NPXS20001_000/savedata0/`. The code is set up to re-iterate through combinations of `000, 001, 002` and `savedata0, savedata1, savedata2`. I don't know what would cause the numbers to go higher but it might occur even though I have never experienced this issue.
- **OTHER ERRORS:** Unknown errors may occur. All newly discovered errors or errors only shown in the terminal will be updated in the next version.

---

## NEXT VERSION IDEAS
- SAVE MOUNTER BOT
- DOWNLOAD MOUNTED SAVE WITHOUT RESIGNING PROCESS
- DOWNLOAD ENCRYPTED GAME SAVES WITHOUT RESIGNING WITHOUT RESIGNING PROCESS
- MORE FTP FEATURES
- MORE SHOP COMMANDS THAT ASSIST USERS WITH SELLING SAVES
- FIX USERNAME LIST REPEATING
- ADD ERROR MESSAGES
- MORE INSTRUCTIONS
