DELIMITER $$
CREATE PROCEDURE password_check(IN pwd text, OUT msg text)
begin
if LENGTH(pwd)<6 then
SET msg="Password is too short";
else 
SET msg="Password is good";
end if;
end
$$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE backup_member()
BEGIN
DECLARE done INT DEFAULT 0;
DECLARE song_name text;
DECLARE artist_name text;
DECLARE cur CURSOR FOR SELECT song_name,artist_name FROM song_ ;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
OPEN cur;
label: LOOP
FETCH cur INTO song_name,artist_name;
INSERT INTO backup VALUES(song_name,artist_name);
IF done = 1 THEN LEAVE label;
END IF;
END LOOP;
CLOSE cur;
END$$
DELIMITER ;


--Creating backup table:
CREATE TABLE backup(song_name text,artist_name text);
-- CALL THE PROCEDURE:
CALL backup_member();
--SHOW THE Backup TABLE created due to this cursor :
SELECT * FROM backup;
