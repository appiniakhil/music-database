# Importing pakages
import streamlit as st
import mysql.connector
import pandas as pd
import random
from streamlit_option_menu import option_menu

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "music db"
)

c = mydb.cursor(buffered=True)

#------------------------------------------------------COUNT--------------------------------------------------------
def songs_count():
    c.execute('SELECT no_of_songs()')
    data=c.fetchall()
    return data


# ------------------------------------------------------CHECK-------------------------------------------------------
def check(username,pwd):
    c.execute(f"select user_name,password_ from users where user_name='{username}'and password_ = '{pwd}'")
    result = c.fetchall()
    return result

def check_id(username):
    c.execute(f"select user_name from users where user_name = '{username}'" )
    result = c.fetchall()
    return result[0][0]

def check_id1(username):
    c.execute(f"select userID from users where user_name = '{username}'" )
    result = c.fetchall()
    return result


# -----------------------------------------------------ADD------------------------------------------------------------

def add_songs(song_name,filename,username,artist_name,album_name,writer_name):
    print(song_name)
    song_id = random.randint(1, 10000000)
    c.execute(f"insert into song_ values('{song_id}','{song_name}','{filename}','{username}','{artist_name}','{album_name}','{writer_name}')")
    mydb.commit()
def add_artist(username,artist_name):
    artistID = random.randint(1, 10000000)
    c.execute(f"insert into artist(artistId,artist_name) values(%s,%s)",(artistID,artist_name))
    mydb.commit()

def add_album(album_name, artist_name):
    album_id=random.randint(1,1000000)
    c.execute("INSERT INTO album(albumID, album_name,artist_name) VALUES(%s,%s,%s)",(album_id,album_name,artist_name))
    mydb.commit()

def add_to_playlist(filename,username,artist_name):
    song = get_song_name(filename)
    songname=song[0][0]
    c.execute(f"insert into playlist_ values('{songname}','{filename}','{username}','{artist_name}')")
    mydb.commit()

def adding_artist(username):
    artist_name=st.text_input("Enter artist")
    if(st.button("ADD")):
        add_artist(username,artist_name)
        st.success("Artist added successfully")

def add_writer(writer_id, writer_name):
    c.execute("insert into writers VALUES (%s, %s)", (writer_id, writer_name))
    mydb.commit()

#--------------------------------------------------------------CREATE-------------------------------------------------------

def create_album_(username):
    album_name = st.text_input("Album Name:")
    artist_name = st.text_input("Artist Name:")
    if st.button("Add Album"):
        if not album_name:
            album_name= None
        if not artist_name:
            artist_name= None
        add_album(album_name, artist_name)
        st.success("Successfully added Album: {}".format(album_name))

def create_add_writer_(username):
    writerID = random.randint(1, 10000000)
    writer_name = st.text_input("Writer Name:")
    if st.button("Add Writer"):
        if not writer_name:
            writer_name = None
        add_writer(writerID,writer_name)
        st.success("Successfully added Writer: {}".format(writer_name))


#-----------------------------------------------------------------VIEW--------------------------------------------------------

def view_all_data_artist():
    c.execute('SELECT * FROM artist ')
    data = c.fetchall()
    return data


def view_all_data_album():
    c.execute('SELECT * FROM Album')
    data = c.fetchall()
    return data

def view_all_data_writer():
    c.execute('SELECT * FROM writers')
    data = c.fetchall()
    return data

#---------------------------------------------------------------------GET-------------------------------------------------------

def get_artist_ids(username):
    c.execute('SELECT artist_name from artist')
    data=c.fetchall()
    return data

def get_writer_ids(username):
    c.execute('SELECT writer_name from writers')
    data=c.fetchall()
    return data

def get_id(username):
    c.execute(f"select * from users where user_name = '{username}'" )
    result = c.fetchall()
    return result[0][0]

def get_song_name(filename):
    c.execute(f'select song_name,artist_name,writer_name from song_ where filename="{filename}"')
    result = c.fetchall()
    return result

def get_album_name():
    c.execute('SELECT album_name from album')
    data=c.fetchall()
    return data

def get_artist_name():
    c.execute('SELECT artist_name from artist')
    data=c.fetchall()
    return data

def get_writer_name():
    c.execute('SELECT writer_name from writers')
    data=c.fetchall()
    return data

