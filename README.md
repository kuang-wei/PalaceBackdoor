# PalaceBackdoor

## Current Features
* Instantly cart one desired item
* Schedule a specific time to execute the bot
* Automatically detect drops
* Add variable delays between refreshs to avoid temporary IP ban

## Background
This python program finds the desired [Palace](https://www.palaceskateboards.com/) item and automatically opens the checkout page with the item in cart.

[Palace](https://www.palaceskateboards.com/) utilizes Shopify for its online [webstore](https://shop-usa.palaceskateboards.com). Shopify websttores have an exploit where the purchase check out page can be opened via a link in such format

```
https://webstoreurl.com/cart/ITEMID:QUANTITY
```

where the ITEMID corresponds to a unique ID that corresponds to a specific size of one item on the webstore. 

This python program finds the unique ID for the user, based on the product name and desired size. It then automatically detects when the item is added to the webstore, and instantly opens a check out page for the user to complete the purchase.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine

### Prerequisites

* Python 2.7 or greater (currently code not compatible with Python 3)
* [Requests](http://docs.python-requests.org/en/master/user/install/) 2.11 or greater
* [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) 4.5 or greater

### Running the program
```
python palacebackdoor.py
```
The program will prompt you to enter key information:

#### Input 1.
```
Target keyword (i.e. block-hood-black)?
```
The item keyword can be found by going to the [lookbook](https://www.palaceskateboards.com/range/summer-2018/). Click on the item of interest and the first line of the description is the item keyword (which includes the color as well). Simply replace all spaces with '-' and you will have the correct keyword.

For example, this [sweater](https://www.palaceskateboards.com/range/summer-2018/p-3-crew/) has the following description in the [lookbook](https://www.palaceskateboards.com/range/summer-2018/):

![](https://imgur.com/FNVbmvv)

So the keyword to be entered will simply be <b>p-3-crew-grey-marl</b>>

#### Input 2.
```
Target size (i.e. medium)?
```
valid size inputs are:
```
small
medium
large
x-large
x2-large
one size
s/m
m/l
```

#### Input 3.
```
Use DirectFetch (True/False)?
```
The recommended setting is True. The first letter 'True/False' must be capitalized. False will prompt the program to first check if the first item in the new section has changed before attempting to find the unique item ID. Using DirectFetch simply go diretly to find the item's unique ID, which is faster.

#### Input 4. 
```
Test run (True/False)?
```
If you fimply want to test out the program, simply enter True. If you are using it on the release day, please enter False.

#### Input 5.
If you enter True in Input 4., you will see
```
Start now (hit ENTER)? 
```
Simply hit enter on your keyboard, or any key to start the program.

If you enter False in Input 4., you will see
```
Start bot at 09:59:x (x from 0 to 59)?
```
Simply enter at number from 0 to 59, and the program will be excuted at 9:59 AM at the second of your input (recommend setting is around 55, since sometimes the drop is earlier than 11 AM EST)

Below is a sample output from the program:

```
Target keyword (i.e. block-hood-black)? basically-a-pique-t-shirt-grey-marl
Target size (i.e. medium)? large
Use DirectFetch (True/False)? True
Test run (True/False)? True
Start now (hit ENTER)? 

Current time:    23:10:27
Bot scheduled at 23:10:29

Bot starting at 23:10:29 

Size matched at 23:10:29

Opening backdoor link at 23:10:29
Backdoor link: https://shop-usa.palaceskateboards.com/cart/3485793943573:1
Succesfully opened link at 23:10:29
```
## Outstanding Issues
* Currently the bot start time is set to 9:59 AM, which is the release time set to the Central Standard Time zone. User would need to <b>change line 18, Column 50</b>, to change the hour according to their local time zone. For example, PST users should change the hour to 7, and EST users should change the hour to 10.

## Author
* **Kuang Wei**