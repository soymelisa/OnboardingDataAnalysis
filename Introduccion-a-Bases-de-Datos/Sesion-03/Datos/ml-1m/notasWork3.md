mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM users WHERE genero= 'F' LIMIT 10;
+----+--------+------+------+-------+
| id | genero | edad | ocup | cp    |
+----+--------+------+------+-------+
| 1  | F      | 1    | 10   | 48067 |
| 6  | F      | 50   | 9    | 55117 |
| 10 | F      | 35   | 1    | 95370 |
| 11 | F      | 25   | 1    | 04093 |
| 16 | F      | 35   | 0    | 20670 |
| 18 | F      | 18   | 3    | 95825 |
| 24 | F      | 25   | 7    | 10023 |
| 28 | F      | 25   | 1    | 14607 |
| 30 | F      | 35   | 7    | 19143 |
| 32 | F      | 25   | 0    | 19355 |
+----+--------+------+------+-------+
10 rows in set
Time: 0.196s
mysql root@tcp.ngrok.io:MELISAPE> SELECT COUNT(*) FROM users WHERE edad IN(18,25,35,45,50,56) A
                                  ND ocup=2 OR ocup=20;
+----------+
| COUNT(*) |
+----------+
| 545      |
+----------+
1 row in set
Time: 0.223s
mysql root@tcp.ngrok.io:MELISAPE>







mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM users WHERE edad IN(18,25,35,45,50,56) AND ocup=2 OR ocup=20;
+------+--------+------+------+------------+
| id   | genero | edad | ocup | cp         |
+------+--------+------+------+------------+
| 5    | M      | 25   | 20   | 55455      |
| 50   | F      | 25   | 2    | 98133      |
| 56   | M      | 35   | 20   | 60440      |
| 58   | M      | 25   | 2    | 30303      |
| 83   | F      | 25   | 2    | 94609      |
| 110  | M      | 25   | 2    | 90803      |
| 114  | F      | 25   | 2    | 83712      |
| 136  | M      | 18   | 2    | 21202      |
| 138  | M      | 18   | 20   | 22203      |
| 139  | F      | 25   | 20   | 45409      |
| 146  | F      | 35   | 20   | 10954      |
| 151  | F      | 25   | 20   | 85013      |
| 154  | M      | 50   | 20   | 94530      |
| 175  | F      | 25   | 2    | 95123      |
| 201  | F      | 35   | 2    | 55117      |
| 214  | M      | 18   | 20   | 80218      |
| 227  | M      | 35   | 20   | 90291      |
| 232  | M      | 25   | 20   | 55408      |
| 233  | F      | 45   | 20   | 37919-4204 |
| 241  | M      | 35   | 20   | 55121      |
| 261  | M      | 25   | 20   | 75801      |
| 269  | M      | 25   | 2    | 55408      |
| 290  | F      | 25   | 20   | 94591      |
| 297  | M      | 18   | 2    | 97211      |
| 308  | M      | 25   | 2    | 10025      |
| 312  | F      | 50   | 2    | 22207      |
| 333  | M      | 35   | 2    | 55410      |
| 334  | F      | 56   | 2    | 55113      |
| 350  | M      | 45   | 20   | 08035      |
| 356  | M      | 56   | 20   | 55101      |
| 362  | M      | 35   | 20   | 55407      |
| 373  | F      | 25   | 2    | 55347      |
| 375  | M      | 25   | 2    | 55106      |
| 380  | M      | 25   | 2    | 92024      |
| 382  | F      | 35   | 20   | 66205      |
| 406  | M      | 25   | 20   | 55105      |
| 454  | M      | 25   | 20   | 55092      |
| 455  | F      | 35   | 2    | 55113      |
| 475  | F      | 25   | 2    | 55421      |
| 500  | F      | 18   | 2    | 55105      |
| 501  | M      | 25   | 2    | 55372      |
| 504  | M      | 25   | 2    | 17003      |
| 509  | M      | 25   | 2    | 55125      |
| 514  | M      | 25   | 2    | 55113      |
| 520  | F      | 35   | 20   | 55104      |
| 527  | F      | 25   | 2    | 11201      |
| 530  | M      | 25   | 2    | 10019      |
| 536  | M      | 25   | 20   | 01267      |
| 539  | M      | 25   | 2    | 55103      |
| 551  | M      | 35   | 20   | 55116      |
| 553  | M      | 25   | 2    | 94131      |
545 rows in set
Time: 0.358s
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE titulo LIKE '%2000%';
+------+----------------------------------------------------+--------+
| id   | titulo                                             | genero |
+------+----------------------------------------------------+--------+
| 3285 |  The (2000)::Adventure|Drama                       | <null> |
| 3287 |  The (2000)::Animation|Children's                  | <null> |
| 3321 |  The (2000)::Comedy                                | <null> |
| 3325 |  The (2000)::Comedy|Drama                          | <null> |
| 3353 |  The (2000)::Comedy|Romance                        | <null> |
| 3355 |  The (2000)::Thriller                              | <null> |
| 3483 |  The (2000)::Animation|Children's                  | <null> |
| 3484 |  The (2000)::Thriller                              | <null> |
| 3539 |  The (2000)::Documentary                           | <null> |
| 3563 |  The (2000)::Action|Horror                         | <null> |
| 3564 |  The (2000)::Children's|Comedy                     | <null> |
| 3566 |  The (2000)::Comedy|Drama                          | <null> |
| 3582 |  Hospitals & Hip-Hop (2000)::Drama                 | <null> |
| 3752 |  Myself and Irene (2000)::Comedy                   | <null> |
| 3753 |  The (2000)::Action|Drama|War                      | <null> |
| 3754 |  The (2000)::Animation|Children's|Comedy           | <null> |
| 3755 |  The (2000)::Action|Adventure|Thriller             | <null> |
| 3756 |  The (2000)::Drama                                 | <null> |
| 3784 |  The (2000)::Comedy                                | <null> |
| 3796 |  The (a.k.a. Immortality) (2000)::Romance|Thriller | <null> |
| 3797 |  The (2000)::Thriller                              | <null> |
| 3852 |  The (2000)::Comedy                                | <null> |
| 3859 |  The (2000)::Documentary                           | <null> |
| 3861 |  The (2000)::Comedy                                | <null> |
| 3863 |  The (2000)::Sci-Fi|Thriller                       | <null> |
| 3865 |  The (2000)::Comedy|Documentary                    | <null> |
| 3879 |  The (2000)::Action                                | <null> |
| 3880 |  The (2000)::Documentary                           | <null> |
35 rows in set
Time: 0.235s
mysql root@tcp.ngrok.io:MELISAPE> SELECT *, COUNT(*) FROM movies WHERE titulo LIKE '%2000%';
(1140, "In aggregated query without GROUP BY, expression #1 of SELECT list contains nonaggregated column 'MELISAPE.movies.id'; this is incompatible with sql_mode=only_full_group_by")
mysql root@tcp.ngrok.io:MELISAPE> SELECT COUNT(*) FROM movies WHERE titulo LIKE '%2000%';
+----------+
| COUNT(*) |
+----------+
| 35       |
+----------+
1 row in set
Time: 0.240s
mysql root@tcp.ngrok.io:MELISAPE> SELECT COUNT(*) FROM movies WHERE titulo LIKE '%(2000)%';
+----------+
| COUNT(*) |
+----------+
| 35       |
+----------+
1 row in set
Time: 0.237s
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero IN(Horror,Mystery,Thriller);
Reconnecting...
(1054, "Unknown column 'Horror' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero IN (Horror,Mystery,Thriller);
(1054, "Unknown column 'Horror' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero IN (horror,Mystery,Thriller);
(1054, "Unknown column 'horror' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM users WHERE genero IN(horror,mistery,thriller);
(1054, "Unknown column 'horror' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero IN(horror,mistery,thriller);
(1054, "Unknown column 'horror' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero IN (mistery,thriller);
(1054, "Unknown column 'mistery' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero IN(mistery,thriller);
(1054, "Unknown column 'mistery' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero IN ('Horror,Mystery,Thriller');
+----+--------+--------+
| id | titulo | genero |
+----+--------+--------+
0 rows in set
Time: 0.227s
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero IN('Horror,Mystery,Thriller');
+----+--------+--------+
| id | titulo | genero |
+----+--------+--------+
0 rows in set
Time: 0.201s
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero=('Horror');
+----+--------+--------+
| id | titulo | genero |
+----+--------+--------+
0 rows in set
Time: 0.228s
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero=Horror;
(1054, "Unknown column 'Horror' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero='Horror';
+----+--------+--------+
| id | titulo | genero |
+----+--------+--------+
0 rows in set
Time: 0.226s
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero IN(misterio,suspenso) AND genero=suspenso OR genero=h
                                  orror;
(1054, "Unknown column 'misterio' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero=thriller AND genero=suspenso OR genero=horror;
(1054, "Unknown column 'thriller' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero=mistery AND genero=suspenso OR genero=horror;
(1054, "Unknown column 'mistery' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero=misterio AND genero=suspenso OR genero=horror;
(1054, "Unknown column 'misterio' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero=misterio
(1054, "Unknown column 'misterio' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero=misterio;
(1054, "Unknown column 'misterio' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero=mistery;
(1054, "Unknown column 'mistery' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero='mistery';
+----+--------+--------+
| id | titulo | genero |
+----+--------+--------+
0 rows in set
Time: 0.222s
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero='mistery';
+----+--------+--------+
| id | titulo | genero |
+----+--------+--------+
0 rows in set
Time: 0.261s
mysql root@tcp.ngrok.io:MELISAPE> SELECT * FROM movies WHERE genero=mistery;
(1054, "Unknown column 'mistery' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT COUNT(*) FROM movies WHERE nombre LIKE '%2000%';
Reconnecting...
(1054, "Unknown column 'nombre' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT COUNT(*) FROM movies WHERE titulo LIKE '%2000%';
+----------+
| COUNT(*) |
+----------+
| 35       |
+----------+
1 row in set
Time: 0.226s
mysql root@tcp.ngrok.io:MELISAPE> SELECT COUNT(*) FROM movies;
+----------+
| COUNT(*) |
+----------+
| 3705     |
+----------+
1 row in set
Time: 0.266s
mysql root@tcp.ngrok.io:MELISAPE> SELECT COUNT(*) FROM movies WHERE gener LIKE '%Mystery%' OR genero='%Thriller%' OR gene
                                  ro='%Horror%';
(1054, "Unknown column 'gener' in 'where clause'")
mysql root@tcp.ngrok.io:MELISAPE> SELECT COUNT(*) FROM movies WHERE gener LIKE '%Mystery%' OR genero='%Thriller%' LIKE OR
                                   genero='%Horror%';
(1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'OR genero='%Horror%'' at line 1")
mysql root@tcp.ngrok.io:MELISAPE> SELECT COUNT(*) FROM movies WHERE genero LIKE '%Mystery%' OR genero='%Thriller%' LIKE O
                                  R genero='%Horror%';
(1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'OR genero='%Horror%'' at line 1")
mysql root@tcp.ngrok.io:MELISAPE> SELECT COUNT(*) FROM movies WHERE genero LIKE '%Mystery%' OR genero='%Thriller%' LIKE g
                                  enero='%Horror%';
+----------+
| COUNT(*) |
+----------+
| 0        |
+----------+
1 row in set
Time: 0.440s
mysql root@tcp.ngrok.io:MELISAPE> SELECT COUNT(*) FROM movies WHERE genero LIKE '%Mystery%' OR genero='%Thriller%';
+----------+
| COUNT(*) |
+----------+
| 0        |
+----------+
1 row in set
Time: 0.310s
mysql root@tcp.ngrok.io:MELISAPE> SELECT COUNT(*) FROM movies WHERE genero='%Thriller%';
+----------+
| COUNT(*) |
+----------+
| 0        |
+----------+
1 row in set
Time: 0.363s
mysql root@tcp.ngrok.io:MELISAPE> SELECT *, lenght(cp) AS len_cp FROM users ORDER BY lenght(cp) DESC;
(1305, 'FUNCTION MELISAPE.lenght does not exist')
mysql root@tcp.ngrok.io:MELISAPE> SELECT DISTINCT *, length(cp) AS len_cp FROM users ORDER BY length(cp) DESC LIMIT 5;
+-----+--------+------+------+------------+--------+
| id  | genero | edad | ocup | cp         | len_cp |
+-----+--------+------+------+------------+--------+
| 293 | M      | 56   | 1    | 55337-4056 | 11     |
| 458 | M      | 50   | 16   | 55405-2546 | 11     |
| 233 | F      | 45   | 20   | 37919-4204 | 11     |
| 506 | M      | 25   | 16   | 55103-1006 | 11     |
| 161 | M      | 45   | 16   | 98107-2117 | 11     |
+-----+--------+------+------+------------+--------+

5 rows in set
Time: 0.231s
mysql root@tcp.ngrok.io:MELISAPE> SELECT DISTINCT *, length(cp) AS len_cp FROM users ORDER BY length(cp) DESC LIMIT 10;
+-----+--------+------+------+------------+--------+
| id  | genero | edad | ocup | cp         | len_cp |
+-----+--------+------+------+------------+--------+
| 458 | M      | 50   | 16   | 55405-2546 | 11     |
| 939 | F      | 25   | 20   | 20110-5616 | 11     |
| 567 | M      | 35   | 20   | 52570-9634 | 11     |
| 506 | M      | 25   | 16   | 55103-1006 | 11     |
| 946 | M      | 35   | 7    | 48103-8929 | 11     |
| 913 | M      | 25   | 0    | 20744-6223 | 11     |
| 293 | M      | 56   | 1    | 55337-4056 | 11     |
| 868 | M      | 50   | 17   | 01702-7224 | 11     |
| 233 | F      | 45   | 20   | 37919-4204 | 11     |
| 161 | M      | 45   | 16   | 98107-2117 | 11     |
+-----+--------+------+------+------------+--------+

mysql root@tcp.ngrok.io:MELISAPE> \T csv
Changed table format to csv
Time: 0.000s
mysql root@tcp.ngrok.io:MELISAPE> \o users-lencp-desc.csv
Time: 0.000s
mysql root@tcp.ngrok.io:MELISAPE>