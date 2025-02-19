# Quote Of The Times
 Quote of the times is a simple three app setup that will display a quote on your lock screen that changes from a list of quotes over a specified time interval. You are going to need to install a few apps to make the whole thing possible:

 ## Steps
 You will first need some applications:
 1. Kustom Lock Screen 
    - This is the app that will display the quote on your lock screen.
 2. Any terminal app, I use Termux.
    - This is the terminal app that will allow you to run the script that will update the quote on your lock screen, as well as to setup the cron job to run the script at a specific time interval.
 3. Automate 
    - This is the app that will allow you to loop the update process of the quote on your lock screen.
 4. Any text editor app, QuickEdit.
    - This is the text editor app that will allow you to edit the `quotes.txt` file.

## Setup 

### File System
1. Create a `quotes.txt` file somewhere on your device. Save the path to the file.
2. Create a `current_quote.txt` file somewhere on your device. Save the path to the file.
3. Add quotes to the `quotes.txt` file, each quote should be on a new line.
4. Download the `update_quote.py` file and save it on your device. *(Preferably in the same directory as the `quotes.txt` file.)*

*I made a directory called QOTD and put my files in there.*

### Kustom Lock Screen
1. Open the Kustom Lock Screen app and grant the app permissions to the lock screen.
2. Create a new preset by tapping the + button
3. Add two text elements to your layout:
   You can use any layout as well, but the directions below are just for the quote.
   - For the quote:
     1. Tap the + button and select "Text"
     2. In the text editor, tap the formula editor and enter: `$br(tasker, qotd)$` 
     3. (Optional) Add padding and adjust alignment as needed
     4. (Optional) Adjust the text box size to fit the quote, as well as any other settings
4. (Optional) You can adjust the following settings for better visibility:
   - Add a background blur or overlay
   - Add a shadow to the text
   - Adjust the text colors for better contrast

5. Save your preset and apply it to your lock screen
   - Tap the three lines in the top left corner of the screen and toggle "Lock Screen" to on.

### Termux
1. Run the following commands to install the necessary packages:
    ```bash
    pkg update && pkg upgrade -y
    pkg install python -y
    pkg install cronie -y
    ```
    If you dont have an editor installed, install one:
    ```bash
    pkg install nano -y
    ```
    OR
    ```bash
    pkg install vim -y
    ```

2. Create a new crontab file:
    ```bash
    crontab -e
    ```
3. Add the following line to the crontab file:

    ```vim
    * * * * * /path/to/your/python/script/update_quote.py
    ```
    Crontabs are a way to schedule tasks to run at a specific time. The line above will run the `update_quote.py` file every minute.

    You can change the time interval by changing the `*`s to the desired time.

#### Crontab Time Format

| Field | Allowed Values | Example |
|-------|---------------|---------|
| Minute | 0-59 | 30 |
| Hour | 0-23 | 15 |
| Day of Month | 1-31 | 1 |
| Month | 1-12 | 12 |
| Day of Week | 0-6 (Sun=0, Sat=6) | 0 |

#### Common Crontab Examples

| Description | Crontab Expression |
|-------------|-------------------|
| Every minute | `* * * * *` |
| Every 10 minutes | `*/10 * * * *` |
| Every day at 2 AM | `0 2 * * *` |
| Every Monday at 5 PM | `0 17 * * 1` |
| Every first day of the month at midnight | `0 0 1 * *` |

So use this information to setup your crontab at the interval you want.

4. Open the `update_quote.py` file and change the `input_file` path to the `quotes.txt` file, and the `output_file` path to the path of `current_quote.txt` file. *(You can use the paths you saved earlier. Usually the files are stored in storage/emulated/0/...)*

5. Save the file and exit the editor.

6. Run the following command to start the crontab update process:
    ```bash
    crond
    ```
7. (Optional) If you want to run the command immediately, run the following command:
    ```bash
    python /path/to/your/python/script/update_quote.py
    ```


### Automate
1. Open the Automate app and create a new workflow by tapping the + button.
2. Create the following nodes:
   - ReadFile
      1. Set the file path to the `current_quote.txt` file.
      2. Set the charset to "UTF-8"
      3. Set the output variable to "QUOTE"
   - Plug-in Action 
      1. Set the pick-plugin field to KLCK Send variable
      2. Hit configure, and in the tasker string, enter: "%QUOTE"
      3. In the Kustom Variable field, enter: "QUOTE" *(if it automatically puts it in lower case, that's fine)*
   - Delay
      1. Set the delay to however long you want before the quote is updated.
      2. Set the proceed field to "Exact"
3. Connect the nodes as follows:
   - Flow beginning -> ReadFile -> Plug-in Action -> Delay -> ReadFile
   - This should create a loop that will update the quote on your lock screen at the specified interval.
   - *Keep in mind the interval in this case is the time it takes for the workflow to run from start to finish, not the crontab interval. You can set it to be the same, however*
4. Save the workflow and run it.

Your lock screen should now display the current time with your changing quote underneath it.


## Some Quotes
- "The only way to do great work is to love what you do." - Steve Jobs
- "Believe you can and you're halfway there." - Theodore Roosevelt
- "The best way to predict the future is to invent it." - Alan Kay
- "The only limit to our realization of tomorrow is our doubts of today." - Franklin D. Roosevelt
- "Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present." - Master Oogway
- "Success is not final, failure is not fatal" - Winston Churchill
- "Fortune favors the bold" - Latin proverb
- "In the midst of chaos, there is also opportunity" - Sun Tzu
- "There's a saying that if you do what you love, you'll never work a day in your life. At Apple, I learned that idea is a total crock: You will work harder than you ever thought possible, but the tools will feel light in your hands." - Tim Cook
- "Power is determined by the gap between your thoughts and your actions. The smaller the gap, the more powerful you become." - Alex Hormozi