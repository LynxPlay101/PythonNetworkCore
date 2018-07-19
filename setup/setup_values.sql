INSERT INTO branches VALUE ('MAIN');
INSERT INTO branches VALUE ('MORDONIA');

INSERT INTO players VALUES (
  UNHEX(REPLACE('434eea72-22a6-4c61-b5ef-945874a5c478', '-', '')), 'LynxPlay', '192.168.1.181'
);

INSERT INTO network_players VALUE (UNHEX(REPLACE('434eea72-22a6-4c61-b5ef-945874a5c478', '-', ''))
  , date(now()), timestamp(now()), 'LynxPlay', NULL);

INSERT INTO profiles (profile_id, uuid, branch, first_name, last_name, gender)
  VALUE (0, UNHEX(REPLACE('434eea72-22a6-4c61-b5ef-945874a5c478', '-', '')), 'MAIN', 'Michael', 'King', 'M');
INSERT INTO profiles (profile_id, uuid, branch, first_name, last_name, gender)
  VALUE (2, UNHEX(REPLACE('434eea72-22a6-4c61-b5ef-945874a5c478', '-', '')), 'MAIN', 'Trenton', 'Lovegood', 'M');
INSERT INTO profiles (profile_id, uuid, branch, first_name, last_name, gender)
  VALUE (3, UNHEX(REPLACE('434eea72-22a6-4c61-b5ef-945874a5c478', '-', '')), 'MAIN', 'Haley', 'Krum', 'F');

INSERT INTO profiles (profile_id, uuid, branch, first_name, last_name, gender)
  VALUE (1, UNHEX(REPLACE('434eea72-22a6-4c61-b5ef-945874a5c478', '-', '')), 'MORDONIA', 'Michael', 'Ascott', 'M');
INSERT INTO profiles (profile_id, uuid, branch, first_name, last_name, gender)
  VALUE (4, UNHEX(REPLACE('434eea72-22a6-4c61-b5ef-945874a5c478', '-', '')), 'MORDONIA', 'Michelle', 'Durmstrong', 'F');

INSERT INTO selected_profile VALUE (UNHEX(REPLACE('434eea72-22a6-4c61-b5ef-945874a5c478', '-', '')), 'MAIN', 0);
INSERT INTO selected_profile VALUE (UNHEX(REPLACE('434eea72-22a6-4c61-b5ef-945874a5c478', '-', '')), 'MORDONIA', 1);

INSERT INTO minecraft_profile VALUE (0, 40, 142);
INSERT INTO minecraft_profile VALUE (2, 1, 3);
INSERT INTO minecraft_profile VALUE (3, 12, 54);

INSERT INTO minecraft_profile VALUE (1, 25, 152);
INSERT INTO minecraft_profile VALUE (4, 40, 23);

INSERT INTO hogwarts_profile VALUE (0, 'Slytherin', 7);
INSERT INTO hogwarts_profile VALUE (2, 'Gryffindor', 5);
INSERT INTO hogwarts_profile VALUE (3, 'Ravenclaw', 1);

INSERT INTO mordonia_profile VALUE (1 , 'SomeKingdom' , 'CoolTown' , 'Archer');
INSERT INTO mordonia_profile VALUE (4 , 'Lynnea' , 'Drathos' , 'Warrior');