#------------------------------------------------------------------------FETCH---------------------------------------------------


def fetch_filename(username):
    c.execute(f'select filename from song_ where username = "{username}"')
    result1=c.fetchall()
    return result1

def fetch_filename_playlist(username):
    c.execute(f'select filename from playlist_ where username = "{username}"')
    result1=c.fetchall()
    return result1


#-------------------------------------------------------------------------READ--------------------------------------------------------


def read_artist_(username):
    result = view_all_data_artist()
    df = pd.DataFrame(result, columns=['Artist Number', 'Artist Name'])
    with st.expander("View all Artists"):
        st.dataframe(df)

def read_album_(username):
    result = view_all_data_album()
    df = pd.DataFrame(result, columns=['Album Number', 'Album Name','Artist Number'])
    with st.expander("View all Albums"):
        st.dataframe(df)

def read_writer_(username):
    result = view_all_data_writer()
    df = pd.DataFrame(result, columns=['Writer Number', 'Writer Name'])
    with st.expander("View all Writers"):
        st.dataframe(df)

#--------------------------------------------------------------------------UPDATE--------------------------------------------------------


def update(old_username,new_username,pwd):
    c.execute(f"update users set user_name='{new_username}' where user_name='{old_username}'")
    c.execute(f"update users set password_='{pwd}' where user_name='{new_username}'")
    mydb.commit()

def update_artist(username):
    list_of_name = [i[0] for i in get_artist_name()]
    old_artist = st.selectbox("Name Of artist you want to Update:", list_of_name)
    new_artist = st.text_input("Name Of new artist:")
    if st.button("Update"):
        c.execute(f"update artist set artist_name='{new_artist}' where artist_name='{old_artist}'")
        st.success("Artist Updated successfully")
    mydb.commit()

def update_writer(username):
    list_of_name = [i[0] for i in get_writer_name()]
    old_writer = st.selectbox("Name of writer you want to Update:", list_of_name)
    new_writer = st.text_input("Name Of new artist:")
    if st.button("Update"):
        c.execute(f"update writers set writer_name='{new_writer}' where writer_name='{old_writer}'")
        st.success("Writer Updated successfully")
    mydb.commit()

#---------------------------------------------------------------------------REMOVE--------------------------------------------------------------


def remove_song(filename,username):
    c.execute(f"delete from song_ where filename='{filename}' and username='{username}'")
    st.success("Song deleted successfully")
    mydb.commit()

def remove_playlist(filename,username):
    c.execute(f"delete from playlist_ where filename='{filename}' and username='{username}'")
    st.success("Playlist deleted successfully")
    mydb.commit()

def remove_artist(username):
    list_of_name = [i[0] for i in get_artist_name()]
    artistname = st.selectbox("Name Of artist you want to remove:", list_of_name)
    if st.button("Remove"):
        c.execute(f"delete from artist where artist_name='{artistname}'")
        st.success("Artist deleted successfully")
    mydb.commit()

def remove_album(username):
    list_of_name = [i[0] for i in get_album_name()]
    albumname = st.selectbox("Name of album you want to remove:", list_of_name)
    if st.button("Remove"):
        c.execute(f"delete from album where album_name='{albumname}'")
        st.success("Album deleted successfully")
    mydb.commit()

def remove_writer(username):
    list_of_name = [i[0] for i in get_writer_name()]
    writername = st.selectbox("Name of writer you want to remove:", list_of_name)
    if st.button("Remove"):
        c.execute(f"delete from writers where writer_name='{writername}'")
        st.success("Writer deleted successfully")
    mydb.commit() 

#---------------------------------------------------------------------------------JOIN-----------------------------------------------------

def artist_songs(username,artist_name):
    c.execute('SELECT song_.song_name  FROM artist JOIN song_ ON artist.artist_name=song_.artist_name WHERE artist.artist_name="{}"'.format(artist_name))
    data=c.fetchall()
    return data 
def album_artists(username,artist_name):
    c.execute('SELECT album.album_name  FROM artist JOIN album ON artist.artist_name=album.artist_name WHERE artist.artist_name="{}"'.format(artist_name))
    data=c.fetchall()
    return data 
def writer_song(username,writer_name):
    c.execute('SELECT song_.song_name  FROM writers JOIN song_ ON writers.writer_name=song_.writer_name WHERE writers.writer_name="{}"'.format(writer_name))
    data=c.fetchall()
    return data 

