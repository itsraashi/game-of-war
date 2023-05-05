CREATE DATABASE WarGame;
USE WarGame;

CREATE TABLE WinnerHistory (
    PlayerId int,
    NumWins int
);

INSERT INTO WinnerHistory (PlayerId, NumWins)
VALUES (1, 0);

INSERT INTO WinnerHistory (PlayerId, NumWins)
VALUES (2, 0);
