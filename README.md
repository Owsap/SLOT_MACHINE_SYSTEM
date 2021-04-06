# Slot Machine System

You can bet your gold and have the chance to win a lot of money if you hit three (3) jackpot reel icons.  
The higher you bet, the better your payout is!

The rules are simple, you have three (3) possible jackpots in which each one has a payout amount.  
Hit the same icon three (3) times and you will win the jackpot.  
If you get any other combination that contain jackpot reel icons, you will win half your bet back with a short bet multiplier.  
So, the jackpot reels work as so,  

Slot 1 | Slot 2 | Slot 3 | Winnings
------ | ------ | ------ | --------
A | A | A | 500.000.000
B | B | B | 250.000.000
C | C | C | 100.000.000

All other possible combinations to have a winning:  
`A, A, B; A, A, C; B, B, A; B, B, C; C, C, A; C, C, B; A, B, C; C, A, B; B, A, C; C, B, A; A, C, B;`

If you happen to win a jackpot while having close to maximum gold, you will receive an item in your inventory if you have space for it otherwise you will receive it in your storage room. The item will contain the jackpot value.  

## How to configure?
@ `game/constants.cpp` you can edit all the betting values you want.  
@ `game/contants.cpp` you can edit as well the jackpot values.  

In-game, you can also use the commands,  
`/e slot_machine_reels < x >` where < x > is the number of reels you want to randomize.  
The more reel icons you have, the harder it is to win a jackpot!  

`/e slot_machine_multiplier < x >` where `< x >` is the value of the multiplied you want.  
The higher this value, the higher the payout is.  

If you happen to win a jackpot while having close to maximum gold, you will receive an item in your inventory if you have space for it otherwise you will receive it in your storage room. The item will contain the jackpot value.  

[![Slot Machine System](http://img.youtube.com/vi/qU68p3WYzD8/0.jpg)](http://www.youtube.com/watch?v=qU68p3WYzD8 "Slot Machine System")
