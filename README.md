# How to get member lists from Whatsapp messages
Do you recall ever the times where you always have to take attendance on Whatsapp following this format and you had to translate the message onto an excel sheet?
> Hey guys! We have this blah blah event, put your name and ID down if you're interested! 
> 1. Alice Tan 19374 
> 2. Bronnie Chan 239801
> 3. Manny Ida 238471
> ... etc

I was annoyed at this issue when I recently received a list of many members... It's simply annoying and labourious if I copy and paste manually onto cells in a table.
So I decided to code a mini program to help me to do things faster :D
Since I'm new to programming, I tried out 3 different ways.

1. Hardcode + writing the data to csv row by row.
2. Using re module to extract the number, name and student ID specifically, then converting the data to csv using dictwriter method.
3. Using re module for preprocessing data, then convert into Panda dataframes for export to xlsx. format directly. 

Please feel free to add on more ways to do so :D 