def song_artist(username):
    list_of_ids = [i[0] for i in get_artist_ids(username)]
    selected_id = st.selectbox("Artist Name:", list_of_ids)
    if st.button("Show"):
        res=artist_songs(username,selected_id)
        df=pd.DataFrame(res)
        st.dataframe(df)

def album_artist(username):
    list_of_ids = [i[0] for i in get_artist_ids(username)]
    selected_id = st.selectbox("Artist Name:", list_of_ids)
    if st.button("Show"):
        res=album_artists(username,selected_id)
        df=pd.DataFrame(res)
        st.dataframe(df)

def song_writer(username):
    list_of_ids = [i[0] for i in get_writer_ids(username)]
    selected_id = st.selectbox("Writer Name:", list_of_ids)
    if st.button("Show"):
        res=writer_song(username,selected_id)
        df=pd.DataFrame(res)
        st.dataframe(df)

def playlist_artists(username):
    list_of_ids = [i[0] for i in get_artist_ids(username)]
    selected_id = st.selectbox("Artist Name:", list_of_ids)
    if selected_id: 
        c.execute("SELECT play_art('{}')".format(selected_id))
        c.execute("SELECT * FROM playlist_artist")
        data = c.fetchall()
        df=pd.DataFrame(data)
        st.dataframe(df)
#----------------------------------------------------------------------------------PLAYLIST-----------------------------------------------------------

