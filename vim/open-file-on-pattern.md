# Open file on a particular pattern in file

Open a file directly to a pattern in Vim:

`vim some_file.name +/your_pattern`

like:

`vim .env +/DEBUG=`

will open `.env` file exactly on line where `DEBUG=` is mentioned.

Why? The pattern in your terminal history allows repetition. Useful for `.env` or `config` files.
