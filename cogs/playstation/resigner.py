import discord
import os, errno
import base64, winsound
import random, string
import shutil, pathlib
from ftplib import FTP
import zipfile, pyzipper
from typing import Literal
from discord import app_commands
from discord.ext import commands

# CONFIGURATIONS
my_port = '2121'
default_config = 'files/config/default_config.txt'
last_config = 'files/config/last_config.txt'
second_config = 'files/config/second_config.txt'
third_config = 'files/config/third_config.txt'
fourth_config = 'files/config/fourth_config.txt'

# FUNCTIONS

## DELETE FILE
def silentremove(filetobedeleted):
    try:
        os.remove(filetobedeleted)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise

## DELETE FOLDER
def silentfolder(thesussydir):
    if os.path.exists(thesussydir) and os.path.isdir(thesussydir):
        shutil.rmtree(thesussydir)

## HEX CONVERTER
def little_to_bigEDIAN(hexstring):
    ba = bytearray.fromhex(hexstring)
    ba.reverse()
    sba = ''.join(format(x, '02x') for x in ba)
    return sba.upper()

## CREATE FOLDER SETUP
try:
    if os.path.isdir('DOWNLOADS') == False: 
        os.mkdir('DOWNLOADS')

    if os.path.isdir('DOWNLOADS/RESIGNED') == False: 
        os.mkdir('DOWNLOADS/RESIGNED/')

    if os.path.isdir('DOWNLOADS/RESIGNED/ENCRYPTED') == False: 
        os.mkdir('DOWNLOADS/RESIGNED/ENCRYPTED')
        encrypted = 'DOWNLOADS/RESIGNED/ENCRYPTED/'

    if os.path.isdir('DOWNLOADS/RESIGNED/DECRYPTED') == False: 
        os.mkdir('DOWNLOADS/RESIGNED/DECRYPTED')
        decrypted = 'DOWNLOADS/RESIGNED/DECRYPTED/'
    
    if os.path.isdir('files') == False: 
        os.mkdir('files')
        
    if os.path.isdir('files/config') == False: 
        os.mkdir('files/config')
    
    if os.path.exists(default_config) == False:
        with open(default_config, 'w') as f:
            f.write(f"""# DEFAULT CONFIGURATION
[Resign ID]
ResignID =
[Folder ID]
FolderID =
[Zip Folder]
ZipFolder =
[Zip Password]
ZipPassword =
[IP Address]
IP =
[Port]
Port = {my_port}""")
        
except: pass

# DEFAULT FORM
class default(discord.ui.Modal, title='NEW DEFAULT VALUES'):
    
            # DEFAULT QUESTIONS
            resignid_set = discord.ui.TextInput(label='Resign ID', placeholder='1234567890123456', required=False)
            folderid_set = discord.ui.TextInput(label='User Folder ID', placeholder='1176bbc6', required=False)
            zip_folder_set = discord.ui.TextInput(label='Zip Folder Name', placeholder='My_GameSave', required=False)
            zip_password_set = discord.ui.TextInput(label='Zip Password', placeholder='MyPassword123', required=False)
            ip_set = discord.ui.TextInput(label='IP Address', placeholder='192.123.1.123', required=False)
            
            # DEFAULT SUBMISSION
            async def on_submit(self, interaction: discord.Interaction):
                
                # READ DEFAULT
                with open(default_config, 'r') as f:
                    ftpinfoBIG = f.read().splitlines()
                    default_resignid = ftpinfoBIG[2].replace(' ', '').replace('ResignID=', '')
                    default_folderid = ftpinfoBIG[4].replace(' ', '').replace('FolderID=', '')
                    default_zip_folder = ftpinfoBIG[6].replace(' ', '').replace('ZipFolder=', '')
                    default_zip_password = ftpinfoBIG[8].replace(' ', '').replace('ZipPassword=', '')
                    default_ip = ftpinfoBIG[10].replace(' ', '').replace('IP=', '')
                    default_port = ftpinfoBIG[12].replace(' ', '').replace('Port=', '')
                    
                # REUSE DEFAULT VALUES IF NO VALUES ENTERED
                global resignid_set, folderid_set, zip_folder_set, zip_password_set, ip_set, port_set
                
                if str(self.resignid_set) != '': resignid_set = str(self.resignid_set)
                else: resignid_set = (default_resignid) 
                
                if str(self.folderid_set) != '': folderid_set = str(self.folderid_set)
                else: folderid_set = (default_folderid)
                
                if str(self.zip_folder_set) != '': zip_folder_set = str(self.zip_folder_set)
                else: zip_folder_set = (default_zip_folder)
                
                if str(self.zip_password_set) != '': zip_password_set = str(self.zip_password_set)
                else: zip_password_set = (default_zip_password)
                
                if str(self.ip_set) != '': ip_set = str(self.ip_set)
                else: ip_set = (default_ip)
                
                port_set = default_port
                
                # DEFAULT RESULTS
                embed = discord.Embed(title = f'📝 __**{config_type} DEFAULT VALUES**__', color = (discord.Color.greyple()))
                embed.set_author(name= f'Confirm Values are Correct ❗', icon_url=interaction.user.avatar)
                embed.add_field(name="__**Resign ID**__", value= resignid_set, inline=False)
                embed.add_field(name="__**User Folder ID**__", value= folderid_set, inline=False)
                embed.add_field(name="__**Zip Folder Name**__", value= zip_folder_set, inline=False)
                embed.add_field(name="__**Zip Password**__", value= zip_password_set, inline=False)
                embed.add_field(name="__**IP Address**__", value= ip_set, inline=False)
                embed.add_field(name="__**Port**__", value= port_set, inline=False)
                embed.set_footer(text="Default values will be reused if no value is entered")
                await interaction.response.send_message(embed=embed, view=set_default(), ephemeral=True)

