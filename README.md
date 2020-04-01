# discord.py

This branch is my personal fork of discord.py to work with MathBot

## Motivation

discord.py keeps a huge amount of state around. Alot of this is not required by all bots. In order to reduce the memory footprint of my bot (and keep hosting costs down), I decided to modify the library itself.

## Changes

- Member: `joined_at`, `premium_since` have been removed. Activities are not stored.
- User: Avatar url is not stored. Activity is not stored.
- Role: Name, colour, mentionable and hoist have been removed.
- All features regarding custom emoji have been removed.

The member cache has been modified slightly:
- It uses a weak value dictionaey, which means that members that are not being referenced from anywhere else will be forgotten about.
- Some members are "important", namely those in the MathBot server, and the bot itself. These are stored indefinitely.

## "Benchmarks"

After starting a couple shards of MathBot using the (modified) library.

Original discord.py:

| Class       | Object Count |
| ----------- | ------------:|
| Member      | 184484       |
| User        | 154373       |
| KeyedRef    | 154223       |
| _Overwrites | 149067       |
| list        | 88968        |
| Colour      | 74905        |
| Role        | 74745        |
| Permissions | 74745        |
| TextChannel | 52258        |
| Emoji       | 36466        |

After stripping some fields, notably colour from role:

| Class        | Object Count |
| ------------ | ------------:|
| Member       | 184135       |
| User         | 154029       |
| KeyedRef     | 153928       |
| _Overwrites  | 149019       |
| list         | 88201        |
| Role         | 74734        |
| TextChannel  | 52252        |
| Emoji        | 36469        |
| VoiceChannel | 17604        |

After stripping custom emoji support:

| Class           | Object Count |
| --------------- | ------------:|
| Member          | 184042       |
| User            | 153974       |
| KeyedRef        | 153862       |
| _Overwrites     | 149018       |
| list            | 91870        |
| Role            | 74734        |
| TextChannel     | 52251        |
| VoiceChannel    | 17604        |
| dict            | 14058        |
| CategoryChannel | 12387        |

After using a weakrefdict to store members

| Class           | Object Count |
| --------------- | ------------:|
| _Overwrites     | 152474       |
| list            | 95298        |
| Role            | 76122        |
| TextChannel     | 53273        |
| function        | 26504        |
| dict            | 22046        |
| VoiceChannel    | 17799        |
| tuple           | 15181        |
| CategoryChannel | 12570        |
| weakref         | 7043         |

Note that these counts are taken a few minutes after startup, so object counts are expected to grow over time. Observed values are that they don't grow all that much.
