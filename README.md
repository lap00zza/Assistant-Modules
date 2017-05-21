# Assistant-Modules
Community created modules/plugins for Assistant. All the modules here are licensed under GPLv3.

### A sample module
```py
from assistant import command


class FunCommands:
    def __init__(self, assistant):
        self.assistant = assistant

    @command(description="A sample command to demonstrate modules.")
    async def test_state(self, message):
        await self.assistant.send_message(message.channel, "This is from a downloaded module.")


def load(assistant):
    assistant.add_module(FunCommands(assistant))
```

### How do I get my module listed?
1. Fork this repository.
2. Create a module. Be sure to place your module in the modules directory. Once done, push it to the forked repository.
3. Edit the `assistant-manifest.json` file and add an entry to your module. Example entry:
```json
{
  "name": "Module_Name", // example: Fun 
  "version": "Major.Minor", // example: 0.1
  "description": "A short description.", // example: Does fun things
  "path": "realtive path to your module from root.", // example: modules/fun.py
  "author": "your name" // example: John Doe
}
```
4. Send a Pull Request.

### Important Links
* **Documentation**: http://assistant.readthedocs.io/en/latest/ (mainly the API reference)

### License
Copyright (C) 2017  Jewel Mahanta

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
