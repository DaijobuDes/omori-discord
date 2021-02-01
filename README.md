# omori-discord
Controlling the game OMORI by using DirectInput through Discord chat

## Requirements
A computer running on Windows (Windows 10 recommended).

You need Python 3.6 or higher which supports asynchronous operations.

Of course, the game [OMORI](https://store.steampowered.com/app/1150690) (legally get the game on steam)

## How to use
1. The `requirements.txt` and installing by `pip3 install -r requirements.txt`.
2. Set your discord bot `TOKEN` on `main.py`.
3. Set channel ID to listen for events on main.py line 41.
4. Run the bot by `py main.py`
5. Make sure the game window is actively focused or else it will not work.


## Controls (Lowercase phrases)
Z - Confirm

X - Cancel

Q - Show the hangman menu (story progress)

W - Show the map (story progress)

(Append `!` to run, e.g. up! or down!)

Up - Go up

Down - Go down

Left - Go left

Right - Go right
