# omori-discord
Controlling the game OMORI by using DirectInput through Discord chat

## Requirements
A computer running on Windows (Windows 10 recommended).

Of course, the game [OMORI](https://store.steampowered.com/app/1150690) (legally get the game on steam)

## How to use
1. You need Python 3.6 or higher which supports asynchronous operations.
2. The `requirements.txt` and installing by `pip3 install -r requirements.txt`.
3. Set you discord bot `TOKEN` on `main.py`.
4. Set channel ID to listen for events on main.py line 41.
5. Run the bot by `py main.py`
6. Make sure the game window is actively focused or else it will not work.


## Controls
Z - Confirm

X - Cancel

Q - Show the hangman menu (story progress)

W - Show the map (story progress)

Up - Go up

Down - Go down

Left - Go left

Right - Go right
