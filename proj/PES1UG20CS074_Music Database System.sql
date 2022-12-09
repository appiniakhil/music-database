
CREATE TABLE `album` (
  `albumID` int(20) NOT NULL,
  `album_name` varchar(20) DEFAULT NULL,
  `artist_name` varchar(100) NOT NULL
)

CREATE TABLE `artist` (
  `artistID` int(20) NOT NULL,
  `artist_name` varchar(30) NOT NULL
)


CREATE TABLE `playlist_` (
  `songname` varchar(200) NOT NULL,
  `filename` varchar(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `artist_name` varchar(200) NOT NULL
)

CREATE TABLE `song_` (
  `songID` int(11) NOT NULL,
  `song_name` varchar(200) NOT NULL,
  `filename` varchar(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `artist_name` varchar(100) NOT NULL,
  `album_name` varchar(100) NOT NULL,
  `writer_name` varchar(100) NOT NULL
)


CREATE TABLE `users` (
  `userID` int(20) NOT NULL,
  `user_name` varchar(200) primary key,
  `password_` varchar(20) NOT NULL
)


CREATE TABLE `writers` (
  `writerID` int(11) NOT NULL,
  `writer_name` varchar(100) NOT NULL
)

INSERT INTO `album` (`albumID`, `album_name`, `artist_name`) VALUES
(1, 'thoda', 'Ben'),
(2, 'vaste', 'Dhvani'),
(3, 'encore', 'bieber'),
(4, 'Ek villan', 'Arijit'),
(5, 'jordi', 'maron 5');

INSERT INTO `artist` (`artistID`, `artist_name`) VALUES
(1, 'Ben'),
(2, 'Dhvani'),
(3, 'bieber'),
(4, 'Arijit'),
(5, 'maron 5');

INSERT INTO `playlist_` (`songname`, `filename`, `username`, `artist_name`) VALUES
('thoda', 'Thoda-Thoda-Pyar(PaglaSongs).mp3', 'Akhil', 'Ben'),
('vaste', 'vaaste.mp3', 'Akhil', 'Dhvani'),
('love you', 'Let-Me-Love-You_320(PaglaSongs).mp3', 'Akhil', 'bieber'),
('humdard', 'Humdard.mp3', 'Akhil', 'Arijit');

INSERT INTO `users` (`userID`, `user_name`, `password_`) VALUES
(7, 'Akhil', '1234');

INSERT INTO `writers` (`writerID`, `writer_name`) VALUES
(1, 'kumar'),
(2, 'Arafat'),
(3, 'bieber'),
(4, 'mithoon'),
(5, 'levin');


INSERT INTO `song_` (`songID`, `song_name`, `filename`, `username`, `artist_name`, `album_name`, `writer_name`) VALUES
(1, 'thoda', 'Thoda-Thoda-Pyar(PaglaSongs).mp3', 'Akhil', 'Ben', 'thoda', 'kumar'),
(2, 'vaste', 'vaaste.mp3', 'Akhil', 'Dhvani', 'vaste', 'Arafat'),
(3, 'love you', 'Let-Me-Love-You_320(PaglaSongs).mp3', 'Akhil', 'bieber', 'encore', 'bieber'),
(4, 'humdard', 'Humdard.mp3', 'Akhil', 'Arijit', 'Ek villan', 'mithoon'),
(5, 'memori', 'Memories.mp3', 'Akhil', 'maron 5', 'jordi', 'levin');