# Execute last command with sudo

From the bash manual:

> 9.3.1 Event Designators
>
> !! - Refer to the previous command. This is a synonym for ‘!-1’.

Use `sudo !!` to run last command with uplifted privilege.
