--------------------FUNCTION 1-----------------
DELIMITER $$
CREATE FUNCTION no_of_songs()
RETURNS int
begin
declare num int;
SET num=(SELECT count(*) FROM song_);
RETURN num;
end
$$
DELIMITER ;


-------------------FUNCTION 2---------------------

DELIMITER $$
CREATE FUNCTION play_art(artistname text) RETURNS int
begin
DROP TEMPORARY TABLE IF EXISTS playlist_artist;
CREATE TEMPORARY TABLE playlist_artist SELECT playlist_.songname  FROM artist JOIN playlist_ ON artist.artist_name=playlist_.artist_name WHERE artist.artist_name = artistname;
return 1;
end
$$
DELIMITER ;


