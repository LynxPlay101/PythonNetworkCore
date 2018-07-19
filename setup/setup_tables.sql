DROP TABLE IF EXISTS hogwarts_profile;
DROP TABLE IF EXISTS mordonia_profile;
DROP TABLE IF EXISTS minecraft_profile;
DROP TABLE IF EXISTS selected_profile;
DROP TABLE IF EXISTS profiles;
DROP TABLE IF EXISTS network_players;
DROP TABLE IF EXISTS branches;
DROP TABLE IF EXISTS players;

CREATE TABLE IF NOT EXISTS players (
  uuid          BINARY(16),
  username      VARCHAR(16),
  last_known_ip VARCHAR(16),

  CONSTRAINT pk_player_uuid PRIMARY KEY (uuid)
);

CREATE TABLE IF NOT EXISTS network_players (
  uuid           BINARY(16),
  first_login    DATETIME  NOT NULL,
  last_login     TIMESTAMP NOT NULL,
  discord_id     VARCHAR(64),
  discourse_name VARCHAR(32),

  CONSTRAINT pk_network_players_uuid PRIMARY KEY (uuid),

  CONSTRAINT fk_network_players_uuid FOREIGN KEY (uuid) REFERENCES players (uuid),

  CONSTRAINT un_network_players_discord_id UNIQUE (discord_id),
  CONSTRAINT un_network_players_discourse_name UNIQUE (discourse_name)
);

CREATE TABLE IF NOT EXISTS branches (
  branch VARCHAR(16),

  CONSTRAINT pk_branches_branch PRIMARY KEY (branch)
);

CREATE TABLE IF NOT EXISTS profiles (
  profile_id INT,
  uuid       BINARY(16)  NOT NULL,
  branch     VARCHAR(16) NOT NULL,
  first_name VARCHAR(16),
  last_name  VARCHAR(16),
  gender     VARCHAR(1),

  CONSTRAINT pk_profiles_profile_id PRIMARY KEY (profile_id),
  CONSTRAINT fk_profiles_uuid FOREIGN KEY (uuid) REFERENCES players (uuid),
  CONSTRAINT fk_profiles_branch FOREIGN KEY (branch) REFERENCES branches (branch)
);

CREATE TABLE IF NOT EXISTS selected_profile (
  uuid       BINARY(16),
  branch     VARCHAR(16),
  profile_id INT NOT NULL,

  CONSTRAINT pk_selected_profile_uuid_branch PRIMARY KEY (uuid, branch),

  CONSTRAINT fk_selected_profile_uuid FOREIGN KEY (uuid) REFERENCES players (uuid),
  CONSTRAINT fk_selected_profile_branch FOREIGN KEY (branch) REFERENCES branches (branch),
  CONSTRAINT fk_selected_profile_profile_id FOREIGN KEY (profile_id) REFERENCES profiles (profile_id)
);

CREATE TABLE IF NOT EXISTS minecraft_profile (
  profile_id INT,
  health     INT,
  experience INT,

  CONSTRAINT pk_minecraft_profile_profile_id PRIMARY KEY (profile_id)
);

CREATE TABLE IF NOT EXISTS hogwarts_profile (
  profile_id INT,
  house      VARCHAR(16),
  year       INT,

  CONSTRAINT pk_hogwarts_profile_profile_id PRIMARY KEY (profile_id),

  CONSTRAINT fk_hogwarts_profile_profile_id FOREIGN KEY (profile_id) REFERENCES profiles (profile_id)
);

CREATE TABLE IF NOT EXISTS mordonia_profile (
  profile_id INT,
  kingdom    VARCHAR(32),
  town       VARCHAR(32),
  job        VARCHAR(32),

  CONSTRAINT pk_mordonia_profile_profile_id PRIMARY KEY (profile_id),

  CONSTRAINT fk_mordonia_profile_profile_id FOREIGN KEY (profile_id) REFERENCES profiles (profile_id)
);