# DEFAULT BUTTON
class set_default(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
        
    @discord.ui.button(label = "SET DEFAULT", style = discord.ButtonStyle.gray, emoji = "✏️" , custom_id = "default_button")
    async def setdefault(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        # CONFIGURATION SWITCH
        if activate_second == True:
            default_config_switch = second_config
        elif activate_third == True:
            default_config_switch = third_config
        elif activate_second == True:
            default_config_switch = fourth_config
        else: 
            default_config_switch = default_config
            
        # SET DEFAULT VALUES
        with open(default_config_switch, 'w') as f:
            f.write(f"""# {config_type} CONFIGURATION
[Resign ID]
ResignID = {resignid_set}
[Folder ID]
FolderID = {folderid_set}
[Zip Folder]
ZipFolder = {zip_folder_set}
[Zip Password]
ZipPassword = {zip_password_set}
[IP Address]
IP = {ip_set}
[Port]
Port = {port_set}""")

        # VALUES SET MESSAGE
        embed = discord.Embed(title = '✅  __**DEFAULT VALUES SET**__', color=discord.Color.green())
        await interaction.response.send_message(embed=embed, ephemeral=True)

# RESIGN FORM BUTTON
class resign_form_button(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
        
    @discord.ui.button(label = "START RESIGNING", style = discord.ButtonStyle.blurple, custom_id = "resign_form_button")
    async def resign(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(resign_form())

# RESIGN FORM
class resign_form(discord.ui.Modal, title='SAVEDATA RESIGNER'):
                    
            # RESIGN QUESTIONS
            resignid = discord.ui.TextInput(label='Resign ID', placeholder='1234567890123456', required=False)
            folderid = discord.ui.TextInput(label='Folder ID', placeholder='1176bbc6', required=False)
            zip_folder = discord.ui.TextInput(label='Zip Name', placeholder='Save-1234', required=False)
            zip_password = discord.ui.TextInput(label='Zip Password', placeholder='MyPassword123', required=False)
            ip = discord.ui.TextInput(label='IP Address', placeholder='192.123.1.456', required=False)
            
            # RESIGN SUBMISSION
            async def on_submit(self, interaction: discord.Interaction):
                
                # ENTER 1 IN RESIGN ID TO USE LAST CONFIG
                entered_resignid = str(self.resignid)
                if entered_resignid == '1':
                    config_switch = last_config
                    use_last_config = True
                
                # SWITCH BETWEEN CONFIGS
                elif entered_resignid == '2':
                    config_switch = second_config
                    use_last_config = False
                    
                elif entered_resignid == '3':
                    config_switch = third_config
                    use_last_config = False
                    
                elif entered_resignid == '4':
                    config_switch = fourth_config
                    use_last_config = False
                else: 
                    config_switch = default_config
                    use_last_config = False
                
                # READ DEFAULT VALUES
                with open(config_switch, 'r') as f:
                    ftpinfoBIG = f.read().splitlines()
                    config_resignid = ftpinfoBIG[2].replace(' ', '').replace('ResignID=', '')
                    config_folderid = ftpinfoBIG[4].replace(' ', '').replace('FolderID=', '')
                    config_zip_folder = ftpinfoBIG[6].replace(' ', '').replace('ZipFolder=', '')
                    config_zip_password = ftpinfoBIG[8].replace(' ', '').replace('ZipPassword=', '')
                    config_ip = ftpinfoBIG[10].replace(' ', '').replace('IP=', '')
                    config_port = int(ftpinfoBIG[12].replace(' ', '').replace('Port=', ''))
                    
                # USE DEFAULT IF NO VALUES ENTERED    
                global resignid, folderid, zip_folder, zip_password, ip, port
                global zip_password_str, set_password, random_num, used_folder_name
            
                if entered_resignid != '':
                    if use_last_config == True: resignid = config_resignid 
                    
                    else: resignid = entered_resignid

                else: resignid = (config_resignid)
                    
        
                if str(self.folderid) != '': folderid = str(self.folderid)
                else: folderid = (config_folderid)
                
                random_num = (random.randint(1000,9999))
                random_num = str(random_num)
                random_letter = (random.choice(string.ascii_uppercase))
                
                entered_zip_folder = str(self.zip_folder)
                if entered_zip_folder != '': 
                
                    zip_folder = (entered_zip_folder + "-" + random_num )
                    used_folder_name = entered_zip_folder
                    
                else: 
                    if use_last_config == True:
                        
                        zip_folder = (config_zip_folder + f"{random_letter}")
                        used_folder_name = config_zip_folder

                    else:
                        zip_folder = (config_zip_folder + "-" + random_num)
                        used_folder_name = config_zip_folder
                
                entered_zip_password = str(self.zip_password)
                if entered_zip_password != '': 
                    
                    # ENTER 1 FOR DEFAULT PASSWORD
                    if entered_zip_password == '1': 
                        zip_password_str = config_zip_password + random_num
                    
                    # ENTER 2 FOR RANDOM PASSWORD
                    elif entered_zip_password == '2': 
                        source = string.ascii_lowercase + string.digits
                        zip_password_str = ''.join((random.choice(source) for i in range(8)))
                        
                    else: zip_password_str = entered_zip_password
                    
                    # CONVERT PASSWORD TO BINARY
                    zip_password = bytes(zip_password_str, encoding='utf-8')
                    set_password = True
                    
                else: 
                    
                    if use_last_config == True: zip_password_str = config_zip_password
                    
                    else:
                        
                        # ENTER NO VALUE FOP NO PASSWORD
                        zip_password_str = ""
                        set_password = False
                
                if str(self.ip) != '': ip = str(self.ip)
                else: ip = (config_ip)
                    
                port = config_port
                
                # SET LAST CONFIG VALUES
                with open(last_config, 'w') as f:
                    f.write(f"""# LAST CONFIGURATION
[Resign ID]
ResignID = {resignid}
[Folder ID]
FolderID = {folderid}
[Zip Folder]
ZipFolder = {zip_folder}
[Zip Password]
ZipPassword = {zip_password_str}
[IP Address]
IP = {ip}
[Port]
Port = {port}""")
                
                # BASE64 CONVERSION
                resignidcheck = resignid[11:]
                if resignidcheck == '=':
                    resignid = base64.b64decode(resignid).hex()

                # CONNECT TO SERVER
                ftp = FTP()
                ftp.connect(ip, port)
                ftp.login()
                
                # CONNECT TO MOUNTED FOLDER
                try:
                    try:
                        try:
                            try: 
                                try: 
                                    ftp.cwd("/mnt/sandbox/NPXS20001_000/savedata0/sce_sys")
                                    directory = ("/mnt/sandbox/NPXS20001_000/savedata0/sce_sys")
                                except: 
                                    ftp.cwd("/mnt/sandbox/NPXS20001_000/savedata1/sce_sys")
                                    directory = ("/mnt/sandbox/NPXS20001_000/savedata1/sce_sys")
                            except: 
                                ftp.cwd("/mnt/sandbox/NPXS20001_000/savedata2/sce_sys")
                                directory = ("/mnt/sandbox/NPXS20001_000/savedata2/sce_sys")
                            
                            
                        except: 
                            try: 
                                try: 
                                    ftp.cwd("/mnt/sandbox/NPXS20001_001/savedata0/sce_sys")
                                    directory = ("/mnt/sandbox/NPXS20001_001/savedata0/sce_sys")
                                except: 
                                    ftp.cwd("/mnt/sandbox/NPXS20001_001/savedata1/sce_sys")
                                    directory = ("/mnt/sandbox/NPXS20001_001/savedata1/sce_sys")
                            except: 
                                ftp.cwd("/mnt/sandbox/NPXS20001_001/savedata2/sce_sys")
                                directory = ("/mnt/sandbox/NPXS20001_001/savedata2/sce_sys")
                            
                            
                    except: 
                        try: 
                            try: 
                                ftp.cwd("/mnt/sandbox/NPXS20001_002/savedata0/sce_sys")
                                directory = ("/mnt/sandbox/NPXS20001_002/savedata0/sce_sys")
                            except: 
                                ftp.cwd("/mnt/sandbox/NPXS20001_002/savedata1/sce_sys")
                                directory = ("/mnt/sandbox/NPXS20001_002/savedata1/sce_sys")
                        except: 
                            ftp.cwd("/mnt/sandbox/NPXS20001_002/savedata2/sce_sys")
                            directory = ("/mnt/sandbox/NPXS2000_002/savedata2/sce_sys")
                    
                except:
                    # ERROR MESSAGE
                    embed = discord.Embed(title = '⛔ __**ERROR: MAKE SURE SAVE IS MOUNTED!**__', color=discord.Color.red())
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    

                # PARAM.SFO
                ftp.retrbinary("RETR " + 'param.sfo' ,open('param.sfo', 'wb').write)

                with open('param.sfo', 'r+b') as ps4sfo:
                    ps4sfo.seek(348)
                    ps4sfo.write(bytearray.fromhex(little_to_bigEDIAN(resignid)))

                with open("param.sfo", "rb") as infile:
                    infile.seek(0x9f8, 0)
                    global save_name
                    save_name = infile.read(0x24).replace(bytearray.fromhex('00'),bytearray.fromhex('20') ).decode("utf-8").strip() # replaces 0x00 with 0x20 (which is a space) so that the strip will remove the last spaces
                
                with open("param.sfo", "rb") as why:
                    why.seek(0xa9c, 0)
                    global gameid
                    gameid = why.read(0x9).decode("utf-8")

                file = open('param.sfo','rb')

                # CONNECT TO SERVER
                ftp = FTP()
                ftp.connect(ip, port)
                ftp.login()
                ftp.cwd(directory)

                # FINALIZING
                ftp.storbinary('STOR param.sfo', file)
                file.close()
                silentremove('param.sfo')
                
                if set_password == True:
                    
                    # SEND PASSWORD TO USER DM
                    embed = discord.Embed(title=f"🔔 __**PASSWORD TO LOCKED ZIP FILE**__", color=discord.Color.fuchsia())
                    embed.set_author(name=f'Thank you {interaction.user.name} for resigning 😁', icon_url= interaction.user.avatar)
                    embed.add_field(name=f"📁 __**ZIP FOLDER NAME:**__", value=f'***{zip_folder}***', inline=False)
                    embed.add_field(name=f"🔒 __**ZIP FOLDER PASSWORD:**__", value=f'***{zip_password_str}***', inline=False)
                    embed.set_footer(text=f"{gameid} saved as {resignid}")
                    await interaction.user.send(embed=embed)
                
                # SUCCESSFUL RESIGN MESSAGE
                embed = discord.Embed(title = '✅ __**SAVE RESIGNED SUCCESSFULLY!**__', color=discord.Color.brand_green())
                embed.set_author(name= f'Thank you {interaction.user.name} for Resigning 😄', icon_url=interaction.user.avatar)
                embed.add_field(name=f"**1)** **DOWNLOAD MOUNTED SAVE**", value='You must select this option __**BEFORE**__ unmounting.', inline=False)
                embed.add_field(name=f"**2)** **DOWNLOAD UNMOUNTED SAVE**", value='You must select this option __**AFTER**__ unmounting.', inline=False)
                embed.add_field(name=f"💌 __**RESIGNED:**__", value= f'***{gameid}*** resigned as***{resignid}***', inline=False)
                embed.set_footer(text="Both options may be selected if the save is un/mounted properly.")
                await interaction.response.send_message(embed=embed, view=download_resign(),ephemeral=True)
                
                # BEEP NOISE
                duration = 500
                freq = 1000
                winsound.Beep(freq, duration)


# DOWNLOAD RESIGNED SELECT MENU
class download_resign(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
    
    # OPTIONS
    @discord.ui.select(placeholder = "SELECT DOWNLOAD OPTIONS",
        options = [
            discord.SelectOption(
                label="🟣 DOWNLOAD MOUNTED FILES",
                description="BEFORE UNMOUNT!",
                emoji='📥'
            ),
            discord.SelectOption(
                label="🟠 DOWNLOAD UNMOUNTED FILES",
                description="AFTER UNMOUNT!",
                emoji='📥'
            )
        ]
    )
    
    # AFTER SELECTION
    async def select_callback(self, interaction, select):
        
        # SUBMISSION VALUES
        selected = select.values[0]
        
        # READ DEFAULT VALUES
        with open(default_config, 'r') as f:
            ftpinfoBIG = f.read().splitlines()
            default_ip = ftpinfoBIG[10].replace(' ', '').replace('IP=', '')
            default_port = int(ftpinfoBIG[12].replace(' ', '').replace('Port=', ''))
        
        # FIRST SELECTION
        if selected == '🟣 DOWNLOAD MOUNTED FILES':
            
            #CONNECT TO PS4
            ftp = FTP()
            ftp.connect(default_ip, default_port)
            ftp.login()
            
            # CONNECT TO MOUNTED FOLDER
            global directory
            try:
                try:
                    try:
                        try: 
                            try: 
                                ftp.cwd("/mnt/sandbox/NPXS20001_000/savedata0/")
                                directory = ("/mnt/sandbox/NPXS20001_000/savedata0/")
                            except: 
                                ftp.cwd("/mnt/sandbox/NPXS20001_000/savedata1/")
                                directory = ("/mnt/sandbox/NPXS20001_000/savedata1/")
                        except: 
                            ftp.cwd("/mnt/sandbox/NPXS20001_000/savedata2/")
                            directory = ("/mnt/sandbox/NPXS20001_000/savedata2/")
                    except: 
                        try: 
                            try: 
                                ftp.cwd("/mnt/sandbox/NPXS20001_001/savedata0/")
                                directory = ("/mnt/sandbox/NPXS20001_001/savedata0/")
                            except: 
                                ftp.cwd("/mnt/sandbox/NPXS20001_001/savedata1/")
                                directory = ("/mnt/sandbox/NPXS20001_001/savedata1/")
                        except: 
                            ftp.cwd("/mnt/sandbox/NPXS20001_001/savedata2/")
                            directory = ("/mnt/sandbox/NPXS20001_001/savedata2/")
                except: 
                    try: 
                        try: 
                            ftp.cwd("/mnt/sandbox/NPXS20001_002/savedata0/")
                            directory = ("/mnt/sandbox/NPXS20001_002/savedata0/")
                        except: 
                            ftp.cwd("/mnt/sandbox/NPXS20001_002/savedata1/")
                            directory = ("/mnt/sandbox/NPXS20001_002/savedata1/")
                    except: 
                        ftp.cwd("/mnt/sandbox/NPXS20001_002/savedata2/")
                        directory = ("/mnt/sandbox/NPXS20001_002/savedata2/")
                
                # START DOWNLOAD MESSAGE
                embed = discord.Embed(title=f"✅ __**DECRYPTED FILES DOWNLOADED**__", color=discord.Color.fuchsia())
                embed.set_author(name= f'Thank you {interaction.user.name} for downloading 😄', icon_url= interaction.user.avatar)
                x = 1
                
                # INITIALIZE LIST
                data = []
                ftp.dir(data.append)
                
                for line in data:
                    
                    # SKIP FIRST TWO BLANK LISTINGS
                    if x > 2:
                        filenames = line.split(" ")[-1]
                        
                        if filenames != "sce_sys":
                            y = x - 3
                        
                            # DOWNLOAD & LIST EACH FILE
                            global decrypted_folder_name, saved_as_decrypted
                            embed.add_field(name = str(y) + ") " + filenames, value = '\u200b', inline=False)
                            ftp.retrbinary("RETR " + filenames ,open(filenames, 'wb').write)
                            decrypted_folder_name = used_folder_name + "-D" + random_num
                            saved_as = ('DOWNLOADS/RESIGNED/DECRYPTED/' + decrypted_folder_name + ".zip")
                            saved_as_decrypted = saved_as
                            
                            # ZIP FILE WITHOUT PASSWORD
                            if set_password == False:

                                silentfolder('TEMPORARY')
                                os.mkdir('TEMPORARY')
                                os.mkdir('TEMPORARY\\DECRYPTED')
                                os.mkdir('TEMPORARY\\DECRYPTED\\' + resignid)
                                os.mkdir('TEMPORARY\\DECRYPTED\\' + resignid + '\\' + gameid)
                                folder_structure = ('TEMPORARY\\DECRYPTED\\' + resignid + '\\' + gameid)
                                os.rename(filenames, folder_structure + '\\' + filenames )
                                
                                directory = pathlib.Path("TEMPORARY")
                                with zipfile.ZipFile(saved_as, mode="w") as archive:
                                    for file_path in directory.rglob("*"):
                                        archive.write(file_path, arcname=file_path.relative_to(directory))
                                silentfolder('TEMPORARY')
                                
                            else: 
                                
                                # ZIP FILE WITH PASSWORD
                                silentfolder('DECRYPTED')
                                os.mkdir('DECRYPTED')
                                os.mkdir('DECRYPTED\\' + resignid)
                                os.mkdir('DECRYPTED\\' + resignid + '\\' + gameid)
                                folder_structure = ('DECRYPTED\\' + resignid + '\\' + gameid)
                                os.rename(filenames, folder_structure + '\\' + filenames )
                                
                                with pyzipper.AESZipFile(saved_as,'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
                                    zf.setpassword(zip_password)
                                    zf.write(folder_structure + '\\' + filenames)
                                silentfolder('DECRYPTED')
                            
                                    
                    x += 1
                    
                # END DOWNLOAD MESSAGE
                if set_password == True: embed.add_field(name=f"🔒 __**PASSWORD:**__", value= f'***{zip_password_str}***', inline=False)
                embed.add_field(name=f"📥 __**SAVED AS:**__", value=f'*DOWNLOADS/RESIGNED/DECRYPTED/*' + f'__**{decrypted_folder_name}**__' + ".zip", inline=False)
                embed.set_footer(text='You may now unmount and select "DOWNLOAD UNMOUNTED FILES"')
                await interaction.response.send_message(embed=embed, view=send_decrypted_button() , ephemeral=True)

            except:
                # ERROR MESSAGE
                embed = discord.Embed(title = '⛔ __**ERROR: MAKE SURE SAVE IS MOUNTED!**__', color=discord.Color.red())
                await interaction.response.send_message(embed=embed, ephemeral=True)
            ftp.quit()

        
        # SECOND SELECTION
        if selected == '🟠 DOWNLOAD UNMOUNTED FILES':
            
            #CONNECT TO PS4
            ftp = FTP()
            ftp.connect(default_ip, default_port)
            ftp.login() 
            try: 
                ftp.cwd('/user/home/' + folderid + '/savedata/' + gameid)
                
                # DOWNLOAD RESIGNED FILES
                global encrypted_folder_name, saved_as_encrypted
                ftp.retrbinary("RETR " + 'sdimg_' + save_name ,open(save_name, 'wb').write)
                ftp.retrbinary("RETR " + save_name + '.bin' ,open(save_name + '.bin' , 'wb').write)
                encrypted_folder_name = used_folder_name + "-E" + random_num
                saved_as = ('DOWNLOADS/RESIGNED/ENCRYPTED/' + encrypted_folder_name + ".zip")
                saved_as_encrypted = saved_as
                
                # ZIP FILE WITHOUT PASSWORD
                if set_password == False:
                    
                    silentfolder('TEMPORARY')
                    os.mkdir('TEMPORARY')
                    os.mkdir('TEMPORARY\\PS4')
                    os.mkdir('TEMPORARY\\PS4\\SAVEDATA')
                    os.mkdir('TEMPORARY\\PS4\\SAVEDATA\\' + resignid)
                    USBstructure = 'TEMPORARY\\PS4\\SAVEDATA\\' + resignid
                    USBstructure = USBstructure + '\\' + gameid
                    os.mkdir(USBstructure)
                    os.rename(save_name, USBstructure + '\\' + save_name )
                    os.rename(save_name + '.bin', USBstructure + '\\' + save_name + '.bin' )
                    
                    directory = pathlib.Path("TEMPORARY")
                    with zipfile.ZipFile(saved_as, mode="w") as archive:
                        for file_path in directory.rglob("*"):
                            archive.write(file_path, arcname=file_path.relative_to(directory))
                    silentfolder('TEMPORARY')
                
                else:
        
                    # ZIP FILE WITH PASSWORD
                    silentfolder('PS4')
                    os.mkdir('PS4')
                    os.mkdir('PS4\\SAVEDATA')
                    os.mkdir('PS4\\SAVEDATA\\' + resignid)
                    USBstructure = 'PS4\\SAVEDATA\\' + resignid
                    USBstructure = USBstructure + '\\' + gameid
                    os.mkdir(USBstructure)
                    os.rename(save_name, USBstructure + '\\' + save_name )
                    os.rename(save_name + '.bin', USBstructure + '\\' + save_name + '.bin' )
                    
                    with pyzipper.AESZipFile(saved_as,'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
                        zf.setpassword(zip_password)
                        zf.write(USBstructure + '\\' + save_name)
                        zf.write(USBstructure + '\\' + save_name + ".bin")
                        silentfolder('PS4')
                
                # DOWNLOAD SUCCESSFUL MESSAGE
                embed = discord.Embed(title=f"✅ __**ENCRYPTED FILES DOWNLOADED**__", color=discord.Color.orange())
                embed.set_author(name=f'Thank you {interaction.user.name} for downloading 😝', icon_url= interaction.user.avatar)
                embed.add_field(name=f"**1)** **{save_name}**", value='\u200b', inline=False)
                embed.add_field(name=f"**2)** **{save_name}.bin**", value='\u200b', inline=False)
                if set_password == True: embed.add_field(name=f"🔒 __**PASSWORD:**__", value= f'***{zip_password_str}***', inline=False)
                embed.add_field(name=f"📥 __**SAVED AS:**__", value=f'*DOWNLOADS/RESIGNED/ENCRYPTED/*' + f'__**{encrypted_folder_name}**__' + ".zip", inline=False)
                embed.set_footer(text="If you did not unmount the save before downloading the file will be corrupted")
                await interaction.response.send_message(embed=embed,view=send_encrypted_button() , ephemeral=True)
            except: 
                embed = discord.Embed(title = f'⛔ __**ERROR: MAKE SURE DIRECTORY IS CORRECT**__', color=discord.Color.red())
                await  interaction.response.send_message(embed=embed, ephemeral=True)
            ftp.quit()

# SEND DECRYPTED FILE BUTTON
class send_decrypted_button(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
        
    @discord.ui.button(label = "SEND DECRYPTED FILE", style = discord.ButtonStyle.grey, emoji="📩", custom_id = "send_decrypted_button")
    async def send_decrypted_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        button.label = "FILE SENT ✅"
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(title = '🗂 __**DECRYPTED SAVE**__', color=discord.Color.fuchsia())
        embed.set_author(name= f'Thank you for choosing {interaction.user.name} ❤️', icon_url=interaction.user.avatar)
        embed.add_field(name="📑 __**FILE:**__", value= f'**{decrypted_folder_name}**', inline=False)
        embed.add_field(name="🎮 __**GAME:**__", value= f'***{gameid}*** has been DECRYPTED', inline=False)
        embed.add_field(name="✅ __**VERIFY:**__", value= 'Download & Verify Save the Works', inline=False)
        if set_password == True: 
            embed.add_field(name="🔐 __**LOCKED:**__", value= 'This save is password protected, request the key.', inline=False)
            embed.set_footer(text="Let me know if you have any issues, payment must be made before password is sent.")
        else: embed.set_footer(text="Let me know if you have any issues or need additional services.")
        await interaction.followup.send(embed=embed)
        await interaction.followup.send(file=discord.File(saved_as_decrypted))
        
    @discord.ui.button(label = "SEND PASSWORD", style = discord.ButtonStyle.grey, emoji="🔓", custom_id = "decrypted_pwd_button")
    async def decrypted_pwd_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        if set_password == True:
            button.label = "PASSWORD SENT ✅"
            await interaction.response.edit_message(view=self)
            embed = discord.Embed(title = '🔓 __**PASSWORD TO DECRYPTED FILE**__', color=discord.Color.fuchsia())
            embed.set_author(name= f'Thank you for choosing {interaction.user.name} ❤️', icon_url=interaction.user.avatar)
            embed.add_field(name="📑 __**FILE:**__", value= f'**{decrypted_folder_name}**', inline=False)
            embed.add_field(name="🔑  __**PASSWORD:**__", value= f'**{zip_password_str}**', inline=False)
            embed.set_footer(text="Please save the password to your file just in case.")
            await interaction.followup.send(embed=embed)
        else: 
            button.label = "NO PASSWORD ❌"
            await interaction.response.edit_message(view=self)

# SEND ENCRYPTED FILE BUTTON
class send_encrypted_button(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
        
    @discord.ui.button(label = "SEND ENCRYPTED FILE", style = discord.ButtonStyle.grey, emoji="📩", custom_id = "send_encrypted_button")
    async def send_encrypted_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        button.label = "FILE SENT ✅"
        await interaction.response.edit_message(view=self)
        embed = discord.Embed(title = '🗂 __**ENCRYPTED SAVE**__', color=discord.Color.orange())
        embed.set_author(name= f'Thank you for choosing {interaction.user.name} 🧡', icon_url=interaction.user.avatar)
        embed.add_field(name="📑 __**FILE:**__", value= f'**{encrypted_folder_name}**', inline=False)
        embed.add_field(name="🎮 __**GAME:**__", value= f'***{gameid}*** has been resigned as ***{resignid}***', inline=False)
        embed.add_field(name="✅ __**VERIFY:**__", value= 'Download & Verify Save the Works', inline=False)
        if set_password == True: 
            embed.add_field(name="🔐 __**LOCKED:**__", value= 'This save is password protected, request the key.', inline=False)
            embed.set_footer(text="Let me know if you have any issues, payment must be made before password is sent.")
        else: embed.set_footer(text="Let me know if you have any issues or need additional services.")
        await interaction.followup.send(embed=embed)
        await interaction.followup.send(file=discord.File(saved_as_encrypted))
    
    @discord.ui.button(label = "SEND PASSWORD", style = discord.ButtonStyle.grey, emoji="🔓", custom_id = "encrypted_pwd_button")
    async def encrypted_pwd_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        if set_password == True:
            button.label = "PASSWORD SENT ✅"
            await interaction.response.edit_message(view=self)
            embed = discord.Embed(title = '🔓 __**PASSWORD TO ENCRYPTED FILE**__', color=discord.Color.orange())
            embed.set_author(name= f'Thank you for choosing {interaction.user.name} 🧡', icon_url=interaction.user.avatar)
            embed.add_field(name="📑 __**FILE:**__", value= f'**{encrypted_folder_name}**', inline=False)
            embed.add_field(name="🔑  __**PASSWORD:**__", value= f'**{zip_password_str}**', inline=False)
            embed.set_footer(text="Please save the password to your file just in case.")
            await interaction.followup.send(embed=embed)
        else: 
            button.label = "NO PASSWORD ❌"
            await interaction.response.edit_message(view=self)
#---------------------------------------------------------------------------------------------#

# COMMANDS
class resigner(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    # DEFAULT CONFIG COMMAND
    @app_commands.command(name = "default", description="Set Default Values")
    
    async def default(self, interaction: discord.Interaction, action: Literal['SECOND', 'THIRD', 'FOURTH']=None) -> None:
        
        # SWITCH TO OTHER CONFIGURATIONS
        global activate_second, activate_third, activate_fourth, config_type
        activate_second = False
        activate_third = False
        activate_fourth = False
        config_type = 'MAIN'
        
        if action == 'SECOND': 
            activate_second = True
            config_type = 'SECOND'
            
        if action == 'THIRD': 
            activate_third = True
            config_type = 'THIRD'
            
        if action == 'FOURTH': 
            activate_fourth = True
            config_type = 'FOURTH'

        await interaction.response.send_modal(default())
        
    # RESIGN COMMAND
    @app_commands.command(name = "resign", description="Start Resigning")
    
    async def resign(self, interaction: discord.Interaction) -> None:
        
        # READ DEFAULT VALUES
        with open(default_config, 'r') as f:
            ftpinfoBIG = f.read().splitlines()
            default_ip = ftpinfoBIG[10].replace(' ', '').replace('IP=', '')
            default_port = int(ftpinfoBIG[12].replace(' ', '').replace('Port=', ''))
        
        #CONNECT TO PS4
        ftp = FTP()
        ftp.connect(default_ip, default_port)
        ftp.login()
        ftp.cwd("/user/home/")
        data = []
        ftp.dir(data.append)
        
        # START RESIGN MESSAGE
        embed = discord.Embed(title=f"❗️❗️ __**MOUNT SAVE NOW**__ ❗️❗️", color=discord.Color.blurple())
        embed.set_author(name="▶️ Copy Folder ID to Enter Next ◀️")
        x = 1
        
        for line in data:
            # SKIP BLANK LISTINGS
            if x > 2:
                y = x - 2
                folderids = line.split(" ")[-1]
                
                #CONVERT FOLDER ID TO USERNAME
                silentremove('username.dat')
                ftp.cwd('/user/home/' + folderids)
                ftp.retrbinary("RETR " + 'username.dat' ,open('username.dat', 'wb').write)
                with open('username.dat', 'r') as moredetailsLOL:
                    text_folderids  = moredetailsLOL.read().rstrip('\x00')
                
                embed.add_field(name = str(y) + ") " + f'__{text_folderids}__' + ' = ' + f'**{folderids}**', value = '\u200b', inline=False)
                
                silentremove('username.dat')
            x += 1
            
        # END RESIGN MESSAGE
        embed.set_footer(text="Default values will be used if nothing is entered")
        await interaction.response.send_message(embed=embed, view=resign_form_button(),ephemeral=True)
        ftp.quit()
        
    # INSTANT RESIGN COMMAND
    @app_commands.command(name = "quickresign", description="Quick Resigning (Skip Folder ID Listing)")
    
    async def quickresign(self, interaction: discord.Interaction) -> None:
        
        # SEND RESIGN FORM
        await interaction.response.send_modal(resign_form())
    
    # LIST OF USERNAMES
    @app_commands.command(name = "usernames", description="A List of PS4 Users & Folder ID's")
    
    async def usernames(self, interaction: discord.Interaction) -> None:
        
        # READ DEFAULT VALUES
        with open(default_config, 'r') as f:
            ftpinfoBIG = f.read().splitlines()
            default_ip = ftpinfoBIG[10].replace(' ', '').replace('IP=', '')
            default_port = int(ftpinfoBIG[12].replace(' ', '').replace('Port=', ''))
        
        #CONNECT TO PS4
        ftp = FTP()
        ftp.connect(default_ip, default_port)
        ftp.login()
        ftp.cwd("/user/home/")
        data = []
        ftp.dir(data.append)
        
        # LIST OF USERS
        embed = discord.Embed(title=f"📑 __**LIST OF USER FOLDER ID'S**__", color=discord.Color.gold())
        embed.set_author(name= f'Thank you {interaction.user.name} calling list 😋', icon_url= interaction.user.avatar)
        x = 1
        
        for line in data:
            # SKIP FIRST THREE DIRECTORY LISTINGS
            if x > 2:
                y = x - 2
                folderids = line.split(" ")[-1]
                ftp.cwd('/user/home/' + folderids)
                ftp.retrbinary("RETR " + 'username.dat' ,open('username.dat', 'wb').write)
                with open('username.dat', 'r') as moredetailsLOL:
                    text_folderids  = moredetailsLOL.read().rstrip('\x00')
                    text_folderids = text_folderids.split(" ")[-1]
                silentremove('username.dat')
                embed.add_field(name = str(y) + ") " + f'__{text_folderids}__' + ' = ' + f'**{folderids}**', value = '\u200b', inline=False) #'\u200b'
                
            x += 1
            
        embed.set_footer(text="Type /guide to see a list of features and commands available.")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        ftp.quit()
        
    # GUIDE TO BOT
    @app_commands.command(name = "guide", description="A guide to this PS4 BOT")
    
    async def guide(self, interaction: discord.Interaction) -> None:
        
        # GUIDE MESSAGE
        embed = discord.Embed(title = '⚠️ __**COMING SOON**__', color=discord.Color.yellow())
        embed.add_field(name = "**Please refer to github README.md**", value = '\u200b', inline=False)
        embed.add_field(name = "**Make sure to set default values using /default**", value = '\u200b', inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
async def setup (bot:commands.Bot) -> None:
    await bot.add_cog(resigner(bot))