def display_playlist(username):
    result = fetch_filename_playlist(username)
    
    col0,col1,col2 = st.columns([2,6,2])
    x=1
    y=100
    z=200
    for i in result:
        filename = i[0]
        with col0:
            st.text("")
            st.text(get_song_name(filename)[0][0])
            st.text("")
            # st.text("")
        with col1:
            audio_file = open(filename, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
        with col2:
            if st.button("Remove",key=y):
                remove_playlist(filename,username)
            st.text("")
            st.text("")
        x+=1
        y+=1
        z+=1

def playlist(filename,username):
    # username = check_id(username)
    song = get_song_name(filename)
    artist_name=song[0][1]
    add_to_playlist(filename,username,artist_name)
    st.success("Song added to playlist")

#---------------------------------------------------------------------------------USER-----------------------------------------------------------

def user(username):
    menu=["Songs","Artist","Album","Playlist","Writers","Custom Query","Profile"]
    choice = st.selectbox("menu",menu)
    if choice=="Songs":
        choice_song=option_menu(
            menu_title=None,
            options=["View Song","Upload Song","Number of songs"],
            orientation="horizontal"
        )
        if choice_song=="View Song":
            home(username)
        elif choice_song=="Upload Song":
            upload(username)
        elif choice_song=="Number of songs":
            res=songs_count()
            st.text("The number of songs:{}".format(res[0][0]))
            songs_count()
    elif choice == "Artist":
        choice_artist=option_menu(
            menu_title=None,
            options=["View Artist","Add Artist","Artist Songs","Album Artist","Update Artist","Remove"],
            orientation="horizontal"
        )
        if choice_artist=="View Artist":
            read_artist_(username)
        elif choice_artist=="Add Artist":
            adding_artist(username)
        elif choice_artist=="Artist Songs":
            song_artist(username)
        elif choice_artist=="Album Artist":
            album_artist(username)
        elif choice_artist=="Update Artist":
            update_artist(username)
        elif choice_artist =="Remove":
            remove_artist(username)
    elif choice == "Album":
        choice_album=option_menu(
            menu_title=None,
            options=["View Album","Add Album","Remove"],
            orientation="horizontal"
        )
        if choice_album=="View Album":
            read_album_(username)
        if choice_album=="Add Album":
            create_album_(username)
        elif choice_album =="Remove":
            remove_album(username)
    elif choice == "Writers":
        choice_writer=option_menu(
            menu_title=None,
            options=["View Writers","Add Writer","Update Writer","Writer Song","Remove"],
            orientation="horizontal"
        )
        if choice_writer=="View Writers":
            read_writer_(username)
        if choice_writer=="Add Writer":
            create_add_writer_(username)
        if choice_writer=="Update Writer":
            update_writer(username)
        if choice_writer=="Writer Song":
            song_writer(username)
        if choice_writer=="Remove":
            remove_writer(username)
    elif choice == "Playlist":
        choice_playlist=option_menu(
            menu_title=None,
            options=["View Playlist","Playlist Artist"],
            orientation="horizontal"
        )
        if choice_playlist=="View Playlist":
            display_playlist(username)
        if choice_playlist=="Playlist Artist":
            playlist_artists(username)
    elif choice == "Profile":
        profile_(username) 
    elif choice == "Custom Query":
        custom()
  


def profile_(username):
    new_username = st.text_input("Enter new username :")
    pwd = st.text_input("Enter new password :")
    if st.button(" Check  Password"):
        args = [pwd,0]
        ans = c.callproc('password_check',args)
        st.write(ans[1])
    if st.button("Update Profile"):
        update(username,new_username,pwd)
        st.success("User details Updated successfully")

#----------------------------------------------------------------------------------HOME------------------------------------------------------

def home(username):
    result = fetch_filename(username)
    col0,col1,col2,col3,col4,col5 = st.columns([1,1,1,4,2,1])
    x=1
    y=100
    z=200
    for i in result:
        filename = i[0]
        song = get_song_name(filename)
        songname=song[0][0]
        artist_name=song[0][1]
        writer_name=song[0][2]
        with col0:
            st.write("Song:",songname)            
            st.text("")
        with col1:
            st.write("Artist:",artist_name)
            st.text("")

        with col2:  
            st.write("Writer:",writer_name)
            st.text("")


        with col3:
            audio_file = open(filename, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
        with col4:
            if st.button("Add Playlist",key=x):
                playlist(filename,username)
            st.text("")
            st.text("")
        with col5:
            if st.button("Remove",key=y):
                remove_song(filename,username)

            st.text("")
            st.text("")   
        x+=1
        y+=1
        
#---------------------------------------------------------------------------------UPLOAD----------------------------------------------------

def upload(username):
    song_name = st.text_input("Enter a song name:")
    artist_name=st.text_input("Enter artist name")
    album_name=st.text_input("Enter album name")
    writer_name=st.text_input("Enter writer name")
    uploaded_files = st.file_uploader("Choose a Audio file", accept_multiple_files=True,key=2)
    if(st.button("ADD")):
        filename = uploaded_files[0].name
        add_songs(song_name,filename,username,artist_name,album_name,writer_name)
        st.success("Song added successfully")
    
#--------------------------------------------------------------------------------CUSTOM-----------------------------------------------

def custom_query(query):
    c.execute(query)
    data = c.fetchall()
    return data

def custom():
    cols = st.text_input("Enter the column names in the resultant dataframe seperated by ',': ")
    cols = cols.split(sep=',')
    query = st.text_input("Enter your query:")
    if query:
        result = custom_query(query)
        df = pd.DataFrame(result, columns=cols)
        with st.expander("View Results"):
            st.dataframe(df)

#----------------------------------------------------------------------------------LOGIN------------------------------------------------------------
def login():
    username = st.sidebar.text_input("Username:")
    pwd = st.sidebar.text_input("Password :")
    if st.sidebar.checkbox("login"):    
        result = check(username,pwd)
        if(len(result)==0):
            st.sidebar.error('Invalid credentials')
        else:
            user(username)

#-----------------------------------------------------------------------------------SIGNUP---------------------------------------------------------
def signup():
    userID = st.sidebar.text_input("Create User Id")
    username = st.sidebar.text_input("Create Username:")
    pwd = st.sidebar.text_input("Create Password :")
    if st.sidebar.checkbox("signup"):
        result = check_id1(username)
        if(len(result)==0):
            st.sidebar.error('Invalid credentials')
        else:
            c.execute("insert into users(userID, user_name, password_) values ('{}','{}','{}');".format(int(userID), username, pwd))
            mydb.commit()
            st.success("User Account created successfully")

#-------------------------------------------------------------------------------------MAIN-------------------------------------------------------------

def main():
    st.title("Music Database System")
    st.subheader("Appini Akhil - PES1UG20CS074")
    menu = ["login","Sign Up"]
    choice = st.sidebar.selectbox("Choose:",menu)
    if choice == "login":
        login()
    elif choice == 'Sign Up':
        signup()


if __name__ == '__main__':
    main()
