# 20-Rooms
## Rock-paper-scissors survival text-game. Make it through 20 rooms.

In this place, you must play a game of rock-paper-scissors, 2-out-of-3, against a mysterious power.

- Win, and you may pass through the door and get an item to aid in your adventure.

- Lose, and suffer the consequences of the unknown.



> ...You're still alive?





> ......Let's see if you can win, this time.

---

## About

This program was made using Python, with PyCharm.

### Rules (Don't Read if You Want to Play Blind!)

- User health begins at 100. User dies and loses when their health gets to 0 or lower. User's health may not go above 100.
- The program tracks the room the user is at. User begins at "Room 0". The processes of the game begin at "Room 1".
- To be allowed into the next room at any point within the main 20 rooms, user must win a game of 2-out-of-3 rock-paper-scissors against the computer.
- If the user gets to "Room 10" or "Room 20", any rock-paper-scissors matches against the computer during only those two rooms will switch to 1-out-of-1 matches, instead of the usual 2-out-of-3 matches. All of the other rules of |'20 Rooms'| will stay the same during these occurrences.
- If the user loses a match, they have a high chance to be attacked by something, decreasing their health by a certain amount depending on what hurt them. In this instance of the user having being attacked, there is a very low chance a second attack will occur. However, there is a low chance there will be no attack whatsoever, where the user will be free from harm for that current "attack-period".
- What attacks the user is randomized from a set of "entities", each with a pre-determined amount of damage that will be dealt to the user, if they are the one chosen from the set. All entities attack only once, and then leave after they have attacked the user. The pool of available entities to be randomly chosen never changes no matter the circumstance.
- If the user is not at 0 health, they will have another chance to try winning a round against the computer. This can keep happening until either the user dies, or the user wins and moves on.
- If the user wins a match (with the exception of being located in "Room 20"), they are given an item of which is randomized from a set of either "defense items" or "health items", depending on whether either set is randomly picked. Then, the user will be allowed into the next room.
- The user's items are stored within their inventory, of which may only hold 3 items. Defense items are the only items that can be stored here.
- If the user already has 3 items in their inventory, they cannot obtain any more items as reward for winning a match.
- Defense items defend directly against entities' attacks, but it will only work if the item used is the "correct strategy". Every item has its own corresponding entity that it may be successful against in defending.
- When an entity attacks the user, an option will be given for the user to pick which of the items in their inventory to try using against the attack. If the user has items in their inventory when an attack period happens, they must always choose one item to try using against the attack.
- Using a defense item against the wrong entity will result in the attack still commencing, but the item will remain in the user's inventory.
- In using the correct defense item against an entity, the attack will be nulled and the user will not lose any health from it. Then, the item will disappear from the user's inventory.
- Health items heal the user, but can be used only when given to the user.
- If the user's health would go over 100 if the given health item were to be used, they cannot use the health item. Otherwise, their health goes up by the item's corresponding amount. The user cannot choose to refuse a health item if they are able to use it by these means.
- Health items cannot be collected in the inventory or saved for later use, even if the user isn't able to use the offered health item due to their health being too high at that current moment.
- If the user gets to "Room 10" or "Room 20", any rock-paper-scissors matches against the computer in only those two rooms will switch to 1-out-of-1 matches, instead of the usual 2-out-of-3 matches.
- Upon the user winning the match of rock-paper-scissors against the computer located in "Room 20", the user has won.


### Videos

- [Code Demo](https://www.youtube.com/watch?v=...)
- [Code Walkthrough](https://www.youtube.com/watch?v=...)

---

##### This game was inspired loosely by the video game "Pressure" by 'Zeal' + 'Urbanshade: Hadal Division' dev team, on Roblox.
##### Also thought of: "Buckshot Roulette" by Mike Klubnika, on itch.io; + 'Critical Reflex' publishing, on Steam.