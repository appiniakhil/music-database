--TRIGGER 1

delimiter @@
CREATE TRIGGER insert_artist
AFTER INSERT ON song_
FOR EACH ROW
begin
INSERT INTO artist(artist_name) VALUES(new.artist_name);
end 
@@
delimiter ;

--TRIGGER 2

delimiter @@
CREATE TRIGGER insert_writer
AFTER INSERT ON song_
FOR EACH ROW
begin
INSERT INTO writers(writer_name) VALUES(new.writer_name);
end 
@@

delimiter ;
--TRIGGER 3

delimiter @@
CREATE TRIGGER insert_album
AFTER INSERT ON song_
FOR EACH ROW
begin
INSERT INTO album(album_name,artist_name) VALUES(new.album_name,new.artist_name);
end 
@@

delimiter ;