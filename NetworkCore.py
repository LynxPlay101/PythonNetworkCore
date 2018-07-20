import json
from uuid import UUID

import LightweightJSON
from player.dao.MinecraftProfileDao import MinecraftProfileDao
from player.dao.NetworkPlayerDao import NetworkPlayerDao
from player.dao.PlayerDao import PlayerDao
from player.dao.PlayerProfileDao import PlayerProfileDao
from player.dao.PlayerProfileSnapshotDao import PlayerProfileSnapshotDao
from player.dao.SelectedProfileDataDao import SelectedProfileDataDao
from player.dao.roleplay.BranchProfileDao import HogwartsProfileDao, MordoniaProfileDao
from player.dao.roleplay.BranchProfileDaoFactory import BranchProfileDaoFactory
from sql.SQLProvider import *
from sql.SQLScriptFile import SQLScriptFile

sql_provider = SQLProvider(MySQLProvider(1, config={
    'user': 'python_user',
    'password': 'spTeQ8WbUA2SnrYP',
    'host': '127.0.0.1',
    'database': 'network',
    'raise_on_warnings': True,
}))

sql_provider.execute(lambda c: SQLScriptFile("setup/setup_tables.sql").execute(c))
sql_provider.execute(lambda c: SQLScriptFile("setup/setup_values.sql").execute(c))

minecraft_profile_dao = MinecraftProfileDao(sql_provider)

branch_profile_dao = BranchProfileDaoFactory()
branch_profile_dao.register_dao("MAIN", HogwartsProfileDao(sql_provider))
branch_profile_dao.register_dao("MORDONIA", MordoniaProfileDao(sql_provider))

profile_dao = PlayerProfileDao(sql_provider, branch_profile_dao, minecraft_profile_dao)
profile_snapshot_dao = PlayerProfileSnapshotDao(sql_provider)

selected_profile_dao = SelectedProfileDataDao(sql_provider)

network_player_dao = NetworkPlayerDao(sql_provider
                                      , selected_profile_dao
                                      , profile_snapshot_dao
                                      , profile_dao
                                      , "MAIN")
player_dao: PlayerDao = PlayerDao(sql_provider, network_player_dao)

result = player_dao.lookup([UUID("434eea72-22a6-4c61-b5ef-945874a5c478").bytes])
sql_provider.close()

json_string = json.dumps(json.loads(LightweightJSON.to_string(result)), indent=4, sort_keys=True)
print(json_string)
# TODO Implement ProfilePlayerDao and load the current profile from the selected snapshot
