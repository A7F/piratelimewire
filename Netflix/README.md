## Netflix comboList checker
This script allows you to import a combo list you found in your most favourite lamer forum and check if accounts inside are valid or not, so you can insult the guy who posted the list calling him "fucking noob" (even if all you can do is copy/paste the work others did).

### How it works?
It relies on [this site's API](https://checker.neftlix.ml). The idea is simple, it loads a combo list from file, parses each line and tests it on that website sending a POST request.

The point is, the whole process is slow because it can only fire 200 requests/minute due to API limitations, also the speed depends on your internet connection so I suggest you to load it on a server and let it run all night long.

### How do I use it?
Open the script and edit the first 2 variables so the script points to the right files:
```
in_filename = complete filepath to the combolist
out_filename = output filename where the script will store valid accounts
```
You don't have to change anything else. If the output file doesn't exists, the script creates it. Example:
```
in_filename = "D:\Desktop\\352k.txt"
out_filename = "D:\Desktop\\results.txt"
```
(remember the high commas "..." and to escape the path correctly)

Input file must follow this format:
```
name@domain:password
anothername@anotherdomain:anotherpassword
```
And so on... Basically is the most common formatting out there for these lists. When the process is running, you will get something like this:

```
rows found: 352073
expected time: 1760.365min
continue? Y/N: y
  0%|          | 201/352073 [00:45<21:47:51,  4.48account/s]
Parsed: 200
Invalid accounts: 1
Working Accounts: 0
Waiting 60s...
  0%|          | 401/352073 [09:08<119:51:49,  1.23s/account]
Parsed: 400
Invalid accounts: 2
Working accounts: 3
Waiting 60s...
  0%|          | 405/352073 [10:17<1112:07:25, 11.38s/account]
```


### Dependencies
This script uses [tqdm](https://github.com/tqdm/tqdm) and [requests](https://github.com/requests/requests) so `pip install` if you don't already have them. 